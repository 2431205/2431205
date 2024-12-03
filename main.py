import streamlit as st

st.title("AI Poet")

# 사용자 입력을 받는 텍스트 박스
user_input = st.text_area("Type something for the AI Poet to generate:")

# AI가 생성한 텍스트 출력
if user_input:
    # 여기에 AI 모델을 통해 텍스트 생성하는 코드 추가
    generated_text = "Generated text based on: " + user_input
    st.write(generated_text)
