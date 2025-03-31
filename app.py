from flask import Flask, render_template, request, redirect, url_for, flash

import sqlite3
from werkzeug
Exception 
import abort # type: ignore
import os

app = Flask(__name__)

# Database setup
DATABASE = 'cigar_inventory.db'

def init_db():
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        c.execute('''CREATE TABLE cigars
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     brand TEXT NOT NULL,
                     name TEXT NOT NULL,
                     size TEXT,
                     strength INTEGER,
                     quantity INTEGER,
                     purchase_date TEXT,
                     notes TEXT)''')
        c.commit()
        c.close()



app.secret_key = 'xyrby5-winduv-Segpij-Karl' # Needed for flash messages

# Initialize SQLite Dataabase
def init_db():
    if not os.path.exists(DATABASE):
    c = sqlite3.connect('cigar_inventory.db')
    c = c.cursor()
    c.execute('''
                   CREATE TABLE IF NOT EXISTS cigars(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       brand TEXT NOT NULL,
                       strength TEXT,
                       quantity integer,
                       price REAL,
                       notes TEXT,
                                          )''')
    c.commit()
    c.close()

    init_db() # Create the table when the app starts



    # Database Helper Function
    def get_db_connection():
        c = sqlite3.connect('cigar_inventory.db')
        c.row_factory = sqlite3.Row  # Access columns by name
        return c
    

     @app.route("/")
    def index():
         return render_template('index.html')
    


    # Routes
    @app.route("/")
    def home():
        c = get_db_connection()
        cigars = c.execute('SELECT * FROM cigars').fetchall()
        c.close()
        return render_template('index.html', cigars=cigars)
    

    @app.route("/", methods=['GET', 'POST'])
    def add_cigar():
        if request.method== 'POST':
            name = request.form['name']
            brand = request.form['brand']
            strength = request.form['strength']
            quantity = request.form['quantity']
            price = request.form['price']
            notes = request.form['notes']

            c = get_db_connection()
            c.execute(
                'INSERT INTO cigars (name, brand, strength, quantity, price, notes) VALUES'
                '(?,?,?,?,?,?,)',
                (name, brand, strength, quantity, price, notes)
                )
            c.commit()
            c.close()
            flash('Cigar added successfully!', 'success')
            return redirect(url_for('home'))
                            

                            return render_template('add_cigar.html')
                            @app.route('/edit/,<int:id>' , methods=['GET', 'POST'])
                            def edit_cigar(id):
                                c = get_db_connection()
                                cigar = conn.execute('SELECT * FROM cigars WHERE id = ?', (id,)).fetchone()
                                c.close()

                                if request.method == ' POST':
                                    name = request.form['name']
                                    brand = request.form['brand']
                                    strength = request.form[' strength']
                                    quantity = request.form['quantity']
                                    price = request.form['price']
                                    notes = request.form['notes']

      c = get_db_connection()
      c.execute(
          'UPDATE cigars (SET name=?, brand=?, strength=?, quantity=?, price=?,  notes=? WHERE id = ?'),
          (name, brand, strength, quantity, price, notes, id )
      )
      c.commit()
      c.close()
      flash('Cigar updated successfully!', 'success')
      return redirect(url_for('home'))
      return render_template('edit_cigar.html' , cigar=cigar)


@app.route('/delete/<int:id>', methods=[POST])
def delete_cigar(id):
          c = get_db_connection()
                 cigar = conn.execute('DELETE * FROM cigars WHERE id = ?', (id,))
c.commit()
c.close()
flash('Cigar deleted successfully!', 'success')
   return redirect(url_for('home'))



@app.route('/search'
def search():
          c = get_db_connection()
                 cigar = conn.execute('SELECT* FROM cigars WHERE iname LIKE ? OR brand LIKE ?',
                                      (f%{query}%', f%{query}%')
                 ).fetchall()
c.close()
   return render_template('index.html' , cigars=cigars)



   if __name__ == '__main__':
   app.run(debug = True)

@app.route('/')


def home():
    return render_template('index.html', title="Home", message="Welcome to the Flask App!")

@app.route('/about')
def about():
    return render_template('about.html', title="About", message="This is the About page.")

if __name__ == '__main__':
    app.run(debug=True)