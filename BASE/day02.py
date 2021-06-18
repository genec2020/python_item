#数据类型转换
# id= str(10)
# new_id = eval(id)
# print(type(new_id))

#多条件判断以及条件优化
# age = int(input('请输入你现在的年龄:'))
# if age<18:
#     print('未成年, 不能有女朋友')
# elif 18<= age<=60:
#     print('成年男性,可以有女朋友')
# else:
#     print('你的年龄太大了, 注意身体')

#上车座位
import random
# money = random.randint(0,3)
# sets=  random.randint(0,3)
# if money ==0:
#     print('没钱请下去')
# else:
#     if sets ==0:
#         print("没座位了,  站着吧")
#     else:
#         print('有座位, 你请坐')


#和电脑猜拳游戏
person = random.randint(0,2)
computer = random.randint(0,2)
#比较的结果
# if (person==0 and computer==1) or(person ==1  and computer==2) or (person==2 and computer==0):
#     print('人赢了')
# elif person== computer:
#     print('打平了')
# else:
#     print('电脑赢了')

#三元
num1 = 20
num2 = 30
c=num2-num1 if num2>num1 else num1 + num2
print(c)
