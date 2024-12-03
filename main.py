import openai
import streamlit as st

# 여기에 당신의 OpenAI API 키를 입력하세요.
openai.api_key = "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"

# Streamlit 앱 제목
st.title("AI Poet")

# 사용자가 입력할 키워드 입력창
keyword = st.text_input("Enter a keyword")

# "Generate Poem" 버튼 생성
if st.button("Generate Poem"):  # 버튼을 눌렀을 때 실행되는 코드
    if keyword:  # 키워드가 입력되었을 때만 시 생성
        # OpenAI API를 호출하여 시를 생성하는 코드
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Write a poem about {keyword}.",
            max_tokens=150
        )
        poem = response.choices[0].text.strip()
        
        # 생성된 시 출력
        st.write(poem)
    else:
        st.warning("Please enter a keyword.")
