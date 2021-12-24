import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from eda_app import run_eda_app
from main import run_main_app
from ml_app import run_ml_app

def main():
    menu = ['펭귄','펭귄 데이터 분석하기','펭귄의 성별 예측하기' ]
    choice = st.sidebar.selectbox('메뉴 선택',menu)

    if choice == '펭귄':
        run_main_app()
    elif choice == '펭귄 데이터 분석하기':
        run_eda_app()

    elif choice == '펭귄의 성별 예측하기':
        run_ml_app()



if __name__ == '__main__':
    main()