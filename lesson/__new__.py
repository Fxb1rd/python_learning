# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-10-08 16:16:45
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-10-08 16:34:18

class Dog(object):
    __instance = None
    #__name = False
    def __new__(cls,name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            #return返回上一次创建的对象的引用
            return cls.__instance

    def __init__(self,name):
        #if Dog.__name == False:
            self.name = name
            #Dog.__name = True


a = Dog("旺财")
print(id(a))
print(a.name)
b = Dog("拉西")
print(id(b))
print(b.name)