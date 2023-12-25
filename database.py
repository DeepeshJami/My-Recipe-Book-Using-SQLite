import sqlite3

def setup_database():
    conn = sqlite3.connect('database.db')
    conn.execute('''
    CREATE TABLE recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        procedure TEXT,
        rating INTEGER,
        time_taken TEXT,
        ingredients TEXT
    )
    ''')
    conn.execute('''
    CREATE TABLE comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recipe_id INTEGER NOT NULL,
        comment TEXT NOT NULL,
        FOREIGN KEY (recipe_id) REFERENCES recipes (id)
    )
    ''')
    conn.close()
    print("Database and tables created successfully")

if __name__ == "__main__":
    setup_database()
