from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

"""
///////////////////////
APP FLASK PADRAO
para começar do ZERO
///////////////////////
"""



app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('Html_Frame.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8001)
