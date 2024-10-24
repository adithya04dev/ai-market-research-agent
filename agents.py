#creating agents
from crewai import Agent, Task, Crew,Process,LLM
import os 
from dotenv import load_dotenv
load_dotenv()
from tools import search_tool,scrape_tool,pdf_tool
llm=LLM(model='openai/Qwen/Qwen2.5-72B-Instruct-Turbo',api_key=os.getenv('TOGETHER_API_KEY'),api_base='https://api.together.xyz')


industry_researcher = Agent(
    role="Industry Research Specialist",
    goal="Conduct thorough research on this company/industry {company} to understand their key offerings and strategic focus areas",
    backstory="""You are an expert in industry analysis with years of experience in 
    market research. Your ability to quickly grasp the nuances of various industries 
    and identify key players and trends is unparalleled. You use your skills to 
    provide comprehensive insights that form the foundation for strategic decision-making.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, scrape_tool],
    llm=llm,
    max_rpm=20,
    max_iter=20
)

# Agent 2: Market Standards & Use Case Generator
use_case_generator = Agent(
    role="AI Use Case Strategist",
    goal="Reasearch industry trends in this company/industry {company} domain .",
    backstory="""With a deep understanding of GenAI, AI and ML technologies, you excel at 
    identifying innovative applications across various industries. Your expertise 
    lies in bridging the gap between cutting-edge technology and practical business 
    needs, consistently proposing transformative solutions that drive efficiency 
    and growth.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, scrape_tool,pdf_tool],
    llm=llm,
    max_rpm=20,
    max_retry_limit=20
)

# Agent 3: Resource Asset Collector
resource_collector = Agent(
    role="AI Resource Specialist for this company/industry {company}",
    goal="Collect and curate relevant datasets and resources for proposed AI use cases",
    backstory="""You are a master at navigating the vast landscape of AI and ML 
    resources. With your extensive knowledge of datasets, libraries, and AI tools, 
    you excel at finding the perfect resources to support AI initiatives. Your 
    ability to match business needs with appropriate technical assets is crucial 
    for successful AI implementation.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, scrape_tool],
    llm=llm,
    max_rpm=20,
    max_retry_limit=20
)