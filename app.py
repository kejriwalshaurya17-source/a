from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

@app.route('/report')
def report():
    return render_template('report.html', title="Report Issue")

@app.route('/login')
def login():
    return render_template('login.html', title="Login")

@app.route('/register')
def register():
    return render_template('register.html', title="Register")

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
