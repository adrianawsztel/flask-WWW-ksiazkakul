from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Tymczasowa baza danych w pamięci
recipes = []

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        # Pobierz dane z formularza i dodaj przepis do listy
        recipe = {
            'title': request.form['title'],
            'ingredients': request.form['ingredients'],
            'instructions': request.form['instructions']
        }
        recipes.append(recipe)
        return redirect(url_for('index'))
    return render_template('add_recipe.html')

# Tutaj można dodać więcej tras dla edycji, szczegółów i usuwania

if __name__ == '__main__':
    app.run(debug=True)