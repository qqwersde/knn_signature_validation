#!/usr/bin/env python

from __future__ import print_function
import cv2
import sys
import numpy as np
import os 

standard_size = (150,50)
training_dir = '../training_set/Offline_Genuine/'

def print_img(img, bg_char='0', fg_char='1', pure_img=False):
	for i in range(len(img)):
		for j in range(len(img[0])):
                    if pure_img:
			print("%3d " % img[i,j], end='')
                    else:
			if img[i,j] == 0 :
				print(fg_char, end='')
			else:
				print(bg_char, end='')

		print('.')
def preprocess_image(img_path):
	img = cv2.imread(img_path, 1);
	img = cv2.resize(img, standard_size, interpolation=cv2.INTER_AREA)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	(thresh, img) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	return img

def get_training_set():
	train_labels = []
	train_datas = []
	for i in range(16):
		train_labels.append(str(i+1).zfill(3))
		train_datas.append([])
		for j in range(10):
			img_path = training_dir + train_labels[-1] + "_" + str(j+1).zfill(2) + '.PNG'
			if not os.path.isfile(img_path):
				break
			img = preprocess_image(img_path)
			train_datas[-1].append(img)
	return (train_datas, train_labels)

def get_testing_set():
	test_labels = []
	test_datas = []
	for i in range(16):
		test_labels.append(str(i+1).zfill(3))
		test_datas.append([])
		for j in range(11,21):
			img_path = training_dir + test_labels[-1] + "_" + str(j+1).zfill(2) + '.PNG'
			if not os.path.isfile(img_path):
				break
			img = preprocess_image(img_path)
			#tmp = cv2.imread(path, 1);
			#tmp = cv2.resize(tmp, standard_size, interpolation=cv2.INTER_AREA)
			#tmp = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
			#(thresh, tmp) = cv2.threshold(tmp, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
			test_datas[-1].append(img)
	return (test_datas, test_labels)

def print_datas(datas):
	for i in datas:
		for j in i:
			print_img(j)

#print_img(train_datas[0][0])
(train_datas, train_labels) = get_training_set()
(test_datas, test_labels) = get_testing_set()
#print_datas(train_datas)
#model = KNeighborsClassifier()
#model.fit(train_datas, test_labels)
#print(train_datas[0])
#cv2.destroyAllWindows()
