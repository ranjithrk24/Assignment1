s='Edyoda'
print(s[::-1])

a=''
for i in s:
    a=i+a
print(a)

a=[]
for i in s:
    a.append(i)
a.reverse()
for i in a:
    print(i,end='')
print('')
for o in reversed(s):
    print(o,end='')


    


