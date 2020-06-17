def largest_factor(n):
    for i in range(1,n):
        if n%(n-i)==0:
            return n-i
