from framework import *
import numpy as np

if __name__ == "__main__":
    parameters = ("#de312a","k--", 20)
    destination_folder = "/Users/bilalqadar/Documents/data_visualization/saved_files"
    #
    # x_bully = [2007,2009,2010,2011,2013,2014,2015,2016,2019]
    # y_bully = [18.8,21.5,20.8,29.2,24.1,34.6,34.0,33.6,36.5]
    # bullying_title = "Cyberbullying Victimization Rates"
    # bullying_plot = DataVis(bullying_title)
    # bullying_plot.add_data(x_bully,y_bully)
    # bullying_plot.add_label("x","Year")
    # bullying_plot.add_label("y", "Bullying Rate (%)")
    # bullying_plot.plot(parameters,True,True,destination_folder)
    #
    # y_vc = [1147.0,2613.0,3297.0,4093.0,5425.0,9334.0]
    # x_vc = [2013,2014,2015,2016,2017,2018]
    # vc_title = "Total VC funding for AI & ML startups"
    # vc_plot = DataVis(vc_title)
    # vc_plot.add_data(x_vc,y_vc)
    # vc_plot.add_label("x","Year")
    # vc_plot.add_label("y", "VC funding (Millions)")
    # vc_plot.plot(parameters,False,True,destination_folder)
    #
    # cyber_title = "Cyberbullying Related Google Searches"
    # file_location ="/Users/bilalqadar/Documents/data_visualization/csv_files/multiTimeline.csv"
    # cyber_trend = DataVis(cyber_title)
    # cyber_trend.add_data_csv(file_location, 2, "Month", "Cyberbullying")
    # cyber_trend.add_label("y", "Normalized Interest")
    # cyber_trend.plot(parameters,True,False,destination_folder)

    cyber_title = "Cyberbullying Related Google Searches"
    file_location ="/Users/bilalqadar/Documents/data_visualization/csv_files/multiTimeline.csv"
    cyber_trend = DataVis(cyber_title)
    cyber_trend.add_data_csv(file_location, 2, "Month", "Cyberbullying")
    cyber_trend.add_label("y", "Normalized Interest")
    cyber_trend.plot(parameters,True,False,destination_folder)
