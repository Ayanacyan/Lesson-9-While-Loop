n=int(input("Enter a number "))
temp=n
sum=0
while temp>0:
    temp=temp//10
    sum+=1
digit=sum
print("The number of digits in",n, "is", digit)

    