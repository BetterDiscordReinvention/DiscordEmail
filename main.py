from flask import *

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello There!"

app.run()