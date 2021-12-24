import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import joblib

def run_search_app():
    df = pd.read_csv('data/penguins.csv', encoding='ISO-8859-1', index_col=0)
    st.title('펭귄 데이터 검색하기')

    # species	island	culmen_length_mm	culmen_depth_mm	
    # flipper_length_mm	body_mass_g	sex

    
    # 컬럼을 선택하면, 해당 컬럼들만 데이터프레임 표시하는 화면
    print(df.columns)

    selected_columns = st.multiselect('컬럼을 선택하세요', df.columns)
    if len(selected_columns) != 0 :
        st.dataframe( df[selected_columns] )
    else :
        st.write('선택한 컬럼이 없습니다.')


    # 상관관계 분석을 위한, 상관계수 보여주는 화면 개발

    st.subheader('상관계수')
    # st.dataframe( df.corr() )

    df_corr = df.iloc[ : , 2 : -2+1 ]
    
    selected_corr = st.multiselect('상관계수 컬럼 선택', df_corr.columns)

    # 유저가 1개라도 컬럼을 선택했을 경우
    if len(selected_corr) > 0 :
        st.dataframe( df_corr[selected_corr].corr() )

        # 상관계수를 수치로도 구하고, 차트로도 표시하라.
        
        fig1 = sns.pairplot(data=  df_corr[selected_corr] )
        st.pyplot(fig1)
    # 유저가 컬럼을 선택하지 않은 경우
    else :
        st.write('선택한 컬럼이 없습니다.')


    