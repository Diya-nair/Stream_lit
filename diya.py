from flask import Flask, request, jsonify

app = Flask(__name__)

# Example cutoff data (usually this would come from a database)
cutoff_data = {
    'Engineering': [
        {'college': 'College A', 'cutoff': 150},
        {'college': 'College B', 'cutoff': 140},
        {'college': 'College C', 'cutoff': 130},
    ]
    # Add more fields and colleges as needed
}

@app.route('/get_colleges', methods=['POST'])
def get_colleges():
    data = request.json
    marks = data.get('marks')
    field = data.get('field')
    
    if not marks or not field:
        return jsonify({"error": "Invalid input"}), 400
    
    available_colleges = [college['college'] for college in cutoff_data[field] if marks >= college['cutoff']]
    
    if not available_colleges:
        return jsonify({"message": "No colleges available for the given marks"}), 200
    
    return jsonify({"available_colleges": available_colleges}), 200

if __name__ == '__main__':
    app.run(debug=True)
