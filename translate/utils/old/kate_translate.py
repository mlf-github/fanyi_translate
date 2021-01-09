#!/usr/bin/python
# coding=utf-8
import requests
import json
from translate.utils.string_utils import contain_zh, contain_en


# 中英文混合，优先翻译成英文
def translate_auto(q):
    try:
        splits = q.split("\n")
        result = ""
        for s in splits:
            if s == "":
                continue
            url = "https://api.66mz8.com/api/translation.php?info=" + s
            rsp = requests.post(url=url)
            result += json.loads(rsp.text).get("fanyi").replace("\\", "") + "\n"
        # 临时的解决办法
        return result.strip().replace("https:/", "https://")
    except BaseException as e:
        import traceback
        print("翻译参数不合法1",traceback.format_exc())
        return None

def translate_to_en(q):
    if q == "":
        return ""
    try:
        if contain_zh(q):
            return translate_auto(q)
        else:
            return q
    except:
        print("翻译参数不合法")
        return None

def translate_to_zh(q):
    if q == "":
        return ""
    try:
        if contain_zh(q) and contain_en(q):
            return translate_auto(translate_auto(q))
        else:
            return translate_auto(q).replace(",", "，")
    except:
        print("翻译参数不合法")
        return None

if __name__ == "__main__":
    # pass
    # print translate("<script>alert(1)</script>")
    # if len(sys.argv) == 2:
    #     print translate_auto(sys.argv[1])
    # elif len(sys.argv) == 3:
    #     print translate_auto(sys.argv[1], sys.argv[2])
    # else:
    #     print "用法： 第一个参数为要翻译的字符串，第二个参数为目标语言，zh/en，可省略"

    # print translate_to_en("Oracle Berkeley DB DataStore组件安全漏洞")

    print(translate_auto("test"))
    print(translate_auto("测试"))
    print(translate_to_zh("test"))
    print(translate_to_en("测试"))
