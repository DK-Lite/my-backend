import json
from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient



@api.route('/')
@api.param('','')
@api.response(404, 'not found.')
class Warehouse(Resource):
    @api.doc('get a warehouse')
    def get(self):
        pass

    def post(self):
        data = request.json
        return chart(data=data)
    