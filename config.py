from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

from dotenv import load_dotenv

load_dotenv()

os.environ['HUGGINGFACEHUB_API_TOKEN'] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# repo_id="Qwen/Qwen2.5-1.5B-Instruct"
repo_id="microsoft/Phi-3-mini-4k-instruct"

llm = HuggingFaceEndpoint(repo_id=repo_id,temperature=0.7, max_length=128)
