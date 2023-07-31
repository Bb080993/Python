from app import app
from app.controllers import dojo_controller
from app.controllers import ninja_controller

 
if __name__=="__main__":   
    app.run(debug=True, port=8000)