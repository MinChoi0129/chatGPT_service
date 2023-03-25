from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

# OpenAI API key 가져오기
with open('api_key', 'r') as f:
    openai.api_key = f.readline()

# 템플릿 렌더링
@app.route("/")
def home():
    return render_template("index.html")

# 답변 생성
@app.route("/answer", methods=["POST"])
def answer():
    # 사용자 입력 가져오기
    user_input = request.form.get("input_text")

    # OpenAI API 호출
    response = openai.Completion.create(
        engine="davinci",
        prompt=user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # 답변 추출
    answer = response.choices[0].text.strip()

    # 템플릿 렌더링
    return render_template("index.html", input_text=user_input, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
