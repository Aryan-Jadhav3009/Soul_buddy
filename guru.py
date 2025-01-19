import streamlit as st
import requests
import json

# Langflow API details
BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "04a145b8-3775-4f9c-b652-897bdfa67625"
FLOW_ID = "31d485c6-2bad-4851-9f5a-4b4b1fd8861d"
APPLICATION_TOKEN = "application_token"
ENDPOINT = ""  # Optional: Specific endpoint name if configured
TWEAKS = {
    "ChatInput-VM31v": {},
    "AstraDBToolComponent-HIcW7": {},
    "Agent-OoJCl": {},
    "Prompt-bnvKs": {},
    "ChatOutput-Xi8DK": {},
    "GoogleGenerativeAIModel-dJBmg": {},
}

# Function to call the Langflow API
def run_flow(message: str, tweaks: dict = None):
    """
    Call Langflow API with the given message and tweaks.
    """
    endpoint = ENDPOINT or FLOW_ID
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {"Authorization": f"Bearer {APPLICATION_TOKEN}", "Content-Type": "application/json"}
    if tweaks:
        payload["tweaks"] = tweaks

    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()
def extract_text(data):
    """Extract text content from a Langflow API response (recursive)."""
    if isinstance(data, str):
        return data  # Base case: return text if it's a string
    elif isinstance(data, list):
        text = ""
        for item in data:
            extracted_item_text = extract_text(item)
            # Stop printing after encountering an error word
            if "error" in extracted_item_text.lower():
                break
            text += extracted_item_text
        return text
    elif isinstance(data, dict):
        text = ""
        if "text" in data:  # Prioritize "text" key
            return data["text"]
        elif "message" in data:
            message_content = data.get("message", {})
            if isinstance(message_content, dict):
                for key, value in message_content.items():
                    text += f"**{key.capitalize()}:** {value}\n"  # Format key-value pairs
            elif isinstance(message_content, str):
                text += message_content + "\n"
            # Stop printing after encountering an error word
            if "error" in text.lower():
                return text
        else:
            for value in data.values():
                extracted_value_text = extract_text(value)
                # Stop printing after encountering an error word
                if "error" in extracted_value_text.lower():
                    break
                text += extracted_value_text
        return text
    else:
        return ""
# Streamlit app UI
st.title("SoulBuddy - AI-Powered Spiritual Guide")
st.subheader("Provide Your Details for Personalized Guidance")

# Collect user input
name = st.text_input("Name", placeholder="Enter your full name")
dob = st.date_input("Date of Birth")
time_of_birth = st.text_input("Time of Birth (HH:MM)", placeholder="e.g., 14:30")
gender = st.radio("Gender", ["Male", "Female", "Other"])
state = st.text_input("State", placeholder="e.g., Maharashtra")
city = st.text_input("City", placeholder="e.g., Pune")

# Action button
if st.button("Get Your Spiritual Guidance"):
    if not name or not time_of_birth or not state or not city:
        st.error("Please fill in all required fields!")
    else:
        # Prepare message for Langflow
        message = f"""
        Name: {name}
        Date of Birth: {dob.strftime('%Y-%m-%d')}
        Time of Birth: {time_of_birth}
        Gender: {gender}
        State: {state}
        City: {city}
        """
        st.info("Connecting to SoulBuddy for guidance...")
        
        # Call the Langflow API
        try:
            response = run_flow(message, tweaks=TWEAKS)

            # Process and display the response
            if "outputs" in response:
                outputs = response["outputs"]
                for output in outputs:
                    st.subheader("Spiritual Guidance")
                    st.write(f"**Input:** {output['inputs']['input_value']}")
                    for item in output.get("outputs", []):
                        if "results" in item:
                            message = item["results"].get("message", {})
                            if isinstance(message, dict):
                                # Render structured message
                                for key, value in message.items():
                                    st.write(f"**{key.capitalize()}:** {value}")
                            else:
                                st.write(message)
            else:
                st.error("Unexpected response format. Please try again.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.caption("Powered by Langflow and Streamlit")
