from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request as request

clock = BlockingScheduler()

@clock.scheduled_job('cron', day_of_week='0-6', hour='5-22', minute='*/2')
def scheduled_job():
    url = "https://replicabot.herokuapp.com/"
    conn = request.urlopen(url)
        
    for key, value in conn.getheaders():
        print(key, value)

clock.start()