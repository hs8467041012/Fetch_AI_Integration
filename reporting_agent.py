from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/report', methods=['POST'])
def report():
    data = request.json
    issues = data.get('issues', [])
    print(f"Issues reported: {issues}")
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(port=5001)
