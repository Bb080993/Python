from app import app
from app.controllers import # CHOOSE CONTROLLERS TO IMPORT

 
if __name__=="__main__":   
    app.run(debug=True, port=8000)