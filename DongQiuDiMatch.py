import requests, re, time
from lxml import etree


    
def sleepTime(hour, min, sec):
    return hour * 3600 + min * 60 + sec
def start():
    second = sleepTime(0, 0, 5)
    while 1 == 1:
        time.sleep(second)
        print('do action')
        test_url = 'https://www.dongqiudi.com/live'

        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }
        reponse = requests.get(url = test_url, headers = headers).text
        html_etree = etree.HTML(reponse)
        allMatch = html_etree.xpath('//*[@id="__layout"]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div')
        for ama in allMatch:
            match = ama.xpath('./div')
            matchDate = ama.xpath('./p/text()')[0]
            print('\n比赛时间:'+matchDate+"\n")
            for ma in match:
                matchTime = ma.xpath('./a/span[1]/text()')[0]
                matchType = ma.xpath('./a/span[2]/text()')[0]
                matchMaster = ma.xpath('./a/div/p[1]/a/span/text()')[0]
                matchGuest = ma.xpath('./a/div/p[2]/a/span/text()')[0]
                matchData = ma.xpath('./a/div/div//p/@class')[0]
                matchScore = ma.xpath('./a/div/div//p/text()')[0]
                if (matchData == 'feature'):
                    matchStatus = '未开始'
                if (matchData == 'going'):
                    matchStatus = '进行中'
                if (matchData == 'score'):
                    matchStatus = '已结束'
                
                print((matchTime+"|比赛类型:"+matchType+'|'+matchMaster+" "+matchScore+' '+matchGuest+"|比赛状态:"+matchStatus).replace('  ',' '))
if __name__ == "__main__":
    start()
