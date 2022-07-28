
n = int(input())

mat = [[] for i in range(n)]
for i in range(n):
    mat[i]= list(map(int,input().split()))

for i in range(1, n-1):
    A, B, C = n-i-2, n-i-1, i
    Blist = [0 for j in range(i + 1)]
    for j in range((B+1)**(i-1) *B + 1):
        save = []
        while(j > B):
            j, temp = divmod(j, n-i)
            save.insert(0, temp)
        save.insert(0, j)
        if sum(list(map(int,list(save)))) == B:
            temp2 = len(save)
            for k in range(i-temp2+1):
                save.insert(0, 0)
            #print(save)
            Blist = save[:]
            nonB = []
            lenA = 0
            for k in range(len(Blist)):
                if Blist[k] ==0:
                    nonB.append(k)
                    lenA += 1
            
            for k in range((A+1)**(lenA-1) * A+1):
                Alist = [0 for j in range(i + 1)]
                save = ''
                #print(k ,A)
                while(k > A):
                    k, temp = divmod(k, A+1)
                    save = str(temp) + save
                save =  str(k) + save
                if sum(list(map(int,list(save)))) == A:
                    for m in range(len(save)):
                        Alist[nonB[len(nonB)-1-m]] = int(save[len(save)-1-m])
                    print(Alist, Blist)
                    
