from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return "<html><body><h1>Test site running under Flask</h1></body></html>"

@app.route("/hello")
def hello():
  return "<html><body><h1>This is the hello page</h1></body></html>"
 
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
