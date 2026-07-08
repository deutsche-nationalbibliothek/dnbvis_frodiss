import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
#from streamlit_plotly_events import plotly_events
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("pages", "data")

#file location paths:
style = "data/style.css"  # online version
#style = dir_path + "\data\style.css" # offline version
#overview = dir_path + "\data\overview.csv"
overview = "data/overview.csv"
unidata = "data/unidata.json"

logo = "https://files.dnb.de/DFG-Viewer/DNB-Logo-Viewer.jpg"
st.set_page_config(page_title='DNBVIS_frodiss', page_icon = logo) # , layout = 'wide')

def local_css(file):
        with open(file) as f:
                st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css(style)


# ---- SIDEBAR ----- 
overview = pd.read_csv(overview, sep=',', encoding="utf-8")
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
        
#----------------        
    
    


st.subheader("Übersicht Publikationsorte") 

st.write("Klicken Sie auf einen Publikationsort, um einen Link zu den zugehörigen Titeln im Katalog zu generieren.")
st.write("Der Link wird im Anschluss unter der Karte angezeigt.")

df_pub = pd.read_json("data/geoplaces.json", encoding="utf-8")
df_pub = df_pub[df_pub['count'].notna()]
df_pub["lat"] = pd.to_numeric(df_pub["lat"].str.replace(",", "."))
df_pub["long"] = pd.to_numeric(df_pub["long"].str.replace(",", "."))

pub_loc = df_pub.copy()
location = pub_loc["Place"].str.replace(" ","%20")
df_pub["url"] = "https://portal.dnb.de/opac.htm?method=simpleSearch&cqlMode=true&query=catalog=dnb.hss+location=onlinefree+"+location

    
fig3 = px.scatter_map(df_pub, lat="lat", lon="long", hover_name="Place",
                        size="count", color="count", color_continuous_scale=px.colors.cyclical.IceFire, zoom=5, #height=500,
                        labels={
                                        "count": "Anzahl",
                                        "lat":"Latitude",
                                        "lon":"Longitude"
                                             }
                        )
fig3.update_layout(map_style="open-street-map", 
                      map=dict(
                            bearing=0,
                            center=dict(
                                    lat=51.10,
                                    lon=10.27
                                            )),
                   clickmode='event+select'
                        )  
fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig3.update_traces(marker_sizemin = 5, marker_sizeref = 10)

#st.plotly_chart(fig3, use_container_width=True)

select=1000
selected_point = st.plotly_chart(fig3, on_select="rerun", use_container_width=True)
select = selected_point['selection']['point_indices']

if select:
        place = df_pub.iloc[select]['place']
        link1 = df_pub.iloc[select]['url']
        st.write(place)
        st.write(link1)
        st.info(f"Zu den im Set enthaltenen Publikationen aus [{place}](%s)" % link1)
else:
        st.write(" ")
        
        
st.write(" ")
st.write(" ") 
        
st.markdown(" ##### Informationen zu dieser Visualisierung")
st.markdown("Ausschlaggebend für die örtliche Zuordnung ist die Angabe des Publikationsortes, oder, falls diese Information nicht vorhanden war, der Sitz der für die Publikation "
            "verantwortlichen Hochschule. Dieser wurde dem Hochschulschriftenvermerk entnommen. Dies ist möglich, weil freie Online-Hochschulschriften in der Regel auf den "
            " Repositorien der promovierenden bzw. habilitierenden Hochschule veröffentlicht werden und damit der Publikationsort überwiegend auch dem Hochschulstandort entspricht. "
            " Der Fokus dieser Darstellung liegt dabei auf dem Publikationsort, der aber durchaus auch im Ausland liegen kann, sofern bspw. der Verlag seinen Hauptsitz im Ausland hat. ")
st.markdown("Die Ortsangaben wurden anschließend bereinigt und vereinheitlicht. Die so entnommenen Ortsangaben wurden mit Hilfe der [lobid-reconciliation-API](https://lobid.org/gnd/reconcile) " 
            " zunächst mit der GND abgeglichen, um bspw. verschiedene Namensformen zu berücksichtigen. Über die SRU-Schnittstelle der DNB wurden zu den einzelnen "
            " Geografika dann die Koordinaten aus dem Normdatensatz abgerufen, um mit diesen schließlich die Kartendarstellung der Publikationsorte realisiert. ")





