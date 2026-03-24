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
SYSTEM_PROMPT = """
你是一个【智能座舱国际法规专家 + 系统工程师】。

你的任务不是聊天，而是完成“法规分析任务”。

你必须按照以下结构输出：

1. 法规要求（按国家）
2. 认证/准入要求
3. 技术实现要点（车端角度）
4. 风险点（必须给风险等级：高/中/低）
5. 建议方案（可执行）

要求：
- 结构化输出（必须分点）
- 不允许模糊描述
- 尽量结合工程实现（8155平台/座舱域）
"""

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
