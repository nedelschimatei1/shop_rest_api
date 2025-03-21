from time import sleep
from celery import shared_task


@shared_task
def notify_customers(message):
    print('Sending a lot of emails')
    print(message)
    sleep(10)
    print('Emails were sent!')
