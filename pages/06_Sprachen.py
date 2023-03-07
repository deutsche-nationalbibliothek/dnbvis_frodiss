import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from streamlit_plotly_events import plotly_events

logo = "https://files.dnb.de/DFG-Viewer/DNB-Logo-Viewer.jpg"
st.set_page_config(page_title='DNBVIS_frodiss', page_icon = logo) # , layout = 'wide')
complete = 295756

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
complete = 295756
used = 295199

with st.sidebar:
        
        st.write("Datensätze im Set: ", complete)     
        st.write("Stand der Daten: 03.11.2022")
        st.write("Zuletzt aktualisiert: 07.03.2023")
        st.markdown('#') 
        st.markdown('#') 
        
        
        github_logo_black = "GitHub_Logo.png"
        github_logo_white = "GitHub_Logo_white.png"
        
        with st.container():
                column1, column2 = st.columns(2)
                
                column1.write("[DNBVIS_frodiss auf GitHub](https://github.com/deutsche-nationalbibliothek/dnbvis_frodiss)")
                column2.markdown('<style>img {width: 75px; display: block; margin-left: auto; margin-right: auto; margin-top: 10px;}</style><a href="https://github.com/deutsche-nationalbibliothek/dnbvis_frodiss", target="new"><img src="https://raw.githubusercontent.com/deutsche-nationalbibliothek/dnbvis_frodiss/main/GitHub_Logo.png"></a>', unsafe_allow_html=True)
                
#--------------        
    
    
    
stats = pd.read_json("data/diss_lang.json")
stats = stats[(stats.name != "Ohne Sprache") & (stats.name != "Nicht zu entscheiden") & (stats.name != "Einzelne andere Sprachen")]

main_lang = stats.copy()
main_lang.loc[main_lang['counts'] < 500, 'name'] = 'Andere Sprachen'  
main_lang = main_lang.groupby('name')['counts'].sum().reset_index()

other_lang = stats.copy()
other_lang = other_lang[other_lang.counts < 500]

st.subheader("Übersicht Sprachen") 

st.write('In der ersten Darstellung werden nur Sprachen mit mehr als 500 Titlen im Datenset ausgewiesen. Sprachen mit weniger als 500 Datensätzen '
         ' sind als "Andere Sprachen" zusammengefasst. Mehr Informationen zu diesen Sprachen finden Sie weiter unten in der zweiten Darstellung.')
         
st.info("Bewegen Sie den Mauszeiger auf ein Tortenstück, um weitere Informationen zu erhalten.")

fig_s1 = px.pie(main_lang, values='counts', labels='name', names='name', height=600, color_discrete_sequence=px.colors.sequential.RdBu)
fig_s1.update_traces(textinfo='label+percent', hovertemplate = "Sprache: %{label} <br>Anzahl: %{value} <br>Anteil: %{percent}")
st.plotly_chart(fig_s1, use_container_width=True)


#selected_points = plotly_events(fig_s1)
#a=selected_points[0]
#selection = a['pointNumber']

#if selection == 0:
st.write('In dieser zweiten Darstellung wird das Verhältnis "Anderer Sprachen" zueinander visualisiert: ')
fig_s2 = px.pie(other_lang, values='counts', labels='name', names='name', height=600, color_discrete_sequence=px.colors.sequential.RdBu)
fig_s2.update_traces(textinfo='label+percent', rotation=180, showlegend=True, textposition="inside", hovertemplate = "Sprache: %{label} <br>Anzahl: %{value} <br>Anteil: %{percent}")
st.plotly_chart(fig_s2, use_container_width=False)
#else:
#        st.write("Keine weitere Untergliederung vorhanden.")


st.write(" ")
st.write(" ")
st.markdown(" ##### Informationen zu dieser Visualisierung") 
st.markdown("In dieser Übersicht konnten lediglich 13 der 295.199 Datensätze nicht angezeigt werden. Grund dafür ist, dass die Datensätze keinen entsprechenden Eintrag "
           " im Sprachenfeld enthalten (5 Datensätze) oder um Einträge der Kategorie 'und - nicht zu entscheiden' (8 Datensätze) handelt. Einträge unter den beiden "
            " Sprachencodes 'mis - einzelne andere Sprachen' sowie 'mul - Mehrere Sprachen' werden dargestellt, können aber aufgrund der Erfassung nicht weiter "
            " aufgeschlüsselt werden." )



