from app import app
from app.controllers import authors_controller, books_controller# CHOOSE CONTROLLERS TO IMPORT

 
if __name__=="__main__":   
    app.run(debug=True, port=8000)