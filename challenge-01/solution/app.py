from flask import Flask, render_template


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html'), 200
    
@app.route('/about')
def about():
    return render_template('about.html'), 200
    
@app.route('/projects')
def projects():
    return render_template('projects.html'), 200

if __name__ == '__main__':
    app.run(debug=True)