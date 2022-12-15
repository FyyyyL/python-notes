year=2000
end_year=2022
years=[]
for i in range(year,end_year+1,4):
	year+=4
	years.append(year)
print(years)

for i in range((end_year-year)//4):
	year+=4
	years.append(year)
print(years)

