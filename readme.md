# 💬 My Web Chatbot

A simple web-based chatbot built with **Flask**, **Bootstrap**, and **OpenAI API**.  
Supports dark/light mode toggle, chat bubbles, and responsive mobile-friendly design.

![screenshot](your-screenshot.png) <!-- 여기에 실제 스크린샷 링크 넣으면 좋아요 -->

---

## 🚀 Features

✅ Conversational interface using OpenAI GPT  
✅ Clean Bootstrap design with chat bubbles  
✅ Dark/Light mode toggle  
✅ Mobile-responsive layout  
✅ Secure API key management via `.env`

---

## 🖥️ Demo

> [Optional] Add link if deployed

---

## ⚙️ Installation

1️⃣ Clone the repository

```bash
git clone https://github.com/YonghoLee79/my_web_chatbot.git
cd my_web_chatbot


2️⃣ Install dependencies

bash
코드 복사
pip install -r requirements.txt
3️⃣ Add your OpenAI API key

Create a .env file in the project root:

ini
코드 복사
OPENAI_API_KEY=your_api_key_here
4️⃣ Run the server

bash
코드 복사
flask run
5️⃣ Visit in browser

cpp
코드 복사
http://127.0.0.1:5000
📱 Screenshots
Add images here to show the UI

📂 Project Structure
bash
코드 복사
my_web_chatbot/
│
├── app.py               # Flask server
├── templates/
│   └── chat.html        # Frontend template
├── static/
│   ├── style.css        # CSS styles
│   └── icons/           # Bootstrap icons if needed
├── .env                 # Your API key (DO NOT COMMIT!)
└── requirements.txt     # Python dependencies
🔒 API Key Management
Your OpenAI API key is stored securely in .env.

Make sure NOT to commit .env to GitHub.

Add .env to .gitignore.

✅ To-Do / Ideas
User authentication

Chat history persistence (DB)

Multilingual support

Deployment (Heroku, Fly.io)

📜 License
This project is licensed under the MIT License.

🙏 Acknowledgements
Flask

Bootstrap

OpenAI

