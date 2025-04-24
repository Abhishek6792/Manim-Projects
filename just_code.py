def subset(L):
    Y=[]
    for i in range(0,len(L)-2):
        l=[]
        l.append(L[i])
        for j in range(i+1,len(L)-1):
            l.append(L[j])
            for k in range(j+1,len(L)):
                if j==len(L)-1:
                    l.append(L[k])
                    Y.append(l)
                    l.pop().pop()
                if k==len(L):
                    l.append(L[k])
                    Y.append(l)
                    l.pop()
                else:
                    l.append(L[k])
                    Y.append(l)
                    l.pop()

    return(print(Y))

subset([1,2,3,4,5,6,7])
