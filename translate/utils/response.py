# coding=utf-8
import collections
import json
from django.http import HttpResponse
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_server_response(result=None, status=0, msg='ok'):
    data = collections.OrderedDict()
    data["status"] = status
    if status != 0:
        data["msg"] = msg
    if result is not None:
        data["result"] = result
    if result is None and status == 0:
        data["status"] = 901
        data["msg"] = "Empty result."
    return HttpResponse(json.dumps(data), content_type="application/json, charset=utf-8")