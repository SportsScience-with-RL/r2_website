import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

from graph import parcours_timeline_fr, parcours_timeline_eng
from r2_fr import page_fr
from r2_eng import page_eng

##############################################
#                                            #
#                  SETTINGS                  #
#                                            #
##############################################

page_title = 'R² Training Hub'
page_icon = 'logo/R²_logo.png'
st.set_page_config(layout='wide', page_icon=page_icon, page_title=page_title)

st.markdown(" <style> div[class^='block-container'] { padding-top: 2rem; } </style> ", unsafe_allow_html=True)

@st.cache_data(hash_funcs={dict: lambda _: None}) # hash_funcs because dict can't be hashed
def exp_timeline():
    xp_fig = {}
    xp_fig['xp_timeline_fr'] = parcours_timeline_fr()
    xp_fig['xp_timeline_eng'] = parcours_timeline_eng()

    return xp_fig 

xp_fig = exp_timeline()

##########################################
#                                        #
#                  MAIN                  #
#                                        #
##########################################

c_header = st.columns([.1, .8, .1])
with c_header[1]:
    st.image('logo/R²_band.png')
with c_header[2]:
    eng = st.toggle('English')

if eng:
    page_eng(xp_fig['xp_timeline_eng'])
elif not eng:
    page_fr(xp_fig['xp_timeline_fr'])