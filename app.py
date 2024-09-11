from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from line_bot import *
import re 
import requests
from bs4 import BeautifulSoup
import datetime
import twstock
import Msg_Template
import mongodb
import EXRate
import json, time
import place

app = Flask(__name__)
IMGUR_CLIENT_ID = '64fe46625b944a1'
access_token = '7o16UDg5Pw9rantbAH1yE7aVZG1UQQyTlNpRtR17oUQ5Mcj2/rJyRpqcq106EIHQt38XThD9j+e8idMjyCpmvCUoKXbhgxyDMHT3ZlLPwvkym3GSuPIF8KdviR6JELjCxcklBRXBsdPNfTsjGvHrVQdB04t89/1O/w1cDnyilFU='

#暫存用dict
mat_d={}
#K線圖
import yfinance as yf
import mplfinance as mpf
import pyimgur

def plot_stock_k_chart(IMGUR_CLIENT_ID, stock="0050", date_from='2020-01-01'):
    """
    進行個股K線圖繪製，回傳至於雲端圖床的連結。將顯示包含5MA、20MA及量價關係，起始預設自2020-01-01起到昨日收盤價。
    :stock :個股代碼(字串)，預設0050。
    :date_from :起始日(字串)，格視為YYYY-MM-DD，預設自2020-01-01起。
    """
    stock = str(stock) + ".TW"
    try:
        #使用yfinance獲取數據
        print(f"正在獲取股票數據: {stock}")
        df = yf.download(stock, start=date_from)
        
        #檢查數據是否獲取成功
        if df is None or df.empty:
            print(f"未能獲取到股票數據，可能因為股票代碼不正確或數據來源問題。")
            return None
        
        print("股票數據獲取成功，開始繪製K線圖...")
        mpf.plot(df, type='candle', mav=(5, 20), volume=True, ylabel=stock.upper() + 'Price', savefig='testsave.png')

        #上傳圖片到Imgur

        PATH = "testsave.png"
        im = pyimgur.Imgur(IMGUR_CLIENT_ID)
        uploaded_image = im.upload_image(PATH, title=stock + "candlestick chart")
        print(f"上傳圖片成功: {uploaded_image.link}")
        return uploaded_image.link
    
    except Exception as e:
        print(f"錯誤: {e}")
        return None

# 抓使用者設定他關心的股票
def cache_users_stock():
    db=mongodb.constructor_stock()
    nameList = db.list_collection_names()
    users = []
    for i in range(len(nameList)):
        collect = db[nameList[i]]
        cel = list(collect.find({"tag":'stock'}))
        users.append(cel)
    return users
# 油價查詢
def oil_price():
    target_url = 'https://gas.goodlife.tw/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    title = soup.select('#main')[0].text.replace('\n', '').split("(")[0]
    gas_price = soup.select('#gas-price')[0].text.replace('\n\n\n', '').replace(' ', '')
    cpc = soup.select('#cpc')[0].text.replace(' ', '')
    content = '{}\n{}{}'.format(title, gas_price, cpc)
    return content

def push_msg(event, msg):
    try:
        user_id = event.source.user_id
        line_bot_api.push_message(user_id, TextSendMessage(text=msg))
    except:
        room_id = event.source.user_id
        line_bot_api.push_message(room_id, TextSendMessage(text=msg))
def reply_image(msg, rk, token):
    headers = {'Authorization':f'Bearer {token}', 'Content-Type':'application/json'}
    body = {
    'replyToken':rk,
    'messages':[{
            'type': 'image',
            'originalContentUrl': msg,
            'previewImageUrl':msg
        }]
    }
    req = requests.request('POST', 'https://api.line.me/v2/bot/message/reply', headers = headers, data=json.dumps(body).encode('utf-8'))
    print(req.text)

def cache_users_currency():
    db=mongodb.constructor_currency()
    nameLsit = db.list_collection_names()
    users = []
    for i in range(len(nameLsit)):
        collect = db[nameLsit(i)]
        cel = list(collect.find({"tag":'currency'}))
        users.append(cel)
    return users
