from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Virtual TA Project deployed successfully!"

if __name__ == '__main__':
    app.run()
