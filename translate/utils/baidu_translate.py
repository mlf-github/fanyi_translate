#!/usr/bin/python
# coding=utf-8
import hashlib
import random
import requests
import json
from string_utils import contain_zh
from string_utils import FullToHalf

class BaiduTranslate():

    keyindex = -1
    # 13207123727
    # 1095151731@qq.com
    # https://github.com/steven-ccq/BaiDu_trans_api/blob/master/BaiduTransAPI-forPython3.py
    # https://github.com/genji1031/languageTranslate/blob/master/translatePDFenglish.py
    appids = ["20200828000553883", "20200920000569601", "20200222000387204", "20191220000368093"]
    keys = ["_Dl2aqj9aTN2Q8UjK7OM", "LAvhErhi3gfQB3t_b3FH", "phr2Wy_0ZScBYzVb7eJl", "0NBx5qcmUsOMQT9O7hET"]

    # reference: https://blog.csdn.net/qq_878799579/article/details/74324869
    def genearteMD5(self, param=""):
        if param == "":
            param = str(random.randint(0, 999999999))
        hl = hashlib.md5()
        hl.update(param)
        return hl.hexdigest()

    def get_translate_from_baidu(self, q, to, _from="auto"):
        try:
            q = q.replace("\0", "")
            self.keyindex = (self.keyindex + 1) % len(self.appids)
            # print self.keyindex
            if q == "" or q.strip() == "":
                return q
            url = "https://fanyi-api.baidu.com/api/trans/vip/translate"
            salt = str(self.genearteMD5())
            # appid和密钥在这里查询
            # https://api.fanyi.baidu.com/api/trans/product/desktop?req=developer
            appid = self.appids[self.keyindex]
            key = self.keys[self.keyindex]
            sign = self.genearteMD5(appid + q + salt + key)
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            data = {
                "q": q,
                "from": _from,
                "to": to,
                "appid": appid,
                "salt": salt,
                "sign": sign
            }
            rsp = requests.post(url=url, data=data, headers=headers)
            versionInfoPython = json.loads(rsp.text)
            return versionInfoPython.get("trans_result")[0].get("dst") + "\n"
        except:
            print("翻译失败，重试")
            return self.get_translate_from_baidu(q, to, _from="auto")

    # _from: "zh" or "en"
    # to  : "zh" or "en"
    def translate(self, q, to, _from="auto"):
        splits = q.split("\n")
        result = ""
        for s in splits:
            result += self.get_translate_from_baidu(s, to) + "\n"
        return result.strip()


    def translate_to_en(self, q):
        # 全角替换为半角
        return FullToHalf(self.translate(q, "en", "zh"))

    def translate_to_zh(self, q):
        return self.translate(q, "zh", "en")

    def translate_auto(self, q):
        if contain_zh(q):
            return self.translate_to_en(q)
        else:
            return self.translate_to_zh(q)

if __name__ == "__main__":
    translater = BaiduTranslate()
    # for i in range(100):
    #     print translater.translate_auto("这是第" + str(i) + "次翻译")

    # print translater.get_translate_from_baidu("翻译", "en")

    print(translater.translate_to_en("""http://www.securityfocus.com/bid/118接:ftp://ftp.freebsd.org/pub/FreeBSD/CERT/advisories/FreeBSD-SA-00%3A17.libmytinfo.asc"""))

    # if len(sys.argv) == 2:
    #     print translate_auto(sys.argv[1])
    # elif len(sys.argv) == 3:
    #     print translate_auto(sys.argv[1], sys.argv[2])
    # else:
    #     print "用法： 第一个参数为要翻译的字符串，第二个参数为目标语言，zh/en，可省略"
    #
    # print translate("test", "zh")
    # print translate("测试", "en")
    # print translate_to_zh("test")
    # print translate_to_en("测试")
    # print translate_auto("test")
    # print translate_auto("测试")
    #
