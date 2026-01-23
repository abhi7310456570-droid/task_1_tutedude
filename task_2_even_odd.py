num=float(input("enter the number you want to check"))
if num%2==0:
    print("that's even number",num)
else :
    print("that's odd number",num)


#...................
#......................
#number from 1 to 50 by using for loop
print("sum of intgers number from 1 to 50 by using for loop ")

total = 0

for i in range(1, 50):
    total += i

print("Sum from 1 to 50:", total)
