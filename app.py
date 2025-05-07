import streamlit as st
from user import get_user_info
from translator import translate_text

st.set_page_config(page_title="🍔 BurgerBot AI", layout="centered")

# --- Chat UI Styling ---
st.markdown("""
    <style>
        .user-msg {
            background-color: #DCF8C6;
            padding: 10px 15px;
            border-radius: 20px;
            margin: 10px 0;
            text-align: right;
        }
        .bot-msg {
            background-color: #F1F0F0;
            padding: 10px 15px;
            border-radius: 20px;
            margin: 10px 0;
            text-align: left;
        }
        .chat-container {
            max-width: 700px;
            margin: auto;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="chat-container">', unsafe_allow_html=True)

# --- App Title & Intro ---
st.title("🤖 BurgerBot AI Assistant")
st.markdown("How can I assist you today? Ask me anything related to food, orders, or support!")

# --- Collect User Info ---
user_data = get_user_info()

st.markdown("---")

# --- Chat Input ---
question = st.text_input("💬 Your Message", placeholder="e.g., Do you have vegetarian options?")

# --- Response Logic ---
if question:
    # Show user message styled
    st.markdown(f'<div class="user-msg">{question}</div>', unsafe_allow_html=True)

    # Simulate AI thinking...
    with st.spinner("BurgerBot is typing..."):
        bot_response = f"Hi {user_data['name']}! Let me help you with: '{question}'"
        translated = translate_text(bot_response, user_data["region"])
        st.markdown(f'<div class="bot-msg">{translated}</div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
