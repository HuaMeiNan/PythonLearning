class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)

class House:
    def __init__(self, house_tupe, area):
        self.house_type = house_tupe
        self.area = area
        self.free_area = area
        self.jiaju_list = []

    def __str__(self):
        return '户型是 %s \n占地面积是 %.2f\n' \
               '剩余面积是 %.2f\n家具 %s' %(self.house_type,
                              self.area, self.free_area, self.jiaju_list)

    def add_jiaju(self,jiaju):
        print('要添加的家具 %s' %jiaju.name)
        if jiaju.area > self.area :
            print('这个%s家具太大了，家里放不下' % jiaju.name)
            return
        else:
            self.free_area -= jiaju.area
            self.jiaju_list.append(jiaju.name)


bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 200)
table = HouseItem('桌子', 1.5)

myhome = House('两室一厅', 60)
myhome.add_jiaju(bed)
myhome.add_jiaju(chest)
myhome.add_jiaju(table)



print(myhome)