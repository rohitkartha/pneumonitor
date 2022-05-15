import os
from random import random
import numpy as np
import pandas as pd
from PIL import Image

class Data():
    def __init__(self):
        self.dataloc = "C:/Users/Advait Patel/Hackathons/hackIMSA/data/chest_xray/"
        self.test_dir = os.path.join(self.dataloc,'test') 
        self.train_dir = os.path.join(self.dataloc,'train') 
        self.val_dir = os.path.join(self.dataloc,'val') 
        self.categ = ["NORMAL", "PNEUMONIA"]

    def format_data(self, output_list, categ, data_dir):
        img_size = 150
        for ca in categ:
            path = os.path.join(data_dir, ca)
            class_num = categ.index(ca)
            for img in os.listdir(path):
                try:
                    img_arr = Image.open(os.path.join(path, img)) 
                    new_img = img_arr.resize((img_size, img_size))
                    new_img = np.asarray(new_img)
                    arr = new_img.reshape((img_size, img_size, 1))
                    output_list.append([arr, class_num])
                except Exception as e:
                    e = e

    def split_data(self, X, y, split_list):
        img_size = 150
        for img, label in split_list:
            X.append(img)
            y.append(label)
        X = np.array(X).reshape(-1, img_size, img_size, 1)

    def preprocess(self):
        train_list = []
        val_list = []
        test_list = []

        self.format_data(train_list, self.categ, self.train_dir)
        self.format_data(val_list, self.categ, self.val_dir)
        self.format_data(test_list, self.categ, self.test_dir)

        np.random.shuffle(train_list)
        np.random.shuffle(test_list)
        np.random.shuffle(val_list)

        for i in range(608):
            ele = train_list.pop(0)
            val_list.append(ele)

        X_train = []
        y_train = []
        X_val = []
        y_val = []
        X_test = []
        y_test = []

        self.split_data(X_train, y_train, train_list)
        self.split_data(X_val, y_val, val_list)
        self.split_data(X_test, y_test, test_list)

        X_train = np.asarray(X_train)
        y_train = np.asarray(y_train)
        X_test = np.asarray(X_test)
        y_test = np.asarray(y_test)
        X_val = np.asarray(X_val)
        y_val = np.asarray(y_val)

        X_train = X_train/255.0
        X_test = X_test/255.0
        X_val = X_val/255.0

        return X_train, y_train, X_test, y_test, X_val, y_val
    
        


