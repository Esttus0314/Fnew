import matplotlib
matplotlib.use('Agg')
import datetime
from imgurpython import ImgurClient
client_id = '64fe46625b944a1'
client_secret = 'a4af3027c5f554675a91015a3b5cc6920d8fac44'
album_id = 'fnewstock'
access_token = 'cf2cc94a1742b039631372f209569ab48655cf17'
refresh_token = '7590522a1ee2e179c737398c0d7e5816ed8a88da'

# https://imgur.com/#access_token=cf2cc94a1742b039631372f209569ab48655cf17&expires_in=315360000&token_type=bearer&refresh_token=7590522a1ee2e179c737398c0d7e5816ed8a88da&account_username=Rony0214&account_id=183376089

def showImgur(fileName):
    client = ImgurClient(client_id, client_secret, access_token, refresh_token)

    config = {
        'album':album_id,
        'name':fileName,
        'title':fileName,
        'description':str(datetime.date.today())
        }
    
    try:
        print("[log:INFO]Uploading image... ")
        imgurl = client.upload_from_path(fileName+'.png', config=config, anon=False)['link']
        print('[log:INFO]Done upload. ')
    except:
        imgurl = 'https://imgur.com/RPrGnmI'
        print('[log:ERROR]Unable upload ! ')

    return imgurl