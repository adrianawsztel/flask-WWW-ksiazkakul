from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

recipes = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        recipe = {
            'name': request.form['name'],
            'ingredients': request.form['ingredients'],
            'preparation_time': request.form['preparation_time'],
            'instructions': request.form['instructions']
        }
        recipes.append(recipe)
        return redirect(url_for('index'))
    return render_template('add_recipe.html')

@app.route('/recipe')
def recipe_details(recipe_id):
    recipe = recipes[recipe_id]
    return render_template('recipe_details.html', recipe=recipe, recipe_id=recipe_id)

@app.route('/edit', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    if request.method == 'POST':
        recipes[recipe_id] = {
            'name': request.form['name'],
            'ingredients': request.form['ingredients'],
            'preparation_time': request.form['preparation_time'],
            'instructions': request.form['instructions']
        }
        return redirect(url_for('index'))
    recipe = recipes[recipe_id]
    return render_template('edit_recipe.html', recipe=recipe, recipe_id=recipe_id)

@app.route('/delete')
def delete_recipe(recipe_id):
    recipes.pop(recipe_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)