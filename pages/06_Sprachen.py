import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from streamlit_plotly_events import plotly_events
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("pages", "data")

#file location paths:
style = "data/style.css"  # online version
#style = dir_path + "\data\style.css" # offline version
#overview = dir_path + "\data\overview.csv"
overview = "data/overview.csv"
diss_lang = "data/diss_lang.json"

logo = "https://files.dnb.de/DFG-Viewer/DNB-Logo-Viewer.jpg"
st.set_page_config(page_title='DNBVIS_frodiss', page_icon = logo) # , layout = 'wide')

def local_css(file):
        with open(file) as f:
                st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css(style)


# ---- SIDEBAR ----- 
overview = pd.read_csv(overview, sep=';', encoding="utf-8")
complete = int(overview['records_all'].values[-1])
used =  int(overview['records_hss'].values[-1])   #301670
timestamp = overview['timestamp'].values[-1]
update = overview['update'].values[-1]

with st.sidebar:
        
        st.write("Datensätze im Set: ", complete)     
        st.write("Stand der Daten: ", timestamp)
        st.write("Zuletzt aktualisiert: ", update)
        st.markdown('#') 
        st.markdown('#') 
        
        st.write("[DNBVIS_frodiss auf GitHub](https://github.com/deutsche-nationalbibliothek/dnbvis_frodiss)")
        
#--------------        
    
    
    
stats = pd.read_json(diss_lang)
stats = stats[(stats.name != "Ohne Sprache") & (stats.name != "Nicht zu entscheiden") & (stats.name != "Einzelne andere Sprachen")]

main_lang = stats.copy()
main_lang.loc[main_lang['counts'] < 500, 'name'] = 'Andere Sprachen'  
main_lang = main_lang.groupby('name')['counts'].sum().reset_index()

other_lang = stats.copy()
other_lang = other_lang[other_lang.counts < 500]

st.subheader("Übersicht Sprachen") 

st.write('In der ersten Darstellung werden nur Sprachen mit mehr als 500 Titlen im Datenset ausgewiesen. Sprachen mit weniger als 500 Datensätzen '
         ' sind als "Andere Sprachen" zusammengefasst. Mehr Informationen zu diesen Sprachen finden Sie weiter unten in der zweiten Darstellung.')
st.info("Bewegen Sie den Mauszeiger auf ein Tortenstück, um weitere Informationen zu erhalten. "
        "Scrollen Sie nach unten, um eine Aufschlüsselung der Einträge unter 'Andere Sprachen' zu betrachten.")

fig_s1 = px.pie(main_lang, values='counts', labels='name', names='name', height=600, color_discrete_sequence=px.colors.sequential.RdBu)
fig_s1.update_traces(textinfo='label+percent', hovertemplate = "Sprache: %{label} <br>Anzahl: %{value} <br>Anteil: %{percent}")
st.plotly_chart(fig_s1, use_container_width=True)

#selected_points = plotly_events(fig_s1)
#a=selected_points[0]
#selection = a['pointNumber']

st.write('In dieser zweiten Darstellung wird das Verhältnis "Anderer Sprachen" zueinander visualisiert: ')
st.info('Durch Klicken auf einzelne Sprachen in der Legende können diese aus der Darstellung ausgeschlossen werden.')
fig_s2 = px.pie(other_lang, values='counts', labels='name', names='name', height=650, color_discrete_sequence=px.colors.diverging.Portland)
fig_s2.update_traces(textinfo='label+percent', rotation=180, showlegend=True, textposition="inside", hovertemplate = "Sprache: %{label} <br>Anzahl: %{value} <br>Anteil: %{percent}")
st.plotly_chart(fig_s2, use_container_width=False)

st.write(" ")
st.write(" ")
st.markdown(" ##### Informationen zu dieser Visualisierung") 
st.markdown("In dieser Übersicht konnten lediglich 13 der 295.199 Datensätze nicht angezeigt werden. Grund dafür ist, dass die Datensätze keinen entsprechenden Eintrag "
           " im Sprachenfeld enthalten (5 Datensätze) oder um Einträge der Kategorie 'und - nicht zu entscheiden' (8 Datensätze) handelt. Einträge unter den beiden "
            " Sprachencodes 'mis - einzelne andere Sprachen' sowie 'mul - Mehrere Sprachen' werden dargestellt, können aber aufgrund der Erfassung nicht weiter "
            " aufgeschlüsselt werden." )



