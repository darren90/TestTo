# -*- coding: UTF-8 -*-

def get_googs_name():
    goods = raw_input("请输入商品名称:\n")
    if len(goods) == 0:
        get_googs_name()
    return goods

def get_googs_price():
    gprice = raw_input("请输入商品价格:\n")
    if len(gprice) == 0:
        get_googs_price()
    return gprice

def get_googs_amount():
    amount = raw_input("请输入商品数量:\n")
    if len(amount) == 0:
        get_googs_amount()
    return amount

def calculate_price():
    goods = get_googs_name()

    gprice = get_googs_price()
    if gprice.isdigit() is False:
        print '价格请输入数字!'
        get_googs_price()
    gprice_int = int(gprice)

    amount = get_googs_amount
    if amount.isdigit() is False:
        print '数量请输入数字!'
        get_googs_amount()
    amount_int = int(amount)

    print '门店:上海浦东第一分店 \n收款台:001 \n-------------------------'
    print '商品   单价   量   金额'
    print '%s   %d   %d   %d' % (goods,gprice_int,amount_int,gprice_int*amount_int)

    print '-------------------------'
if __name__ == '__main__':
    calculate_price()






# #-*-coding:utf-8-*-
#
# commodity = raw_input("please enter the goods\n")
# unit_price = raw_input("Please enter the commodity price\n")
# numbe
# total_price = int(unit_price) * int(number)
# # total_price = unit_price * number
# total_price = str(total_price)
# list=[commodity,unit_price,number,total_price]
#
# print u"\t欢迎光临\n\n门店：佳怡服装店\n\n收款台：001\n"
# print "-"*30
# print u"商品\t单价\t数量\t金额"
# print '\t'.join(list)
# print "-"*30
# r = raw_input("Please enter the quantity\n")

