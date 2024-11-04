list = [3, 2, 1, 4, 5]
print(list)
def bubble_sort(n):
    step = 0
    
    for j in range(0, len(n)-1):
        for i in range(0, len(n)-1):
            if n[i] > n[i+1]:

                n[i], n[i+1] = n[i+1], n[i]
                step += 1
        print(step)
        print(n)

bubble_sort(list)