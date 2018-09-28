# coding=utf-8

import urllib
import urllib2
import cookielib

def login():
    post_url = "http://www.renren.com/PLogin.do"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    form_dict = {
                "email": "mr_mao_hacker@163.com",
                "password": "ALARMCHIME"
            }
    form_data = urllib.urlencode(form_dict)
    request = urllib2.Request(post_url, data=form_data, headers=headers)
    cookie_jar = cookielib.CookieJar()
    cookie_hander = urllib2.HTTPCookieProcessor(cookie_jar)
    opener = urllib2.build_opener(cookie_hander)
    opener.open(request)
    url_list = [
            "http://www.renren.com/327550029/profile",
            "http://www.renren.com/410043129/profile",
            "http://www.renren.com/403811175/profile"
            ]
    for index, url in enumerate(url_list):
        request = urllib2.Request(url, headers=headers)
        response = opener.open(request)
        with open(str(index) + ".html", "w") as f:
            f.write(response.read())



if __name__ == "__main__":
    login()
