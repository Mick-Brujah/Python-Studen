'''
手机：电池  屏幕  主板  摄像头   金属壳
# 手机：一个完整的项目
# 电池：功能---函数/方法
屏幕：

认识函数/方法/行为：在一个完整的项目中，某些功能可能会反复使用，那么将这个
功能封装成函数，当我们想要使用这个功能时，直接调用该函数即可。

本质：函数就是对功能模块的封装。
优点：1、简化代码结构，增加代码的复用度（重复使用程度）
      2、如果想修改某些功能或者调试某些功能，只需要修改或调试相应函数即可。
'''
'''
函数的定义：
格式：
def 函数名(参数列表):
    语句
    return 表达式
1、def：定义函数的关键字：函数的代码块是以def关键字开始的
2、函数名：当前函数的名称，命名规则遵循标识符命名规则。
3、()：参数列表的开始与结束
4、参数列表：格式：(参数1, 参数2,参数3,...参数n):任何传入函数的参数
用逗号隔开，参数必须在括号中，参数类似于变量名称。函数的参数从函数调用时
获取值。形参。
注：即使没有参数，小括号依旧不能省略
5、: 冒号：函数内容以冒号开始，并且开始四位缩进
6、语句：函数封装的功能模块
7、return：一般用于当前函数的结束，并将信息返回给函数的调用者
8、表达式：即将返回给函数的调用者的信息
注：函数最后的return 表达式 可以不写，默认返回None，相当于写了return None
注：函数仅仅定义时不会执行，如果函数只定义时，只能说明该函数有这个
功能，但是没有被使用。
'''
'''
函数的调用：
格式：
函数名(参数列表)
1、函数名：要调用的功能的函数名称
2、():参数列表的开始与结束
3、参数列表：函数调用者传给函数的信息，参数类似于常量。实参。
注：即使没有参数，小括号依旧不能省略

函数调用的本质：将实参传递给形参赋值的过程。
'''
'''
注意：在python中，函数只能先定义再调用。
'''

