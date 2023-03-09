import os

import dotenv
import openai
from flask import Flask, render_template, request

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
  prompt = request.form['prompt']
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=1,
    messages=[
        {"role": "user", "content": prompt}
    ]
  )

  message = response["choices"][0]["message"]["content"]
  return render_template('index.html', message=message)

if __name__ == '__main__':
  port = int(os.getenv('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
