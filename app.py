from flask import Flask,render_template,redirect,url_for
app=Flask(__name__)

@app.route('/')
def welcome():
    return '<h1>welcome</h1>'
if __name__=='__main__':
    app.run(debug=True)