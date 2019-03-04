def find_a(x,y,dy):
    xy_avg=0
    sum_dy=0
    for i in range(0,len(x)):
        xy_avg=xy_avg+(x[i]*y[i])/(dy[i]**2)
        sum_dy=sum_dy+(1/(dy[i]**2))
    xy_avg=xy_avg/(sum_dy)
    x_avg=0
    x_avg_power = 0
    for i in range(0,len(x)):
        x_avg=x_avg+(x[i]/(dy[i]**2))
        x_avg_power = x_avg_power+(x[i]**2/(dy[i]**2))
    x_avg=x_avg/(sum_dy)
    x_avg_power=x_avg_power/(sum_dy)
    y_avg=0
    for i in range(0,len(y)):
        y_avg=y_avg+(y[i]/(dy[i]**2))
    y_avg=y_avg/(sum_dy)

    return ((xy_avg-(x_avg*y_avg))/(x_avg_power-(x_avg**2)))
def find_da(x,dy):
    dy_avg_power=0
    sum_dy = 0
    count=0
    for i in range(0,len(dy)):
        dy_avg_power=dy_avg_power+((dy[i] ** 2)/dy[i] ** 2)
        sum_dy=sum_dy+(1/(dy[i]**2))
        count=count+1
    dy_avg_power = dy_avg_power / (sum_dy)
    x_avg = 0
    x_avg_power = 0
    for i in range(0, len(x)):
        x_avg = x_avg + (x[i] / (dy[i] ** 2))
        x_avg_power = x_avg_power + (x[i] ** 2 / (dy[i] ** 2))
    x_avg = x_avg / (sum_dy)
    x_avg_power = x_avg_power /(sum_dy)

    return ((dy_avg_power/(count*(x_avg_power-(x_avg**2)))))**(0.5)
def find_b(y,a,x,dy):
    sum_dy = 0
    y_avg=0
    for i in range(0,len(y)):
        y_avg=y_avg+(y[i]/(dy[i]**2))
        sum_dy = sum_dy + (1 / (dy[i] ** 2))
    y_avg=y_avg/(sum_dy)
    x_avg = 0
    for i in range(0, len(x)):
        x_avg = x_avg + (x[i] / (dy[i] ** 2))
    x_avg = x_avg / (sum_dy)

    return y_avg-a*x_avg
def find_db(x,dy):
    dy_avg_power = 0
    sum_dy = 0
    count = 0
    for i in range(0, len(dy)):
        dy_avg_power = dy_avg_power + ((dy[i] ** 2) / dy[i] ** 2)
        sum_dy = sum_dy + (1 / (dy[i] ** 2))
        count = count+ 1
    dy_avg_power = dy_avg_power / (sum_dy)
    x_avg = 0
    x_avg_power = 0
    for i in range(0, len(x)):
        x_avg = x_avg + (x[i] / (dy[i] ** 2))
        x_avg_power = x_avg_power + (x[i] ** 2 / (dy[i] ** 2))
    x_avg = x_avg / (sum_dy)
    x_avg_power = x_avg_power / (sum_dy)

    return ((dy_avg_power)*(x_avg_power) / (count * (x_avg_power - (x_avg ** 2))))**(0.5)
def find_chi2red(chi,x):
    count=0
    for i in range(0,len(x)):
        count=count+1
    return chi/(count-2)


def find_chi2(y,a,b,x,dy):
    Chi2=0
    for i in range(0,len(x)):
        Chi2=Chi2+((y[i]-(a*x[i]+b))/(dy[i]))**2
    return Chi2
    
def data_with_rows (data):
	for x in data:
		line_data_list = x.split(" ")
		a = line_data_list[0].lower()
		line_data_list.pop(0)
		if a =="x":
			x_data = map(float,line_data_list)

		elif a== "y":
			y_data = map(float,line_data_list)
		elif a =="dx":
			dx_data = map(float,line_data_list)
		elif a == "dy":
			dy_data = map(float,line_data_list)


	if len(x_data) != len(y_data) and len(x_data) != len(dy_data) and len(x_data) != len(dx_data) and len(y_data) != len(dx_data) and len(y_data) != len(dy_data) and len(dy_data) != len(dx_data):
		print("Input file error: Data lists are not the same length")
		exit()
	for i in dx_data:
		if i <=0:
			print ("Input file error: Not all uncertainties are positive.")
			exit()
	for i in dy_data:
		if i <=0:
			print ("Input file error: Not all uncertainties are positive.")
			exit()
	return (x_data,y_data,dx_data,dy_data)

