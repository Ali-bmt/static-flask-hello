from flask import Flask
print('flask app loaded')

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')