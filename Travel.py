import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

sec_key="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"
os.environ["HUGGINGFACEHUB_API_TOKEN"]=sec_key

# repo_id="Qwen/Qwen2.5-1.5B-Instruct"
repo_id="microsoft/Phi-3-mini-4k-instruct"

llm = HuggingFaceEndpoint(repo_id=repo_id,temperature=0.7, max_length=128)


st.title("Customized Travel Recommendations")

n_days=st.text_input("Enter your vacation days as a number:")
country=st.text_input("what country you hope to Travel:")
Ques = st.text_input("Enter your question:" )

prompt = PromptTemplate(
    input_variables=["days", "country", "question"],
    template=(
        "You are an AI assistant designed to provide detailed and accurate responses based on user input. "
        "The user will specify a number of days, a country, and a question. Use this information to generate "
        "a tailored response, considering the given context, location, and time frame.\n\n"
        "Input:\n"
        "Number of Days: {days}\n"
        "Country: {country}\n"
        "Question: {question}\n\n"
        "Output:\n"
        "Provide a detailed and actionable response to the user's query."
    )
)


llm_chain = LLMChain(llm=llm, prompt=prompt)
# Generate the response on user input
if st.button("Generate Recommendation"):
    if n_days and country and Ques:
        try:
            response = llm_chain.run({"days": n_days, "country": country, "question": Ques})
            st.write("### Your Customized Recommendation:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please fill in all fields before generating a recommendation.")