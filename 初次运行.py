import win32api
import os
def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
        print (path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path+' 目录已存在')
        return False
drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
#print (drives)   #返回示例：['C:\\', 'D:\\']
i = 0
neirong2 = ''
for i in range(len(drives)):
    neirong = drives[i]+'\n'
    neirong2 = neirong2+neirong
    i=i+1
#print(neirong2)       #返回示例：C:\ 
                            # D:\ 
                            # 
程序名 = os.path.basename(__file__)
o = os.path.realpath(程序名)
o = o.replace(程序名,'')  #可根据C盘容量自主选择存储位置，默认为D盘
o = o.replace('\\','/')
file_path = o
try:
    m = open(r''+file_path+'panfu.txt','w')
    m.write(neirong2)
    m.close
except FileNotFoundError:
    mkdir(file_path)
    m = open(r''+file_path+'panfu.txt','w')
    m.write(neirong2)
    m.close
