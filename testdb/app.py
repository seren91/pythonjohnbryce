from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="garage"  # Add database name
)
mycursor = mydb.cursor()

@app.route('/')
def index():
    mycursor.execute("SELECT * FROM cars")
    cars = mycursor.fetchall()
    return render_template('index.html', cars=cars)

@app.route('/add', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        model = request.form['model']
        brand = request.form['brand']
        color = request.form['color']
        sql = "INSERT INTO cars (model, brand, color) VALUES (%s, %s, %s)"
        val = (model, brand, color)
        mycursor.execute(sql, val)
        mydb.commit()
        flash('Car added successfully', 'success')  # Flash success message
        return redirect(url_for('index'))
    return render_template('add_car.html')

@app.route('/edit/<int:car_id>', methods=['GET', 'POST'])
def edit_car(car_id):
    if request.method == 'POST':
        model = request.form['model']
        brand = request.form['brand']
        color = request.form['color']
        sql = "UPDATE cars SET model=%s, brand=%s, color=%s WHERE id=%s"
        val = (model, brand, color, car_id)
        mycursor.execute(sql, val)
        mydb.commit()
        flash('Car updated successfully', 'success')  # Flash success message
        return redirect(url_for('index'))
    mycursor.execute("SELECT * FROM cars WHERE id = %s", (car_id,))
    car = mycursor.fetchone()
    return render_template('edit_car.html', car=car)

@app.route('/delete/<int:car_id>', methods=['POST'])
def delete_car(car_id):
    sql = "DELETE FROM cars WHERE id = %s"
    mycursor.execute(sql, (car_id,))
    mydb.commit()
    flash('Car deleted successfully', 'success')  # Flash success message
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