def Usage(event):
    push_msg(event, '  ***使用說明***   \
             \n\
             \n 本機器人可查詢油價、匯率、股票、氣象\
             \n\
             \n 點擊下方"點我"，方便快速查詢\
             \n\
             \n⭐最新氣象 >>>> 雷達回波&氣象網站\
             \n⭐油價查詢 >>>> 最新油價&預計調整\
             \n⭐匯率大小事 >> 匯率查詢&匯率兌換 \
             \n⭐股價查詢 >>>> 即時股價&股票關注\
             \n\
             \n 有任何問題可以聯繫:\
             \n ronywu0214@gmail.com')

@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    try:
        handler.handle(body, signature)

        json_data = json.loads(body)
        reply_token = json_data['events'][0]['replyToken']
        user_id = json_data['events'][0]['source']['userId']
        print(json_data)
        if 'message' in json_data['events'][0]:
            if json_data['events'][0]['message']['type'] == 'text':
                text = json_data['events'][0]['message']['text']
                if text == '雷達回波圖' or text == '雷達回波':
                    reply_image(f'https://cwbopendata.s3.ap-northeast-1.amazonaws.com/MSC/O-A0058-003.png?{time.time_ns()}', reply_token, access_token)

    except:
        print('error')
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text))
    msg = str(event.message.text).upper().strip()
    profile = line_bot_api.get_profile(event.source.user_id)

    usespeak=str(event.message.text)
    uid = profile.user_id
    user_name = profile.display_name

    if event.message.text == '油價查詢':
        content = oil_price()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content)
        )

################## K線圖 ##########################
    if event.message.text[:2].upper()== "@K":
        input_word = event.message.text.replace(" ","")
        stock_name = input_word[2:6]
        start_date = input_word[6:]
        content = plot_stock_k_chart(IMGUR_CLIENT_ID,stock_name,start_date)
        message = ImageSendMessage(original_content_url=content,preview_image_url=content)
        line_bot_api.reply_message(event.reply_token, message)

