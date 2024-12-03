import openai
import streamlit as st
import os

# OpenAI API 키 설정 (env 파일에서 불러오기)
openai.api_key = os.getenv("OPENAI_API_KEY")  # env 파일에서 API 키 불러오기

# Streamlit UI 설정
st.title("AI Poet")

# 키워드 입력받기
keyword = st.text_input("키워드를 입력하세요:")

# 버튼 클릭 시 시 생성
if st.button("시 작성"):
    if keyword:
        # 최신 API 방식으로 시 생성 요청
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # 사용할 모델 (GPT-3.5 또는 GPT-4)
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"'{keyword}'을(를) 주제로 한 시를 작성해 주세요."},
            ]
        )

        # 시 생성 결과 출력
        st.write("생성된 시:")
        st.write(response['choices'][0]['message']['content'].strip())
    else:
        st.write("키워드를 입력해주세요.")
