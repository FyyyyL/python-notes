dinner=["曹佳怡","段子杰","张嘉阳","庞博","赵泰基"]
for i in dinner:
	s="邀请"+i+"参加我的晚宴。"
	print(s)

print(dinner[1]+"来不了了")
del dinner[1]

dinner.append("吴柯妤")
for i in dinner:
	print("邀请"+i+"参加我的晚宴。")

for i in dinner[:3]:
	print("im so sorry for cancelling the dinner"+i)

#sdfdsfsfdsjlkfdsjflksjlkj fjeklksjfkndskj
for i in range(3):
	del dinner[0]
	print(dinner)
#wertyuiopasdfghjklzxcvbnm
