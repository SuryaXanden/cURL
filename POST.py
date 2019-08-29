from flask import Flask, request
from werkzeug import secure_filename
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=['POST'])
def index():
	data = request.files['data']
	data.save( secure_filename( datetime.now().strftime( "%Y%m%d%H%M%S" ) ) )
	return ""
app.run(port=80, debug=True)
# curl -X POST -F "data=@curl.exe" 127.0.0.1
