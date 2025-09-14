import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("API key not found. Please set GEMINI_API_KEY in your .env file.")
    st.stop()

genai.configure(api_key=api_key)


model = genai.GenerativeModel("gemini-2.0-flash-001")


st.title("📰 AI News Summarizer & Q&A Tool 🚀")

# User inputs article
user_input = st.text_area("📌  your news article here:")

if user_input.strip():
    word_count = len(user_input.split())
    st.info(f"📝 Word count of article: {word_count} words")
    st.subheader("🔎 Summaries at Different Temperatures")
    temperatures = [0.1, 0.7, 1.0]

    # Generate summaries at different temperatures
    for temp in temperatures:
        prompt = f"Summarize the following article in 3-4 sentences:\n\n{user_input}"
        response_temp = model.generate_content(contents=prompt,
            generation_config={"temperature": temp}
        )
        st.markdown(f"**Summary (temperature={temp}):**")
        st.write(response_temp.text)

else:
    st.warning("Please paste an article above ⬆️")


if user_input.strip():
    st.subheader("💬 Ask Questions About the Article")

    ask_questions = st.text_area("Type your questions (one per line):")

    if ask_questions.strip():
        questions_list = ask_questions.split("\n")

        for q in questions_list:
            if q.strip():  # skip empty lines
                # Step 1: Check if question is related
                check_prompt = f"""
                Article: {user_input}
                Question: {q}
                Is this question related to the article? Answer only 'Yes' or 'No'.
                """
                check_response = model.generate_content(contents=check_prompt)
                is_related = check_response.text.strip().lower()

                # Step 2: Answer if related
                if "yes" in is_related:
                    prompt2 = f"Based on this article:\n{user_input}\nAnswer the question: {q}"
                    answer_response = model.generate_content(contents=prompt2)
                    st.markdown(f"### Q: {q}")
                    st.write(answer_response.text)
                else:
                    st.info(f"❌ '{q}' is not related to the article.")
