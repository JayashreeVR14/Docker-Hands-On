from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello User! This Flask app runs inside Docker"
if__name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
