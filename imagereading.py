#!/usr/bin/python3
# 2018.01.16 01:11:49 CST
# 2018.01.16 01:55:01 CST
import cv2
import numpy as np

## (1) read - doc anh, convert anh ve dang thuoc xam
img = cv2.imread("mm.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('0',gray)
cv2.waitKey(0)

## (2) threshold - dat nguong gi  a tri cua anh
th, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
# cv2.imwrite("rr1.png", threshed)

cv2.imshow('1',threshed)
cv2.waitKey(0)


## (3) minAreaRect on the nozeros
# ma tran cac diem khac 0
pts = cv2.findNonZero(gray)
# tra ve cac thong so cua hinh chu nhat quay co dien tich nho nhat
ret = cv2.minAreaRect(pts)
(cx,cy), (w,h), ang = ret
# print('w: ',img.shape[1],'h: ',img.shape[0])
# print('w1: ', w,'h2: ',h)

# neu w > h thi quay them 90'
if img.shape[1]<img.shape[0]:
    # print('run1')
    w,h = h,w
    ang -= 90

if img.shape[1]>img.shape[0] and w<h:
    # print('run2')
    w,h = h,w
    ang -= 90

## (4) Find rotated matrix, do rotation
# truyen tham so ve tam, goc quay va ti le cua hinh de thuc hien quay ma tran
M = cv2.getRotationMatrix2D((cx,cy), ang, 1.0)
# truyen anh, ma tran bien doi M va kich thuoc anh de quay, tra ve anh da duoc quay
rotated = cv2.warpAffine(threshed, M, (img.shape[1], img.shape[0]))

## (5) find and draw the upper and lower boundary of each lines
# giam chieu ma tran 2D ve 1D, sau do reshape ma tran voi so chieu va so kenh khac
hist = cv2.reduce(rotated,1, cv2.REDUCE_AVG).reshape(-1)

thresh = 0
# kich thuoc anh
H,W = img.shape[:2]

# luu lai hang pixel co su thay doi ve gia tri mau sac
# danh dau dong ke tren
uppers = [y for y in range(H-1) if hist[y]<=thresh and hist[y+1]>thresh]
# danh dau dong ke duoi
lowers = [y for y in range(H-1) if hist[y]>thresh and hist[y+1]<=thresh]

# convert anh tu dang thuoc xam sang anh mau
rotated = cv2.cvtColor(rotated, cv2.COLOR_GRAY2BGR)
# cv2.imwrite("rr2.png", rotated)
cv2.imshow('2',rotated)
cv2.waitKey(0)

# ve duong gioi han tren
for y in uppers:
    cv2.line(rotated, (0,y), (W, y), (255,0,0), 1)

# ve duong gioi han duoi
for y in lowers:
    cv2.line(rotated, (0,y), (W, y), (0,255,0), 1)

# tao anh
# cv2.imwrite("rr3.png", rotated)
cv2.imshow('3',rotated)
cv2.waitKey(0)