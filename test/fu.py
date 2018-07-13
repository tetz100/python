## _*_ coding:UTF-8 _*_
#运行命令cmd /k C:/python3.6.6/python.exe "D:\pyFiles\fu.py" & ECHO. & PAUSE & EXIT

class fu:
  #属性，全局变量
  name = "父类"
  age = 44
  __info = "这是类的私有属性"
  
  #构造方法，产生对象时调用，用于初始化 ，跟java不一样，不支持重载，只能定义一个
  def __init__(self,args1,args2,args3):
    print ("进入构造方法")
    self.name = args1
    self.age = args2
    self.__info = args3
    
  #析构方法，在对象被释放时调用，支持重载，不需要显示调用
  def __del__(self):
    print ("对象被释放")

  #在Python中实例方法的定义至少有一个参数，一般以名为'self'的变量作为该参数（用其他名称也可以），而且需要作为第一个参数，self可以理解为java中的this。
  def printClass(self):
    return "进入普通方法",self.name," + ",self.age
  
  #类方法，用classmethod来进行修饰，第一个参数通常使用cls代替self
  @classmethod
  def printSelf(cls):
    return "进入类方法",cls.name," + ",cls.age
  
  #这是类的私有方法   
  def __printInfo(self):
    return self.__info

#实例化对象
f = fu("thename","theage","theinfo")
print (f.printClass())
print (f.printSelf)

#print(f.__info) #报错，私有属性和方法访问不到
f.age = 12 #给对象f的age赋值