import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config import llm

#streamli
st.title("🌍 GlobeGuide")

n_days=st.text_input("Enter your vacation days as a number:")
country=st.text_input("what country you hope to Travel:")
Ques = st.text_input("Enter your question:" )



prompt = PromptTemplate(
    input_variables=["days", "country", "question"],
    template=(
        "You are an AI assistant specialized in providing detailed, context-aware, and actionable responses. "
        "Your task is to interpret the input provided by the user and generate a customized reply. "
        "Focus on delivering accurate information that aligns with the user's specified time frame, "
        "location, and inquiry.\n\n"
        "### User Input ###\n"
        "- Number of Days: {days}\n"
        "- Country: {country}\n"
        "- Question: {question}\n\n"
        "### Instructions for Response ###\n"
        "1. Clearly acknowledge the input details (time frame, location, and question).\n"
        "2. Provide a detailed answer tailored to the specified number of days and the context of the country.\n"
        "3. Ensure the response is actionable and relevant to the user's query.\n"
        "4. If applicable, include cultural, economic, or situational context for the country.\n"
        "5. Offer additional resources, examples, or references if necessary.\n\n"
        "### Response ###\n"
        "Generate a clear and structured reply that directly addresses the user's question while considering "
        "the specified time frame and location. Be concise yet comprehensive, ensuring the user has a complete "
        "understanding and next steps if required."
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





# for testing


if st.button("Test Example Question"):
    d=10
    cou="Sri Lanka"
    que="what are the best places to visit in Sri Lanka ?"
    with st.spinner("Generating response for test question..."):
        test_res=llm_chain.run({"days" : d,"country" : cou,"question" : que})
        st.write("### Test Response:")
        st.write(test_res)