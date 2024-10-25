## Description  
A market research tool built with CrewAI that analyzes companies and industries, generates relevant use cases , and identifies implementation resources. 
Simplifies the process of gathering strategic business insights.     
  


## Architecture Flow Chart
![Architecture Diagram 1](./images/Screenshot%202024-10-25%20115531.png)
![Architecture Diagram 2](./images/Screenshot%202024-10-25%20115702.png)

## Output Screenshots

### 1. Market Researcher's Response
![Market Research Output 1](./images/Screenshot%202024-10-25%20124129.png)
![Market Research Output 2](./images/Screenshot%202024-10-25%20124138.png)

### 2. Use Case Agent's Response
![Use Case Output](./images/Screenshot%202024-10-25%20124204.png)

### 3. Final Report
![Final Report 1](./images/Screenshot%202024-10-25%20124212.png)
![Final Report 2](./images/Screenshot%202024-10-25%20124219.png)
  


## Frameworks/Tools used   
-Crew AI -for building multiple agents.   
-CrewAI tools SerperDev for searching internet,ScrapeWebsite for scraping webpage dataPDFSearchTool for searching through pdf reports.      
  
## Learning Resources  
CrewAI docs : https://docs.crewai.com/introduction  
Deeplearnig.ai short course : https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/  


## Installation  and Seup
1.clone repo  
```
git clone https://github.com/adithya04dev/ai-market-research-agent.git  
```
2.create environment and activate  
```
python -m venv venv    
cd venv    
.\venv\scripts\activate   
```
3.install requirements  
```
pip install - r requirements.txt   
```
4. set serper,together api key in .env file
5. Run streamlit app 
```  
streamlit run app.py  
```

