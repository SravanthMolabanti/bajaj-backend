from flask import Flask, request, jsonify

app = Flask(__name__)

# GET endpoint that returns a hardcoded operation code
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({
        "operation_code": 1
    }), 200

# POST endpoint that processes the input data
@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    
    if not isinstance(data, list):
        return jsonify({
            "is_success": False,
            "message": "Invalid data format. 'data' should be an array."
        }), 400

    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]

    lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
    highest_lowercase_alphabet = [max(lowercase_alphabets)] if lowercase_alphabets else []

    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",  # Replace with your actual full_name and DOB
        "email": "john@xyz.com",
        "roll_number": "ABCD123",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
