from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'academies'

mysql = MySQL(app)

@app.route('/academy', methods=['POST'])
def saveCustomer():
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO academies (name, phone, website) VALUES (%s, %s, %s);", (request.json['name'], request.json['phone'], request.json['website']))
    mysql.connection.commit()
    return 'saved academy'

@app.route('/academy/<int:id>', methods=['DELETE'])
def removeCustomer(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM academies WHERE academies.id = " + str(id) + ";")
    mysql.connection.commit()
    return 'removed academy'

@app.route('/academy/<int:id>')
def getCustomer(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM academies WHERE academies.id = " + str(id) + ";")
    data = cur.fetchall()
    content = {}
    for row in data:
        content = { "id": row[0], "name": row[1], "phone": row[2], "website": row[3]}
    return jsonify(content)

@app.route('/academies')
def getAllCustomers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM academies ;")
    data = cur.fetchall()
    result = []
    for row in data:
        content = { "id": row[0], "name": row[1], "phone": row[2], "website": row[3]}
        result.append(content)
    return jsonify(result)

@app.route('/')
def index():
    return render_template('frontend/index.html')

if __name__ == '__main__':
    app.run(None, 3000, True)