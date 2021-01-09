#!/usr/bin/python
# coding=utf-8
import sys

from django.views.decorators.http import require_http_methods
from django.http.request import *

reload(sys)
sys.setdefaultencoding('utf-8')
from translate.service.translate_service import *

translateService = TranslateService()

@require_http_methods(["GET", "POST"])
def translate_auto_controller(request, param):
    if param == "":
        if request.method == 'POST':
            param = request.POST.get('')
        elif request.method == 'GET':
            param = request.GET.get('')
            print(param)
    return translateService.translate_auto_service(param)


@require_http_methods(["GET", "POST"])
def translate_to_en_controller(request, param):
    param = param.replace("://", ":/").replace(":/", "://")
    if param == "":
        if request.method == 'POST':
            param = request.POST.get('')
        elif request.method == 'GET':
            param = request.GET.get('')
    return translateService.translate_to_en_service(param)


@require_http_methods(["GET", "POST"])
def translate_to_zh_controller(request, param):
    param = param.replace("://", ":/").replace(":/", "://")
    if param == "":
        if request.method == 'POST':
            param = request.POST.get('')
        elif request.method == 'GET':
            param = request.GET.get('')
    return translateService.translate_to_zh_service(param)
