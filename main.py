import openai
import streamlit as st

# OpenAI API 키 설정
openai.api_key = "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"

# Streamlit UI
st.title("AI Poet")

# 키워드 입력
keyword = st.text_input("Enter a keyword")

if st.button("Generate Poem"):
    if keyword:
        try:
            # OpenAI API 호출 - ChatCompletion 방식 사용
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # GPT 모델 설정
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Write a poem about {keyword}."},
                ]
            )
            
            # 결과 출력
            poem = response['choices'][0]['message']['content']
            st.write(poem)

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Please enter a keyword.")
