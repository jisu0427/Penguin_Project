import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from PIL import Image
import random

def run_information_app():
    # 1. 자료 출처
    st.markdown('자료 출처 : https://github.com/allisonhorst/palmerpenguins')
    # 2. 내 깃허브 주소
    st.markdown('My Github : https://github.com/jisu0427/My_Project')