from pymongo import MongoClient
import urllib.parse
import datetime
import EXRate
from line_bot import *
currency_list = {
        "USD" : "美元",
        "JPY" : "日圓",
        "HKD" : "港幣",
        "GBP" : "英鎊",
        "AUD" : "澳幣",
        "CAD" : "加拿大幣",
        "CHF" : "瑞士法郎",
        "SGD" : "新加坡幣",
        "ZAR" : "南非幣",
        "SEK" : "瑞典幣",
        "NZD" : "紐元",
        "THB" : "泰銖",
        "PHP" : "菲國比索",
        "IDR" : "印尼幣",
        "KRW" : "韓元",
        "MYR" : "馬來幣",
        "VND" : "越南盾",
        "CNY" : "人民幣",
    }


Authdb='test-good1'
stockDB='mydb'
currencyDB = 'users'
dbname = 'test-good1'

def constructor_stock():
    client = MongoClient("mongodb://ronywu:LAINvem0314@ac-bqvk48i-shard-00-00.mdetvrd.mongodb.net:27017,ac-bqvk48i-shard-00-01.mdetvrd.mongodb.net:27017,ac-bqvk48i-shard-00-02.mdetvrd.mongodb.net:27017/?ssl=true&replicaSet=atlas-104wi3-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0")
    db = client[stockDB]
    return db

def constructor_currency():
    client = MongoClient("mongodb://ronywu:LAINvem0314@ac-bqvk48i-shard-00-00.mdetvrd.mongodb.net:27017,ac-bqvk48i-shard-00-01.mdetvrd.mongodb.net:27017,ac-bqvk48i-shard-00-02.mdetvrd.mongodb.net:27017/?ssl=true&replicaSet=atlas-104wi3-shard-0&authSource=admin&retryWrites=true&w=majority&appName=Cluster0")
    db = client[currencyDB]
    return db

#-----------------新增使用者的股票-------------------

def write_my_stock(userID, user_name, stockNumber, condition, target_price):
    db=constructor_stock()
    collect =db[user_name]
    is_exit = collect.find_one({"favorite_stock":stockNumber})
    if is_exit != None :
        content = update_my_stock(user_name, stockNumber, condition, target_price)
        return content
    else:
        collect.insert_one({
            "userID":userID,
            "favorite_stock":stockNumber,
            "condition":condition,
            "price":target_price,
            "tag":"stock",
            "date_info":datetime.datetime.now()
        })
    return f"{stockNumber}已新增至您的股票清單"
#----------------更新站存的股票名稱--------------------
def update_my_stock(user_name, stockNumber, condition, target_price):
    db=constructor_stock()
    collect = db[user_name]
    collect.update_many({"favorite_stock":stockNumber},{'$set':{'condition':condition, "price":target_price}})
    content = f"股票{stockNumber}更新成功"
    return content
#---------------秀出使用者的股票條件--------------------
def  show_stock_settimg(user_name, userID):
    db = constructor_stock()
    collect = db[user_name]
    datalist = list(collect.find({"userID":userID}))
    if datalist == []: return "您的股票清單為空，請透過指令新增股票至清單中"
    content = "您清單中的選股條件為: \n"
    for i in range(len(datalist)):
        content += f'{datalist[i]["favorite_stock"]} {datalist[i]["condition"]} {datalist[i]["price"]}\n'
    return content
#--------------    刪除使用者特定的股票     --------------------
def delete_my_stock(user_name, stockNumber):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_one({'favorite_stock':stockNumber})
    return stockNumber + "刪除成功"
#--------------刪除使用者股票清單內所有的股票--------------------
def delete_my_allstock(user_name, userID):
    db = constructor_stock()
    collect = db[user_name]
    collect.delete_many({'userID':userID})
    return "全部股票刪除成功"
#----------------------------  更新匯率清單的匯率  --------------------------
def update_my_currency(user_name, currency, condition , target_price):
    db=constructor_currency()
    collect = db[user_name]
    collect.update_many({"favorite_currency": currency }, {'$set': {'condition':condition , "price": target_price}})
    return f"{currency_list[currency]}更新成功"
#----------------------------  新增匯率至匯率清單  -------------------------
def write_my_currency(userID , user_name, currency, condition, target_price):
    db = constructor_currency()
    collect = db[user_name]
    is_exit = collect.find_one({"favorite_currency": currency})
    content = ""
    if is_exit != None : return update_my_currency(user_name, currency, condition , target_price)
    else:
        collect.insert_one({
                "userID": userID,
                "favorite_currency": currency,
                "condition" :  condition,
                "price" : target_price,
                "tag": "currency",
                "date_info": datetime.datetime.now()
            })
        return f"{currency_list[currency]}已新增至您的外幣清單"

#------------------查詢資料庫中匯率清單的匯率(文字)---------------------------
def show_my_currency(userID, user_name):
    db = constructor_currency()
    collect = db[user_name]
    datalist = list(collect.find({"userID": userID}))
    if datalist == []: return "您的外幣清單為空，請透過指令新增外幣至清單中"
    content = ""
    for i in range(len(datalist)):
        content += EXRate.showCurrency(datalist[i]["favorite_currency"])
    return content

#-------------------刪除使用者清單特定的匯率------------------------------
def delete_my_currency(user_name, currency):
    db = constructor_currency()
    collect = db[user_name]
    collect.delete_one({'favorite_currency': currency})
    return currency_list[currency] + "刪除成功"

#---------------------刪除匯率清單全部匯率-------------------------------
def delete_my_allcurrency(user_name, userID):
    db = constructor_currency()
    collect = db[user_name]
    collect.delete_many({'userID': userID})
    return "外幣清單已清空"