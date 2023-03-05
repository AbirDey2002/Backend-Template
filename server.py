from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

# members api route
arr = []
for i in range(0,9):
  arr.append(i**i)
  
arrjson = jsonify(arr)

@app.route("/members")
def members():
  return {"members":arrjson}

if __name__ == "__main__":
  app.run(debug=True)