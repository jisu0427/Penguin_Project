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



    