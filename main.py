import openai
import streamlit as st

# API 키 설정
openai.api_key = "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"
# 제목과 설명을 위한 UI 구성
st.title("AI Poet")
st.write("Enter a keyword, and the AI will generate a poem based on it!")

# 키워드를 입력받기 위한 텍스트 박스
keyword = st.text_input("Enter a keyword:")

# 시 작성 버튼 클릭 시 처리
if st.button("Generate Poem"):
    if keywor
