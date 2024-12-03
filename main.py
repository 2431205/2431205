import openai
import streamlit as st

openai.api_key = "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"

# Streamlit 앱 제목
st.title("AI Poet")

# 사용자가 입력할 키워드 입력창
keyword = st.text_input("Enter a keyword")

if keyword:  # 조건문 뒤에 콜론 추가
    # OpenAI API를 호출하여 시를 생성하는 코드
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write a poem about {keyword}.",
        max_tokens=150
    )
    poem = response.choices[0].text.strip()
    
    # 생성된 시 출력
    st.write(poem)
