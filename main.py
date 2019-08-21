from framework import *
import numpy as np

if __name__ == "__main__":
    parameters = ("#763dff",'-',"#000000",'--', 3)
    destination_folder = "/Users/bilalqadar/Documents/GitHub/Data_visualization/saved_figures/"

    # x_bully = [2007,2009,2010,2011,2013,2014,2015,2016,2019]
    # y_bully = [18.8,21.5,20.8,29.2,24.1,34.6,34.0,33.6,36.5]
    # bullying_title = "Cyberbullying Victimization Rates (2007-2019)"
    # bullying_plot = DataVis(bullying_title)
    # bullying_plot.add_caption("Figure 1: Percentage of Toronto students who identify with being bullied each year. Dataset is of random Toronto middle and highschool students (N=3000).")
    # bullying_plot.add_data(x_bully,y_bully)
    # bullying_plot.add_label("x","Year")
    # bullying_plot.add_label("y", "Bullying Rate (%)")
    # bullying_plot.plot(0,parameters,3,False,destination_folder)

    # cyber_title = "Cyberbullying Related Google Searches (2004-2019)"
    # file_location ="/Users/bilalqadar/Documents/GitHub/Data_visualization/csv_files/cyberbullying.csv"
    # cyber_trend = DataVis(cyber_title)
    # cyber_trend.add_caption("Figure 2: Candian Google searches related to cyberbullying since 2004. Youth sometimes don’t feel comfortable identifying being bullied. The data is normalized with 100 being the peak number of searches and all other data points scaled appropriately.")
    # cyber_trend.add_data_csv(file_location, 2, "Month", "Cyberbullying")
    # cyber_trend.add_label("y", "Normalized Interest")
    # cyber_trend.plot(0,parameters,3,False,destination_folder)

    insta_title = "Instagram Bullying Related Google Searches (2006-2019)"
    file_location ="/Users/bilalqadar/Documents/GitHub/Data_visualization/csv_files/instaBully.csv"
    insta_trend = DataVis(insta_title)
    insta_trend.add_caption("Figure 3: Canadian Google searches related to instagram bullying since 2006. The data is normalized with 100 being the peak number of searches and all other data points scaled appropriately.")
    insta_trend.add_data_csv(file_location, 2, "Month", "instagram bullying: (Worldwide)")
    insta_trend.add_label("y", "Normalized Interest (%)")
    insta_trend.add_label("x","Time (Years)")
    insta_trend.plot(48,parameters,3,False,destination_folder)

    # y_vc = [1147.0,2613.0,3297.0,4093.0,5425.0,9334.0]
    # x_vc = [2013,2014,2015,2016,2017,2018]
    # vc_title = "Total VC funding for AI & ML startups (2013-2018)"
    # vc_plot = DataVis(vc_title)
    # vc_plot.add_caption("Figure 4: Amount of VC funding for AI & Machine learning startups over time. As trendline suggest VC's investing in machine learning is growing linearly with respect to time.")
    # vc_plot.add_data(x_vc,y_vc)
    # vc_plot.add_label("x","Year")
    # vc_plot.add_label("y", "VC funding (Millions)")
    # vc_plot.plot(0,parameters,1,False,destination_folder)

    # howML_title = "How to Learn Machine Learning Related Google Searches (2004-2019)"
    # file_location ="/Users/bilalqadar/Documents/GitHub/Data_visualization/csv_files/howML.csv"
    # howML = DataVis(howML_title)
    # howML.add_caption("Figure 5: anadian Google searches related to learning about machine learning since 2006. The data is normalized with 100 being the peak number of searches and all other data points scaled appropriately.")
    # howML.add_data_csv(file_location, 2, "Month", "how to learn machine learning: (Worldwide)")
    # howML.add_label("y", "Normalized Interest")
    # howML.plot(0,parameters,3,False,destination_folder)
