from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_experimental.tools import PythonREPLTool

from config import TAVILY_API_KEY

tavily_tool = TavilySearchResults(max_results=5, tavily_api_key=TAVILY_API_KEY)
python_repl_tool = PythonREPLTool(sanitize_input=True, response_format="content_and_artifact")