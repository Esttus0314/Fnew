from linebot.models import *
def stock_reply_rate():
    content_text = "想知道匯率?"
    text_message = TextSendMessage(
                                text = content_text ,
                               quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="⭐查詢單一幣別匯率", 
                                                    text="匯率查詢",
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="⭐查詢幣別匯率", 
                                                    text="輸入範例:換匯USD/TWD/100",
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="⭐關注的匯率", 
                                                    text="我的外幣",
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="⭐新增外幣", 
                                                    text="新增外幣",
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="⭐刪除外幣", 
                                                    text="輸入範例:刪除外幣USD",
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="⭐清空外幣", 
                                                    text="清空外幣",
                                                )
                                       ),
                                    ]
                                ))
    return text_message

def stock_reply_other():
    content_text = "股票那檔事"
    text_message = TextSendMessage(
                                text = content_text ,
                               quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="⭐即時股價", 
                                                    text="輸入範例:#2330",
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="⭐匯率圖", 
                                                    text="輸入範例:CTUSD",
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="⭐股價K線圖", 
                                                    text="輸入範例:@K23302024-01-01",
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="⭐新增股票目標", 
                                                    text="輸入範例:關注2330>1000",
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="⭐查詢目標清單", 
                                                    text="股票清單",
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="⭐刪除目標股票", 
                                                    text="輸入範例:刪除2330",
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="⭐清空目標股票", 
                                                    text="清空股票",
                                                )
                                       ),
                                    ]
                                ))
    return text_message

# 幣別種類Button
def show_Button():
    flex_message = FlexSendMessage(
            alt_text="幣別種類",
            contents={
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://i.imgur.com/p38wcTy.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "message",
                    "label": "action",
                    "text": "hello"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "text",
                        "text": "點擊幣別種類",
                        "size": "lg",
                        "color": "#FF6485",
                        "weight": "bold",
                        "decoration": "underline",
                        "align": "center"
                    }
                    ],
                    "backgroundColor": "#000000"
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "美金",
                            "text": "USD"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#D200D2"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "日幣",
                            "text": "JPY"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#D200D2",
                            "margin": "md"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "港幣",
                            "text": "HKD"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#D200D2",
                            "margin": "md"
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "英鎊",
                            "text": "GBP"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#FF00FF"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "澳幣",
                            "text": "AUD"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#FF00FF",
                            "margin": "md"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "加拿大幣",
                            "text": "CAD"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#FF00FF",
                            "margin": "md"
                        }
                        ],
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "瑞士法郎",
                            "text": "CHF"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#FF77FF"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "新加坡",
                            "text": "SGD"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#FF77FF",
                            "margin": "md"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "南非幣",
                            "text": "ZAR"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#FF77FF",
                            "margin": "md"
                        }
                        ],
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "瑞典幣",
                            "text": "SEK"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#FF0080"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "泰銖",
                            "text": "THB"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#FF0080",
                            "margin": "md"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "菲比索",
                            "text": "PHP"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#FF0080",
                            "margin": "md"
                        }
                        ],
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "印尼盾",
                            "text": "IDR"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#FF359A"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "韓元",
                            "text": "KRW"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#FF359A",
                            "margin": "md"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "馬來幣",
                            "text": "MYR"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#FF359A",
                            "margin": "md"
                        }
                        ],
                        "margin": "md"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "越南盾",
                            "text": "VND"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#FF60AF"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "人民幣",
                            "text": "CNY"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#FF60AF",
                            "margin": "md"
                        },
                        {
                            "type": "button",
                            "action": {
                            "type": "message",
                            "label": "紐元",
                            "text": "NZD"
                            },
                            "height": "md",
                            "style": "primary",
                            "color": "#FF60AF",
                            "margin": "md"
                        }
                        ],
                        "margin": "md"
                    }
                    ],
                    "backgroundColor": "#000000"
                }
            }
                    
    )
    return flex_message
def youtube_channel():
    flex_message = FlexSendMessage(
            alt_text="youtube_channel",
            contents=
            {
                "type": "carousel",
                "contents": [
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/SJPH542.jpg",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "size": "full",
                        "backgroundColor": "#000000"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "理財達人秀",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "最精彩最好懂",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/channel/UCQvsuaih5lE0n_Ne54nNezg"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/dPW0jcC.jpg",
                        "size": "full",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "backgroundColor": "#AA0000"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "CMoney理財寶",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "基本理財知識",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/user/CMoneySchool"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    },
                    {
                    "type": "bubble",
                    "size": "micro",
                    "hero": {
                        "type": "image",
                        "url": "https://imgur.com/zkUZrCj.jpg",
                        "size": "full",
                        "aspectMode": "fit",
                        "aspectRatio": "320:213",
                        "backgroundColor": "#444444"
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                        {
                            "type": "text",
                            "text": "我要做富翁",
                            "weight": "bold",
                            "size": "lg",
                            "wrap": True,
                            "align": "center"
                        },
                        {
                            "type": "box",
                            "layout": "baseline",
                            "contents": [
                            {
                                "type": "icon",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
                            },
                            {
                                "type": "text",
                                "text": "平民化&分享形式",
                                "size": "xs",
                                "color": "#8c8c8c",
                                "margin": "md",
                                "flex": 0,
                                "weight": "bold"
                            }
                            ]
                        },
                        {
                            "type": "button",
                            "style": "link",
                            "height": "sm",
                            "action": {
                            "type": "uri",
                            "label": "點我觀看",
                            "uri": "https://www.youtube.com/user/SyLingHim"
                            }
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "理財youtuber",
                                    "wrap": True,
                                    "color": "#8c8c8c",
                                    "size": "xxs",
                                    "flex": 5
                                }
                                ]
                            }
                            ]
                        }
                        ],
                        "spacing": "sm",
                        "paddingAll": "13px"
                    }
                    }
                ]
            }
        )
    return flex_message

def realtime_currency_other(currency):
    content = "想知道更多?"
    text_message = TextSendMessage(
                                text = content ,
                               quick_reply=QuickReply(
                                   items=[
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="即時匯率", 
                                                    text="外幣"+currency,
                                                )
                                       ),
                                       QuickReplyButton(
                                                action=MessageAction(
                                                    label="加入清單", 
                                                    text="新增外幣"+currency,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="走勢圖", 
                                                    text="CT"+currency,
                                                )
                                       ),
                                        QuickReplyButton(
                                                action=MessageAction(
                                                    label="新聞", 
                                                    text="N外匯"+currency,
                                                )
                                       )
                                ]
                            ))
    return text_message

