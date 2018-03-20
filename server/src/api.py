from readprep import *
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/get_nutritions', methods=['POST'])
def get_nutritions():
    if not request.json:
        abort(400)
    
    rezept = Rezept(request.json)
    return jsonify(rezept.returnJson())


if __name__ == '__main__':
     app.run(port=5000)