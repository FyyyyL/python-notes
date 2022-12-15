"""
你要准备一个晚宴
你需要邀请你的好友来参加
现在 你需要 用 input函数 来输入好友的名称
并将其存储在 列表中
然后 通过 for循环 打印邀请信息


friend name:>>ztj
friend name:>>zjy
friend name:>>ztj
friend name:>>ztj

"""


a=[]
for i in range(4):
	a.append(input("friend name:>>"))
print(a)

for i in range(len(a)):
	print("邀请"+a[i])

