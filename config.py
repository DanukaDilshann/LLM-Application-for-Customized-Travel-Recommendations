from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

sec_key="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"
os.environ["HUGGINGFACEHUB_API_TOKEN"]=sec_key

# repo_id="Qwen/Qwen2.5-1.5B-Instruct"
repo_id="microsoft/Phi-3-mini-4k-instruct"

llm = HuggingFaceEndpoint(repo_id=repo_id,temperature=0.7, max_length=128)