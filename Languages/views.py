from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Language
from .serializers import LanguageSerializer


class LanguageList(APIView):

    def get(self, request, *args, **kwargs):
        language_name = self.kwargs.get('languageName', None)
        if language_name is None:
            language = Language.objects.all()
        else:
            language = Language.objects.filter(language_name=language_name.title())
        serializer = LanguageSerializer(language, many=True)

        return Response(serializer.data)

    def post(self):
        pass

