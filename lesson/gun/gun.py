# -*- coding: utf-8 -*-
# @Author: fxb1rd
# @Date:   2017-10-08 19:19:40
# @Last Modified by:   fxb1rd
# @Last Modified time: 2017-10-08 20:37:40
class Person(object):
    """docstring for Person"""
    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name
        self.gun = None
        self.hp = 100

    def __str__(self):
        if self.gun:
            return "%s的血量为:%d,他有枪,%s"%(self.name,self.hp,self.gun)
        else:
            if self.hp > 0:
                return "%s的血量为:%d,他没枪"%(self.name,self.hp)
            else:
                return "%s已挂"%self.name

    def anzhuang_zidan(self,dan_jia_temp,zi_dan_temp):
        '''安装子弹'''
        dan_jia_temp.baocui_zidan(zi_dan_temp)

    def anzhuang_danjia(self,gun_temp,dan_jia_temp):
        '''安装弹夹'''
        gun_temp.baocui_danjia(dan_jia_temp)

    def naqiang(self,gun_temp):
        '''拿枪'''
        self.gun = gun_temp

    def kaiqiang(self,diren):
        '''开枪'''
        self.gun.fire(diren)

    def diao_xue(self,damage):
        self.hp -= damage

class Gun(object):
    """docstring for Gun"""
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name#记录枪的类型
        self.danjia = None

    def __str__(self):
        if self.danjia:
            return "枪的信息为%s,%s"%(self.name,self.danjia)
        else:
            return "枪的信息为%s,这把枪中没弹夹"%(self.name)

    def baocui_danjia(self,dan_jia_temp):
        '''枪保存子弹'''
        self.danjia = dan_jia_temp

    def fire(self,diren):
        '''开火'''
        zidan_temp = self.danjia.push()

        #伤害敌人
        if zidan_temp:
            zidan_temp.jizhong(diren)
        else:
            print("没有子弹了")

class Danjia(object):
    """docstring for Danjia"""
    def __init__(self, max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num#弹夹的容量
        self.zi_dan_list = []

    def __str__(self):
        return "弹夹的信息为%d/%d"%(len(self.zi_dan_list),self.max_num)

    def baocui_zidan(self,zi_dan_temp):
        '''弹夹保存子弹'''
        self.zi_dan_list.append(zi_dan_temp)

    def push(self):
        '''弹出最上面的子弹'''
        if self.zi_dan_list:
            return  self.zi_dan_list.pop()
        else:
            return None

class Zidan(object):
    """docstring for Zidan"""
    def __init__(self, damage):
        super(Zidan, self).__init__()
        self.damage = damage#伤害

    def jizhong(self,diren):
        '''伤害敌人'''
        diren.diao_xue(self.damage)

#############################################################
def main():
    '''控制程序流程'''
#############################################################
    #1.老王
    laowang = Person("老王")

    #2.枪
    ak47 = Gun("AK47")

    #3.弹夹
    dan_jia = Danjia(20)

    #4.子弹
    for i in range(20):
        zi_dan = Zidan(10)
    #5.老王把子弹放到弹夹
        laowang.anzhuang_zidan(dan_jia,zi_dan)

    #6.老王把弹夹放到枪里面
    laowang.anzhuang_danjia(ak47,dan_jia)

    #7.老王拿起枪
    laowang.naqiang(ak47)

    #8.敌人
    daitu = Person("歹徒")

    #9.老王开枪
    for i in range(12):
        print(daitu)
        print(laowang)
        laowang.kaiqiang(daitu)
##############################################################

if __name__ == '__main__':
    main()