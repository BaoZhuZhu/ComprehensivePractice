import os
from math import ceil

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "model.settings")
import django
django.setup()
from django.utils import timezone
import random
from comprehensivePractice.models import UserInfo
import datetime
base_time = "2020/09/11/{hour}/{minute}/{second}/0"

uid_all = [2020888000 + i for i in range(1000)]
temp_all = [round(36.0 + 2 * random.random(), 2) for _ in range(1000)]
area_all = [random.randrange(1, 4) for _ in range(1000)]
dtm_all = [base_time.format(hour=random.randrange(6, 21),
                            minute=random.randrange(0, 60),
                            second=random.randrange(0, 60)) for _ in range(1000)
           ]

DATETIME_DICT_KEYS = ['year', 'month', 'day',
                      'hour', 'minute', 'second',
                      'microsecond']


def create_datetime(dts: str) -> timezone.datetime:
    dic = {DATETIME_DICT_KEYS[i]: int(e) for i, e in enumerate(dts.split('/'))}
    return timezone.datetime(**dic)

def create_fake_date():
    """write sqlite database by fake data"""
    for i in range(len(uid_all)):
        UserInfo(uid_all[i], str(uid_all[i]),
                 temp_all[i], create_datetime(dtm_all[i]),
                 area_all[i]).save()

def query_data_by_hour_and_area(start_hour, end_hour, area_index):
    data = UserInfo.objects.all()

    area_fliter_result = []
    for i in data:
        if int(i.measuredPlace) == area_index:
            area_fliter_result.append(i)

    hour_fliter_result = []
    for i in area_fliter_result:
        if start_hour <= i.measuredDatetime.hour <= end_hour:
            hour_fliter_result.append(i)
    return hour_fliter_result

def query_data_by_userID(userID):
    data = UserInfo.objects.all()
    names = []
    for i in data:
        if i.userId == userID:
            names.append(i)
    return names[0]

def query_name_by_userID(userID):
    data = UserInfo.objects.all()
    id_fliter_result = []
    for i in data:
        if i.userId == userID:
            id_fliter_result.append(i)
    return id_fliter_result

class UserDataAnalysis(object):
    def __init__(self,userID):
        self.data = query_data_by_userID(userID)
        self.name = query_name_by_userID(userID)
        temp_all = []
        for i in self.data:
            temp_all.append(i.userTemperature)
        sorted(self.data,key=lambda temp_all:self.date[2],reverse=True)
        self.place = []
        self.temp = []
        self.time = []
        if len(self.data)>7:
            for i in self.data[0:7]:
                self.temp.append(i.userTemperature)
                self.place.append(i.measuredPlace)
                self.time.append(datetime.datetime.strftime(i.measuredDatetime,'%Y-%m-%d %H:%M:%S'))
        else:
            for i in temp_all:
                self.temp.append(i.userTemperature)
                self.place.append(i.measuredPlace)
                self.time.append(datetime.datetime.strftime(i.measuredDatetime,'%Y-%m-%d %H:%M:%S'))
        average = sum(temp_all) / len(temp_all)
        maxx = max(temp_all)
        minn = min(temp_all)
        self.__average_temperature = average
        self.__max_temperature = maxx
        self.__min_temperature = minn
        self.info = []
        for i in len(self.place):
            str = '体温: ' + str(self.temp[i]) + ' ' + '测温地点： ' + str(self.place[i]) + ' ' + '测温时间 ' + self.time[i]
            self.info.append(str)
    @property
    def average_temperature(self):
        return self.__average_temperature

    @property
    def max_temperature(self):
        return self.__max_temperature

    @property
    def min_temperature(self):
        return self.__min_temperature

    @property
    def user_info(self):
        return self.info

class DataAnalysis(object):

    def __init__(self, start_hour, end_hour, area_index):
        self.data = query_data_by_hour_and_area(start_hour,
                                                end_hour,
                                                area_index)

        temp_all = []
        uid_all = []
        for i in self.data:
            temp_all.append(i.userTemperature)
            if i.userId not in uid_all:
                uid_all.append(i.userId)

        average = sum(temp_all) / len(temp_all)
        count = len(uid_all)
        self.__average_temperature = average
        self.__people_count = count

    @property
    def average_temperature(self):
        return self.__average_temperature

    @property
    def people_count(self):
        return self.__people_count

    @property
    def area_risk_level(self):
        return 0 if self.__average_temperature < 37.2 else 1

    def get_people_count_by_temperature_range(self, l, h, step):
        categories = [0 for _ in range(ceil((h - l) / step) + 2)]
        for i in self.data:
            category = ceil((i.userTemperature - l) / step)
            if category < 0:
                category = 0
            elif category >= len(categories):
                category = len(categories) - 1
            categories[category] += 1

        return categories



if __name__ == "__main__":
    res = query_data_by_hour_and_area(6, 11, 1)
