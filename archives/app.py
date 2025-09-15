from flask import Flask, render_template

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    """Main demo page"""
    return render_template('index.html')

@app.route('/health')
def health():
    """Health check endpoint"""
    return {'status': 'healthy', 'message': 'Clean Theme Demo is running!'}

if __name__ == '__main__':
    # For Replit - use host='0.0.0.0' to make it accessible
    app.run(host='0.0.0.0', port=5000, debug=True)
