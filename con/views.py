# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response

# Create your views here.
class Test(views.APIView):
	def get(self, request):

		return Response({'name': 'abc'})