from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "hello docker flask"
if __name__ == '__main__':
    #for container
    app.run(host="0.0.0.0", port=5000)
    #for host
    #app.run(debug=True)
