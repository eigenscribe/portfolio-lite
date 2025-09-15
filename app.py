from flask import Flask, render_template

app = Flask(__name__)

# Configure Flask to disable caching for development
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    """Main portfolio page"""
    return render_template('index.html')

@app.route('/about')
def about():
    """About section"""
    return render_template('index.html', section='about')

@app.route('/projects')
def projects():
    """Projects section"""
    return render_template('index.html', section='projects')

@app.route('/skills')
def skills():
    """Skills section"""
    return render_template('index.html', section='skills')

@app.route('/contact')
def contact():
    """Contact section"""      
    return render_template('index.html', section='contact')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)