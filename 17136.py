input_arr = [list(map(int,input().split())) for _ in range(10)]
cnt = 0
min_paper = 25
test = [[0] * 10 for i in range(10)]
while(1):
    paper = [0, 0, 0, 0, 0]
    size = [1, 4, 9, 16, 25]
    for i in range(10):
        test[i] = input_arr[i]
    for i in range(10):
        for j in range(10):
            
