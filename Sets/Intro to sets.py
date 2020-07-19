def average(array):
    sum=0
    s=set(array)
    for x in s:
        sum+=x
    avg=sum/len(s)
    return avg
