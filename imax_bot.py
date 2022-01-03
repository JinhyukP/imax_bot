from bs4 import BeautifulSoup 
import requests 
import datetime 
import telegram 
from apscheduler.schedulers.blocking import BlockingScheduler 

# make telegram bot and write your token here
bot = telegram.Bot(token="1234567890:AAAAAAAAAA11111111aaaaaaaaaaaa")

def movie_alarm_telegram(areacode='01', theatercode='0013', date='20220101', check_title='스파이더맨-노 웨이 홈', chat_id='telegram_chat_id'):
    movie_dict = {}
    
    url = f"http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode={areacode}&theatercode={theatercode}&date={date}"

    request = requests.get(url)
    html_txt = request.text
    html_soup = BeautifulSoup(html_txt, 'html.parser')

    movie_titles = []
    result = []
    
    movie_infos = html_soup.select("div.col-times > div.info-movie")
    check_date = (date in html_txt)
    if (movie_infos and check_date):
        for movie_info in movie_infos:
            screentype_list = []
            title = movie_info.select('a > strong')[0].text.strip()
            result.append(title)

            screentypes = movie_info.parent.select("span.screentype")

            for screentype in screentypes:
                screentype_list.append(str(screentype.text))

            movie_dict[title] = ", ".join(screentype_list)

        for movie in movie_dict.keys():
            movie_open_check_condition1 = (check_title == movie)
            if True in {movie_open_check_condition1}:
                bot.sendMessage(chat_id=chat_id, text = f"{movie}의 {movie_dict[movie]}예매가 오픈되었습니다.")           
    else:
#         bot.sendMessage(chat_id=chat_id, text = "아직 오픈된 예매가 없습니다.")
        print(datetime.datetime.now().strftime("%Y-%m-%d | %H:%M:%S"), "아직 오픈된 예매가 없습니다.")
        
if __name__ == "__main__":
    movie_alarm_telegram(areacode='01', theatercode='0013', date='20220105', check_title='스파이더맨-노 웨이 홈', chat_id='chat id')

sc = BlockingScheduler()
sc.add_job(movie_alarm_telegram, 'interval', seconds = 30)
sc.start()    