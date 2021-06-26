import logging
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
        serializer = StepSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {"message": "Successfully created!"}
            logger.info(request.data)
            return Response(context, status=status.HTTP_201_CREATED)

        context = {"message": "invalid."}
        return Response(context, status=status.HTTP_400_BAD_REQUEST)
