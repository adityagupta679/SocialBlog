from app import app
from flask import render_template


@app.errorhandler(404)
def page_not_found(e):
	params={}
	# params["Name"]="Aadi"
	params["title"]="Oops! Page Not Found"
	return render_template('404.html',params=params),404
	# return "Hello Developer",302

@app.errorhandler(500)
def page_not_found(e):
	params={}
	# params["Name"]="Aadi"
	params["title"]="Oops! Internal Server Error"
	return render_template('500.html',params=params),500
