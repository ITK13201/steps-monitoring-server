import logging
import urllib.parse
import pprint
from django.http.request import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

from .serializer import StepSerializer
from backend.steps.models import Step


logger = logging.getLogger(__name__)


class StepAddAPIView(APIView):
    authentication_classes = (authentication.BasicAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        context = {"message": "Unsupported method ('GET')"}
        return Response(context, status=status.HTTP_501_NOT_IMPLEMENTED)

    def post(self, request: HttpRequest):
        query = request.META.get("QUERY_STRING")
        param = urllib.parse.parse_qs(query)
        is_valid = False
        try:
            param["number"] = param.get("number")[0]
            serializer = StepSerializer(data=param)
            is_valid = serializer.is_valid()
        except TypeError:
            pass

        if is_valid:
            serializer.save()
            logger.info("data:" + pprint.pformat(param))
            context = {"message": "Successfully created!", "data": param}
            return Response(context, status=status.HTTP_201_CREATED)
        else:
            logger.info("data:" + pprint.pformat(param))
            context = {"message": "invalid.", "data": param}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)