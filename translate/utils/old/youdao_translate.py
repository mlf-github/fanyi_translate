#!/usr/bin/python
# coding=utf-8

import requests
import json
import sys


from translate.utils.string_utils import contain_zh
from translate.utils.string_utils import contain_en


# Reference: https://zhuanlan.zhihu.com/p/111346459
# 优先翻译成英文
def translate_auto(word):
        result = ""
        splits = word.split("\n")
        for s in splits:
            if s == "":
                continue
            url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
            # 传输的参数，其中 i 为需要翻译的内容
            key = {
                'type': "AUTO",
                'i': s,
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "ue": "UTF-8",
                "action": "FY_BY_CLICKBUTTON",
                "typoResult": "true"
            }
            # key 这个字典为发送给有道词典服务器的内容
            response = requests.post(url, data=key)
            # 判断服务器是否相应成功
            print(response.text)
            if response.status_code == 200:
                # 然后相应的结果
                result += json.loads(response.text)['translateResult'][0][0][
                              'tgt'] + "\n"
            else:
                print("有道词典调用失败")
                # 相应失败就返回空
                return None
        return result.strip()



def translate_to_en(q):
    try:
        if not contain_zh(q):
            return q
        else:
            return translate_auto(q)
    except:
        print("翻译参数不合法")
        return None


def translate_to_zh(q):
    try:
        if contain_zh(q) and contain_en(q):
            return translate_auto(translate_auto(q))
        else:
            return translate_auto(q)
    except:
        print("翻译参数不合法")
        return None


if __name__ == "__main__":
    # 调用
    for i in range(1000):
        print(translate_auto("我是Chinese"))
        # print get_main("这是第" + str(i) + "次翻译")

    # 结果《The 21st century》
