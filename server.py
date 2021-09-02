from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def hello_name(name):
    print(name)
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_object(num, word):
    return f"Output: {num * word}"






if __name__=="__main__":
    app.run(debug=True)