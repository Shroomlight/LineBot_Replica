from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request as request
import datetime

clock = BlockingScheduler()

@clock.scheduled_job('cron', day_of_week='0-6', hour='5-22', minute='*/2')
def scheduled_job():
    print("\n"+"===== APScheduler ====="+"\n")
    print("clock.py runs every AM:6.00 to PM:11.00 */2")
    print("Current time："f'{datetime.datetime.now().ctime()}'"\n")
    print("===== APScheduler =====")

    try:
        url = "https://replicabot.herokuapp.com/"
        conn = request.urlopen(url)
        servertime=conn.getheaders()[2][1]
        print("ServerTime："+servertime)
        print("Success")

    except:
        print("Error！")

clock.start()