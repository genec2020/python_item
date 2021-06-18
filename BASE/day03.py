#while 循环
i =1
sum=0
while i<=100:
    sum+=i  #必须在上面,  先用再变, 不然结果错误
    i+=1
print(sum)

#1-100偶数求和,  比较2种方法时间
import time
j =0
sum1=0
while j<=100:
    sum1+=j
    j+=2
print(sum1)

#方法2
k= 0
sum2 = 0
while k<=100:
    if k%2==0:
        sum2+=k
    k+=1
print(sum2)
