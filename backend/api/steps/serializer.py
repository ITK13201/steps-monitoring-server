from rest_framework import serializers
from backend.steps.models import Step


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ("number",)
