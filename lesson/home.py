# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-10-06 15:46:51
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-10-07 14:07:10

class Home:
    """docstring for Home"""
    def __init__(self, new_area, new_info, new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area
        self.item_content = []

    def __str__(self):
        msg = "房子的总面积是:%d，可用面积是:%d,户型是:%s,地址是:%s"%(self.area, self.left_area, self.info, self.addr)
        msg +="当前房子里的物品有:%s"%(str(self.item_content))
        return msg

    def add_item(self,item):
        self.left_area -= item.area
        self.item_content.append(item.name)

class Furniture:
    """docstring for Furniture"""
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return "%s占用的面积是%d"%(self.name, self.area)

fangzi = Home(129,"三室一厅","海淀区888号")
print(fangzi)

bed = Furniture("床",4)
print(bed)

sofa = Furniture("沙发",6)
print(sofa)

fangzi.add_item(bed)
fangzi.add_item(sofa)
print(fangzi)