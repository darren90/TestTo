# import unittest


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()



brandlist = ['A','B','C','D','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','W','X','Y','Z']

# http://www.autohome.com.cn/grade/carhtml/U.html

# print len(brandlist)

baseUrl = 'http://www.autohome.com.cn/grade/carhtml/'

for list in brandlist:
    url = baseUrl + list +'.html'
    print url