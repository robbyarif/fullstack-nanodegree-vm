from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item
from datetime import datetime
app = Flask(__name__)

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Authentication
# @app.route('/login/')
# def showLogin():
#     return "This page will show a Google login button here"

# @app.route('/gconnect/')
# def gconnect():
#     return "This is a helper page for connecting with Google API OAuth"

# @app.route('/gdisconnect/')
# def gdisconnect():
#     return "This is for disconnecting a logged in user"

# # JSON APIs
# @app.route('/catalog/JSON/')
# @app.route('/catalog/json/')
# def catalogJSON():
#     return "This page will show all catalog and its items in JSON format"

# @app.route('/catalog/<int:category_id>/items/<item_id>/JSON/')
# @app.route('/catalog/<int:category_id>/items/<item_id>/json/')
# def itemJSON(category_id, item_id):
#     return "This page will show an item {0} from catalog {1} in JSON format".format(item_id, category_id)

# @app.route('/catalog/<int:category_id>/JSON/')
# @app.route('/catalog/<int:category_id>/json/')
# @app.route('/catalog/<int:category_id>/items/JSON/')
# @app.route('/catalog/<int:category_id>/items/json/')
# def catalogItemJSON(category_id):
#     return "This page will show items from catalog %s in JSON format" % category_id

# Show all catalog
@app.route('/')
@app.route('/catalog/')
def showCatalog():
    categories = session.query(Category)
    items = session.query(Item).order_by(Item.created_datetime.desc()).all()
    #if authorized
    return render_template('catalog.html', categories = categories, items = items)
    #else not authorized
    # return render_template('publicCatalog.html', categories = categories, items = items)

# Show catalog items
@app.route('/catalog/<category>/items/')
def showCatalogItems(category):
    categories = session.query(Category)
    category = session.query(Category).filter_by(name = category).one()
    #if category not found return 404
    categoryItems = session.query(Item).filter_by(category_id = category.id).all()
    #if empty show flash message no items yet. do you want to add some?
    #if authorized
    return render_template('catalogItems.html', categories = categories, category = category, items= categoryItems)
    #else not authorized
    # return render_template('publicCatalogItems.html', categories = categories, category= category, items= categoryItems)

# Create a new item
@app.route('/catalog/items/new/', methods=['GET', 'POST'])
def newItem():
    categories = session.query(Category)
    if request.method == 'POST':
        newItem = Item(name = request.form['name'], description = request.form['description'],
                       category = request.form['category_id'], created_datetime = datetime.now())
        session.add(newItem)
        session.commit()
        #flash message
        return redirect(url_for('showCatalog'))
    else:
        return render_template('newItem.html', categories = categories)

# Show an item
@app.route('/catalog/<category>/<item>/')
def showItem(category, item):
    item = session.query(Item).join(Category)\
    .filter(Category.name == category)\
    .filter(Item.name == item).one()
    #if not found return 404
    #if authorized
    return render_template('itemDetails.html', item = item)
    #else not authorized
    # return render_template('publicItemDetails.html', item = item)

# Edit an item
@app.route('/catalog/<item>/edit/', methods=['GET', 'POST'])
def editItem(item):
    item = session.query(Item).filter_by(name = item).one()
    return render_template('editItem.html', item = item)

# Delete an item
@app.route('/catalog/<item>/delete/', methods=['GET', 'POST'])
def deleteItem(item):
    item = session.query(Item).filter_by(name = item).one()
    return render_template('deleteItem.html', item = item)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
