for _ in range(int(input())):
    s=0
    for x in input():s+=1 if x== '(' else (-1 if s else 50)
    print("NO" if s else "YES")
        

for r in[*open(0)][1:]:
	for _ in range(25):
		r=r.replace('()','')
	print('YNEOS'[r>'!'::2])
