list = [3, 2, 1, 4, 5]
print(list)
def bubble_sort(l):
    step = 0
    
    for a in range(0, len(l)-1):
        for b in range(0, len(l)-1):
            if l[b] > l[b+1]:

                l[b], l[b+1] = l[b+1], l[b]
                step += 1
        print(step)
        print(l)

bubble_sort(list)