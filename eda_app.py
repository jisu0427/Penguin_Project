import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda_app():
    st.markdown('# Palmer Penguins Data EDA')

    ### Data colums Markdown syntax ###
    st.subheader('데이터 컬럼명 설명')
    st.markdown('- Species: 펭귄의 종 (Chinstrap, Adelie, or Gentoo)')
    st.markdown('- Island: 펭귄이 발견되는 남극 섬 (Dream, Torgersen, or Biscoe) ')
    st.markdown('- bill_length_mm: 펭귄 부리의 길이 (mm)')
    st.markdown('- bill_depth_mm: 펭귄 부리의 깊이 (mm)')
    st.markdown('- flipper_length_mm: 펭귄 지느러미의 길이 (mm)')
    st.markdown('- body_mass_g: 펭귄의 체질량 (g)')
    st.markdown('- Sex: 펭귄의 성별')


    ### DataFrame ###
    st.subheader('DataFrame')
    df = pd.read_csv('data/penguins_size.csv')
    st.dataframe(df)


    # 컬럼별 히스토그램 확인하기
    st.subheader('각 컬럼별 히스토그램 확인')
    # 'Species', 'Island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm','body_mass_g', 'Sex'
    select_columns = st.selectbox('컬럼을 선택하세요', df.columns)
    bins = st.slider('bin의 갯수 조절',min_value=10, max_value=50)
    fig1 = plt.figure()
    df[select_columns].hist(bins = bins)
    st.pyplot(fig1)


    