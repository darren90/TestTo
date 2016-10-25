# -*- coding: utf-8 -*-
import optparse
import os
import sys
import getpass
import json
import hashlib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from datetime import date, time, datetime, timedelta

# jenkins
# http://www.jianshu.com/p/02e010bb2b3c

# git 仓库： 用户名git  密码rrmjgit

#配置文件路径
commendPath = "/Users/" + getpass.getuser() + "/"
 
#工程名
targetName = "PUClient"
#临时文件夹名称
tempFinder = "test001"
#git地址
gitPath = "ssh://git@106.75.11.245:29876/data/rrmj_git/rrmjiPad.git"
#checkout后的本地路径 /Users/Fengtf/Documents/git/iPad
# target_path = commendPath + "Documents/git/iPad"
#主路径
mainPath = commendPath + "github/TestTo/iIpa/rrmjiPad/PUClient"
#证书名
certificateName = "123"
#firToken
firToken = "09dc8056c60a0179622024dfcb00ae98"
#邮件参数
emailFromUser = "2176695339@qq.com"
emailToUser = "1005052145@qq.com"
emailPassword = "qazwsx"
emailHost = "smtp.qq.com"

#判断是否是workspace
isWorkSpace = False

#版本
tag = "origin/RRMJ_YS"

#钥匙链相关
keychainPath="~/Library/Keychains/login.keychain"
keychainPassword=""

#显示已有的参数
def showParameter():
    print "targetName                 :%s"%targetName
    print "gitPath                    :%s"%gitPath
    print "certificateName            :%s"%certificateName
    print "firToken                   :%s"%firToken
    print "emailFromUser              :%s"%emailFromUser
    print "emailToUser                :%s"%emailToUser
    print "emailPassword              :%s"%emailPassword
    print "emailHost                  :%s"%emailHost
    print "keychainPassword(Optional) :%s"%keychainPassword
    
#判断字符串是否为空
def isNone(para):
    if para == None or len(para) == 0:
        return True
    else:
        return False
    
#是否需要设置参数
def isNeedSetParameter():
    if isNone(targetName) or isNone(gitPath) or isNone(certificateName) or isNone(firToken) or isNone(emailFromUser) or isNone(emailToUser) or isNone(emailPassword) or isNone(emailHost) :
        return True
    else :
        return False
        

#参数设置
def setOptparse():
    p = optparse.OptionParser()
    #参数配置指令
    p.add_option("--config","-c",action="store_true", default=None,help = "config User's data")
    #获取所有版本
    p.add_option("--showTags","-s",action="store_true", default=None,help = "show all tags")
    #设置版本指令
    p.add_option('--tag','-t',default="master",help = "app's tag")
    options,arguments = p.parse_args()
    global tag
    tag = options.tag
    #配置信息
    # if options.config == True and len(arguments) == 0 :
    configMethod()
    #获取所有版本
    if options.showTags == True and len(arguments) == 0 :
        gitShowTags()
   
#配置信息 
def configMethod():
    os.system("clear")
    print "您的参数如下:"
    print "************************************"
    showParameter()
    print "************************************"
    # sys.exit()
        
#删除文件夹
def rmoveFinder():
    os.system("rm -r -f %s"%mainPath)
    return
    
#创建文件夹
def createFileFinder():
    os.system("mkdir %s"%mainPath)
    return
    
#对文件夹授权
def allowFinder():
    os.system("chmod -R 777 %s"%mainPath)
    return
    
#查找文件
def scan_files(directory,postfix):
  files_list=[]
  for root, sub_dirs, files in os.walk(directory):
    for special_file in sub_dirs:
        if special_file.endswith(postfix):
            files_list.append(os.path.join(root,special_file))    
  return files_list
  
#判断文件夹是否存在
def isFinderExists():
    return os.path.exists(mainPath)

#clone工程
def gitClone():
    os.system ('git clone %s %s --depth 1'%(gitPath,mainPath))
    return
    
#显示所有版本
def gitShowTags():
    os.system("clear")
    print "所有的版本"
    print mainPath
    print "************************************"
    os.system ('cd %s;git tag'%mainPath)
    print "************************************"
    sys.exit()

#pull工程
def gitPull():
    os.system("cd %s;git reset --hard;git pull"%mainPath)
    return
   
#设置版本 
def setGitVersion(version):
    if len(version)>0:
        os.system("cd %s;git reset --hard;git checkout %s"%(mainPath,version))
    return
    
#回到主版本
def setGitVersionMaster():
    setGitVersion("master")
    return
 
#clean工程   
def cleanPro():
    global isWorkSpace
    if isWorkSpace:
        os.system('cd %s;xcodebuild -workspace %s.xcworkspace -scheme %s clean'%(mainPath,targetName,targetName))
    else:
        os.system('cd %s;xcodebuild -target %s clean'%(mainPath,targetName))
    return

#清理pbxproj文件
def clearPbxproj():
    global all_the_text
    path = "%s/%s.xcodeproj/project.pbxproj"%(mainPath,targetName)
    print '--------path:%s' % path
    file_object = open(path)
    try:
        all_the_text=file_object.readlines()
        for text in all_the_text:
            if 'PROVISIONING_PROFILE' in text:
                all_the_text.remove(text)
    finally:
        file_object.close()
       
    file_object = open(path,'w')
    try:
        for text in all_the_text:
            file_object.write(text)
    finally:
        file_object.close()
    return

