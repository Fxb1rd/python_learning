# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-10-07 13:51:27
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-10-07 14:49:11

class CarStore(object):
    """docstring for CarStore"""
    def __init__(self):
        self.factory = Factory()

    def order(self,car_type):
        return self.factory.select_car_by_type(car_type)

class Factory(object):
    """docstring for Factory"""
    def select_car_by_type(self,car_type):
        if car_type=="索纳塔":
            return Suonata()
        elif car_type=="桑塔纳":
            return Sangtana()

class Car(object):
    """docstring for Car"""
    def move(self):
        print("车在移动")
    def music(self):
        print("播放音乐")
    def stop(self):
        print("汽车停止")

class Sangtana(Car):
    """docstring for Sangtana"""
    def __init__(self):
        print("购买了桑塔纳")

class Suonata(Car):
    """docstring for Suonata"""
    def __init__(self):
        print("购买了索纳塔")




car_store = CarStore()
car = car_store.order("桑塔纳")
car.move()
car.music()
car.stop()