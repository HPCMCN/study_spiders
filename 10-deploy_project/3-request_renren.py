# coding=utf-8

import requests


def login():
    post_url = "http://www.renren.com/PLogin.do"
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
    form_dict = {
                "email": "mr_mao_hacker@163.com",
                "password": "ALARMCHIME"
            }
    s = requests.session()
    s.post(post_url, headers=headers, data=form_dict)
    url_list = [
            "http://www.renren.com/327550029/profile",
            "http://www.renren.com/410043129/profile",
            "http://www.renren.com/403811175/profile"
            ]
    for index, url in enumerate(url_list):
        response = s.get(url, headers=headers)
        with open(str(index) + ".html", "w") as f:
            f.write(response.text)



if __name__ == "__main__":
    login()
