from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
from datetime import datetime

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create dummy user
User1 = User(name="Robby Dummy", email="test@mail.com",
             picture="https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_960_720.png")
session.add(User1)
session.commit()

# Add Categories
category1 = Category(id = 1, name = "Soccer")
session.add(category1)
session.commit()

category2 = Category(id = 2, name = "Basketball")
session.add(category2)
session.commit()

category3 = Category(id = 3, name = "Baseball")
session.add(category3)
session.commit()

category4 = Category(id = 4, name = "Frisbee")
session.add(category4)
session.commit()

category5 = Category(id = 5, name = "Snowboarding")
session.add(category5)
session.commit()

category6 = Category(id = 6, name = "Rock Climbing")
session.add(category6)
session.commit()

category7 = Category(id = 7, name = "Foosball")
session.add(category7)
session.commit()

category8 = Category(id = 8, name = "Skating")
session.add(category8)
session.commit()

category9 = Category(id = 9, name = "Hockey")
session.add(category9)
session.commit()

# Add items
item1 = Item(id = 1, name = "Two shinguards", description = "Two shinguards to protect your shins",
             category = category1, created_datetime = datetime(2018, 3, 7, 23,10),
             user = User1)
session.add(item1)
session.commit()

item2 = Item(id = 2, name = "Shinguards", description = "Shinguards to protect your shins",
             category = category1, created_datetime = datetime(2018, 3, 8, 0, 5),
             user = User1)
session.add(item2)
session.commit()

item3 = Item(id = 3, name = "Jersey", description = "A customizable jersey for your favourite team",
             category = category1, created_datetime = datetime(2018, 3, 6, 0, 5),
             user = User1)
session.add(item3)
session.commit()

item4 = Item(id = 4, name = "Soccer cleats", description = "Firm ground of soccer shoes",
             category = category1, created_datetime = datetime(2018, 3, 8, 1, 5),
             user = User1)
session.add(item4)
session.commit()

item5 = Item(id = 5, name = "Bat", description = "Wooden stick to hit the ball",
             category = category3, created_datetime = datetime(2018, 3, 7, 10, 5),
             user = User1)
session.add(item5)
session.commit()

item6 = Item(id = 6, name = "Frisbee", description = "Flying saucer yay",
             category = category4, created_datetime = datetime(2018, 3, 7, 16, 5),
             user = User1)
session.add(item6)
session.commit()

item7 = Item(id = 7, name = "Goggles", description = "Pair of eyeglasses to cover you from debrees or snow",
             category = category5, created_datetime = datetime(2018, 3, 5, 1, 5),
             user = User1)
session.add(item7)
session.commit()

item8 = Item(id = 8, name = "Snowboard", description = "The main board you step on for surfing on snow",
             category = category5, created_datetime = datetime(2018, 3, 8, 2, 5),
             user = User1)
session.add(item8)
session.commit()

item9 = Item(id=9, name="Stick", description="A long steel stick to hit the ball", 
             category = category9, created_datetime = datetime(2018, 3, 4, 12, 5),
             user = User1)
session.add(item9)
session.commit()

print "Added items..."