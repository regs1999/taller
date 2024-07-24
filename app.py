from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    is_mobile = 'Mobile' in user_agent
    return render_template('index.html', is_mobile=is_mobile)

if __name__ == '__main__':
    app.run(debug=True)