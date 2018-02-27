from flask import Flask
app = Flask(__name__)

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

@app.route('/catalogs/<catalog_id>/items/<item_id>/JSON/')
@app.route('/catalogs/<catalog_id>/items/<item_id>/json/')
def itemJSON(catalog_id, item_id):
    return "This page will show an item {0} from catalog {1} in JSON format".format(item_id, catalog_id)

@app.route('/catalogs/<catalog_id>/JSON/')
@app.route('/catalogs/<catalog_id>/json/')
@app.route('/catalogs/<catalog_id>/items/JSON/')
@app.route('/catalogs/<catalog_id>/items/json/')
def catalogItemJSON(catalog_id):
    return "This page will show items from catalog %s in JSON format" % catalog_id

# Show all catalogs
@app.route('/')
@app.route('/catalogs/')
def showCatalogs():
    return "This page will be the homepage of the project showing all the catalogs"

# Create new catalog
@app.route('/catalogs/new/')
def newCatalog():
    return "This page will be for making a new catalog"

# Edit a catalog
@app.route('/catalogs/<catalog_id>/edit/')
def editCatalog(catalog_id):
    return "This page will show edit form for catalog %s" % catalog_id

# Delete a catalog
@app.route('/catalogs/<catalog_id>/delete/')
def deleteCatalog(catalog_id):
    return "This page is for deleting catalog %s" % catalog_id

# Show catalog items
@app.route('/catalogs/<catalog_id>/')
@app.route('/catalogs/<catalog_id>/items/')
def showCatalogItems(catalog_id):
    return "This page will show all items from catalog %s" % catalog_id

# Create a new item
@app.route('/catalogs/<catalog_id>/items/new/')
def newItem(catalog_id):
    return "This page is for adding new item from catalog %s" % catalog_id

# Edit an item
@app.route('/catalogs/<catalog_id>/items/<item_id>/edit/')
def editItem(catalog_id, item_id):
    return "This page is for editing item {0} from catalog {1}".format(item_id, catalog_id)

# Delete an item
@app.route('/catalogs/<catalog_id>/items/<item_id>/delete/')
def deleteItem(catalog_id, item_id):
    return "This page is for deleting item {0} from catalog {1}".format(item_id, catalog_id)

# Show an item
@app.route('/catalogs/<catalog_id>/items/<item_id>/')
def showItem(catalog_id, item_id):
    return "This page will show details of item {0} from catalog {1}".format(item_id, catalog_id)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
