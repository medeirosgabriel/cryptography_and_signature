from flask import Flask

# create a server instance
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!\n"

# run the server
app.run(port=5000, debug=True, ssl_context=('./server.crt', './private.key'))