#for 循环   break使用
# str =  '我的中国心, my love1'
# for i  in  str:
#     #遇到空格和o不打印,跳过
#     if i ==' ' or i == 'o':
#         continue
#     elif i == 'e':
#         break
#     else:
#         print(i)
# else:
#         print("我是最后的单独的")

#while  break else 配合使用
# i =0
# while i<3 :
#     if i == 1:
#         #第二遍, 需要对话
#         print('我真的错了, 单独的')
#     else:
#         print('我错了')
#     i += 1
# else:
#     print("我是单独的,打印输出下")

#案例
j = 0
while j<4:
    if j ==2:
        print('这次不真诚,跳过')
        #如果没有j+=1, 这句,  contunue 后面代码不执行  j会=2,  一直循环下去
        j+=1
        continue

    print(f'我的心好疼{j+1}次')
    j+=1
else:
    print('一切结束了')

