from flask import Flask, render_template, url_for, flash

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True)
