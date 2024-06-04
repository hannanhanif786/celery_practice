from celery import shared_task
from celerypractice.celery import app
import time


@shared_task
def sum_numbers(a, b):
    time.sleep(20)
    return a + b


@shared_task
def sub_numbers(a, b):
    time.sleep(20)
    return a - b