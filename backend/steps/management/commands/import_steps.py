import logging
import random
import datetime
import pprint
from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils import timezone

from backend.steps.models import Step

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Import steps data"

    def handle(self, *args, **options):
        Step.objects.all().delete()

        now = timezone.now()
        recent_7_dates = [now + datetime.timedelta(days=i) for i in range(-6, 1)]
        numbers = []
        dates = []
        for date in recent_7_dates:
            rand = random.randint(0, 100)
            numbers.append(rand)
            dates.append(date)

        for i in range(7):
            step = Step(
                number=numbers[i],
                created_at=dates[i]
            )
            step.save()

        logger.info("Import Steps Data")
        logger.info(pprint.pformat(numbers))
        logger.info(pprint.pformat(dates))
