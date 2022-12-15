name=["cjy","zjy","pb"]
name[0]="dzj"
age=[18,19,18]
s1=name[0]+" is "+str(age[0])+" years old."
s2=name[1]+" is "+str(age[1])+" years old."
s3=name[2]+" is "+str(age[2])+" years old."
print(s1)
for i in name:
	print("Hello"+i)
names=["cjy","zjy","pb"]
names.append("dzj")
names.insert(1,"dzj")
print(names)
del names[3]
print(names)