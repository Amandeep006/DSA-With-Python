def count(n):
    i=1
    while True:
        if (i==n+1):
            break
        yield i
        i=i+1

        

for i in count(9):
    print(i, end=" ")