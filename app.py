from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '123',
    'database': 'cars',
}

# MySQL connection
app.config['MYSQL_HOST'] = db_config['host']
app.config['MYSQL_USER'] = db_config['user']
app.config['MYSQL_PASSWORD'] = db_config['password']
app.config['MYSQL_DB'] = db_config['database']
mysql = MySQL(app)


@app.route('/cars', methods=['GET'])
def get_all_cars():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cars')
    data = cur.fetchall()
    cur.close()
    cars_list = []
    for car in data:
        car_info = {
            'id': car[0],
            'model': car[1],
            'color': car[2],
            'plate_number': car[3]
        }
        cars_list.append(car_info)
    return jsonify(cars_list)


@app.route('/cars', methods=['POST'])
def add_car():
    model = request.json['model']
    color = request.json['color']
    plate_number = request.json['plate_number']
    
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO cars (model, color, plate_number) VALUES (%s, %s, %s)', (model, color, plate_number))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'Car added successfully!'})


@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    model = request.json['model']
    color = request.json['color']
    plate_number = request.json['plate_number']
    
    cur = mysql.connection.cursor()
    cur.execute('UPDATE cars SET model=%s, color=%s, plate_number=%s WHERE id=%s', (model, color, plate_number, car_id))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'Car updated successfully!'})


@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM cars WHERE id=%s', (car_id,))
    mysql.connection.commit()
    cur.close()
    
    return jsonify({'message': 'Car deleted successfully!'})


if __name__ == '__main__':
    app.run(debug=True)
