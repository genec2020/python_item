#字符串  3种创建
str1 = '我的家'
str2 = "我的家"
str3 = '''我爱我的家,to english
                i love  my home'''
print(type(str3))
print(str3)

#切片   默认步长为1
new_str3 = str3[2:5:1]
print(new_str3)

#步长2是什么? 控制截取顺序
new_str4 = str3[1:4:2]
print(new_str4+"===")

new_str5 = str3[1:4:-2] #无法获取数据
print(new_str5+"-2")

new_str6 = str3[-1:-4:-2]
print(new_str6+"-22")

#find   index  字符第一次出现位置下标
str = "hello world and  home and wonder"
num  =  str.find('and')
print(num)

#查找最后一次出现的字串, 返回位置值
num  =  str.rfind('and')
print(num)


