#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 데이터를 넘겨주는 데로 알아서 이상치 값을 출력하는 기능
# 메개변수가 두개 있는 함수 만들기
import numpy as np

def outliers_iqr3(data,column):
    
    # percentile() 25%와 75% 시점의 데이터값을 알려줌(return)
    q1,q3 = np.percentile(data[column],[25, 75])
    # iqr값 계산하기
    iqr = q3-q1
    
    # 최대, 최소값 계산하기
    u_bound = q3 + (iqr*1.5)
    l_bound = q1 - (iqr*1.5)
    
    # 이상치 데이터 찾아보기
    df_temp = data[(data[column] > u_bound)|
                   (data[column] < l_bound)]
    print(df_temp)
    print(len(df_temp))
    return