def allowKeychain():
    # User interaction is not allowed
    os.system("security unlock-keychain -p '%s' %s"%(keychainPassword,keychainPath))
    return

#编译获取.app文件和dsym
def buildApp():
    global isWorkSpace
    print '----mainpath:%s' % mainPath
    files_list=scan_files(mainPath,postfix=".xcodeproj")
    temp = -1
    for k in range(len(files_list)):
        if files_list[k] == mainPath + "/" + targetName + ".xcodeproj":
            temp = k
    if temp >= 0:
        files_list.pop(temp)
    for target in files_list:
        target=target.replace(".xcodeproj","")
        tmpList=target.split('/')
        name=tmpList[len(tmpList)-1]
        path=target.replace(name,"")
        path=path[0:len(path)-1]
        os.system("cd %s;xcodebuild -target %s CODE_SIGN_IDENTITY='%s'"%(path,name,certificateName))
    if isWorkSpace:
        os.system("cd %s;xcodebuild -workspace %s.xcworkspace -scheme %s CODE_SIGN_IDENTITY='%s' -derivedDataPath build/"%(mainPath,targetName,targetName,certificateName))
    else:
        os.system("cd %s;xcodebuild -target %s CODE_SIGN_IDENTITY='%s'"%(mainPath,targetName,certificateName))
    return
    
#创建ipa
def cerateIPA():
    os.system ("cd %s;rm -r -f %s.ipa"%(mainPath,targetName))
    os.system ("cd %s;xcrun -sdk iphoneos PackageApplication -v %s/build/Build/Products/Debug-iphoneos/%s.app -o %s/%s.ipa CODE_SIGN_IDENTITY='%s'"%(mainPath,mainPath,targetName,mainPath,targetName,certificateName))
    return
    
#上传
def uploadToFir():
    httpAddress = None
    if os.path.exists("%s/%s.ipa"%(mainPath,targetName)):
        ret = os.popen("fir p '%s/%s.ipa' -T '%s'"%(mainPath,targetName,firToken))
        for info in ret.readlines():
            if "Published succeed" in info:
                httpAddress = info
                print httpAddress
                break
    else:
        print "没有找到ipa文件"
    return httpAddress
        
#发邮件给测试不带附件
def sendEmail(text):
    if not os.path.exists("%s/%s.ipa"%(mainPath,targetName)):
        print "没有找到ipa文件"
        return
    msg = MIMEText('地址:%s'%text,'plain','utf-8')
    msg['to'] = emailToUser
    msg['from'] = emailFromUser
    msg['subject'] = '新的测试包已经上传'
    try:
        server = smtplib.SMTP()
        server.connect(emailHost)
        server.login(emailFromUser,emailPassword)
        server.sendmail(msg['from'], msg['to'],msg.as_string())
        server.quit()
        print '发送成功'
    except Exception, e:  
        print str(e)
    return
    
#定时任务
def runTask(func, day=0, hour=0, min=0, second=0):
  # Init time
  now = datetime.now()
  strnow = now.strftime('%Y-%m-%d %H:%M:%S')
  print "now:",strnow
  # First next run time
  period = timedelta(days=day, hours=hour, minutes=min, seconds=second)
  next_time = now + period
  strnext_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
  print "next run:",strnext_time
  while True:
      # Get system current time
      iter_now = datetime.now()
      iter_now_time = iter_now.strftime('%Y-%m-%d %H:%M:%S')
      if str(iter_now_time) == str(strnext_time):
          # Get every start work time
          print "start work: %s" % iter_now_time
          # Call task func
          func()
          print "task done."
          # Get next iteration time
          iter_time = iter_now + period
          strnext_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
          print "next_iter: %s" % strnext_time
          # Continue next iteration
          continue

    
def setVersion():
    global tag
    setGitVersion(tag)
    return

#判断是否是workspace
def checkWorkSpace():
    global isWorkSpace
    if os.path.exists("%s/%s.xcworkspace"%(mainPath,targetName)):
        isWorkSpace = True
    else:
        isWorkSpace = False
    return

#主函数
def main():
    #参数设置
    setOptparse()
    #读取json文件
    #是否需要设置参数
    if isNeedSetParameter():
        print "您需要设置参数,您的参数如下(使用 --config 或者 -c):"
        showParameter()
        sys.exit()
    #获取最新代码
    if not isFinderExists():
        createFileFinder()
        gitClone()
    else:
        gitPull()
    #判断是否是workspace
    checkWorkSpace()
    #设置版本
    setVersion()
    #设置文件夹权限
    allowFinder()
    allowKeychain()
    #clear pbxproj文件
    clearPbxproj()
    #clean工程
    cleanPro()
    #编译
    print '-----cleanPro-----'
    buildApp()
    print '-----buildApp-----'
    #生成ipa文件
    cerateIPA()
    print '-----cerateIPA-----'
    #上传到fir.im
    httpAddress = uploadToFir()
    #发邮件给测试
    print '-----上传到fir.im-----'
    if not isNone(httpAddress):
        sendEmail(httpAddress)
    return

main()
