from flask import request
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Tu navegador web es %s</p>' % user_agent

if __name__ == '__main__':
    app.run(debug=True)
