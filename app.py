import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from eda_app import run_eda_app
from main import run_main_app

def main():
    menu = ['펭귄','Data EDA','데이터 분석' ]
    choice = st.sidebar.selectbox('메뉴 선택',menu)

    if choice == '펭귄':
        run_main_app()
    elif choice == 'Data EDA':
        run_eda_app()

    elif choice == '데이터 분석':
        pass

    elif choice == '데이터 모델링':
        pass

if __name__ == '__main__':
    main()