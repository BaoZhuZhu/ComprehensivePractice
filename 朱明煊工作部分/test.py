import time
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "model.settings")
import django
django.setup()
from django.utils import timezone
import random
from comprehensivePractice.models import UserInfo
import datetime

A=36
B=37#小数的范围A ~ B
a=random.uniform(A,B)
C=2#随机数的精度round(数值，精度)
temp = round(a,C)
st = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
now = datetime.datetime.strptime(st, '%Y-%m-%d %H:%M:%S')
place = random.choice(["1","2","3"])
base_time = "2020/09/17/{hour}/{minute}/{second}/0"

#uid_all = [2020888000 + i for i in range(1000)]
temp_all = [round(36.0 + 1.5 * random.random(), 2) for _ in range(200)]
area_all = [random.randrange(1, 4) for _ in range(200)]
dtm_all = [base_time.format(hour=random.randrange(6, 21),
                            minute=random.randrange(0, 60),
                            second=random.randrange(0, 60)) for _ in range(200)
           ]


DATETIME_DICT_KEYS = ['year', 'month', 'day',
                      'hour', 'minute', 'second',
                      'microsecond']

def create_datetime(dts: str) -> timezone.datetime:
    dic = {DATETIME_DICT_KEYS[i]: int(e) for i, e in enumerate(dts.split('/'))}
    return timezone.datetime(**dic)
def create_fake_date():
    """write sqlite database by fake data"""
    for i in range(len(temp_all)):
        UserInfo(3018216304, '张开',
                 temp_all[i], create_datetime(dtm_all[i]),
                 area_all[i]).save()



if __name__ == "__main__":
   create_fake_date()