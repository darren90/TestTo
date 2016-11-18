# -*- coding: UTF-8 -*-

def judge_url():
    url_str = raw_input("Please string to judge if that is a url:\n")
    if len(url_str) == 0:
        loginSys()
    elif (url_str.startswith('http://')) and len(url_str) > 7:
		print 'right,this is a url'
    else:
		print 'wrong,this is not a url'

if __name__ == '__main__':
    judge_url()
