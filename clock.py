from apscheduler.schedulers.blocking import BlockingScheduler
from honey_love import send_msg




sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_msg, 'interval', seconds=12)

sched.start()