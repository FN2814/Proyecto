import sqlite3

def fetch_data():
    try:
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM contacts")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("Error al consultar la base de datos:", e)
    finally:
        if con:
            con.close()

if __name__ == '__main__':
    fetch_data()

