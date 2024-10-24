from crewai import Agent, Task, Crew
from langchain_together import ChatTogether
from crewai import Crew, Process
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


from crewai_tools import ScrapeWebsiteTool, SerperDevTool, PDFSearchTool
load_dotenv()
os.environ['SERPER_API_KEY']=os.getenv('SERPER_API_KEY')
os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')
pdf_tool = PDFSearchTool()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-002")

# OR

# Initialize the tool with a specific PDF path for exclusive search within that document
pdf_tool = PDFSearchTool(pdf='.\report.pdf')

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

industry_researcher = Agent(
    role="Industry Research Specialist",
    goal="Conduct thorough research on this company/industry {company} to understand their key offerings and strategic focus areas",
    backstory="""You are an expert in industry analysis with years of experience in 
    market research. Your ability to quickly grasp the nuances of various industries 
    and identify key players and trends is unparalleled. You use your skills to 
    provide comprehensive insights that form the foundation for strategic decision-making.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool, scrape_tool]
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
    tools=[search_tool, scrape_tool,pdf_tool]
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
    tools=[search_tool, scrape_tool]
)


# Task for Industry Researcher Agent
industry_research_task = Task(
    description=(
        "Research and analyze this company/industry  {company}. "
        "Utilise the  tools to research, given to u.(use correct input formats to call the tool)"
        "Identify key offerings, strategic focus areas, and market position. "
        "Provide a comprehensive overview of the industry landscape, "
        "including major players, trends, and challenges."
        "First use the tools by passing  correct input formats..then after reasearching finally return "
        "a detailed report on this company/industry  {company}."
    ),
    expected_output=(
        " After using tools with correct input formats for researching the company,then finally return "
        "A detailed report on this company/industry  {company}, including:\n"
        "1. Company/Industry overview\n"
        "2. Key products/services\n"
        "3. Strategic focus areas\n"
        "4. Major competitors\n"
        "5. Current market trends\n"
        "6. Challenges and opportunities in the industry"

    ),
    agent=industry_researcher
)

# Task for Market Standards & Use Case Generator Agent
use_case_generation_task = Task(
    description=(
        "Undersand previous agent's response and Research and  analyze trends related to Generative or AI/ML in that particular domain/area. and finally generate 4-5 use cases for them. "
        "Resarch using the search-internet ,website scrape,pdf search tool given to u. ( use correct input format while calling the tool) "
        "Generate relevant use cases where the company can leverage GenAI, LLMs, and ML technologies. "
        "First use the tools by passing  correct input formats..then after reasearching finally return "
        "A list of 4-5 GenAI/AI/ML use cases for this company/industry and description about it  {company}\n"
    ),
    expected_output=(
       
        " After using tools with correct input formats for researching then finally return  list of 4-5 GenAI/AI/ML use cases for this company/industry and description. "


    ),
    agent=use_case_generator
)

# Task for Resource Asset Collector Agent
resource_collection_task = Task(
    description=(
        "For each Generative AI or AI/ML use case generated for this company/industry {company}, find relevant datasets, tools, and resources. "
        "Search platforms like Kaggle, HuggingFace, and GitHub for applicable datasets or open-source tools or frameworks that could be used for implementation. "
        "Remember don't ever try to open/scrape any kaggle/hugging face datasets as they are of huge size. "
        "Just try to understand by seeing name of the dataset, if you find it relevant then list them."
        "Remember don't makeup/hallucinate to create links on your own..return only found links from the search tool."
    ),
    expected_output=(

    """  
    After using tools with correct input formats  for finding then finally return


   -A curated list of top use cases  that contains description,impact,refernces.
    -Remember don't makeup/hallucinate to create links on your own..return only found links from the search tool.


        """



    ),
    agent=resource_collector
)

ai_use_case_crew = Crew(
    agents=[industry_researcher, use_case_generator, resource_collector],
    tasks=[industry_research_task, use_case_generation_task, resource_collection_task],
    process=Process.sequential,  # or hierarchical, depending on your preference
    llm=llm,
    
    verbose=True
)
def run(company):
    global ai_use_case_crew
    result = ai_use_case_crew.kickoff(inputs={'company':'CricViz'})
    return result