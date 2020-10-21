import json
from urllib import request
from urllib.request import Request
from urllib.parse import quote
from random import choice
import os
import sys

# 多少条一页
rn = 30
# 页码
pageNum = 2
#爬取图片数
num = 0
#子文件名
fileName = 0

def getImg(data):
    global num
    global folder
    global fileName
    for item in data:
        if item:
            request.urlretrieve(
                item['thumbURL'], folder + '\\' + str(fileName + 1)+".jpg", _progress)
            fileName += 1
            num += 1
            print('图片数量', num)


def _progress(block_num, block_size, total_size):
    '''回调函数
       @block_num: 已经下载的数据块
       @block_size: 数据块的大小
       @total_size: 远程文件的大小
    '''
    sys.stdout.write('\r>> 图片大小{0}，下载进度{1:.2f}%'.format(
        total_size, float(block_num * block_size / total_size) * 100.0))
    sys.stdout.flush()


def init(key):
    global pageNum
    for k in range(0, pageNum):
        # 百度地址
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=' + key + \
              '&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=' + key + \
              '&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=' + \
              str(rn * k) + '&rn=' + str(rn)
        print(url)
        userAgents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
            "Mozill#/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3766.400 QQBrowser/10.6.4163.400",
        ]
        Headers = {
            "User-Agent": choice(userAgents)
        }
        req = Request(url,headers=Headers)
        res = request.urlopen(req).read()
        #print(res)
        jsonData = json.loads(res)['data']
        print("init end")
        getImg(jsonData)



# animals = ["老虎","柴犬","非洲狮","非洲豹","北美灰熊",
#            "灰狼","孔雀","猕猴","黄牛","梅花鹿",
#            "骆驼","非洲长颈鹿","丹顶鹤","大熊猫","大象",
#            "河马","欧洲红松鼠","斑马","红熊猫","黑猩猩",
#            "鸡"]
# animal_names = ["tiger","dog","lion","leopard","bear",
#        "wolf","peacock","monkey","cattle","deer",
#        "camel","giraffe","crane","panda","elephant",
#        "hippo","squirrel","zebra","Red panda","chimpanzee",
#        "cock"]

#输入你要搜索的关键字
targets = ["非洲长颈鹿"]
#该关键字对应的目录名
targets_en = ["giraffe"]
#存入的目录 必须实际存在
dst_folder = "E:\\detection\\"

if __name__ == "__main__":
    for target,target_en in zip(targets,targets_en):
        #创建该分类文件夹
        folder = dst_folder + target_en
        if os.path.exists(folder):
            print("文件夹已存在")
        else:
            os.mkdir(folder)
        print('文件夹为', folder)
        print(target)
        target = quote(target)
        fileName = 0
        init(target)
    print('数据爬取完成'.center(50, '*'))
