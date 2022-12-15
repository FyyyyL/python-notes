user_input=input("please type your name>>")
namelist=["pb","zjy","dzj","cjy"]
status=False
for i in range(len(namelist)):
	if namelist[i]==user_input:
		status=True
if status:
	print("Welcome back")
else:
	print("byebye!")