from datetime import datetime, timedelta

now = datetime.now()
fmt = now.strftime("%Y年 %m月 %d日 %H時%M分%S秒")
print(fmt)

yester = datetime(2022,3,6)
print(yester)
feb = yester - timedelta(days=12)
print(feb)

delta = now - yester
print("開始日から" + str(delta.days +1) + "日です")
sec = delta.seconds
print(sec)