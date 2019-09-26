# 그래프 그리기
# 함수 준비
import pandas as pd
import numpy as np
import platform
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 사용하기
path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')

plt.rcParams['axes.unicode_minus'] = False

# 대전시 미세먼지 1
daejeon1 = pd.read_csv('Data/',
                       encoding = 'euc-kr')

daejeon1