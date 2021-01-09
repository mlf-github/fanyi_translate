#!/usr/bin/python
# coding=utf-8
import execjs
# Python2: pip install pyexecjs
# Python3: pip install PyExecJS
import requests
import json
import sys
from translate.utils.string_utils import contain_zh

# Reference https://blog.csdn.net/yingshukun/article/details/53470424
def get_tk(q):
    ctx = execjs.compile("""function TL(a){var k="";var b=406644;var b1=3293161072;var jd=".";var $b="+-a^+6";var Zb="+-3^+b+-f";for(var e=[],f=0,g=0;g<a.length;g++){var m=a.charCodeAt(g);128>m?e[f++]=m:(2048>m?e[f++]=m>>6|192:(55296==(m&64512)&&g+1<a.length&&56320==(a.charCodeAt(g+1)&64512)?(m=65536+((m&1023)<<10)+(a.charCodeAt(++g)&1023),e[f++]=m>>18|240,e[f++]=m>>12&63|128):e[f++]=m>>12|224,e[f++]=m>>6&63|128),e[f++]=m&63|128)}a=b;for(f=0;f<e.length;f++){a+=e[f],a=RL(a,$b)}a=RL(a,Zb);a^=b1||0;0>a&&(a=(a&2147483647)+2147483648);a%=1000000;return a.toString()+jd+(a^b)}function RL(a,b){var t="a";var Yb="+";for(var c=0;c<b.length-2;c+=3){var d=b.charAt(c+2),d=d>=t?d.charCodeAt(0)-87:Number(d),d=b.charAt(c+1)==Yb?a>>>d:a<<d;a=b.charAt(c)==Yb?a+d&4294967295:a^d}return a};""")
    return ctx.call("TL", q)

def translate_to_en(q):
    try:
        splits = q.split("\n")
        result = ""
        for s in splits:
            if s == "":
                continue
            tk = get_tk(s)
            url = "https://translate.google.cn/translate_a/single?client=webapp&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=sos&dt=ss&dt=t&otf=2&ssel=0&tsel=0&xid=45662847&kc=1&tk=" + tk + "&q=" + s
            rsp = requests.post(url=url)
            result += json.loads(rsp.text)[0][0][0] + "\n"
        return result.strip()
    except:
        print("翻译参数不合法")
        return None

def translate_to_zh(q):
    try:
        splits = q.split("\n")
        result = ""
        for s in splits:
            if s == "":
                continue
            tk = get_tk(s)
            url = "https://translate.google.cn/translate_a/single?client=webapp&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=sos&dt=ss&dt=t&ssel=3&tsel=3&xid=45662847&kc=0&tk=" + tk + "&q=" + q
            rsp = requests.post(url=url)
            result += json.loads(rsp.text)[0][0][0] + "\n"
        return result.strip()
    except:
        print("翻译参数不合法")
        return None

def translate_auto(q):
    if contain_zh(q):
        return translate_to_en(q)
    else:
        return translate_to_zh(q)

if __name__ == "__main__":
    print(translate_auto("test"))
    print(translate_auto("测试"))
    print(translate_to_zh("test"))
    print(translate_to_en("测试"))
    # for i in range(1000):
    #     print translate_to_zh("ok" + str(i))
