from app import app
from app.controllers import order_controller

 
if __name__=="__main__":   
    app.run(debug=True, port=8000)