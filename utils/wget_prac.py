#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import shutil
import os
import requests
import progressbar as bar
"""
time: 2019/4/1
contain: wget脚本，完成对图片的批量预测
inputs：标题图片
outputs：OCR识别结果，保存在txt中，并且以预测结果命名
"""

def wget_ocr(inputs_path):
    files = os.listdir(inputs_path)
    # 遍历文件夹下所有内容
    for file in files:
        # f = open(inputs_path+'/'+file)
        urls = os.path.join("http://localhost:4444/")
        print(file)
        name = requests.get(urls, {'path': os.path.join(inputs_path, file)})
        print(name.text)


def ocr_files(input_root, ocr_outputs, target=None ):
    # print(os.listdir(input_root))
    # match = 0
    filenames = list(filter(lambda n: n.split('.')[-1] in ('jpg', 'png', 'jpeg'), os.listdir(input_root)))
    match = 0
    total = len(filenames)
    
    new_names = list(map(lambda n: n.split('.')[-1], filenames))
    url = "http://localhost:4444"
    with bar.ProgressBar(max=total) as b:
        for idx, filename in enumerate(filenames):
            name = requests.get(url, {'path': os.path.join(input_root, filename)}).text.strip()
            if name.find(target):
                match += 1
            new_names[idx] = name+'.'+new_names[idx]
            b.update(idx+1)

    for idx, (old_name, new_name) in enumerate(zip(filenames, new_names)):
        shutil.copyfile(os.path.join(input_root, old_name), os.path.join(ocr_outputs, '..', '%d_'%idx+ new_name))
        print(os.path.join(input_root, old_name), '\t->\t', os.path.join(ocr_outputs, '..', '%d_'%idx+ new_name))
    return match, total

if __name__ == '__main__':
    path = "G:\图像处理\\title_img\\title_img\CDS"
    ocr_out = "G:\图像处理\\title_img\\title_img\CDS\\test"
    m, t = ocr_files(path,  ocr_out,target="裁定书")
    print(m/t)
