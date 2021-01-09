#!/usr/bin/python
# coding=utf-8

# from translate.utils.kate_translate import *
# from translate.utils.google_translate import *
# from translate.utils.youdao_translate import *
from translate.utils.baidu_translate import *
from translate.utils.response import get_server_response
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class TranslateService:

    translater = ""

    def __init__(self):
        self.translater = BaiduTranslate()

    def translate_auto_service(self, param):
        try:
            result = self.translater.translate_auto(param)
            return get_server_response(result)
        except:
            return get_server_response()

    def translate_to_en_service(self, param):
        try:
            result = self.translater.translate_to_en(param)
            return get_server_response(result)
        except:
            return get_server_response()

    def translate_to_zh_service(self, param):
        try:
            result = self.translater.translate_to_zh(param)
            return get_server_response(result)
        except:
            return get_server_response()
