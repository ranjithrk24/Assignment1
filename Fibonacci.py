n0=0
n1=1
count=0
nth=0

while n0<50:
    print(n0,end=' ')
    nth=n0+n1
    count+=1
    n0=n1
    n1=nth
