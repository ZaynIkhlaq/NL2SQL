# Set up Streamlit interface
import streamlit as st
from agent import graph
st.title("NL2SQL") 
st.write("Ask questions about the Chinook music database!")

# Create a text input for user questions
user_query = st.text_input("Enter your question about the music database:")

if user_query:
    # Display a spinner while processing
    with st.spinner("Processing your question..."):
            # Get response from graph
            response = graph.invoke({"question": user_query})
            
            # Create columns for displaying SQL and results
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("SQL Query")
                # Display the generated SQL query in a code block
                st.code(response["query"], language="sql")
            
            with col2:
                st.subheader("Query Results") 
                # Display the raw query results
                st.json(response["result"])
            
            # Display the final answer
            st.subheader("Answer")
            st.write(response["answer"])
            