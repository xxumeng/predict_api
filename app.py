from flask import Flask
app = Flask(__name__)

@app.route('/getJson')
def get_json():
    return 'Hello, World!'