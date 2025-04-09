# Set up Streamlit interface
import streamlit as st
from agent import agent_executor

st.title("NL2SQL Chat Interface")
st.write("Ask questions about the Chinook music database!")

# Create a text input for user queries
user_query = st.text_input("Enter your query:")

# Button to submit the query
if st.button("Submit"):
    if user_query:
        # Process the query using the agent executor
        events = agent_executor.stream(
            {"messages": [("user", user_query)]},
            stream_mode="values",
        )
        
        # Display the response
        for event in events:
            st.write(event["messages"][-1].content)
    else:
        st.write("Please enter a query.")
