#第一个python语句
print('第一个python语句,HellO Python')

#输出: 1,格式化字符,  格式化输出
stu_id = 414
print('我的工号是MN%02u'%stu_id)

#组合使用
age = 30
sex = '男'
name = 'pence'
print('我的名字是%s,我的年龄是%u,我的工号是%u,我的性别是%s' % (name,age,stu_id,sex))
#格式化高级使用
myId = 4140
height = 174.35
print('我的学号是%03d,我的身高是%.3f' %(myId,height))
print(f'我的学号是{myId},我的身高是{height}')

#扩展   格式化字符串 s%特殊使用
print('我的姓名是%s,我的年龄是%s,我的工号是%s' %(name,sex,stu_id))

#格式化输出的高级模式 f{}
print(f'我的姓名是{name},我的年龄是{age}我的性别是{sex}')

