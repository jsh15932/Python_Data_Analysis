# 패키지 가져오기

%matplotlib inline

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

mpl.rcParams['axes.unicode_minus'] = False

# 데이터 생성

import numpy as np

data = np.random.randint(-100, 100, 50).cumsum()
data

# 한글 폰트 사용 

plt.plot(range(50), data, 'r')
mpl.rcParams['axes.unicode_minus'] = False
plt.title('시간별 가격 추이')
plt.ylabel('주식 가격')
plt.xlabel('시간(분)')

# matplotlib 버전, 위치정보

print('버전: ', mpl.__version__)
print('설치 위치: ', mpl.__file__)
print('설정 위치: ', mpl.get_configdir())
print('캐시 위치: ', mpl.get_cachedir())

print('설정파일 위치: ', mpl.matplotlib_fname())

# 설치된 폰트 확인

font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')

print(len(font_list))