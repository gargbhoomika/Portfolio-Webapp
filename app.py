from flask import Flask,request, render_template,redirect,url_for
import mysql.connector
from emailsend import *
from mysql.connector import Error
from mysql.connector import errorcode
app = Flask(__name__)


@app.route('/')

def home():
    return render_template('index.html')

@app.route('/success/', methods=['POST','GET'])
def success():
    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        try:
            connection = mysql.connector.connect(host='localhost',database='portfolio_connections',user='root',password='Bhoomi13@')
            insertquery = """INSERT INTO people (name,email,subject,message) VALUES (%s,%s,%s,%s)"""
            cursor = connection.cursor()
            result = cursor.execute(insertquery,(name,email,subject,message))
            connection.commit()
            print("Inserted")
            send_email(email,name)
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("My sql CLosed")
            return render_template('success.html',user=name)
        except:
            return render_template('error.html',user=name)
        # except mysql.connector.Error as e:
        #     connection.rollback()
        #     print("Failed due to: "+format(e))
        #     if connection.is_connected():
        #         cursor.close()
        #         connection.close()
        #         print("My sql CLosed")
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    # app.debug = True
    app.run()
