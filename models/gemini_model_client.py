from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv

# load_dotenv()

def get_model_client():
    openai_model_client = OpenAIChatCompletionClient(
        model="gemini-2.5-flash",
        api_key=os.getenv('GEMINI_API_KEY')  or "AIzaSyB4V4UF7nqItjx1-0pMhH58CibeCUe40V4"
    )

    return openai_model_client