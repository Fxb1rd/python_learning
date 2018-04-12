# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-10-06 15:12:36
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-10-06 15:59:53

class SweetPotato:
    """docstring for SweetPotato"""
    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0
        self.condiments = []

    def __str__(self):
        return "地瓜 状态:%s(%d),添加的作料有:%s"%(self.cookedString,self.cookedLevel,str(self.condiments))

    def cook(self,cooked_time):
        self.cookedLevel += cooked_time

        if self.cookedLevel >= 0 and self.cookedLevel < 3:
            self.cookedString = "生的"
        elif self.cookedLevel >= 3 and self.cookedLevel < 5:
            self.cookedString = "半生不熟"
        elif self.cookedLevel >= 5 and self.cookedLevel < 8:
            self.cookedString = "熟了"
        elif self.cookedLevel >= 8:
            self.cookedString = "糊了"

    def addCondiments(self,item):
        self.condiments.append(item)




di_gua = SweetPotato()
print(di_gua)

di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("孜然")
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("盐")
print(di_gua)
di_gua.cook(1)
di_gua.addCondiments("辣椒")
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)


