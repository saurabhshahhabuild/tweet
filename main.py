from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import streamlit as st
import os

os.environ['GOOGLE_API_KEY'] = "AIzaSyBefhFGtFPGoi4tWIrvNfPk3ePDshxvmAU"

# Initialize Google's Gemini model
gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")



# Create prompt template for generating tweets

tweet_template = "Give me {number} tweets on {topic} in {language} language"
tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ['number', 'topic', 'language'])


# Create LLM chain using the prompt template and model
tweet_chain = tweet_prompt | gemini_model

#-------------------------------Streamlit UI------------------------

st.header("Tweet Generator - this is a new change")
st.subheader("Generate tweets using Generative AI")
st.html(
    """<div>
        <image style="width:50%" src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Logo_of_Twitter.svg/934px-Logo_of_Twitter.svg.png"/>
    </div>""")
language = st.selectbox("Pick one", ["hindi", "english"])
topic = st.text_input("Topic")
number = st.number_input("Number of tweets", min_value = 1, max_value = 10, value = 1, step = 1)

if st.button("Generate"):
    tweets = tweet_chain.invoke({"number" : number, "topic" : topic, "language" : language})
    st.write(tweets.content)
    
