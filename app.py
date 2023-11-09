from flask import Flask, render_template

app = Flask(__name__)


# make a homepage 
@app.route('/') 
def homepage():
    return render_template('base.html') 

@app.route('/hello')
def hello(name):
    listOfNames = [name, "Yoyo" , "Yennifer"]
    return render_template('name.html',  Sname = name, nameList = listOfNames) 

# Add the option to run this file directly
if __name__ == "__main__":
    app.run(debug=True)