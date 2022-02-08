from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone

from .models import Meet

DATETIME_FORMAT = '%d/%b/%Y %H:%M:%S'


def log(msg):
    now = timezone.now()
    print(f'[{now.strftime(DATETIME_FORMAT)}] {msg}')


def _update_meets():
    now = timezone.now()
    seven_days = timezone.timedelta(days=7)

    log('Starting Meet Updates')
    for meet in Meet.objects.filter(end_datetime__lt=now):
        meet.start_datetime += seven_days
        meet.end_datetime += seven_days
        meet.save()
    log('Ended Meet Updates')


def run_schedules():
    scheduler = BackgroundScheduler(
        timezone=timezone.get_current_timezone_name())
    scheduler.add_job(_update_meets, 'cron', hour=00)
    scheduler.start()
