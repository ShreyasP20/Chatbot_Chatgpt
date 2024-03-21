from flask import Flask, render_template, request
# import openai
import pathlib
import textwrap

import google.generativeai as genai
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

app = Flask(__name__)
genai.configure(api_key='AIzaSyB2ykTpIgDjPe59LxWAIw_6QYjLdwrmNAA')
# Set up OpenAI API credentials
# openai.api_key = 'AIzaSyB2ykTpIgDjPe59LxWAIw_6QYjLdwrmNAA'
model = genai.GenerativeModel('gemini-pro')

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    
    
    # completion = openai.chat.completions.create(
    # model="gpt-3.5-turbo",
    # messages=[
    #     {"role": "user", "content": message}
    # ]
    # )
    print(message)
    response = model.generate_content(message)
    print(response.text)
    res=to_markdown(response.text)
    if res!=None:
        return str(response)
    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
