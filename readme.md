# NL2SQL - Natural Language to Structured Query Language 

## Overview
An advanced database management system that converts natural language queries into SQL commands, built as part of a Semester 4 project.

## 🚀 Live Demo
**[Try the demo here: nl2sqldb.streamlit.app](https://nl2sqldb.streamlit.app)**
> Will probably shut this down soon.

## ✨ Features
- Natural language to SQL query conversion
- In-memory SQLite database (using chinook.db as an example)
- Intelligent query analysis and execution
- Human-readable response formatting
- Built with LangChain's SQL operator

## 🔧 How It Works
1. **Input**: User asks questions about the database in plain English
2. **Analysis**: Agent analyzes and understands the user query
3. **Generation**: System generates appropriate SQL query
4. **Execution**: Query is executed against the database
5. **Output**: Results are returned in formatted, plain English

## 🛠️ Technology Stack
- **Framework**: Streamlit
- **Database**: SQLite (in-memory)
- **NLP**: LangChain SQL Operator
- **Language**: Python

## 📋 Requirements
- Python 3.x
- Streamlit
- LangChain
- SQLite3

## 🚀 Getting Started
```bash
# Clone the repository
git clone <repository-url>

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## 📝 Usage Examples
- "Show me all customers from New York"
- "How is the Invoice table related with the Customers?"
- "How many orders were placed last month?"

## 🤝 Contributing
Made this for my fourth semester. Bossman couldn't see the value. Hope Seecs will have better teachers in the future (low probability) 
Feel free to fork and use, you might have better luck than I did.
