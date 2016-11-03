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
    if gprice.isdigit() is False:
        print '价格请输入数字!'
        get_googs_price()
    return int(gprice)

def get_googs_amount():
    amount = raw_input("请输入商品数量:\n")
    if len(amount) == 0:
        get_googs_amount()
    if amount.isdigit() is False:
        print '数量请输入数字!'
        get_googs_amount()
    return int(amount)

def calculate_price():
    goods = get_googs_name()

    gprice_int = get_googs_price()

    amount_int = get_googs_amount

    print '门店:上海浦东第一分店 \n收款台:001 \n-------------------------'
    print '商品   单价   量   金额'
    print '%s   %d   %d   %d' % (goods,gprice_int,amount_int,gprice_int*amount_int)

    print '-------------------------'
if __name__ == '__main__':
    calculate_price()