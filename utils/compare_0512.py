import subprocess as sp
import requests as rq
import argparse
import os
from time import time

parser = argparse.ArgumentParser()
parser.add_argument('src')
parser.add_argument('dst')
args = parser.parse_args()
if __name__ == '__main__':
    # print(args.path)
    init_tick = time()
    # args.src: 存放需要预测的图片的目录
    # args.dst: 预测结果存放路径

    for img in os.listdir(args.src):
        img_out_path = os.path.join('%s/%s.txt' % (args.dst, img))
        img_in_path = os.path.join(args.src, img)
        sp.check_output('tesseract %s %s-ts -l chi_sim'%(img_in_path, img_out_path), shell=True)
        ts_tick = time()
        out_text = rq.get('http://ocr4judging:4444', {'path':img_in_path, 'remove_lines':True}).text
        cnn_tick = time()
        ts_time = '%d' % ((ts_tick - init_tick)*1000,)
        cnn_time = '%d' % ((cnn_tick - ts_tick)*1000,)
        with open('%s-cnn-%s.txt' % (args.dst, cnn_time), 'w') as f:
            f.write(out_text)

        os.rename('%s-ts.txt' % args.dst, '%s-ts-%s.txt' % (args.dst, ts_time))
    print('done')
