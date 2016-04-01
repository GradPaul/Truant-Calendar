import requests
from copy import deepcopy
from flask import abort, session, request
from flask import current_app as app
import json, re
from functools import wraps
import random, string, json, hashlib, time


base_headers = {
    "Content-Type": "application/json",
}


def merge(a, b):
    res = {}
    for k in a:
        res[k] = a[k]
    for k in b:
        res[k] = b[k]
    return res


class api(object):
    def __init__(self, path, method='GET', params=None, data=None, headers={}, server='core', format="list",
                 collection=None, version="v1"):
        headers = {}
        if "token" in session:
            headers["Authorization"] = "Bearer " + session["token"]
        self.c = collection
        self.f = format

        version = "_" + version if version == 'v2' else ''

        api_url = app.config["BASE_" + server.upper() + version.upper()] % path
        r = requests.request(
            method,
            api_url,
            params=params,
            data=json.dumps(data),
            headers=merge(base_headers, headers)
        )
        if r.content and r.json():
            self.res = r.json()
        else:
            print(r.status_code, r.content)
            abort(500)


    def get(self, path):
        if not (self.res and path):
            return None
        if isinstance(path, str) and isinstance(self.res, dict) and path in self.res:
            return self.res[path]
        res = deepcopy(self.res)
        for k in path:
            if (isinstance(k, int) and isinstance(res, list) and k < len(res)) \
                    or (isinstance(k, str) and isinstance(res, dict) and k in res):
                res = res[k]
            else:
                return None
        return res


    def form(self):
        if self.f == "raw":
            return {
                "data": self.res,
                "total": 1
            }
        if not self.c:
            return None
        if self.f == "list":
            res = self.get(["data", self.c])
        elif self.f == "first":
            res = self.get(["data", self.c, 0])
        else:
            res = self.get("data")
        return {
            "data": res,
            "total": self.get(["data", "total"])
        }

    def raw(self):
        return self.res


def hideSensitiveInfos(r):
    if "data" in r:
        users = r["data"]["users"]
        for user in users:
            del user["tokens"]
            del user["password"]
    else:
        del r["tokens"]
        del r["password"]
    return r


def getUserAgent(req):
    userAgent = req.headers['User-Agent'].lower()

    if re.search(r'spider', userAgent):
        return 'spider'
    elif re.search(r'micromessenger', userAgent):
        return 'wechat'
    elif re.search(r'ipad|iphone', userAgent):
        return 'apple'
    elif re.search(r'android', userAgent):
        return 'android'
    elif re.search(r'msie ([0-9.]+)', userAgent):
        ieVersion = float(re.search(r'msie ([0-9.]+)', userAgent).group(1))
        if ieVersion < 10:
            return 'notCompatible'
        else:
            return 'pc'
    else:
        return 'pc'


def compatibilityCheck(handler):
    @wraps(handler)
    def decorated_function(*args, **kwargs):
        userAgent = getUserAgent(request)
        if userAgent == "notCompatible":
            return render_template("notCompatible.html")
        else:
            return handler(*args, **kwargs)

    return decorated_function


def getTemplateByUserAgent():
    userAgent = getUserAgent(request)
    if userAgent == "apple" or userAgent == "android" or userAgent == "wechat":
        return "mobile.html"
    elif userAgent == "pc":
        return "index.html"
    else:
        return "notCompatible.html"


def refresh_access_token():
    # Get SB wechat SB access_toekn
    r = requests.get("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (app.config["PUB_APPID"], app.config["PUB_APPSECRET"]))
    data = json.loads(r.text)
    app.config["ACCESS_TOKEN_EXPIRE"] = time.time()+7100

    # Exchange SB access_token and jsapi_ticket
    r = requests.get("https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=%s&type=jsapi" % data["access_token"])
    data = json.loads(r.text)
    app.config["JSAPI_TICKET"] = data["ticket"]


def calc_signature(noncestr, timestamp, url):
    SBWeChat = {}
    SBWeChat["noncestr"] = noncestr
    SBWeChat["timestamp"] = timestamp
    SBWeChat["url"] = url
    SBWeChat["appId"] = app.config["PUB_APPID"]
    SBWeChat["signature"] = hashlib.sha1(("jsapi_ticket=%s&noncestr=%s&timestamp=%s&url=%s" % (app.config["JSAPI_TICKET"], noncestr, timestamp, url)).encode("utf-8")).hexdigest()
    return SBWeChat


def random_string():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
