from flask import Flask, render_template, request, jsonify
import pathlib
import textwrap
import json
import google.generativeai as genai


app = Flask(__name__)
genai.configure(api_key='AIzaSyB2ykTpIgDjPe59LxWAIw_6QYjLdwrmNAA')
model = genai.GenerativeModel('gemini-pro')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
    message = request.json.get("message")
    response = model.generate_content(message)
    response_json = json.dumps({"content":response.text})
    if response!=None:
        return response_json
    else :
        return 'Failed to Generate response!'
    

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
