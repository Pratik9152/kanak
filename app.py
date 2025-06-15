import streamlit as st
from utils import get_answer

st.set_page_config(
    page_title="IRCLASS Payroll Chatbot",
    layout="wide",
    page_icon="🤖"
)

# Background gradient styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
            color: white;
        }
        .stApp {
            background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
            color: white;
        }
        .title h1, .markdown-text-container h1, .markdown-text-container h2, .markdown-text-container h3 {
            color: #00ffd5;
        }
        .block-container {
            padding: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 IRCLASS Payroll Chatbot")
st.markdown("""
Welcome to the intelligent payroll assistant for Indian Register of Shipping.

🧾 Ask payroll-related queries in **English, Hindi, Tamil, Kannada, Bengali**
📎 Trained on official IRCLASS Employee Handbook & Policy PDF
""")

st.markdown("---")

query = st.text_input("💬 Enter your payroll question:")

if query:
    with st.spinner("🔍 Thinking like HR..."):
        answer = get_answer(query)
        st.markdown("""
        <div style='padding: 1rem; background-color: #ffffff20; border-radius: 10px;'>
        <h4>📌 Answer:</h4>
        <p>{}</p>
        </div>
        """.format(answer), unsafe_allow_html=True)

st.markdown("---")

st.subheader("📄 About IRCLASS Payroll Bot")
try:
    with open("about_us.md", "r", encoding="utf-8") as f:
        st.markdown(f.read())
except:
    st.info("About information not available.")

st.markdown("""
---
🔐 [Go to Admin Panel](https://your-app-name.streamlit.app/admin/panel) *(Password required)*
""")
