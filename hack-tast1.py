n=input("Enter any number")
n=int(n)

i=1
num=0
while i<=n:
	
	temp=i
	while temp>0:
		r=temp%10
		num=num*10+r
		temp=temp//10
	i=i+1
		

print(num)	
