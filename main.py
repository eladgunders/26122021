from datetime import datetime
from sqlalchemy import text
from db_config import local_session, create_all_entities
from Facade import Facade
# from Flight import Flight
# from Country import Country
# from Ticket import Ticket
# from Airline_Company import Airline_Company
# from Customer import Customer
# from User import User
# from User_Role import User_Role
# from Administrator import Administrator
from Tourist import Tourist
from Attraction import Attraction
from Visit import Visit
import sys


fac = Facade()  # creating a 'DAO'
fac.drop_all_tables()
create_all_entities()  # create tables if not exist

# inserting tourists
t1 = Tourist(name='Elad', origin_country='Israel')
t2 = Tourist(name='Yuval', origin_country='Israel')
fac.add_all([t1, t2])

# inserting attractions
a1 = Attraction(name='Museum', price='100')
a2 = Attraction(name='Theater', price='75')
fac.add_all([a1, a2])

# inserting visits
v1 = Visit(tourist_id=1, attraction_id=1)
v2 = Visit(tourist_id=1, attraction_id=2)
v3 = Visit(tourist_id=2, attraction_id=1)
v4 = Visit(tourist_id=2, attraction_id=1)
fac.add_all([v1, v2, v3, v4])


print(fac.get_by_condition(Tourist, lambda query: query.filter(Tourist.id == 1).all()[0].visits))
print(fac.get_by_condition(Attraction, lambda query: query.filter(Attraction.id == 1).all()[0].visits))

