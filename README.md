# Soul_buddy
# SoulBuddy - AI-Powered Spiritual Guide

SoulBuddy is an AI-powered spiritual guide that provides personalized spiritual guidance based on user input, such as name, date of birth, time of birth, and location. This application leverages Langflow's API, powered by **Datastax**, and Streamlit for building an interactive user interface.

## Features
- Personalized spiritual guidance based on user's birth details (Name, Date of Birth, Time of Birth, Gender, State, and City).
- Uses Langflow API, powered by Datastax, for AI-driven responses.
- Streamlit for an interactive, easy-to-use web interface.
  
## Requirements
- Python 3.x
- Streamlit
- Requests
- Langflow API access (API token, Langflow ID, Flow ID)
- Datastax-powered Langflow API integration

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Install the required Python packages:

    ```bash
    pip install streamlit requests
    ```

3. Update the API credentials:
    - Replace the `BASE_API_URL`, `LANGFLOW_ID`, `FLOW_ID`, and `APPLICATION_TOKEN` in the code with your own credentials.
    - The API is powered by **Datastax** for seamless data integration and flow execution.

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

5. Open the app in your browser.

## How It Works
- The user inputs personal details including name, date of birth, time of birth, gender, state, and city.
- Once the user clicks "Get Your Spiritual Guidance," the app sends these details to the Langflow API, powered by **Datastax**.
- The response from the API is processed and displayed in a structured format, showing personalized spiritual guidance.

## Code Explanation

### Langflow API Integration with Datastax
The `run_flow` function interacts with Langflow's API to retrieve responses based on user input. It takes the message and any optional tweaks as parameters. Langflow, powered by **Datastax**, ensures high-performance AI-driven insights.

### Text Extraction
The `extract_text` function processes the API response and extracts meaningful text from the nested structure of the response.

### Streamlit UI
The Streamlit UI consists of:
- A title and subheader for the app.
- Input fields for user details (Name, Date of Birth, Time of Birth, Gender, State, and City).
- An action button to trigger the API call and display the results.
- Error handling if any required fields are missing or if an error occurs during the API call.

yt: https://www.youtube.com/watch?v=aLScFLPVpAs

### Example Flow
- The user enters their details (Name, Date of Birth, etc.).
- They click "Get Your Spiritual Guidance."
- The app connects to the Langflow API, powered by **Datastax**, and processes the response.
- The results are displayed to the user in a readable format.

## Contributing
Feel free to submit issues, suggestions, or pull requests to improve the functionality or UI of the app.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Powered by Langflow and Streamlit, with data integration and flow execution provided by **Datastax**.
