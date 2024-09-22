# 09.1.py
# class


class Dog:
    """Dog class"""

    # __init__ 实例初始化时调用
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = 0  # 默认值

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


# 创建实例
my_dog = Dog("bb", 2)
# 访问属性
print(my_dog.name)
# 调用方法
my_dog.sit()
my_dog.roll_over()
