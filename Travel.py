import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from src.config import llm
from src.prompt_temp import prompt









#streamli
st.title("🌍 GlobeGuide")
n_days=st.text_input("Enter your vacation days as a number:")
country=st.text_input("what country you hope to Travel:")
Ques = st.text_input("Enter your question:" )


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