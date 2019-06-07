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
    num = 0
    path_total = os.listdir(src)
    l = []
    l_s = []
    for folder in path_total:
        ts_l = []
        img_path = os.listdir(os.path.join(src, folder))
        for img in img_path:
            img_out_path = os.path.join(dst, folder)
            if not os.path.isdir(img_out_path):
                os.mkdir(img_out_path)
            init_tick = time()
            # img_out_path = ''.join([dst, img])
            # img_in_path = ''.join([src, img])
            img_in_path = os.path.join(src, folder, img)
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
        l.append(ts_l)
        l_s.append(sum(ts_l)/num)

    print("l", l)
    print("l_s", l_s)
    print('done')
    with open(dst, 'w', encoding='utf-8') as f:
        f.write('l', l)
        f.write('l_s', l_s)