#################### 目錄區 ###########################
    if event.message.text == '使用說明':
        Usage(event)
    if event.message.text == '召喚選單': 
        message = TemplateSendMessage(
        alt_text='目錄 template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/rwR2yUr.jpg',
                        title='選擇服務',
                        text='請選擇',
                        actions=[
                            URIAction(
                                label='yahoo股市',
                                uri='https://liff.line.me/2006134066-epqYprqO'
                            ),
                            URIAction(
                                label='國際金融',
                                uri='https://liff.line.me/2006134066-1vd2egdj'
                            ),
                            URIAction(
                                label='聯成粉絲團',
                                uri='https://zh-tw.facebook.com/lccnet10/'
                            )
                        ]
                ),
                CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/VqOzXUo.jpeg',
                        title='來點音樂',
                        text='請選擇',
                        actions=[
                            URIAction(
                                label='2024抖音',
                                uri='https://liff.line.me/2006134066-1X075P0L'
                            ),
                            URIAction(
                                label='Relexingmusic',
                                uri='https://liff.line.me/2006134066-EG91GB93'
                            ),
                            URIAction(
                                label='HACHI',
                                uri='https://liff.line.me/2006134066-1VKjrBKL'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    if re.match("理財",msg):
        content = Msg_Template.youtube_channel()
        line_bot_api.push_message(uid, content)
        return 0
    if re.match('股票那檔事', msg):
        message = Msg_Template.stock_reply_other()
        line_bot_api.reply_message(event.reply_token, message)
######################股票區########################
    if event.message.text == "股價查詢":
        line_bot_api.push_message(uid,TextSendMessage("請輸入#股票代號....."))
    #新增使用者關注的股票到mongodb EX:關注2330>xxx
    if re.match('關注[0-9]{4}[<>][0-9]', msg):
        stockNumber = msg[2:6]
        content = mongodb.write_my_stock(uid, user_name, stockNumber, msg[6:7], msg[7:])
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    # 查詢股票篩選條件清單
    if re.match('股票清單', msg):
        line_bot_api.push_message(uid, TextSendMessage('稍等一下, 股票查詢中...'))
        content = mongodb.show_stock_settimg(user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    # 刪除存在資料庫裡面的股票
    if re.match('刪除[0-9]{4}', msg):
        content = mongodb.delete_my_stock(user_name,msg[2:])
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    # 清空存在資料庫裡面的股票
    if re.match('清空股票', msg):
        content = mongodb.delete_my_allstock(user_name,uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    if (msg.startswith('#')):
        text = msg[1:]
        content = ''

        stock_rt = twstock.realtime.get(text)
        my_datetime = datetime.datetime.fromtimestamp(stock_rt['timestamp']+8*60*60)
        my_time = my_datetime.strftime('%H:%M:%S')

        content += '%s (%s) %s\n'%(
            stock_rt['info']['name'],
            stock_rt['info']['code'],
            my_time
        )
        content += '現價: %s / 開盤: %s\n'%(
            stock_rt['realtime']['latest_trade_price'],
            stock_rt['realtime']['open']
        )
        content += '最高: %s / 最低: %s\n'%(
            stock_rt['realtime']['high'],
            stock_rt['realtime']['low']
        )
        content += '量: %s\n' %(stock_rt['realtime']['accumulate_trade_volume'])

        stock = twstock.Stock(text)
        content += '-----\n'
        content += '最近五日價格: \n'
        price5 = stock.price[-5:][::-1]
        date5 = stock.date[-5:][::-1]
        for i in range(len(price5)):
            content += '[%s] %s\n' %(date5[i].strftime("%Y-%m-%d"), price5[i])
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content)
        )
###################### 股票提醒 ##############################
    if re.match("關閉提醒",msg):
        import schedule
        schedule.clear()
    if re.match("股價提醒",msg):
        import schedule
        import time
        #查看當前股價
        def look_stock_price(stock, condition, price, userID):
            print(userID)
            url = 'https://tw.stock.yahoo.com/q/q?s=' + stock
            list_req = requests.get(url)
            soup = BeautifulSoup(list_req.content, "html.parser")
            getstock = soup.find('span', class_='Fz(32px)').string
            content = stock + "當前股市價格為: " + getstock
            if condition == '<':
                content += "\n篩選條件為: < "+ price
                if float(getstock) < float(price):
                    content += "\n符合" + getstock + " < " + price + "的篩選條件"
                    line_bot_api.push_message(userID, TextSendMessage(text=content))
            elif condition == '>':
                content += "\n篩選條件為: > "+ price
                if float(getstock) > float(price):
                    content += "\n符合" + getstock + " > " + price + "的篩選條件"
                    line_bot_api.push_message(userID, TextSendMessage(text=content))
            elif condition == '=':
                content += "\n篩選條件為: = "+ price
                if float(getstock) > float(price):
                    content += "\n符合" + getstock + " = " + price + "的篩選條件"
                    line_bot_api.push_message(userID, TextSendMessage(text=content))
        # look_stock_price(stock='2002', condition='>', price=31)
        def job():
            print('HH')
            dataList = cache_users_stock()
            #print(dataList)
            for i in range(len(dataList)):
                for k in range(len(dataList[i])):
                    #print(dataList[i][k])
                    look_stock_price(dataList[i][k]['favorite_stock'], dataList[i][k]['condition'], dataList[i][k]['price'], dataList[i][k]['userID'])
                    # look_stock_price(stock='2002', condition='>', price=31)
        schedule.every(5).seconds.do(job).tag('daily-tasks-stock'+uid, 'second')
        while True:
            schedule.run_pending()
            time.sleep(10)
######################## 匯率區 ############################
    if re.match('匯率查詢',msg):
        message = Msg_Template.show_Button()
        line_bot_api.reply_message(event.reply_token,message)
    if re.match('匯率大小事',msg):
        btn_msg = Msg_Template.stock_reply_rate()
        line_bot_api.push_message(uid, btn_msg)
        return 0
    if re.match('[A-Z]{3}',msg):
        currency_name = EXRate.getCurrencyName(msg)
        if currency_name == '無可支援的外幣': content = "無可支援的外幣"
        else:
            line_bot_api.push_message(uid, TextSendMessage("正在為您做外幣換算......"))
            content = EXRate.showCurrency(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    if re.match('換匯[A-Z]{3}/[A-Z]{3}/[0-9]',msg):
        line_bot_api.push_message(uid, TextSendMessage("將為您做外匯計算....."))
        content = EXRate.getExchangeRate(msg)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    if re.match('新增外幣[A-Z]{3}',msg):
        currency = msg[4:7]
        currency_name = EXRate.getCurrencyName(currency)
        if currency_name == '無可支援的外幣': content = "無可支援的外幣"
        elif re.match('新增外幣[A-Z]{3}[<>][0-9]',msg):
            content = mongodb.write_my_currency(uid, user_name, currency, msg[7:8], msg[8:])
        else:
            content = mongodb.write_my_currency(uid, user_name, currency, "未設定", "未設定")
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    if re.match('我的外幣', msg):
        line_bot_api.push_message(uid, TextSendMessage('稍等一下, 匯率查詢中...'))
        content = mongodb.show_my_currency(uid, user_name)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    if re.match('刪除外幣[A-Z]{3}', msg):
        content = mongodb.delete_my_currency(user_name, msg[4:7])
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
    if re.match('清空外幣', msg):
        content = mongodb.delete_my_currency(user_name, uid)
        line_bot_api.push_message(uid, TextSendMessage(content))
        return 0
#################### 匯率圖 ###################################
    if re.match("ct[A-Z]{3}", msg):
        currency = msg[2:5]
        if EXRate.getCurrencyName(currency) == "無可支援的外幣":
            line_bot_api.push_message(uid, TextSendMessage('無可支援的外幣'))
            return 0
        line_bot_api.push_message(uid, TextSendMessage('稍等一下, 將會給您匯率走勢圖'))
        cash_imgurl = EXRate.cash_exrate_sixMonth(currency)
        if cash_imgurl == "現金匯率無資料可分析":
            line_bot_api.push_message(uid, TextSendMessage('現金匯率無資料可分析'))
        else:
            line_bot_api.push_message(uid, ImageSendMessage(original_content_url=cash_imgurl, preview_image_url=cash_imgurl))
        
        spot_imgurl = EXRate.spot_exrate_sixMonth(currency)
        if spot_imgurl == "即期匯率無資料可分析":
            line_bot_api.push_message(uid, TextSendMessage('即期匯率無資料可分析'))
        else:
            line_bot_api.push_message(uid, ImagemapSendMessage(original_content_url=spot_imgurl, preview_image_url=spot_imgurl))
        btn_msg = Msg_Template.realtime_currency_other(currency)
        line_bot_api.push_message(uid, btn_msg)
        return 0
    ###########################################################################
    #圖文選單
    #第一層-最新氣象->4格圖片flex message
    if re.match('最新氣象|查詢天氣|天氣查詢|weather|Weather',msg):
        content = place.img_Carousel()
        line_bot_api.reply_message(event.reply_token,content)
        return 0
    #######################1.即時天氣-OK##############################
    # 1.第二層 及時天氣->呼叫quick_reply
    if re.match('即時天氣|即時氣象',msg):
        mat_d[uid]='即時天氣'
        content=place.quick_reply_weather(mat_d[uid])
        line_bot_api.reply_message(event.reply_token, content)
        return 0
    
@handler.add(FollowEvent)
def handle_follow(event):
    welcome_msg = '''Hello! 您好，歡迎您成為 Master 財經小幫手 的好友!

我是Master 財經小幫手

-這裡有股票，匯率資訊哦~
-直接點選下方[圖中]選單功能

-期待您的光臨'''

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=welcome_msg)
    )

@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print(event)





if __name__ == '__main__':
    app.run()