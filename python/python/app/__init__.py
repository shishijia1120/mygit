from flask import  Flask
from flask_restful import Api
from flask_cors import  CORS
from app import resource

app = Flask(__name__)

def create_app():

     CORS(app)
     app.scret_key="A0Zr98j/3yX R~XHH!jmNjLWX/,?RT"
     api = Api(app)
     api.add_resource(resource.ResourceUser,"/")
     return app

 if __name__=="__main__":
     app = create_app()
     app.run()