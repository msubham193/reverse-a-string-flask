from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reverse_string', methods=['POST'])
def reverse_string():
    input_str = request.get_data().decode('UTF-8')
    reversed_str = input_str[::-1]
    return reversed_str


if __name__ == '__main__':
    app.run()
