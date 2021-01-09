# 免费的翻译API

[https://api.wangshaogang.com/translate/?=自动识别](https://api.wangshaogang.com/translate/?=%E8%87%AA%E5%8A%A8%E8%AF%86%E5%88%AB)

[https://api.wangshaogang.com/translate/?=Automatic identification](https://api.wangshaogang.com/translate/?=Automatic%20identification)

[https://api.wangshaogang.com/translate/zh/?=Translate to Chinese](https://api.wangshaogang.com/translate/zh/?=Translate%20to%20Chinese)

[https://api.wangshaogang.com/translate/en/?=翻译成英文](https://api.wangshaogang.com/translate/en/?=%E7%BF%BB%E8%AF%91%E6%88%90%E8%8B%B1%E6%96%87)

# 直接调用Python调用API

此API支持GET和POST请求方式，传参有两种：
* RESTFUL API风格(<https://api.wangshaogang.com/test>)，参数在URL中，URL长度限制为65536字节
* 传统方式传参(<https://api.wangshaogang.com/?=test>)，GET请求URL长度限制为65536字节，POST请求参数长度不限(在settings.py中自定义)

推荐使用传统方式传参，POST请求

下面是用Python调用此API的示例：

```
vi test_translate.py
```

```python
#!/usr/bin/python
# coding=utf-8
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def translate(q):
    return request_api(q)

def translate_to_en(q):
    return request_api(q, "en/")

def translate_to_zh(q):
    return request_api(q, "zh/")

def request_api(q, to=""):
    rsp = requests.post(url="https://api.wangshaogang.com/translate/"+to, data={"": q})
    data = json.loads(rsp.text)
    if data.get("status") == 0:
        return data.get("result")
    else:
        raise RuntimeError("translateError")

if __name__ == "__main__":
    print translate("yes")
    print translate_to_zh("it")
    print translate_to_en("测试")

```

```
python test_translate.py
```

# Quick Start

> 请先安装`Python2`和`Django`

```
git clone git@github.com:Wesley1999/translate.git
```

在文件`translate/utils/baidu_translate.py`中，需要提供百度翻译的appid和key，可添加多个，一一对应即可


```
cd translate
python manager.py runserver 127.0.0.1:8000
```


浏览器访问
```
http://127.0.0.1:8000/自动识别
http://127.0.0.1:8000/Automatic identification
http://127.0.0.1:8000/zh/Translate to Chinese
http://127.0.0.1:8000/en/翻译成英文

http://127.0.0.1:8000/?=自动识别
http://127.0.0.1:8000/?=Automatic identification
http://127.0.0.1:8000/zh/?=Translate to Chinese
http://127.0.0.1:8000/en/?=翻译成英文
```

如需用公网IP访问，`settings.py`的`ALLOWED_HOSTS`中要添加服务器IP

# Nginx反向代理
如果不想暴露端口，可将服务运行在内网
```
python manager.py runserver 127.0.0.0:8000
```
然后用Nginx对其进行反向代理，参考如下配置：

```
server {
    listen                  443 ssl;
    charset                 utf-8;
    server_name             api.wangshaogang.com;
    location ~ ^/translate {
        rewrite ^.*translate/([\d\D]*)$       /$1 break;
        proxy_pass      http://localhost:8000;
    }
}
```
翻译的文本中可能包含换行符，`[\d\D]`可以匹配换行，而`.`不能
