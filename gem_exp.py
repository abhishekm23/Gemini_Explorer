import vertexai
import streamlit as st
from vertexai import init, preview
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession, GenerationConfig

### Vertex AI: The vertexai library is imported along with specific components like init and preview, used to set up and interact with Vertex AI services.
### Streamlit: It's being used here to create the user interface for the chat application.
### Generative Models: Imports specific classes needed to manage the large language model, including initiating sessions and sending messages.

# (Initializes the Vertex AI client with my Google Cloud project ID.)
init(project="gemini-explorer-424707")

# GenerationConfig: Configures the model's behavior, such as the temperature, which influences the randomness of the responses.
config = GenerationConfig(temperature=0.4)

# Loads the generative model with config
model = GenerativeModel("gemini-pro", generation_config=config)

# start_chat: Starts a chat session with the model.
chat = model.start_chat(response_validation=False)

# helper function to display and send streamlit messages
def llm_function(chat: ChatSession, query):
    response = chat.send_message(query) #define response that sending 'query' over to the ChatSession
    output = response.candidates[0].content.parts[0].text # the response may include multiple candidates and function extracts the text from the first part of the first candidate.
    with st.chat_message("model"):
        st.markdown(output)
        
    st.session_state.message.append( # here we append the user prompt into session memory
        {
            "role": "user",
            "content": query,
        }
    )
    
    st.session_state.message.append(  # here we append the model output 
        {
            "role": "model",
            "content": output,
        }
    )
        
st.title("Gemini Explorer Chat")

# Initialize chat session
if "message" not in st.session_state:
    st.session_state.message = [] 
    
# (Iterates through saved messages in history and displays them, also appending them to the chat's history to maintain state.)
for index, message in enumerate(st.session_state.message):
    # create a variable holding Content class with two parameters "role" and "parts", corresponding to "role" and "content" in 'session_state'
    content = Content(
        role=message["role"],   # stores as a string
        parts=[Part.from_text(message["content"])]  # stores multiple things as an array
    )
    with st.chat_message(message["role"]):  # Used the correct role variable here
        st.markdown(message["content"])
        
    chat.history.append(content) # Important : appends to make it a interactive conversation with a 'user' role followed by a 'model' role
    
# Initial Message behind following up the conversation( This triggers the system prompt, by checking if initial message is there or not!)
if len(st.session_state.message) == 0:  
    initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive."
    llm_function(chat, initial_prompt)
    
# For capture user input
query = st.chat_input("Gemini Explorer")
if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)