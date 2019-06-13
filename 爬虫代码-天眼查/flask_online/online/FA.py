# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import math
from sklearn.decomposition import FactorAnalysis
from factor_analyzer import Rotator
import copy
# select:基于特征根贡献率Eigenvalue/因子数量n_components， subselect：特征根大于/提取因子个数
NAME = 'Factor_Analysis'
CLASS = 'Preprocessing'


def extract(x):
    y = [int(xx) for xx in x.split(',')]
    return y


Ind = '0,1,2,3,4,5'
# 读取数据

data = pd.read_excel("example.xlsx")
data.describe()
# fit_transform=fit+transform
fa = FactorAnalysis(n_components=2)
data_two_dim = fa.fit_transform(data)

# test1=fa.fit(data)
# test2=fa.transform(data)
# test3=fa.get_covariance()
# test4=fa.get_params()
# test5=fa.get_precision()
# test6=fa.score(data)
# test7=fa.score_samples(data)

# 获取相应的列
print("因子分析原始数据为 ", data)
col = data.columns
#  取出数据转换为dataframe类型
# !!!!!!!!!!!!!!!!原程序是从1取得，本处改为从0开始取!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111
data = pd.DataFrame(data[0:len(data)], columns=col)
#  尝试强制转换为数字（包括字符串），并且不可转换的值将变为NaN
data = data.convert_objects(convert_numeric=True)
#  将表头变为list
labels = list(data.columns)
#  将传过来需要处理的列从str转化为int
ind = extract(Ind)
#  拿出数据对应的列名称
xlabel = [labels[i] for i in ind]
#  取出相应的列
data0 = data[xlabel]
#  获取到有几列
N = data0.shape[1]
# 步骤一、样本标准化  StandardScaler()标准化数据，保证每个维度的特征数据方差为1，均值为0，使得预测结果不会被某些维度过大的特征值而主导
scaler = StandardScaler()
#  transform()数据标准化
data = scaler.fit_transform(data0)
#  data类型为<class 'numpy.ndarray'>转化为dataframe类型
data = pd.DataFrame(data, columns=data0.columns)
print("标准化后的数据为 \n", data)
# 步骤二、计算样本离差矩阵
# 2.1 计算每一列的平均值
data_mean = data.mean()
#  构造[[0,0,...],[0,0,...],...]
E = np.mat(np.zeros((N, N)))
#  2.2计算样本离差矩阵
for i in range(len(data)):

    E += (data.iloc[i, :].values.reshape(N, 1) - data_mean.values.reshape(N, 1)) * \
        (data.iloc[i, :].values.reshape(1, N) - data_mean.values.reshape(1, N))
# 将列平均值证转换1行N列
data_mean.values.reshape(1, N)
# 步骤三、计算相关性矩阵
#  样本的自相关矩阵  corr()计算列的成对相关性，不包括NA /空值
# Fins1
# 因子抽取选项choic,choic == 'corr'时采用相关系数，choic == 'cov'时采用协方差。
choic = 'corr'
if choic == 'corr':
    R = data.corr()
    # 相关系数
else:
    R = data.cov()
# 协方差
# Fins1_end
#  求特征值eig_value，特征向量eig_vector
eig_value, eig_vector = np.linalg.eig(R)
print("特征根和特征向量\n", eig_value, eig_vector)
eig = pd.DataFrame()
eig['names'] = data.columns
eig['eig_value'] = eig_value
#  降序排序
eig.sort_values('eig_value', ascending=False, axis=0, inplace=True)
eig['eig_num'] = eig.index
#  根据特征值进行降序排序,返回dataframe
eig = eig.reset_index(drop=True)
#  取出eig的行索引
eig_num = eig['eig_num']


#  构造N行一列的二维数组
ratio_contribution = np.zeros((N, 1))
sum_ratio_contribution = np.zeros((N, 1))
#  ratio_contribution特征值占比   sum_ratio_contribution所在行之前所占比例
for i in range(1, N):
    print("eig['eig_value'][i - 1] is", eig['eig_value'][i - 1])
    print(" eig['eig_value'].sum() is", eig['eig_value'].sum())
    print("eig['eig_value'][:i].sum() is", eig['eig_value'][:i].sum())
    print(" eig['eig_value'].sum() is", eig['eig_value'].sum())
    ratio_contribution[i - 1, 0] = eig['eig_value'][i - 1] / \
        eig['eig_value'].sum()
    sum_ratio_contribution[i - 1,
                           0] = eig['eig_value'][:i].sum() / eig['eig_value'].sum()
# 重新构造dataframe
Contribution = pd.DataFrame(ratio_contribution, columns=[u'因子贡献率'])
Contribution.insert(1, u'累计贡献率', sum_ratio_contribution)
# Contribution.insert(0, u'列名', eig['names'])
my_list = []
for i in range(len(Ind.split(','))):
    a = 'F_' + str(i + 1)
    my_list.append(a)
# Contribution.insert(0, u'列名', eig['names'])
Contribution.insert(0, u'列名', pd.DataFrame(my_list))
#  构造xy
d = {'name': 'Index', 'value': list(range(N + 1)[1:])}
d1 = {'name': 'original data', 'value': eig['eig_value'].tolist()}
l = []
l.append(d1)
result_dict = {'x': d,
               'Y': l}
#  因子分析选择对应参数
select = 'n_components'
subselect = 2
m = 0
my_m = -1
if select == 'n_components':
    if subselect > len(ind):
        subselect = len(ind)
    m = subselect
    my_m = subselect
