
from app.config.mysqlconnection import connectToMySQL
from flask import flash
from app.models import user_model
import pprint



class Ride:
    DB = "ohana_rideshare"
    def __init__(self, data):
        self.id= data['id']
        self.destination=data["destination"]
        self.pickup_location=data["pickup_location"]
        self.date=data["date"]
        self.details=data["details"]
        self.rider_id=data["rider_id"]
        self.driver_id=data["driver_id"] or None
        self.rider=None
        self.driver=None

    @classmethod
    def add_ride(cls, data):
        query=  """
                INSERT INTO rides (destination, pickup_location, date, details, rider_id)
                VALUES (%(destination)s, %(pickup_location)s, %(date)s, %(details)s, %(rider_id)s);
                """
        results=connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    @classmethod
    def get_all_ride_requests_w_rider_info(cls):
        query=  """
                SELECT * FROM rides
                LEFT JOIN users ON users.id=rides.rider_id
                """
        results=connectToMySQL(cls.DB).query_db(query)
        # print("THESE ARE SELECT RESULTS!!!!!", results)
        all_rides=[]
        for row in results:
            one_ride=cls(row)
            one_ride_user_info={
                "id":row["users.id"],
                "first_name":row["first_name"],
                "last_name":row["last_name"],
                "email":row["email"],
                "password":row["password"],
                "created_at":row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
            user=user_model.User(one_ride_user_info)
            one_ride.rider=user
            # print(one_ride.__dict__)
            all_rides.append(one_ride)
        return all_rides
    
    @classmethod
    def insert_driver_id(cls, data):
        query=  """
                UPDATE rides 
                SET driver_id=%(driver_id)s
                WHERE rides.id=%(id)s
                """
        results=connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    #Get all requests with rider_id and driver_id
    @classmethod
    def get_all_booked_requests(cls):
        query=  """           
                SELECT * FROM rides
                LEFT JOIN users as riders ON riders.id=rides.rider_id
                JOIN users as drivers ON drivers.id=rides.driver_id
                """
        results=connectToMySQL(cls.DB).query_db(query)
        # print("GET ALL BOOKED")
        # pprint.pprint(results)
        all_booked=[]
        for row in results:
            one_booked=cls(row)
            rider_info={
                "id":row["riders.id"],
                "first_name":row["first_name"],
                "last_name":row["last_name"],
                "email":row["email"],
                "password":row["password"],
                "created_at":row["riders.created_at"],
                "updated_at": row["riders.updated_at"]
            }
            driver_info={
                "id":row["drivers.id"],
                "first_name":row["drivers.first_name"],
                "last_name":row["drivers.last_name"],
                "email":row["drivers.email"],
                "password":row["drivers.password"],
                "created_at":row["drivers.created_at"],
                "updated_at": row["drivers.updated_at"]
            }
            rider=user_model.User(rider_info)
            one_booked.rider=rider
            driver=user_model.User(driver_info)
            one_booked.driver=driver
            all_booked.append(one_booked)
        # print("ALL booked with rider and driver", all_booked)
        return all_booked
    
    @classmethod
    def driver_cancelled(cls, data):
        query=  """ 
                UPDATE rides
                SET driver_id=Null
                WHERE rides.id=%(id)s
                """
        results=connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    #Get one request with rider_id and driver_id
    @classmethod
    def get_one_booked_requests(cls, id):
        query=  """           
                SELECT * FROM rides
                LEFT JOIN users as riders ON riders.id=rides.rider_id
                JOIN users as drivers ON drivers.id=rides.driver_id
                WHERE rides.id=%(id)s
                """
        results=connectToMySQL(cls.DB).query_db(query, id)
        print("ONE BOOKED RESULTS", results)
        one_ride_w_rider_driver=cls(results[0])
        for row in results:
            rider_info={
                "id":row["riders.id"],
                "first_name":row["first_name"],
                "last_name":row["last_name"],
                "email":row["email"],
                "password":row["password"],
                "created_at":row["riders.created_at"],
                "updated_at": row["riders.updated_at"]
            }
            driver_info={
                "id":row["drivers.id"],
                "first_name":row["drivers.first_name"],
                "last_name":row["drivers.last_name"],
                "email":row["drivers.email"],
                "password":row["drivers.password"],
                "created_at":row["drivers.created_at"],
                "updated_at": row["drivers.updated_at"]
            }
            rider=user_model.User(rider_info)
            one_ride_w_rider_driver.rider=rider
            driver=user_model.User(driver_info)
            one_ride_w_rider_driver.driver=driver
        print("ONE booked with rider and driver", one_ride_w_rider_driver)
        return one_ride_w_rider_driver
    
    @classmethod
    def update_ride(cls, data):
        query=  """
                UPDATE rides
                SET pickup_location=%(pickup_location)s, details=%(details)s
                WHERE rides.id=%(id)s
                """
        results=connectToMySQL(cls.DB).query_db(query, data)
        return results
    
    @staticmethod
    def validate_update(data):
        is_valid=True

        if len(data["pickup_location"])<3:
            flash("Pickup location required. Must be 3 or more characters", 'rides')
            is_valid=False
  
        if len(data["details"])<10:
            flash("Details required. Must be 10 or more characters", 'rides')
        return is_valid


    
    @classmethod
    def delete_request(cls, id):
        query=  """
                DELETE FROM rides
                WHERE id=%(id)s
                """
        results=connectToMySQL(cls.DB).query_db(query, id)
        return results

    @staticmethod
    def validate_ride(data):
        is_valid=True

        if len(data["destination"])<3:
            flash("Destination Required. Must be 3 or more characters", 'rides')
            is_valid=False
        if len(data["pickup_location"])<3:
            flash("Pickup location required. Must be 3 or more characters", 'rides')
            is_valid=False
        if not data["date"]:
            flash("Choose pickup date", 'rides')
            is_valid=False
        if len(data["details"])<10:
            flash("Details required. Must be 10 or more characters", 'rides')
        return is_valid
    
    
