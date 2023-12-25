from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    recipes = conn.execute('SELECT * FROM recipes').fetchall()
    conn.close()
    return render_template('index.html', recipes=recipes)

@app.route('/<int:id>', methods=['GET', 'POST'])
def recipe(id):
    conn = get_db_connection()
    recipe = conn.execute('SELECT * FROM recipes WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        comment = request.form['comment']
        conn.execute('INSERT INTO comments (recipe_id, comment) VALUES (?, ?)', (id, comment))
        conn.commit()

    comments = conn.execute('SELECT * FROM comments WHERE recipe_id = ?', (id,)).fetchall()
    conn.close()

    return render_template('recipe.html', recipe=recipe, comments=comments)


@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        procedure = request.form['procedure']
        rating = request.form['rating']
        time_taken = request.form['time_taken']
        ingredients = request.form['ingredients']

        conn = get_db_connection()
        conn.execute('INSERT INTO recipes (title, description, procedure, rating, time_taken, ingredients) VALUES (?, ?, ?, ?, ?, ?)',
                     (title, description, procedure, rating, time_taken, ingredients))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    recipe = conn.execute('SELECT * FROM recipes WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        procedure = request.form['procedure']
        rating = request.form['rating']
        time_taken = request.form['time_taken']
        ingredients = request.form['ingredients']

        conn.execute('UPDATE recipes SET title = ?, description = ?, procedure = ?, rating = ?, time_taken = ?, ingredients = ? WHERE id = ?',
                     (title, description, procedure, rating, time_taken, ingredients, id))
        conn.commit()
        conn.close()
        return redirect(url_for('recipe', id=id))

    conn.close()
    return render_template('edit.html', recipe=recipe)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM recipes WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/<int:id>/comments', methods=('GET', 'POST'))
def comments(id):
    conn = get_db_connection()
    if request.method == 'POST':
        comment = request.form['comment']
        conn.execute('INSERT INTO comments (recipe_id, comment) VALUES (?, ?)',
                     (id, comment))
        conn.commit()

    recipe = conn.execute('SELECT * FROM recipes WHERE id = ?', (id,)).fetchone()
    recipe_comments = conn.execute('SELECT * FROM comments WHERE recipe_id = ?', (id,)).fetchall()
    conn.close()

    return render_template('comments.html', recipe=recipe, comments=recipe_comments)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form['search']
        conn = get_db_connection()
        recipes = conn.execute("SELECT * FROM recipes WHERE title LIKE ?", ('%' + search_query + '%',)).fetchall()
        conn.close()

        if recipes:
            return render_template('search_results.html', recipes=recipes, query=search_query)
        else:
            return render_template('search_results.html', recipes=[], query=search_query, message="No recipes found.")

    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)