elif select == 'Eigenvalue':
    for i in range(N):
        if eig['eig_value'][i] >= subselect:
            my_m = i + 1
            for i in range(1, N + 1):
                if sum_ratio_contribution[i - 1, 0] >= 1.0:
                    m = i
                    break
# 根据特征向量取出特征值
weight = ratio_contribution[0:m]
#  构造n行m列的二维数组
A = np.zeros((N, m))
#  根据参数拿出对应的 特征值的平方*特征向量
# 因子载荷矩阵
for i in range(0, m):
    A[:, i] = math.sqrt(eig_value[eig_num[i]]) * eig_vector[:, eig_num[i]]
# 重新生成矩阵载荷矩阵(成分矩阵)，对应成分（载荷）矩阵，为什么取ma而不直接用a呢？？？？？？？？？？？？？？？？
a = (pd.DataFrame(A))
ma = -(pd.DataFrame(A))
a_list = []
ma_list = []
for i in range(int(len(a.columns.tolist()))):
    q = 'F_' + str(i + 1)
    a_list.append(q)
    ma_list.append(q)
a.columns = a_list
ma.columns = ma_list
a.index = xlabel
ma.index = xlabel
component_matrix = copy.deepcopy(ma)
component_matrix.insert(0, u'列名', ma.index)
#  样本的相关系数矩阵，旋转成分矩阵，重点需要看的地方！！！！！！！！！！！！！！！！！
# 如果rowvar是1（默认），那么每行代表一个variables，每列代表一个observations（样本）；反之则每行是observations，每列是variables
covr = np.corrcoef(data, rowvar=0)  # 计算相关系数矩阵
covrr = pd.DataFrame(covr)


rotator = Rotator()
test1 = covrr.T
test2 = test1.T
covrr = covrr.T.values.tolist()
covrr = rotator.rotate(pd.DataFrame(covrr), 'varimax')
covrr = pd.DataFrame(list(covrr)[0].values.tolist())
# 因子得分系数矩阵，对应成分得分矩阵
b = np.dot(np.linalg.inv(covr), a)
score_matrix = pd.DataFrame(b)
# rotate stop
b_list = []
for i in range(int(len(score_matrix.columns.tolist()))):
    q = 'F_' + str(i + 1)
    b_list.append(q)
score_matrix.columns = b_list
score_matrix.insert(0, u'列名', a.index)
# 模型结果
tran_data = np.dot(data, b)
integrated_score = np.dot(tran_data, weight)
result_data = pd.DataFrame(tran_data)
c_list = []
for i in range(int(len(result_data.columns.tolist()))):
    q = 'F_' + str(i + 1)
    c_list.append(q)
result_data.columns = c_list
result_data = pd.concat([data0, result_data], axis=1)
result_data.insert(N + m, u'综合得分因子', integrated_score.ravel())

NoFac = [u'没有符合条件的因子'] + ['0' for i in range(1000001)]
title1 = list(Contribution.columns)
title2 = list(component_matrix.columns)
title3 = list(score_matrix.columns)
title4 = list(result_data.columns)

output = {}
output["function_name"] = NAME
output["function_class"] = CLASS
# 载荷矩阵
if my_m == -1:
    output["result_validation_1"] = [['没有符合条件的因子']]
else:
    output["result_validation_1"] = pd.DataFrame(
        ([title1] + Contribution.values.tolist())[:int(my_m) + 1]).T.values.tolist()
# output["result_validation_2"] = [title2] + component_matrix.fillna('nan').values.tolist()
if my_m == -1:
    output["result_validation_2"] = [['没有符合条件的因子']]
else:
    output["result_validation_2"] = pd.DataFrame(
        ([title2] + component_matrix.fillna('nan').values.tolist())).iloc[:,
                                                                          :int(my_m) + 1].values.tolist()  # 载荷矩阵

if int(subselect) > 1 or select == 'Eigenvalue':
    from factor_analyzer import Rotator

    rotator = Rotator()
    rotate_mtx = rotator.rotate(pd.DataFrame(
        component_matrix.T[1:].T.values.tolist()), 'varimax')
    rotate_mtx = pd.DataFrame(list(rotate_mtx)[0].values.tolist())
    rotate_mtx.insert(0, u'列名', a.index)
    rml = rotate_mtx.fillna('nan').values.tolist()
    n_rml = []
    for row in rml:
        row = row[:2] + row[2:3] + row[3:4] + row[4:]
        n_rml.append(row)
    # output["xuanzhuan"] = ([title2] + n_rml)
    if my_m == -1:
        output["xuanzhuan"] = [['没有符合条件的因子']]
    else:
        output["xuanzhuan"] = pd.DataFrame(
            ([title2] + n_rml)).iloc[:, :int(my_m) + 1].values.tolist()
else:
    output["xuanzhuan"] = [['因子固定数量小于1，无法进行因子旋转']]
if my_m == -1:
    output["result_validation_3"] = [['没有符合条件的因子']]
else:
    output["result_validation_3"] = pd.DataFrame(
        [title3] + score_matrix.values.tolist()).iloc[:, :int(my_m) + 1].T.values.tolist()  # 得分矩阵
# my_result_data = result_data
my_result_data = copy.deepcopy(result_data)
my_result_data.insert(0, '序号', result_data.index.tolist())
output["result_data"] = [my_result_data.columns.tolist(
)] + my_result_data.fillna('nan').values.tolist()  # 模型结果
output[u"DRAW_DATA"] = result_dict
from sklearn.cluster import KMeans

for i in range(2, 10):
    clf = KMeans(n_clusters=i)
    clf.fit(output)
    #    print(clf.cluster_centers_)#类中心
    print(i, clf.inertia_)  # 用