def data_with_column(data):
    mycheked_list=[]

    for i in data [:len(data)-1]:
        a = i.strip('\n').lower().split()
        mycheked_list.append(a)
    column= len(mycheked_list[0])
    r= len(mycheked_list)
    my_data=[]
    for k in range (column):
        newlist=[]
        for i in range (r):
            newlist.append(mycheked_list[i][k])
        my_data.append(newlist)
    for c in my_data :
        b= c[0]
        if b == "x":
             x = list(map(float, c[1:]))
        elif b == "y":
             Y = list(map(float, c[1:]))
        elif b == "dx":
             Dx = list(map(float, c[1:]))
        elif b == "dy":
             dY = list(map(float, c[1:]))
    if len(x) != len(Y) and len(x) != len(dY) and len(x) != len(Dx) and len(Y) != len(Dx) and len(Y) != len(dY) and len(dY) != len(Dx):
        print("Input file error: Data lists are not the same length")
        exit()
    for c2 in Dx:
         if c2 <=0:
            print ("Input file error: Not all uncertainties are positive.")
            exit()
    for c2 in dY:
         if c2 <=0:
            print ("Input file error: Not all uncertainties are positive.")
            exit()
    return (x,Y,Dx,dY)

import matplotlib.pyplot as plt
import numpy as np

def fit_linear(filename):
    my_file = open(filename)
    data = my_file.read()
    data = data.split("\n")
    
    data_header = data[0]
    data_header_list = data_header.split(" ")
    count = len(data_header_list)
    if count == 4:
       x,Y,Dx,dY = data_with_column(data)
       y_lable = data_header_list[0]
       x_lable = data_header_list[2]
       a = find_a(x, Y, dY)
       b = find_b(Y, a, x, dY)
       chi = find_chi2(Y, a, b, x, dY)
       print("a=", find_a(x,Y,dY), "+-", find_da(x,dY))
       print("b=", find_b(Y,a,x,dY), "+-", find_db(x,dY))
       print("chi2=", find_chi2(Y,a,b,x,dY))
       print("chi2_reduced=", find_chi2red(chi,x))
       my_x = np.array(x)
       my_y = np.array(Y)
       d = a * my_x + b
       my_x_errey = np.array(Dx)
       my_y_errey = np.array(dY)

       y = d
       plt.errorbar(my_x, my_y, yerr=my_y_errey, xerr=my_x_errey, fmt='none', ecolor='b')
       plt.plot(my_x, y, "r")
       plt.xlabel(x_lable)
       plt.ylabel(y_lable)
       plt.show()
       plt.savefig("linear_fit.svg")
       my_file.close()

    else:
       x,Y,Dx,dY=data_with_rows(data)
       y_lable = data[0].split(" ")[0]
       x_lable = data[2].split(" ")[0]
       a = find_a(x, Y, dY)
       b = find_b(Y, a, x, dY)
       chi = find_chi2(Y, a, b, x, dY)
       print("a=", find_a(x, Y, dY), "+-", find_da(x, dY))
       print("b=", find_b(Y, a, x, dY), "+-", find_db(x, dY))
       print("chi2=", find_chi2(Y, a, b, x, dY))
       print("chi2_reduced=", find_chi2red(chi, x))
       my_x = np.array(x)
       my_y = np.array(Y)
       d = a * my_x + b
       my_x_errey = np.array(Dx)
       my_y_errey = np.array(dY)

       y = d
       plt.errorbar(my_x, my_y, yerr=my_y_errey, xerr=my_x_errey, fmt='none', ecolor='b')
       plt.plot(my_x, y, "r")
       plt.xlabel(x_lable)
       plt.ylabel(y_lable)
       plt.show()
       plt.savefig("linear_fit.svg")
       my_file.close()
