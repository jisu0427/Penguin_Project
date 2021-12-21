import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
import seaborn as sns 

def main():
    df = pd.read_csv('인천광역시_미세먼지 경보내역_20210909.csv',encoding= 'cp949')
    st.dataframe(df)

if __name__ == '__main__':
    main()