from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # Habilitar CORS en tu aplicación Flask

# Conectar a la base de datos
def connect_db():
    return sqlite3.connect('database.db')

# Crear tabla si no existe
def create_table():
    with connect_db() as con:
        con.execute('''CREATE TABLE IF NOT EXISTS contacts (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        message TEXT NOT NULL
                    )''')

create_table()

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        with connect_db() as con:
            cur = con.cursor()
            cur.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
            con.commit()
        
        return jsonify({"status": "success", "message": "Datos guardados exitosamente"}), 200
    except Exception as e:
        import traceback
        print(traceback.format_exc())  # Imprimir la traza completa del error en la terminal
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

