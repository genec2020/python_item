#for 循环   break使用
str =  '我的中国心, my love'
for i  in  str:
    #遇到空格和o不打印,跳过
    if i ==' 'or i == 'o':
        continue
    elif i == 'e':
        break
    else:
        print(i)

#while  break else 配合使用

