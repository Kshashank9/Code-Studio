def printPascal(n:int):
    l=[]
    if n==1:
        l.append([1])
        return l
    elif n==2:
        l.append([1])
        l.append([1,1])
        return l
    else:
        l.append([1])
        l.append([1,1])
        for i in range(2,n):
            k=[]
            for j in range(len(l[i-1])+1):
                if j==0 or j==len(l[i-1]):
                    k.append(1)
                else:
                    k.append(l[i-1][j-1]+l[i-1][j])
            l.append(k)
    return l
