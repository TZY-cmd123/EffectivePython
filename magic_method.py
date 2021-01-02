#魔术方法
class Student(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def __add__(self, other):
        new_name=self.name+other.name
        new_id=self.id+other.id
        return Student(new_name,new_id)

    def __str__(self):
        return self.name+str(self.id)

    def __getitem__(self, item): # 类似与数组
        return self.id


s1=Student('小明',1)
s2=Student('小红',2)
s3=s1+s2 #一开始是不能相加的,必须要求重写魔术方法__add__()
print(s3[0])

