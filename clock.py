from apscheduler.schedulers.blocking import BlockingScheduler
import urllib

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='0-6', hour='5-22', minute='*/20')
def scheduled_job():
    url = "https://replicabot.herokuapp.com/"
    conn = urllib.request.urlopen(url)
        
    for key, value in conn.getheaders():
        print(key, value)

sched.start()