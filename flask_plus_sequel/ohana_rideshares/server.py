from app import app
from app.controllers import rides_controller, users_controller

 
if __name__=="__main__":   
    app.run(debug=True, port=8000)