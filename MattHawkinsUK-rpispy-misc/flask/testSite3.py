from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
  data=['Index Page','My Header','red']
  return render_template('template1.html',data=data)

@app.route("/hello")
def hello():
  data=['Hello Page','My Header','orange']
  return render_template('template1.html',data=data)
 
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)
