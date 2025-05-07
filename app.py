
import streamlit as st
from agent import agent_executor


st.title("NL2SQL Agent")
st.write("Agent has full context of the database and can answer any query")
st.subheader("Database Schema")
st.image("schema.png")

st.write("""
This database contains information about:
- Customers and their details
- Employees and reporting structure  
- Invoices and line items
- Music tracks, albums, artists and genres
- Playlists and playlist tracks

You can ask questions about any (literally any) of these entities and their relationships. Ask it to do something you would tell a human sql engineer to do.
""")

st.divider()

user_query = st.text_input(
    "Ask a question about the database",
    placeholder="e.g. How many users are in the database?",
    help="Enter your question in natural language and I'll translate it to SQL"
)

response_container = st.container()





if user_query:
    with st.spinner('Analyzing your question...'):
        events = agent_executor.stream(
            {"messages": [("user", user_query)]},
            stream_mode="values",
        )
        
        with response_container:
            all_events = list(events)
            
            if len(all_events) > 1:
                with st.expander("See agentic workflow"):
                    for event in all_events[:-1]:
                        st.info(event["messages"][-1].content)
            st.success(all_events[-1]["messages"][-1].content)
