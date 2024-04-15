from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Home"

@app.route('/submit-json', methods=['POST'])
def submit_json():
    if request.method == 'POST':
        data = request.get_json() 
        if data is None:
            return jsonify({'error': 'No JSON data received'}), 400
        
        name = data.get('name')
        email = data.get('email')
        
        if not name or not email:
            return jsonify({'error': 'Name or email missing in JSON data'}), 400
        
        return jsonify({'message': 'JSON data received successfully',
                        'name': name,
                        'email': email}), 200

if __name__ == '__main__':
    app.run(debug=True)