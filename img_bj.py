#!/usr/bin/python
# Filename: histsimilar.py
# -*- coding: utf-8 -*-
import Image
import time

def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    return sum(1 - (0 if l == r else float(abs(l - r))/max(l, r)) for l, r in zip(lh, rh))/len(lh)

def calc_similar(li, ri):
    return hist_similar(li.histogram(), ri.histogram())

def split_image_calc_similar(img1,img2, part_nber_x, part_nber_y,ist):
    img1=img1.convert('L')
    img2=img2.convert('L')
    w, h = img1.size
    pw=w/part_nber_y
    ph=h/part_nber_y
    i=0
    j=0
    brk=0
    for i in xrange(0, w, pw):
        if brk!=0:
            break
        for j in xrange(0, h, ph):
            l=img1.crop((i, j, i+pw, j+ph)).copy()
            r=img2.crop((i, j, i+pw, j+ph)).copy()
            ll=hist_similar(l.histogram(), r.histogram())
            print ll
            if abs(ll)<ist:
                    brk=1
                    l.save('C:/Users/pnkiu/Desktop/tmp/l1.jpg')
                    r.save('C:/Users/pnkiu/Desktop/tmp/r1.jpg')
                    break
    if brk==1:
        return 1
    else:
        return 0

if __name__ == '__main__':
    timestamp=time.time()
    print timestamp
    img1=Image.open('C:/Users/pnkiu/Desktop/tmp/0007w01609130753s.jpg')
    img2=Image.open('C:/Users/pnkiu/Desktop/tmp/0007w01609130754s.jpg')                
    print split_image_calc_similar(img1,img2, 4,4,0.3)
    timestamp2=time.time()
    print timestamp2
    print timestamp2-timestamp
