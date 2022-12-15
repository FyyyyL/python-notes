# numbers = [2, 5, 8, 9]
# number=0
# for i in range(len(numbers)):
# 	number+=numbers[i]
# number/=len(numbers)
# print(number)




# names=[]
# for i in range(5):
# 	b=input("please type your name>>")
# 	names.append(b)
# print(names)

# F=[1,1]
# for i in range(1,49):
# 	numbers=F[i-1]+F[i]
# 	F.append(numbers)
# print(F)
# print(len(F))

# #list int 
# [1,2,3] 3
# [3,6,9]


# def mul(flist,fint):
# 	for i in range(len(flist)):
# 		flist[i]*=fint
# 	print(flist)
# 	return flist
# flist=[1,2,3]
# fint=3
# mul(flist,fint)


# def flen(list1):
# 	cont=0
# 	for _ in list1:
# 		cont+=1
# 	return cont


# list1 = [1,2,3,4,5]
# for i in range(len(list1)):
# 	print(list1[i])

def two_sum(list1,target):
	result = []
	#---------------------------------------
	for i in range(0,len(list1)):
		for j in range (0,len(list1)):
			targets=list1[i]+list1[j]
			if targets==target:
				result.append(list1[i])
				result.append(list1[j])
				print(result)
	#---------------------------------------
	return result


#test
list1 = [1,2,3,4,5]
target = 7
rs = two_sum(list1,target)
print("[TEST] {}+{}={}".format(rs[0],rs[1],target))
if (rs[0] + rs[1]) == target:
	print("[TEST] you pass")
else:
	print("[TEST] still have some problem")

#双层 for 循环， 开始和结束位置
#if 语句
# 列表的添加 函数

# two sum 题目 是leedcode？？？的一个 面试题目
# 我需要付总写一个 函数，函数有两个传入参数
# 第一个是一个 列表，第二个是一个 int 数字

# 我将会给 付总 提供这两个传入值

# 付总需要在函数内部 解决以下问题

# 例如： 
# 	list1 = [1,2,3,4,5] 这个列表为第一个传入参数
# 	target = 5 这个是 第二个是一个 int 数字

# 函数需要返回一个列表 包含两个int 类型的元素
	
# 	result:[1,4] or [2,3]

# 因为 list1 中 需要将两个元素相加，然后得出 result

