import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader

def main():
    st.title("Gemini API와 Streamlit 연동")

    # 사용자로부터 API 키 입력 받기
    api_key = st.text_input("API Key를 입력하세요:", type="password")

    if api_key:
        # Gemini API 초기화
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')

        # PDF 파일 업로드
        uploaded_file = st.file_uploader("PDF 파일을 업로드하세요", type="pdf")

        if uploaded_file is not None:
            # PDF 파일 처리
            pdf_reader = PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            # 사용자 질문 입력
            user_question = st.text_input("PDF에 대해 질문하세요:")

            if user_question:
                try:
                    # API 호출
                    response = model.generate_content([
                        f"다음 PDF 내용을 바탕으로 질문에 답변해주세요.\n\nPDF 내용: {text}\n\n질문: {user_question}"
                    ])
                    st.write("답변:", response.text)
                except Exception as e:
                    st.error(f"API 호출 중 오류가 발생했습니다: {str(e)}")

if __name__ == "__main__":
    main()
