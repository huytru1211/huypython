# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route("/")
# def index():
#     return render_template('index.html')
#
# if __name__ =="__main__":
#     app.run(debug=True)

from flask import Flask, Response
import json
app = Flask(__name__)
@app.route('/average/<num1>/<num2>')
def average(num1, num2):
    first_num = int(num1)
    second_num = int(num2)
    average = (first_num + second_num)/2

    response = {
        "first number" : first_num,
        "second number" : second_num,
        "average" : average,
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=200, mimetype="application/json")
    return http_response

if __name__ == '__main__' :
    app.run(use_reloader = True, host='127.0.0.1',port=5000)
