
def minMax(l):
    l.sort(reverse=True)

    max=l[0]
    print('Max value is: ' + str(max))

    min=l[int(len(l))-1]
    print('Min value is: '+ str(min))

    diff = max-min
    print('Difference is :' + str(diff))



minMax([1,2,3,9, -1, 11])