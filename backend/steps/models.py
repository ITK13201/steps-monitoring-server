import uuid
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _


class Step(models.Model):
    id = models.BigAutoField(_("ID"), primary_key=True, editable=False)
    number = models.IntegerField(_("歩数"), blank=False, null=False)
    created_at = models.DateTimeField(
        _("作成日時"), default=timezone.now, blank=False, null=False
    )
    updated_at = models.DateTimeField(
        _("更新日時"), default=timezone.now, blank=False, null=False
    )

    class Meta:
        verbose_name = "step"
        verbose_name_plural = "steps"

    def __str__(self):
        return str(self.created_at)
