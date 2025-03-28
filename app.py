from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Tymczasowa baza danych w pamięci
recipes = []

@app.route('/')
def index():
    search_query = request.args.get('search', '').lower()
    filtered_recipes = [recipe for recipe in recipes if search_query in recipe['title'].lower() or search_query in recipe['ingredients'].lower()]
    return render_template('index.html', recipes=filtered_recipes, search_query=search_query)

@app.route('/recipe/<int:recipe_id>')
def recipe_details(recipe_id):
    if 0 <= recipe_id < len(recipes):
        return render_template('recipe_details.html', recipe=recipes[recipe_id])
    return redirect(url_for('index'))

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        recipe = {
            'title': request.form['title'],
            'ingredients': request.form['ingredients'],
            'preparation_time': request.form['preparation_time'],
            'instructions': request.form['instructions']
        }
        recipes.append(recipe)
        return redirect(url_for('index'))
    return render_template('add_recipe.html')

@app.route('/edit_recipe/<int:recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    if 0 <= recipe_id < len(recipes):
        if request.method == 'POST':
            recipes[recipe_id] = {
                'title': request.form['title'],
                'ingredients': request.form['ingredients'],
                'preparation_time': request.form['preparation_time'],
                'instructions': request.form['instructions']
            }
            return redirect(url_for('index'))
        return render_template('edit_recipe.html', recipe=recipes[recipe_id], recipe_id=recipe_id)
    return redirect(url_for('index'))

@app.route('/delete_recipe/<int:recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    if 0 <= recipe_id < len(recipes):
        recipes.pop(recipe_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
