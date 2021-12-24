import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from eda_app import run_eda_app
from main import run_main_app
from search_app import run_search_app

def main():
    menu = ['펭귄','Data EDA','검색하기' ]
    choice = st.sidebar.selectbox('메뉴 선택',menu)

    if choice == '펭귄':
        run_main_app()
    elif choice == 'Data EDA':
        run_eda_app()

    elif choice == '검색하기':
        run_search_app()



if __name__ == '__main__':
    main()