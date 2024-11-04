import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyDp56YMGHW30tWC_GDugqq4ylpr_CFs0WI")

# Set up the model configuration
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Instantiate the model with configurations
model = genai.GenerativeModel(model_name="gemini-1.5-flash-002",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Initialize chat session in Streamlit
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Streamlit app title
st.title("Chatbot")

# Display chat history in Streamlit
for message in st.session_state.chat.history:
    with st.chat_message(message.role):
        st.markdown(message.parts[0].text)

# User input field
user_input = st.chat_input("Nhập tin nhắn của bạn...")

# Handling user input and generating a response
if user_input:
    # Display user message in chat
    st.chat_message("user").markdown(user_input)
    
    # Try generating the response from the assistant
    try:
        response = st.session_state.chat.send_message(user_input)
        assistant_response = response.parts[0].text  # Access text of response part
    except Exception as e:
        assistant_response = f"An error occurred: {e}"
    
    # Display assistant's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
