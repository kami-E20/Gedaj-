
import schedule
import time
from scripts.generate_film_message import send_film_of_the_day
from scripts.generate_quiz_message import send_quiz_of_the_day

def run_scheduler():
    schedule.every().day.at("08:59").do(send_film_of_the_day)
    schedule.every().day.at("09:00").do(send_quiz_of_the_day)

    while True:
        schedule.run_pending()
        time.sleep(1)
