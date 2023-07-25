from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods = ['POST'])
def upload():
    if request.method == 'POST':
        raw_data = request.data
        print(raw_data)
        return "Data received successfully!"
    return "Data not received successfully"

if __name__ == '__main__':
    app.run()