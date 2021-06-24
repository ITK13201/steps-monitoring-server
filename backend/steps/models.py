from django.db import models
from django.utils.translation import gettext_lazy as _


class Step(models.Model):
    number = models.IntegerField(_("歩数"), blank=False, null=False)
    created_at = models.DateTimeField(_("作成日時"), auto_now_add=True)
    updated_at = models.DateTimeField(_("更新日時"), auto_now=True)

    class Meta:
        verbose_name = "step"
        verbose_name_plural = "steps"

    def __str__(self):
        return self.number
