import matplotlib.pyplot as plt
import numpy as np
import operator
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import cross_val_predict
import os
import pandas as pd

class DataVis:

    def __init__(self,title):
        self.x = [False]
        self.y = [False]
        self.trendline = False
        self.x_label = ""
        self.y_label = ""
        self.title = title
        plot = None

    def add_data(self,x,y):
        if type(x[0]) == str:
            self.x = x
        else:
            print('here')
            x = np.array(x)
            self.x = x

        self.y = np.array(y)

    def add_data_csv(self,file_destination,skip_rows,label_x,label_y):
        data = pd.read_csv(file_destination,skiprows=skip_rows)
        df1 = list(data[label_x])
        df2 = data[label_y]

        self.add_data(df1,df2)

    def add_label(self,type,label):
        if type == "x":
            self.x_label = label
        elif type == "y":
            self.y_label = label
        else:
            raise TypeError("Invalid label type")

    def update_title(self,new_title):
        self.title = new_title

    def get_trendline(self):
        if type(self.x[0]) == str:
            size = range(0,len(self.x))
            x = []
            for i in size:
                x.append(i)
            x = np.array(x)
            x = x[:, np.newaxis]
        else:
            x = self.x[:, np.newaxis]
        y = self.y[:, np.newaxis]

        polynomial_features= PolynomialFeatures(degree=3)
        x_poly = polynomial_features.fit_transform(x)

        model = LinearRegression()
        model.fit(x_poly, y)
        y_poly_pred = model.predict(x_poly)
        self.trendline = y_poly_pred

    def plot(self,parameters,trendline,grid,destination_folder):
        (data_fmt, trendline_fmt, line_width) = parameters
        if self.x[0] is False or self.y[0] is False:
            raise TypeError("Add data using add_data(x,y)")

        else:
            plt.plot(self.x,self.y, data_fmt)

        if trendline != False:
            self.get_trendline()
            plt.plot(self.x, self.trendline, trendline_fmt)

        plt.title(self.title, fontweight="bold",fontname="Open Sans")
        plt.xlabel(self.x_label,fontname="Open Sans", fontweight="bold")
        plt.ylabel(self.y_label,fontname="Open Sans", fontweight="bold")
        plt.xticks([])
        if grid is True:
            plt.grid(True)
        plt.savefig(os.path.join(destination_folder,self.title) + ".png" )
