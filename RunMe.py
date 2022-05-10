import sys
import win32api
import os
import shutil 
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
def copy_dir(src_path, target_path):
	if os.path.isdir(src_path) and os.path.isdir(target_path):		
		filelist_src = os.listdir(src_path)							
		for file in filelist_src:
			path = os.path.join(os.path.abspath(src_path), file)	
			if os.path.isdir(path):
				path1 = os.path.join(os.path.abspath(target_path), file)	
				if not os.path.exists(path1):						
					os.mkdir(path1)
				copy_dir(path,path1)			
			else:								
				with open(path, 'rb') as read_stream:
					contents = read_stream.read()
					path1 = os.path.join(target_path, file)
					with open(path1, 'wb') as write_stream:
						write_stream.write(contents)
		return 	True	
						
	else:
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
程序名 = os.path.basename(__file__)
oa= os.path.realpath(程序名)
o = oa.replace(程序名,'')  #可根据C盘容量自主选择存储位置，默认为D盘
o = o.replace('\\','/')
file_path = o+'usb自动复制计划/初始盘符/'
try:
    m = open(r''+file_path+'panfu2.txt','w')
    m.write(neirong2)
    m.close
except FileNotFoundError:
    mkdir(file_path)
    m = open(r''+file_path+'panfu2.txt','w')
    m.write(neirong2)
    m.close

m = open(r''+file_path+'panfu.txt','r')
count = len(m.readlines())
m.close()
文件 = open(file_path+'panfu.txt',mode='r',encoding='utf-8')
neirong3 = 文件.read()
文件.close()
#print(文件.read())       #返回示例：C:\
                                    #D:\
                                    #
    ##for i in range(count):   #逐行读取，已被废弃
        ##r = 文件.readline()
        ##i = r
        ##i = i.replace('\n','')
if neirong3 != neirong2 :
    with open(file_path+'panfu2.txt', 'r') as f:  #打开文件
        lines = f.readlines() #读取所有行
        last_line = lines[-1] #取最后一行     
        #print ('最后一行为：'+ last_line)       #返回示例：最后一行为：D:\   
                                                                    #
    last_line = last_line.replace('\n','')
    print(last_line)
    mkdir('C:/Usb '+last_line.replace(':/',''))
    copy_dir(last_line,'C:/桌面/')
    #copy_allfiles(last_line,'D:/gzm/test')
elif neirong3 == neirong2 :
    print('相同')
n = oa
#n = n.encode('UTF-8')
n = n.replace("'",'')
n = n.replace('b','')
n = n.replace('鐩戞祴绋嬪簭','')
#n = n.replace('\\RunMe.py','\\usb自动复制计划\\RunMe.py')
import time
time.sleep(15)
path = os.path.dirname(os.path.realpath(sys.argv[0]))
    #realpath = path+r"\ " + 程序名
                #realpath = realpath.replace(' ','')
                #realpath = realpath.replace('\\','/')
                #run = 'python '+realpath
path = path.replace(r'\\','/')
os.system(r'cd '+path)
#os.system('dir')
os.system('python '+程序名)
