from flask import Flask, render_template, request, redirect, url_for
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key = os.environ.get("OPENAI_API_KEY")

# 대화 히스토리
messages = [
    {"role": "system", "content": "너는 친절한 AI 챗봇이야."}
]

@app.route("/", methods=["GET", "POST"])
def chat():
    global messages
    if request.method == "POST":
        user_input = request.form["user_input"]
        if user_input.strip() != "":
            # 사용자가 입력한 메시지를 히스토리에 추가
            messages.append({"role": "user", "content": user_input})

            # GPT 호출
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages
            )
            assistant_reply = response.choices[0].message.content.strip()
            messages.append({"role": "assistant", "content": assistant_reply})
    
    # 히스토리를 전부 전달해 렌더링
    return render_template("chat.html", messages=messages)

if __name__ == "__main__":
    app.run(debug=True)
