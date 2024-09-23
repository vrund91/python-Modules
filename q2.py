from module2 import details,percentage,result

name=input("Enter a name:")
eno=int(input("Enter enrollment no:"))

n=int(input("Enter no of subject:"))
total=0

for i in range(n):
    marks=int(input("Enter the marks:"))
    total += marks

details(name,eno)
percent=percentage(total,n)
print("The percentage is:",percent)
result(percent)