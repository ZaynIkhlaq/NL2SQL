# Set up Streamlit interface
import streamlit as st
from agent import agent_executor

st.title("NL2SQL Agent")
st.write("Agent has full context of the database and can answer any query")

# Create a text input for user queries with a more descriptive placeholder
user_query = st.text_input(
    "Ask a question about the database",
    placeholder="e.g. How many users are in the database?",
    help="Enter your question in natural language and I'll translate it to SQL"
)

# Add a container for the response
response_container = st.container()

# Process query when entered
if user_query:
    with st.spinner('Analyzing your question...'):
        # Process the query using the agent executor
        events = agent_executor.stream(
            {"messages": [("user", user_query)]},
            stream_mode="values",
        )
        
        # Display the response in the container
        with response_container:
            # Create a list to store all events
            all_events = list(events)
            
            # Display previous responses in expanders
            if len(all_events) > 1:
                with st.expander("See intermediate steps"):
                    for event in all_events[:-1]:
                        st.info(event["messages"][-1].content)
            
            # Always show the final response
            st.info(all_events[-1]["messages"][-1].content)
