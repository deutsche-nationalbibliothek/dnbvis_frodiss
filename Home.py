import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

logo = "https://files.dnb.de/DFG-Viewer/DNB-Logo-Viewer.jpg"
st.set_page_config(page_title='DNBVIS_frodiss', page_icon = logo) # , layout = 'wide')

#last update: 21-03-2023

st.markdown(
        """
        <style>
           [data-testid="stSidebarNav"]{
                height: 450px;
                background-image: url(https://files.dnb.de/DFG-Viewer/DNB-Logo-Viewer.jpg);
                background-repeat: no-repeat;
                background-position: 25px 25px;
                }
           [data-testid="stSidebarNav"]::before{
                content: "DNBVIS_frodiss";
                font-size: 25px;
                top: 90px;
                margin-left: 25px;
                position: relative;
                }
           .css-wjbhl0{
                max-height: 450px;
                padding-top: 125px;
                height: 400px;
                }
           .css-hied5v{
                max-height: 450px;
                padding-top: 125px;
                height: 400px;
                }
           [data-testid=stSidebar]:nth-of-type(1) [data-testid=stVerticalBlock]{
                 gap: 0rem;
                }
           [data-testid=stSidebar] [data-testid=stImage]{
                text-align: center;
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 100%;
                }
            [data-testid=stSidebar] a:link{
                text-decoration: none;
                color: black
                }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ---- SIDEBAR ----- 
overview = pd.read_csv("data/overview.csv", sep=';', encoding="utf-8")
complete = int(overview['records_all'].values[-1])
used =  int(overview['records_hss'].values[-1])   #301670

with st.sidebar:
        
        st.write("Datensätze im Set: ", complete)     
        st.write("Stand der Daten: 16.03.2023")
        st.write("Zuletzt aktualisiert: 21.03.2023")
        st.markdown('#') 
        st.markdown('#') 
        
        
        github_logo_black = "GitHub_Logo.png"
        github_logo_white = "GitHub_Logo_white.png"
        
        with st.container():
                column1, column2 = st.columns(2)
                
                column1.write("[DNBVIS_frodiss auf GitHub](https://github.com/deutsche-nationalbibliothek/dnbvis_frodiss)")
                column2.markdown('<style>img {width: 75px; display: block; margin-left: auto; margin-right: auto; margin-top: 10px;}</style><a href="https://github.com/deutsche-nationalbibliothek/dnbvis_frodiss", target="new"><img src="https://raw.githubusercontent.com/deutsche-nationalbibliothek/dnbvis_frodiss/main/GitHub_Logo.png"></a>', unsafe_allow_html=True)
                
        
    
    
    

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

st.dataframe(overview)

all_ofd = used
all_ofd_11_2022 = 295199
conv_ofd = f'{all_ofd:,}'
conv1_ofd = conv_ofd.replace(',', '.')

growth = all_ofd-all_ofd_11_2022
conv_growth = f'{growth:,}'
conv1_growth = conv_growth.replace(',', '.')
update = conv1_growth + ' (seit der letzten Aktualisierung hinzugekommen)'


diss_032023 = 298540
diss_112022 = 292161
delta_diss = diss_032023 - diss_112022
conv_diss_032023 = f'{diss_032023:,}'
conv1_diss_032023 = conv_diss_032023.replace(',', '.')
conv_delta_diss = f'{delta_diss:,}'
conv1_delta_diss = conv_delta_diss.replace(',', '.')

habil_032023 = 3089
habil_112022 = 2994 
habil_062022 = 2896
delta_habil = habil_032023 - habil_112022
conv_habil_032023 = f'{habil_032023:,}'
conv1_habil_032023 = conv_habil_032023.replace(',', '.')
conv_delta_habil = f'{delta_habil:,}'
conv1_delta_habil = conv_delta_habil.replace(',', '.')

other_112022 = 44
other_062022 = 44
delta_other = other_112022-other_062022
conv_other_112022 = f'{other_112022:,}'
conv1_other_112022 = conv_other_112022.replace(',', '.')
conv_delta_other = f'{delta_other:,}'
conv1_delta_other = conv_delta_other.replace(',', '.')
       
  
st.metric(label="Anzahl Hochschulschriten im Set", value=conv1_ofd, delta=update)

st.write(" ")
st.write(" ")
st.write("Darin enthalten:")

one, two, three = st.columns(3)
one.metric(label="Dissertationen", value=conv1_diss_032023, delta=conv1_delta_diss)
two.metric(label="Habilitationen", value=conv1_habil_032023, delta=conv1_delta_habil)
three.metric(label="Andere Hochschulschriften", value=conv1_other_112022)
