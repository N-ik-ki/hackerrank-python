n=int(input())
lst=[]
for i in range(n):
    lst.append(input())
c=set(lst)
print(sum(1 for i in c))
