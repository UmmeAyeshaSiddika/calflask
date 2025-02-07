from flask import Flask,request,render_template,jsonify
import json


app=Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to Flask"

@app.route('/calculator',methods=["GET"])
def math_operator():
    operation=request.json["operation"]
    numbers1=request.json["numbers1"]
    numbers2=request.json["numbers2"]

    if operation=="add":
        result=int(numbers1)+int(numbers2)
    elif operation=="multiply":
        result=int(numbers1)*int(numbers2)
    elif operation=="division":
        result=int(numbers1)/int(numbers2)
    else:
        result=int(numbers1)-int(numbers2) 
    
    return jsonify(result)               

if __name__=='__main__':

     app.run(debug=True)
