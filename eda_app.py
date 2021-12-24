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
    st.markdown('- culmen_length_mm: 펭귄 부리의 길이 (mm)')
    st.markdown('- culmen_depth_mm: 펭귄 부리의 깊이 (mm)')
    st.markdown('- flipper_length_mm: 펭귄 지느러미의 길이 (mm)')
    st.markdown('- body_mass_g: 펭귄의 체질량 (g)')
    st.markdown('- Sex: 펭귄의 성별')


    ### DataFrame ###
    st.subheader('DataFrame')
    df = pd.read_csv('data/penguins.csv',index_col=0)
    radio_menu = ['데이터프레임', '통계치' ]
    selected_radio = st.radio('선택하세요', radio_menu)

    if selected_radio == '데이터프레임' :
        st.dataframe(df)
    elif selected_radio == '통계치' :
        st.dataframe( df.describe() )


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

    # 유저가 컬럼을 선택하면, 
    # 해당 컬럼의 min과 max에 해당하는 사람이 누구인지
    # 그 사람의 데이터를 화면에 보여주는 기능 개발

    ### 문자열 데이터가 아닌, 컬럼들만 가져오는 코드!!! ###
    st.subheader('최대 최소에 해당되는 펭귄 정보 찾기')
    print( df.columns )
    print( df.dtypes != object )
    print( df.columns[ df.dtypes != object ] )

    number_colums = df.columns[ df.dtypes != object ] 

    selected_minmax_column = st.selectbox('컬럼 선택', number_colums)

    # 선택한 컬럼의 최소값에 해당되는 사람의 데이터 출력
    # df[selected_minmax_column] == df[selected_minmax_column].min()
    st.text('MIN')
    min_data = df.loc[ df[selected_minmax_column] == df[selected_minmax_column].min() , ]
    st.dataframe(min_data)

    # 선탁한 컬럼의 최대값에 해당되는 사람의 데이터 출력
    # df[selected_minmax_column] == df[selected_minmax_column].max()
    st.text('MAX')
    max_data = df.loc[ df[selected_minmax_column] == df[selected_minmax_column].max()  , ]
    st.dataframe(max_data)







