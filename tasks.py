from crewai import Task
from tools import yt_tool

from agents import blog_researcher,blog_writer


researcher_task =Task(
    description=(
        "Identify the video{topic}."
        "Get detailed information about the video from the channel."
        
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the {topic}of video ',
    tools=[yt_tool],
    agent=blog_researcher,
)




write_task =Task(
    description=(
        "get the info from the youtube channel on the topic{topic}"
        
    ),
    expected_output='summarize the info from the youtube channel video on the topic{topic}and create the blog',
    tools=[yt_tool],
    agent=writer,
    async_execution=False,
    output_file='new-blog-post.md'
)