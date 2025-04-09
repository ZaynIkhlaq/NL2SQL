from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from testdb import db
from llm import llm
from langchain_community.tools.sql_database.tool import (
    InfoSQLDatabaseTool,
    ListSQLDatabaseTool,
    QuerySQLCheckerTool,
    QuerySQLDatabaseTool,
)
from langchain import hub
from langgraph.prebuilt import create_react_agent


toolkit = SQLDatabaseToolkit(db=db, llm=llm)

prompt_template = hub.pull("langchain-ai/sql-agent-system-prompt")

assert len(prompt_template.messages) == 1
print(prompt_template.input_variables)

system_message = prompt_template.format(dialect="SQLite", top_k=5)
agent_executor = create_react_agent(llm, toolkit.get_tools(), prompt=system_message)