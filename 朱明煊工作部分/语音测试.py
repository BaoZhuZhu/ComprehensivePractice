# coding=utf-8

import pyttsx3
temp = float(input("请输入被测者体温: "))
suggestion1 = '  您的体温正常，最近天气变化大，注意早晚添衣'
suggestion2 = '  您的体温属过高，请再次接受测量，如果仍高温，请到指定医院就诊，就诊过程中注意带好口罩'
suggestion3 = '  您体温过低，建议去医院查看，是否身体过于虚弱，或者有中毒状况'
suggestion4 = '  您的体温不在人类标准体温范围，请重新测试'
text='您的体温是  '
ans = ''
alarm = '体温过高滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴滴'
if(temp<35.5):
    if(temp<33):
        ans = suggestion4
    else:
        ans = text + str(temp) + '度 ' + suggestion3
elif(temp>37.2):
    if (temp > 42):
        ans = suggestion4
    else:
        ans = text + str(temp) + '度 ' + suggestion2 + alarm
else:
    ans = text + str(temp) + '度 ' + suggestion1
    
voice=pyttsx3.init()
voice.say(ans)
voice.runAndWait()