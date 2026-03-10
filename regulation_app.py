import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key = st.secrets["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com"
)

st.title("AI Regulatory Research Assistant")

country = st.selectbox(
    "Country/Region",
    ["Global", "EU", "Russia", "Saudi Arabia", "Central Asia"]
)

domain = st.selectbox(
    "Regulation Domain",
    ["Cybersecurity", "Data Privacy", "Connectivity", "Safety"]
)

question = st.text_input("Ask a regulation question")

def ask_llm(country, domain, question):

    prompt = f"""
You are an automotive regulation expert.

Country: {country}
Domain: {domain}

Question:
{question}

Provide:
1. Key regulations
2. Technical requirements
3. Certification implications
"""

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are an automotive regulation expert."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


if st.button("Search Regulation"):

    if question:

        with st.spinner("Analyzing regulations..."):

            result = ask_llm(country, domain, question)

        st.write(result)