import openai
import streamlit as st
import os

# OpenAI API 키 설정 (env 파일에서 불러오기)
openai.api_key = os.getenv("OPENAI_API_KEY")  # 여기서 OPENAI_API_KEY는 env 파일에서 가져옵니다.

# Streamlit UI 설정
st.title("AI Poet")

# 키워드 입력받기
keyword = st.text_input("키워드를 입력하세요:")

# 버튼 클릭 시 시 생성
if st.button("시 작성"):
    if keyword:
        # OpenAI GPT 모델을 사용하여 시 생성
        response = openai.Completion.create(
            engine="text-davinci-003",  # 사용하려는 GPT 모델 (최신 모델은 "gpt-3.5-turbo" 또는 "gpt-4")
            prompt=f"'{keyword}'을(를) 주제로 한 시를 작성해 주세요.",
            max_tokens=150
        )

        # 시 생성 결과 출력
        st.write("생성된 시:")
        st.write(response.choices[0].text.strip())
    else:
        st.write("키워드를 입력해주세요.")
