from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Shop, Base, OfferItem, User
 
engine = create_engine('sqlite:///shopofferwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

#Create first user
User1 = User(name="Mona Musterfrau", email="mona22@gmail.com", picture='https://cdn.pixabay.com/photo/2017/09/01/21/53/blue-2705642_1280.jpg')
session.add(User1)
session.commit()

# Offer for Fancy Dresses
shop1 = Shop(user_id=1, name = "Fancy Wedding Dresses")

session.add(shop1)
session.commit()


offerItem1 = OfferItem(user_id=1, name = "Wedding dress", description = "A dream for the best day of your life", price = "$2000.99", style = "Dresses", shop = shop1)

session.add(offerItem1)
session.commit()

offerItem2 = OfferItem(user_id=1, name = "High Heels", description = "Fabulous and still comfortable to wear", price = "$20.50", style = "Shoes", shop = shop1)

session.add(offerItem2)
session.commit()

offerItem3 = OfferItem(user_id=1, name = "Maid of honour T-shirt", description = "be her best friend with this unique shirt", price = "$5.99", style = "Shirts", shop = shop1)

session.add(offerItem3)
session.commit()


# Offer for Everything for Hiking
shop2 = Shop(user_id=1, name = "Everything for Hiking")

session.add(shop2)
session.commit()


offerItem1 = OfferItem(user_id=1, name = "Brown Boots", description = "these boots are made for walking", price = "$14.99", style = "Shoes", shop = shop2)

session.add(offerItem1)
session.commit()

offerItem2 = OfferItem(user_id=1, name = "Sport shirt", description = "warming and cooling", price = "$25", style = "Shirts", shop = shop2)

session.add(offerItem2)
session.commit()



print "added offer items!"

