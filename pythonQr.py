#-*- coding: utf-8 -*-
import zbar
from PIL import Image

#创建图片扫描对象
scanner = zbar.ImageScanner()
#设置对象属性
scanner.parse_config('enable')

#打开含有二维码的图片
img = Image.open('C:/Users/pnkiu/Desktop/tmp/qr.jpg').convert('L')
#获取图片的尺寸
width, height = img.size

#建立zbar图片对象并扫描转换为字节信息
qrCode = zbar.Image(width, height, 'Y800', img.tostring())
scanner.scan(qrCode)

data = ''
for s in qrCode:
    data += s.data

# 删除图片对象
del img

# 输出解码结果
print data

