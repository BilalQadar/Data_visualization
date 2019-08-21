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
        self.caption = ""
        plot = None

    def add_caption(self,caption):
        self.caption = caption

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

    def calc_trendline(self,degree):
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

        polynomial_features= PolynomialFeatures(degree=degree)
        x_poly = polynomial_features.fit_transform(x)

        model = LinearRegression()
        model.fit(x_poly, y)
        y_poly_pred = model.predict(x_poly)
        self.trendline = y_poly_pred

    def plot(self,skip_data,parameters,trendline,grid,destination_folder):
        (data_color, data_line, trend_color, trend_line, line_width) = parameters

        plt.figure(figsize=(12, 9))
        ax = plt.subplot(111)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

        if self.x[0] is False or self.y[0] is False:
            raise TypeError("Add data using add_data(x,y)")

        else:
            plt.plot(self.x[skip_data:],self.y[skip_data:], color=data_color, linestyle=data_line,linewidth=line_width)

        if trendline != 0:
            print(trendline)
            self.calc_trendline(trendline)
            plt.plot(self.x[skip_data:], self.trendline[skip_data:], color=trend_color, linestyle=trend_line, linewidth=line_width)

        plt.title(self.title, fontsize=14,fontname="Open Sans")
        plt.xlabel(self.x_label,fontsize=14, fontname="Open Sans")
        plt.ylabel(self.y_label,fontsize=14,fontname="Open Sans")
        #Uncomment if want to specify  xtick labels and positions
        ## TODO: Make this more robust
        #[2006,2009,2012,2015,2019]
        # plt.xticks([0,(len(self.x) - skip_data)/4,(len(self.x) - skip_data)/2, (len(self.x) - skip_data) - (len(self.x) - skip_data)/4,len(self.x) - skip_data],[2006,2009,2012,2015,2019])
        if grid is True:
            plt.grid(True)

        if self.caption != "":
            plt.figtext(0.09, 0.01, self.caption, wrap=True, horizontalalignment='left', fontsize=10)

        bbox_inches="tight"
        plt.savefig(os.path.join(destination_folder,self.title) + ".png" )
