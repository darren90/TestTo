#-*-coding:utf-8-*-

commodity = raw_input("please enter the goods\n")
unit_price = raw_input("Please enter the commodity price\n")
number = raw_input("Please enter the quantity\n")

total_price = int(unit_price) * int(number)

print u"\t欢迎光临\n\n门店：佳怡服装店\n\n收款台：001\n"
print "-------------------------"
print '商品   单价   量   金额'
print '%s   %s   %s   %d' % (commodity, unit_price, number, total_price)
print "-------------------------"
