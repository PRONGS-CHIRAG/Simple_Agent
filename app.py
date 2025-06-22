from smolagents import CodeAgent,DuckDuckGoSearchTool, HfApiModel,load_tool,tool
import datetime
import requests
import pytz
import yaml
from tools.final_answer import FinalAnswerTool

from Gradio_UI import GradioUI

# Below is an example of a tool that does nothing. Amaze us with your creativity !
@tool
def get_temperature(city:str)-> str: #it's import to specify the return type
    #Keep this format for the description / args / args description but feel free to modify the tool
    """A tool that fetches the current temperature given the city name or location name
    Args:
        city: A string representing the city name or location (e.g., 'New York').
    """
    url = f"https://wttr.in/{city}?format=%t"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            temperature = response.text.strip()
            print(f"The current temperature in {city} is {temperature}")
            return f"The current temperature in {city} is {temperature}"
        else:
            print(f"Error fetching weather for {city}: HTTP {response.status_code}")
            return f"Error fetching weather for {city}: HTTP {response.status_code}"
    except Exception as e:
        print(f"Request failed: {e}")

@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """A tool that fetches the current local time in a specified timezone.
    Args:
        timezone: A string representing a valid timezone (e.g., 'America/New_York').
    """
    try:
        # Create timezone object
        tz = pytz.timezone(timezone)
        # Get current time in that timezone
        local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"The current local time in {timezone} is: {local_time}"
    except Exception as e:
        return f"Error fetching time for timezone '{timezone}': {str(e)}"


final_answer = FinalAnswerTool()

# If the agent does not answer, the model is overloaded, please use another model or the following Hugging Face Endpoint that also contains qwen2.5 coder:
# model_id='https://pflgm2locj2t89co.us-east-1.aws.endpoints.huggingface.cloud' 

model = HfApiModel(
max_tokens=2096,
temperature=0.5,
model_id='Qwen/Qwen2.5-Coder-32B-Instruct',# it is possible that this model may be overloaded
custom_role_conversions=None,
)


# Import tool from Hub
image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True)

with open("prompts.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)
print("TOOLS:", [final_answer, get_temperature, get_current_time_in_timezone, image_generation_tool])
prompt_templates["final_answer"] = {
    "pre_messages": [
        {"role": "system", "content": "You are a helpful assistant. Return the final answer clearly."}
    ],
    "format": "{output}",
    "post_messages": []
}
agent = CodeAgent(
    model=model,
    tools=[final_answer,get_current_time_in_timezone,get_temperature,image_generation_tool], ## add your tools here (don't remove final answer)
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    prompt_templates=prompt_templates
)


GradioUI(agent).launch()