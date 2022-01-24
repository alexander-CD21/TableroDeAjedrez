from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')

def tableroAjedrez():
    return render_template("index.html",num1=8,x=8)

@app.route('/<int:x>')
def tableroAjedrezX(x):
    return render_template("index.html",x=x,num1=8)

@app.route('/<int:x>/<int:num1>')
def tableroAjedrezY(x,num1):
    return render_template("index.html",x=x,num1=num1)

@app.route('/<int:x>/<int:num1>/<string:color1>/<string:color2>')
def tableroAjedrezXY(x,num1,color1,color2):
    return render_template("index.html",x=x,num1=num1,color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)