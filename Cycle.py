cycle1 = int(input("Enter the speed of the first cyclist: "))
cycle2 = int(input("Enter the speed of the second cyclist: "))
cycle3 = int(input("Enter the speed of the third cyclist: "))
avg = (cycle1 + cycle2 + cycle3)/3
print("The average speed is",avg)
if cycle1<avg:
    print("The first cyclist is slower than the average!")
if cycle2<avg:
    print("The second cyclist is slower than the average!")
if cycle3<avg:
    print("The third cyclist is slower than the average!")
if cycle1>avg and cycle2>avg and cycle3>avg:
    print("All of these are doing amazing!")
elif cycle1==cycle2==cycle3==avg:
    print("All cyclists are going at the same speed!")
