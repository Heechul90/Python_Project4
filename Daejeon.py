import numpy as np
import pandas as pd


# 데이터 불러오기

raw_data = pd.read_csv('Data/Daejeon.csv',
                       encoding = 'euc-kr')
data = raw_data.copy()
data.head()

data['location'] =  data['location'].map({'UND' : 0,
                                          'DSD' : 1,
                                          'GSD' : 2,
                                          'JLD' : 3,
                                          'MCD' : 4,
                                          'MPD' : 5,
                                          'NED' : 6,
                                          'SND' : 7,
                                          'UND' : 8,
                                          'WPD' : 9})

data['SO2'] = data['SO2'].fillna(data['SO2'].mean())
data['SO2'] = data['SO2'].fillna(0)
data['PM10'] = data['PM10'].fillna(0)
data['O3'] = data['O3'].fillna(0)
data['NO2'] = data['NO2'].fillna(0)
data['CO'] = data['CO'].fillna(0)
data['PM25'] = data['PM25'].fillna(0)

data

def MinMaxScaler(data1):
    numerator = data1 - np.min(data1, 0)
    denominator = np.max(data1, 0) - np.min(data1, 0)
    return numerator / (denominator + 1e-7), np.min(data1, 0), np.max(data1, 0)

data1 = np.reshape(data[:, 2:], [-1, 25, 6, 1])