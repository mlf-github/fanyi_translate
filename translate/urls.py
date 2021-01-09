# coding=utf-8
from django.conf.urls import url

from .controller import translate_controller

# [\d\D] 可以匹配换行，而 . 不能
urlpatterns = [
    url(r'^en/([\d\D]*)$', translate_controller.translate_to_en_controller),
    url(r'^zh/([\d\D]*)$', translate_controller.translate_to_zh_controller),
    url(r'^(?!favicon.ico)([\d\D]*)$', translate_controller.translate_auto_controller),
]