from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request as request
import datetime

clock = BlockingScheduler()

@clock.scheduled_job('cron', day_of_week='0-6', hour='5-22', minute='*/20')
def scheduled_job():
    print(">>=== APScheduler ====="+"\n")
    print("clock.py runs every AM:6.00 to PM:11.00 */20")
    print("CurrentTime："+f'{datetime.datetime.now().ctime()}')

    try:
        url = "https://replicabot.herokuapp.com/"
        conn = request.urlopen(url)
        servertime=conn.getheaders()[2][1]
        print("ServerTime："+servertime)
        print("[Success]"+"\n")
        print("===== APScheduler ====<<")

    except:
        print("[Error！]"+"\n")
        print("===== APScheduler ====<<")

clock.start()