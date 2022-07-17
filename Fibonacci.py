n=9
#n=int(input('Enter a number:'))
n0=1
n1=1
count=0
nth=0

while n>count:
    print(n0,end=' ')
    nth=n0+n1
    count+=1
    n0=n1
    n1=nth