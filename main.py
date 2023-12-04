import os
from dotenv import load_dotenv
from openai import OpenAI
from flask import Flask, jsonify, request

load_dotenv()
client = OpenAI(api_key = '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')

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": "You are a recruiter for Data Scientists at one of the leading tech firms."},
      {"role": "user", "content": "Generate a typical behavioral interview question"}
  ]
)

print(completion.choices[0].message)

app = Flask(__name__)

@app.route('/behavioral-question', methods=['POST'])
def behavioral_question():
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
      {"role": "system", "content": "You are a recruiter for Data Scientists at one of the leading tech firms."},
      {"role": "user", "content": "Generate a typical behavioral interview question"}
      ],
      max_tokens=100
    )
    return jsonify(question=response.choices[0].text.strip())