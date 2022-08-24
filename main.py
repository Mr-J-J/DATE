from datetime import date, datetime, time
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import json
import os
import random


class main:
    #   初始化
    #  参数：
    #   微信公众号appid
    #   微信公众号secret
    #   开始时间start_date
    #   城市city
    #   生日birthday
    #   用户id:user_id
    #  模板id:template_id
    def __init__(self, app_id, app_secret, start_date, city, birthday, user_id, template_id):
        self.today = datetime.now()
        self.start_date = start_date
        self.city = city
        self.birthday = birthday
        self.app_id = app_id
        self.app_secret = app_secret
        self.user_id = user_id
        self.template_id = template_id
        print(self.template_id, self.user_id ,self.app_id, self.app_secret)
        self.client = WeChatClient(self.app_id, self.app_secret)

        self.wm = WeChatMessage(self.client)
        self.wea, self.temperature, self.pm = self.get_weather()
        self.data = {"weather": {"value": self.wea, "color": self.get_random_color()},
                     "yan": {"value": self.get_yan(), "color": self.get_random_color()},
                     "date": {"value": self.get_date(), "color": self.get_random_color()},
                     "pm": {"value": self.pm, "color": self.get_random_color()},
                     "temperature": {"value": self.temperature, "color": self.get_random_color()},
                     "love_days": {"value": self.get_count(), "color": self.get_random_color()},
                     "birthday_left": {"value": self.get_birthday(), "color": self.get_random_color()},
                     "words": {"value": self.get_words()}}
        self.res = self.wm.send_template(self.user_id, self.template_id, self.data)
        print(self.res)

    def get_weather(self):
        url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + self.city
        res = requests.get(url).json()
        weather = res['data']['list'][0]
        return weather['weather'], math.floor(weather['temp']), math.floor(weather['pm25'])

    #   获取今天日期及星期
    def get_date(self):
        return self.today.strftime("%Y-%m-%d") + " " + self.today.strftime("%A")

    # 获取每日一言
    def get_yan(self):
        yan = requests.get("https://v.api.aa1.cn/api/yiyan/index.php").text
        return yan[3:len(yan) - 4]

    def get_count(self):
        print(self.start_date)
        delta = self.today - datetime.strptime(self.start_date, "%Y-%m-%d")
        return delta.days

    def get_birthday(self):
        print(self.birthday)
        next = datetime.strptime(str(date.today().year) + "-" + self.birthday, "%Y-%m-%d")
        if next < datetime.now():
            next = next.replace(year=next.year + 1)
        return (next - self.today).days

    def get_words(self):
        words = requests.get("https://api.shadiao.pro/chp")
        if words.status_code != 200:
            return self.get_words()
        return words.json()['data']['text']

    def get_random_color(self):
        return "#%06x" % random.randint(0, 0xFFFFFF)


if __name__ == '__main__':
    list = os.environ["LIST"]
    list = json.loads(list)
    for i in list:
        main(i['app_id'], i['app_secret'], i['start_date'], i['city'], i['birthday'], i['user_id'], i['template_id'])
        print("第" + str(list.index(i) + 1) + "个发送成功")
    print("完成")
