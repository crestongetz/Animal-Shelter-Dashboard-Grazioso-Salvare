from flask import jsonify, request
from bson.json_util import dumps
import json


def register_animal_routes(server, shelter):

    @server.route("/api/animals", methods=["GET"])
    def get_animals():
        query = request.args.to_dict()  # e.g. ?animal_type=Dog
        results = shelter.read(query)
        return json.loads(dumps(results))  # bson -> json handles ObjectId
