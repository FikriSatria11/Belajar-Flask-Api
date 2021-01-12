# import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# inisiasi objek flask
app = Flask(__name__)

# inisiasi objek flask_resful
api = Api(app)

# inisiasi objek flask_core
CORS(app)

# inisiasi variabel kosong bertipi dictionary
identitas = {} # variabel global, dictionary = json

# membuat class resource
class ContohResource(Resource):
    # method get dan post
    def get(self):
        #response = {"msg":"hallo dunia, ini app restfull pertamaku"}
        return identitas
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg" : "data berhasil dimasukkan"}
        return response

# setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")