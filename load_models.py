from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.models.ollama import OllamaModel
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI model with API key from environment
OPENAI_MODEL = OpenAIModel(
    'gpt-3.5-turbo',  # Changed to a standard OpenAI model name
    api_key=os.getenv('OPENAI_API_KEY')
)

# Comment out Ollama model if not needed
# OLLAMA_MODEL = OllamaModel('llama3.1')

