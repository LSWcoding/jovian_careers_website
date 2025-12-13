from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_jovian():
    return render_template('home.html')

if __name__ == '__main__':#assign the host
    app.run(debug=True)
