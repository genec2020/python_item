#打印正方形
i=0
while i<5:
    j=0  #每次打印5个后,j初始化值
    while j<5:
        if j==4:
            print('*')
        else:
            print('*',end='')
        j+=1
    i+=1

#循环嵌套打印三角形    简单三角形, *个数=行数
i=1
while i<6:
    j=1
    while j<=i:
        if j==i:
            print('*')
        else:
            print('*',end='')
        j+=1
    i+=1

#循环嵌套打印99乘法表  和直角三角形类似
i=1
while i<10:
    j=1
    while j<=i:
        if j==i:
            #print(f'{j}*{i}={i*j}')
            print(j+"*"+i+"="+)
        else:
            print(f'{j}*{i}={i*j}',end='\t')
        j+=1
    i+=1

#等腰三角形
print('===========')
i=1  #行数
while i<10:
    if i%2!=0:  #奇数
        #打印   kong
        kong = int((9-i)/2)
        print(' '*kong+'*'*i+" "*kong)
    i+=1

