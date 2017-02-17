from flask import Flask, render_template, request
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

mysql = MySQL(cursorclass=DictCursor)
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'raspberry'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

mysql.init_app(app)

@app.route('/')
def main():
	return render_template('index.html')	

@app.route('/badgerlist')
def badgerlist():
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT * FROM badger")
	badgerlist = cursor.fetchall()

	return render_template('userlist.html', badgerlist=badgerlist)	

@app.route('/roomlist')
def roomlist():
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT * FROM room")
	roomlist = cursor.fetchall()

	return render_template('roomlist.html', roomlist=roomlist)	

@app.route('/roomplanning', methods=['GET'])
def roomplanning():
	cursor = mysql.connect().cursor()
	return render_template('roomplanning.html')	

if __name__ == '__main__':
	app.run()
