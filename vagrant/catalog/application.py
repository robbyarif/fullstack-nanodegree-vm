from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
from datetime import datetime
from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests


app = Flask(__name__)


CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Item Catalog Application"


engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Authentication
@app.route('/login/')
def showLogin():
    state = ''.join(random.choice(string.ascii_lowercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "%s" % login_session['state']
    print login_session['state']
    return render_template('login.html', STATE = state)

@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    
    
    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user

def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

@app.route('/gdisconnect/')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

# # JSON APIs
@app.route('/catalog/JSON/')
def catalogJSON():
    categories = session.query(Category).all()
    return jsonify(categories=[c.serialize for c in categories])

@app.route('/catalog/<category_name>/<item_name>/JSON/')
def itemJSON(category_name, item_name):
    category = session.query(Category).filter_by(name=category_name).one()
    item = session.query(Item).filter_by(name = item_name, category_id = category.id).one()
    return jsonify(item=item.serialize)

@app.route('/catalog/<category_name>/JSON/')
@app.route('/catalog/<category_name>/items/JSON/')
def catalogItemJSON(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(Item).filter_by(category_id = category.id).all()
    return jsonify(items=[i.serialize for i in items])

# Show all catalog
@app.route('/')
@app.route('/catalog/')
def showCatalog():
    categories = session.query(Category)
    items = session.query(Item).order_by(Item.created_datetime.desc()).all()
    if 'username' not in login_session:
        return render_template('publicCatalog.html', categories = categories, items = items)
    else:
        return render_template('catalog.html', categories = categories, items = items)

# Show catalog items
@app.route('/catalog/<category>/items/')
def showCatalogItems(category):
    categories = session.query(Category)
    category = session.query(Category).filter_by(name = category).one()
    categoryItems = session.query(Item).filter_by(category_id = category.id).all()
    if 'username' not in login_session:
        return render_template('publicCatalogItems.html', categories = categories, category= category, items= categoryItems)
    else:
        return render_template('catalogItems.html', categories = categories, category = category, items= categoryItems)

# Create a new item
@app.route('/catalog/items/new/', methods=['GET', 'POST'])
def newItem():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        item = session.query(Item).filter_by(name = request.form['name']).all()
        print item
        if len(item) != 0:
            flash("Error: Same item already created")
            return redirect(url_for('newItem'))
        else:
            new_item = Item(name = request.form['name'], description = request.form['description'],
                        category_id = request.form['category_id'], created_datetime = datetime.now(),
                        user_id = login_session['user_id'])
            session.add(new_item)
            session.commit()
            flash("New catalog item created!")
            return redirect(url_for('showCatalog'))
    else:
        categories = session.query(Category)
        return render_template('newItem.html', categories = categories)

# Show an item
@app.route('/catalog/<category>/<item>/')
def showItem(category, item):
    item = session.query(Item).join(Category)\
    .filter(Category.name == category)\
    .filter(Item.name == item).one()
    creator = getUserInfo(item.user_id)
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('publicItemDetails.html', item = item, creator=creator)
    else:
        return render_template('itemDetails.html', item = item, creator=creator)

# Edit an item
@app.route('/catalog/<item>/edit/', methods=['GET', 'POST'])
def editItem(item):
    if 'username' not in login_session:
        return redirect('/login')
    edited_item = session.query(Item).filter_by(name = item).one()
    if login_session['user_id'] != edited_item.user_id:
        return "<script>function myFunction() {alert('You are not authorized to edit this item. Please create your own item in order to edit them.');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        edited_item.name = request.form['name']
        edited_item.description = request.form['description']
        edited_item.category_id = request.form['category_id']
        session.add(edited_item)
        session.commit()
        flash("Item {item_name} updated!".format(item_name = edited_item.name))
        return redirect(url_for('showItem', category = edited_item.category.name, item = edited_item.name))
    else:
        categories = session.query(Category)
        return render_template('editItem.html', item = edited_item, categories = categories)

# Delete an item
@app.route('/catalog/<item>/delete/', methods=['GET', 'POST'])
def deleteItem(item):
    if 'username' not in login_session:
        return redirect('/login')
    item_to_delete = session.query(Item).filter_by(name = item).one()
    if login_session['user_id'] != item_to_delete.user_id:
        return "<script>function myFunction() {alert('You are not authorized to delete this item. Please create your own item in order to delete them.');}</script><body onload='myFunction()'>"
    if request.method == 'POST':
        parent_category = item_to_delete.category.name
        session.delete(item_to_delete)
        session.commit()
        flash("{item_name} deleted!".format(item_name = item_to_delete.name))
        return redirect(url_for('showCatalogItems', category = parent_category))
    else :
        return render_template('deleteItem.html', item = item_to_delete)

if __name__ == '__main__':
    app.secret_key = "asdfasdf"
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
