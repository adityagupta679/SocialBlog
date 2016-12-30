from app import app

@app.route('/')
@app.route('/index')
def index():

	return "Hello Developer",302