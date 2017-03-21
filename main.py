from flask import Flask, send_from_directory, render_template
import os

app = Flask(__name__);

@app.route('/')
def send_static():
    return render_template('index.html')

@app.route('/photoshop')
def photoshop():
    return render_template('Photoshop.html')

if __name__ == '__main__':
    app.debug = True
    port = int(os.getenv('PORT',8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run()