from flask import Flask, send_from_directory

app = Flask(__name__);


@app.route('/')
def send_static():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def send_static2(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
   app.run(port=5000, host='127.0.0.1', debug=True)
    # app.run()