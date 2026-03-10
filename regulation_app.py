import streamlit as st
from openai import OpenAI

# ⚠️ 请替换为你的 DeepSeek API Key
DEEPSEEK_API_KEY = "sk-38152d265ffc42358b0b0f0c2cefbd33"
DEEPSEEK_BASE_URL = "https://api.deepseek.com"

# 初始化 AI 客户端
client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)

# Streamlit 页面标题
st.title("🚗 汽车法规 AI 研究助手")

st.write("""
这是一个自动化法规研究工具。
输入法规研究主题，AI 会输出结构化法规总结。
""")

# 用户输入框
query = st.text_input("请输入研究主题，例如：欧盟 座舱联网法规")

# 点击按钮触发研究
if st.button("开始研究"):

    if not query.strip():
        st.warning("请输入研究主题！")
    else:
        with st.spinner("AI 正在分析法规，请稍候..."):
            prompt = f"""
你是一名汽车法规研究专家。
请针对以下主题进行分析，并输出结构化总结：

主题: {query}

输出格式：
1. 国家/地区
2. 法规名称
3. 主管机构
4. 认证要求
5. 测试要求
6. 对汽车系统影响模块
"""

            try:
                response = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.3
                )

                result = response.choices[0].message.content
                st.subheader("📄 研究结果")
                st.text(result)

            except Exception as e:
                st.error(f"AI 请求失败: {e}")
