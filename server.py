from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'hello world!',200

@app.route("/calculator/add", methods=['POST'])
def add():
    try:
        data=request.json
        num1=data['first']
        num2=data['second']
        result=num1+num2
        response={
            "result":result
        }
        return jsonify(response),200
    except KeyError:
        return jsonify({"error":"Invalid"}),400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    try:
        data=request.json
        num1=data['first']
        num2=data['second']
        result=num1-num2
        response={
            "result":result
        }
        return jsonify(response),200
    except KeyError:
        return jsonify({"error":"Invalid"}),400

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
