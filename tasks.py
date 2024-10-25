from crewai import Task
from agents import  industry_researcher,use_case_generator,resource_collector
# creating tasks
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
        "Research by searching internet,then reading the articles using links,or searching in pdfs . ( Undersatand how you can use use tool for each of given task and call with correct inputs ) "
        "Generate relevant use cases where the company can leverage GenAI, LLMs, and ML technologies and research how it could be implemented by searching about libraries/frameworks "
        "First use the tools by passing  correct input formats..then after reasearching finally return "
        "A list of 4-5 GenAI/AI/ML use cases for this company/industry and description(around 2 lines),and how it could be implemented. about it  {company}\n"
    ),
    expected_output=(
       
        " After using tools with correct input formats for researching then finally return  list of 4-5 GenAI/AI/ML use cases for this company/industry and description(around 2 lines) and how it could be implemented . "


    ),
    agent=use_case_generator
)

# Task for Resource Asset Collector Agent
resource_collection_task = Task(
    description=(
        "For each Generative AI or AI/ML use case generated for this company/industry {company}, find relevant resources(i.e datasets/tools/libraries ). "
        "Search platforms like Kaggle, HuggingFace, and GitHub for applicable datasets or open-source tools or frameworks that could be used for implementation. "
        "Remember don't ever try to open/scrape any kaggle/hugging face datasets as they are of huge size. "
        "Just try to understand by seeing name of the dataset, if you find it relevant then list them."
        "Remember don't makeup/hallucinate to create links on your own..return only found links from the search tool."
    ),
    expected_output=(

    """  
    After using tools with correct input formats  for finding then finally return


   -A curated list of top use cases  that contains description,how it could be implemented, impactit could have ,relevant resources/References (2-3 are enough).
    -Remember don't makeup/hallucinate to create links on your own..return only found links from the search tool.


        """




    ),
    agent=resource_collector
)
