import subprocess as sp
#import requests as rq
import argparse
import os
from time import time

parser = argparse.ArgumentParser()
parser.add_argument('src')
parser.add_argument('dst')
args = parser.parse_args()
print(args)
if __name__ == '__main__':
    src = args.src#.replace('(', '\(').replace(')', '\)')
    dst = args.dst#.replace('(', '\(').replace(')', '\)')
    print(src, dst)
    ts_l = []
    num = 0
    for img in os.listdir(src):
        init_tick = time()
        img_out_path = ''.join([dst, img])
        img_in_path = ''.join([src, img])
        sp.check_output("tesseract '%s' '%s'-ts -l chi_sim"%(img_in_path, img_out_path), shell=True)
        ts_tick = time()
#        out_text = rq.get('http://nju-vm:4444', {'path':img_in_path, 'remove_lines':True}).text
#        cnn_tick = time()
        ts_time = '%d' % ((ts_tick - init_tick)*1000,)
#        cnn_time = '%d' % ((cnn_tick - ts_tick)*1000,)
#        with open('%s-cnn-%s.txt' % (args.dst, cnn_time), 'w') as f:
#            f.write(out_text)
        ts_l.append(int(ts_time))
        num += 1
        os.rename('%s-ts.txt' % img_out_path, '%s-ts-%s.txt' % (img_out_path, ts_time))
    print("num", num)
    print("l", ts_l)
    print("average_time", sum(ts_l)/num)
    print('done')
