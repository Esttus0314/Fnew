from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import(
    InvalidSignatureError
)
from linebot.models import(
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage, FollowEvent, UnfollowEvent, TemplateSendMessage, CarouselColumn, CarouselTemplate, URIAction
)
line_bot_api = LineBotApi('7o16UDg5Pw9rantbAH1yE7aVZG1UQQyTlNpRtR17oUQ5Mcj2/rJyRpqcq106EIHQt38XThD9j+e8idMjyCpmvCUoKXbhgxyDMHT3ZlLPwvkym3GSuPIF8KdviR6JELjCxcklBRXBsdPNfTsjGvHrVQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('97f78a395232acacea8c91df82d9e0b1')