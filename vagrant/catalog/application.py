from flask import Flask
app = Flask(__name__)

# Authentication
@app.route('/login')
def showLogin():
    return "This page will show a Google login button here"

@app.route('/gconnect')
def gconnect():
    return "This is a helper page for connecting with Google API OAuth"

@app.route('/gdisconnect')
def gdisconnect():
    return "This is for disconnecting a logged in user"

# JSON APIs
@app.route('/catalogs/JSON')
@app.route('/catalogs/json')
def catalogJSON():
    return "This page will show all catalogs and its items in JSON format"

@app.route('/catalogs/<catalog_id>/items/<item_id>/JSON')
@app.route('/catalogs/<catalog_id>/items/<item_id>/json')
def itemJSON(catalog_id, item_id):
    return "This page will show an item: catalog_id:{1} and item_id:{0} in JSON format".format(catalog_id, item_id)

@app.route('/catalogs/<catalog_id>/items/JSON')
@app.route('/catalogs/<catalog_id>/items/json')
def catalogItemJSON(catalog_id):
    return "This page will show items under a catalog %s in JSON format" % catalog_id

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
    return "Catalog no %s - edit" % catalog_id

# Delete a catalog
@app.route('/catalogs/<catalog_id>/delete/')
def deleteCatalog(catalog_id):
    return "Catalog - delete"

# Show catalog items
@app.route('/catalogs/<catalog_id>/')
@app.route('/catalogs/<catalog_id>/items/')
def showCatalogItems(catalog):
    return "Catalog items"

# Create a new item
@app.route('/catalogs/<catalog_id>/items/new/')
def newItem(item):
    return "Item - new"

# Edit an item
@app.route('/catalogs/<item_id>/edit/')
def editItem(item):
    return "Item - edit"

# Delete an item
@app.route('/catalogs/<item_id>/delete/')
def deleteItem(item):
    return "Item - delete"

# Show an item
@app.route('/catalogs/<catalog_id>/items/<item_id>/')
def showItem(catalog, item):
    return "Item"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
