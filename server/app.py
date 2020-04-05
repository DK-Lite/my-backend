import json
from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)

def change_key(dic, key, value):
    dic[key]=value
    return dic

@app.route("/", methods=["GET"])
def StartPage():
    return 'hello'
@app.route("/data-lake/apt-trade-info", methods=['POST'])
def PostDataLake():
    client = MongoClient("mongo", 27017)
    db = client.data_lake
    collection = db.apt_trade_info
    collection.insert(request.form.to_dict())
    client.close()
    return "Success!!"

@app.route("/data-lake/apt-trade-info", methods=['GET'])
def GetDataLake():
    client = MongoClient("mongo", 27017)
    db = client.data_lake
    collection = db.apt_trade_info
    cursor = collection.find()
    docs = [ change_key(doc,'_id', idx) for idx, doc in enumerate(cursor)]
    client.close()
    return { 'info': docs }

@app.route("/data-warehouse/apt-trade-info", methods=['GET'])
def GetDataWarehouse():
    client = MongoClient("mongo", 27017)
    db = client.data_warehouse
    collection = db.apt_trade_info
    cursor = collection.find()
    docs = [ change_key(doc,'_id', idx) for idx, doc in enumerate(cursor)]
    client.close()
    return { 'info': docs }

@app.route("/data-warehouse/apt-unique-info", methods=['GET'])
def GetAptUniInfo():
    client = MongoClient("mongo", 27017)
    db = client.data_warehouse
    collection = db.apt_unique_info
    cursor = collection.find()
    docs = [ change_key(doc,'_id', idx) for idx, doc in enumerate(cursor)]
    client.close()
    return { 'info': docs }

@app.route("/data-warehouse/apt-unique-info/apt-info", methods=['POST'])
def PostAptInfoFrom():
    client = MongoClient("mongo", 27017)
    db = client.data_warehouse
    collection = db.apt_trade_info
    cursor = collection.find(request.json)
    docs = [ change_key(doc,'_id', idx) for idx, doc in enumerate(cursor)]
    client.close()
    return { 'info': docs }

@app.route("/data-mart/apt-trade-month-avg/apt-info", methods=['POST'])
def PostAptAvgFrom():
    client = MongoClient("mongo", 27017)
    db = client.data_mart
    collection = db.apt_trade_month_avg
    cursor = collection.find(request.json)
    docs = [ doc for idx, doc in enumerate(cursor)]
    client.close()
    return { 'info': docs }


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port='3691')

