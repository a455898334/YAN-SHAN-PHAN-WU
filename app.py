from flask import request,Flask,render_template, url_for,redirect,request
import urllib2,json
import database

app = Flask(__name__)
#app.secret_key = "secret"


Latitude = 0
Longitude = 0



@app.route('/', methods=['GET', 'POST'])
def main():
	global Longitude
	global Latitude

    	if request.method == 'GET':
		return render_template('GPS.html', Latitude = Latitude, Longitude = Longitude)
	else:
    		button = request.form['button']
#_______________________________________________________________Main page has "Scan" and "New" buttons

		if button == 'SCAN':
			if  request.form['Latitude'] != None:
				Latitude = request.form['Latitude']
				Longitude = request.form['Longitude']
			return redirect(url_for('scan'))

		elif button == 'NEW':
			if  request.form['Latitude'] != None:
				Latitude = request.form['Latitude']
				Longitude = request.form['Longitude']
			return redirect(url_for('new'))







@app.route('/scan', methods=['GET', 'POST'])
def scan():
	global Longitude
	global Latitude

    	if request.method == 'GET':
		
    			messages = database.returnMessagesinRange(Latitude,Longitude)
    			return render_template('SCAN.html',messages=messages, Latitude = Latitude, Longitude = Longitude)
	else:
    		button = request.form['button']
#_______________________________________________________________SCAN page has "Back" button
    		if button == 'BACK':
			mode = ""
			return redirect('/')		





@app.route('/new', methods=['GET', 'POST'])  		   
def new():    		
	global Longitude
	global Latitude

    	if request.method == 'GET':	
		return render_template('NEW.html', Latitude = Latitude, Longitude = Longitude)
	else:
    		button = request.form['button']
#_______________________________________________________________NEW page has "Create Message" and "Cancel" buttons
		if button == 'Create Message':
			newM = request.form['line']
			if newM:
				database.writeMessage(newM,float(Longitude),float(Latitude))
				return redirect('/')
			return redirect('/new')

		elif button == 'Cancel':
			return redirect('/')



if __name__=="__main__":
    app.debug=True
    app.run(port=5000)
