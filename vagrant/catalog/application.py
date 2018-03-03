from flask import Flask, render_template, jsonify
app = Flask(__name__)

# Dummy Catalogs
category = {'id':'5', 'name':'Snowboarding', 'number_of_items':2}
categories = [
    {'id':'1', 'name':'Soccer'}, 
    {'id':'2', 'name':'Basketball'}, 
    {'id':'3', 'name':'Baseball'}, 
    {'id':'4', 'name':'Frisbee'}, 
    {'id':'5', 'name':'Snowboarding'}, 
    {'id':'6', 'name':'Rock climbing'}, 
    {'id':'7', 'name':'Foosball'}, 
    {'id':'8', 'name':'Skating'}, 
    {'id':'9', 'name':'Hockey'}
]

# Dummy Items
item = {'id':'1', 'name':'Snowboard', 'category_name':'Snowboarding', 'description':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'}
categoryItems = [
    {'id':'2', 'name':'Goggles', 'category_name':'Snowboarding', 'description':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'},
    {'id':'3', 'name':'Snowboard', 'category_name':'Snowboarding', 'description':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'}
]
items = [
    {'id':'1', 'name':'Stick', 'category_name':'Hockey', 'description':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'},
    {'id':'2', 'name':'Goggles', 'category_name':'Snowboarding', 'description':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'},
    {'id':'3', 'name':'Snowboard', 'category_name':'Snowboarding', 'description':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'},
    {'id':'4', 'name':'Two shinguards', 'category_name':'Soccer', 'description':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'},
    {'id':'5', 'name':'Shinguards', 'category_name':'Soccer', 'description':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'},
    {'id':'6', 'name':'Frisbee', 'category_name':'Frisbee', 'description':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'},
    {'id':'7', 'name':'Bat', 'category_name':'Baseball', 'description':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'},
    {'id':'8', 'name':'Jersey', 'category_name':'Soccer', 'description':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'},
    {'id':'9', 'name':'Soccer cleats', 'category_name':'Soccer', 'description':'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'}
]

# Authentication
@app.route('/login/')
def showLogin():
    return "This page will show a Google login button here"

@app.route('/gconnect/')
def gconnect():
    return "This is a helper page for connecting with Google API OAuth"

@app.route('/gdisconnect/')
def gdisconnect():
    return "This is for disconnecting a logged in user"

# JSON APIs
@app.route('/catalogs/JSON/')
@app.route('/catalogs/json/')
def catalogJSON():
    return "This page will show all catalogs and its items in JSON format"

@app.route('/catalogs/<category_id>/items/<item_id>/JSON/')
@app.route('/catalogs/<category_id>/items/<item_id>/json/')
def itemJSON(category_id, item_id):
    return "This page will show an item {0} from catalog {1} in JSON format".format(item_id, category_id)

@app.route('/catalogs/<category_id>/JSON/')
@app.route('/catalogs/<category_id>/json/')
@app.route('/catalogs/<category_id>/items/JSON/')
@app.route('/catalogs/<category_id>/items/json/')
def catalogItemJSON(category_id):
    return "This page will show items from catalog %s in JSON format" % category_id

# Show all catalogs
@app.route('/')
@app.route('/catalogs/')
def showCatalogs():
    return render_template('catalog.html', categories = categories, items = items)
    # return render_template('publicCatalog.html', categories = categories, items = items)

# Create new catalog
@app.route('/catalogs/new/')
def newCatalog():
    return render_template('newCategory.html')

# Edit a catalog
@app.route('/catalogs/<category_id>/edit/')
def editCatalog(category_id):
    return render_template('editCategory.html', category = category)

# Delete a catalog
@app.route('/catalogs/<category_id>/delete/')
def deleteCatalog(category_id):
    return render_template('deleteCategory.html', category = category)

# Show catalog items
@app.route('/catalogs/<category_id>/')
@app.route('/catalogs/<category_id>/items/')
def showCatalogItems(category_id):
    return render_template('catalogItems.html', categories = categories, category = category, items= categoryItems)
    # return render_template('publicCatalogItems.html', categories = categories, category= category, items= categoryItems)

# Create a new item
@app.route('/catalogs/<category_id>/items/new/')
def newItem(category_id):
    return render_template('newItem.html', categories = categories)

# Show an item
@app.route('/catalogs/<category_id>/items/<item_id>/')
def showItem(category_id, item_id):
    return render_template('itemDetails.html', item = item)
    # return render_template('publicItemDetails.html', item = item)

# Edit an item
@app.route('/catalogs/<category_id>/items/<item_id>/edit/')
def editItem(category_id, item_id):
    return render_template('editItem.html', categories = categories, item = item)

# Delete an item
@app.route('/catalogs/<category_id>/items/<item_id>/delete/')
def deleteItem(category_id, item_id):
    return render_template('deleteItem.html', item = item)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
