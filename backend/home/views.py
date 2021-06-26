import logging
import pprint
import datetime

from django.http import HttpResponse
from django.views import generic
from django.utils import timezone

from backend.utils.generate_figures import plot_figure
from backend.steps.models import Step

logger = logging.getLogger(__name__)
JST = datetime.timezone(datetime.timedelta(hours=+9), "JST")


class HomeView(generic.TemplateView):
    template_name = "home/index.html"


def plot_figure_view(*args, **kwargs):
    steps = Step.objects.all().order_by("-created_at")
    data_dates = [step.created_at for step in steps]
    data_dates = [timezone.localtime(date, JST) for date in data_dates]
    data_numbers = [step.number for step in steps]

    now = timezone.localtime(timezone.now(), JST).date()
    recent_7_dates = [now + datetime.timedelta(days=i) for i in range(-6, 1)]

    x = []
    y = [0 for i in range(7)]
    for i, date in enumerate(recent_7_dates):
        for j in range(len(data_dates)):
            if date <= data_dates[j].date() < date + datetime.timedelta(days=1):
                y[i] += data_numbers[j]
        x.append(datetime.datetime.combine(date, datetime.time()))

    logger.info(pprint.pformat(x))
    logger.info(pprint.pformat(y))

    fig = plot_figure(x, y, xlabel="日時[月/日]", ylabel="歩数[回]")
    response = HttpResponse(fig, content_type="image/svg+xml")
    return response
