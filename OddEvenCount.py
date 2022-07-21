start_number=int(input())
end_number=int(input())
odd=0
even=0
for i in range(start_number,end_number+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print('Number of even numbers:',even)
print('Number of odd numbers:',odd)
