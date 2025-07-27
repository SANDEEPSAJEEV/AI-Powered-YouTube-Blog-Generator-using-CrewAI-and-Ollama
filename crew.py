from crewai import Crew,Process
from tools import yt_tool

from agents import blog_researcher,blog_writer
from tasks import researcher_task,write_task


crew=Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
    
)




##Start the task execution process with enhanced feedback
result=crew.kickoff(input={'topic':'Survive 100 Days Trapped In A Private Jet, Keep It'})
print(result)