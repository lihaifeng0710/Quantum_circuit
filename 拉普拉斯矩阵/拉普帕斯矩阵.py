import pandas as pd
import numpy as np

def excel_one_line_to_list():
    df=pd.read_excel("E:\Pycharm-workspace\量子电路\拉普拉斯矩阵.xlsx")
    df.columns=["0","1","2","3","4","5","6","7","8","9"]
    x=df[["1","2","3","4","5","6","7","8","9"]]
    x=np.array(x)
    return x
def Degree_matrix():
    x=excel_one_line_to_list()
    sum=np.sum(x,axis=0);#每一列的和
    du=np.full((9,9),0)
    for i in range(len(x)):
        du[i][i] = sum[i]
    return du

def Laplacian_matrix():
    A=excel_one_line_to_list()
    D=Degree_matrix()
    lpls=A-D
    return lpls

if __name__ =='__main__':
    print("----------邻接矩阵为------------")
    print(excel_one_line_to_list())
    print("----------度矩阵为--------------")
    print(Degree_matrix())
    print("---------拉普帕斯矩阵为-----------")
    print(Laplacian_matrix())


