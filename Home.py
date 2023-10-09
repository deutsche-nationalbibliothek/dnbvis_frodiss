import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

#file location paths:
style = \data\style.css  # online version
#style = dir_path + "\data\style.css" # offline version
#overview = dir_path + "\data\overview.csv"
overview = \data\overview.csv


logo = "https://files.dnb.de/DFG-Viewer/DNB-Logo-Viewer.jpg"
st.set_page_config(page_title='DNBVIS_frodiss', page_icon = logo) # , layout = 'wide')

def local_css(file):
        with open(file) as f:
                st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#last update: 02-10-2023

local_css(style)


# ---- SIDEBAR ----- 
overview = pd.read_csv(overview, sep=';', encoding="utf-8")
complete = int(overview['records_all'].values[-1]) #311607
used =  int(overview['records_hss'].values[-1])   
previous_used = int(overview['records_hss'].values[-2])
diss =  int(overview['diss'].values[-1])   
previous_diss = int(overview['diss'].values[-2])
habil =  int(overview['habil'].values[-1])   
previous_habil = int(overview['habil'].values[-2])
timestamp = overview['timestamp'].values[-1]
update = overview['update'].values[-1]

with st.sidebar:
        
        st.write("Datensätze im Set: ", complete)     
        st.write("Stand der Daten: ", timestamp)
        st.write("Zuletzt aktualisiert: ", update)
        st.markdown('#') 
        st.markdown('#') 
        
        st.write("[DNBVIS_frodiss auf GitHub](https://github.com/deutsche-nationalbibliothek/dnbvis_frodiss)")
         
    

# ----- color codes ---------

dnbcolor = ['#FEFEFE', '#2499ff', '#f33930', '#b6c73f', '#ffd44d',
            '#3cb8f6', '#f9852e', '#e3d98f', '#000000', '#01be00']
testcolor = ['#ff6900', '#fcb900', '#7bdcb5', '#00d084', '#8ed1fc',
            '#0693e3', '#abb8c3', '#eb144c', '#f78da7', '#9900ef']

#st.header('"Freie Online-Hochschulschriften" in der DNB')
st.markdown('''
                <p style="font-size:34px; margin-bottom:0px"><b> "Freie Online-Hochschulschriften" in der DNB </b></p>
                <p style="font-size:22px; margin-bottom:3px; margin-top:5px"> von Stephanie Palek </p><p style="font-size:19px"> unter Leitung von Dr. Kurt Schneider </p>
                <br> 
               ''',
       unsafe_allow_html=True,
    )


st.markdown("Informationen zur Datengrundlage: "
         " Die hier gezeigten Visualisierungen basieren auf Titeldaten der [Deutschen Nationalbibliothek](https://www.dnb.de). Hierfür wurde das Datenset "
         ' "Freie Online-Hochschulschriften" aus dem [DNBLab](https://www.dnb.de/dnblabsets) genutzt, welches die bibliographischen Metadaten all jener ' 
         ' Online-Hochschulschriften enthält, die ohne Zugriffsbeschränkung '
         " über den [Katalog der DNB](https://portal.dnb.de) aufgerufen werden können. ")

st.write("Informationen zu den einzelnen Visualisierungen finden Sie unter den jeweiligen Darstellungen. "
         ' Weitere Informationen zur Anwendung finden Sie unter dem Menüpunkt "Über DNBVIS_frodiss". ')

st.write(" Das Datenset wird alle 4 Monate aktualisiert. Entsprechend aktuell sind die gezeigten Auswertungen. ")
          
st.write("")

conv_used = f'{used:,}'
conv1_used = conv_used.replace(',', '.')

growth = used-previous_used
conv_growth = f'{growth:,}'
conv1_growth = conv_growth.replace(',', '.')
update = conv1_growth + ' (seit der letzten Aktualisierung hinzugekommen)'



delta_diss = diss - previous_diss
conv_diss = f'{diss:,}'
conv1_diss = conv_diss.replace(',', '.')
conv_delta_diss = f'{delta_diss:,}'
conv1_delta_diss = conv_delta_diss.replace(',', '.')

delta_habil = habil - previous_habil
conv_habil = f'{habil:,}'
conv1_habil = conv_habil.replace(',', '.')
conv_delta_habil = f'{delta_habil:,}'
conv1_delta_habil = conv_delta_habil.replace(',', '.')

other_current = 44
other_112022 = 44
other_062022 = 44
other_previous = other_112022
delta_other = other_current-other_previous
conv_other_current = f'{other_current:,}'
conv1_other_current = conv_other_current.replace(',', '.')
conv_delta_other = f'{delta_other:,}'
conv1_delta_other = conv_delta_other.replace(',', '.')
       
  
st.metric(label="Anzahl Hochschulschriten im Set", value=conv1_used, delta=update)

st.write(" ")
st.write(" ")
st.write("Darin enthalten:")

one, two, three = st.columns(3)
one.metric(label="Dissertationen", value=conv1_diss, delta=conv1_delta_diss)
two.metric(label="Habilitationen", value=conv1_habil, delta=conv1_delta_habil)
three.metric(label="Andere Hochschulschriften", value=conv1_other_current)
