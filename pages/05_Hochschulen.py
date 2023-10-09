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
unidata = "data/unidata.json"

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
        
#----------------        
    
    


st.subheader("Übersicht Hochschulen") 

st.write("Klicken Sie auf eine Hochschule, um einen Link zu den Titeln im Katalog zu generieren.")
st.write("Der Link wird im Anschluss unter der Karte angezeigt.")

df_uni = pd.read_json(unidata, encoding="utf-8")
uni_loc = df_uni["Hochschule"].astype(str)
uni_loc = uni_loc.str.replace(" ","%20")
df_uni["url"] = "https://portal.dnb.de/opac.htm?method=simpleSearch&cqlMode=true&query=catalog=dnb.hss+location=onlinefree+"+uni_loc
    
    
fig4 = px.scatter_mapbox(df_uni, lat="lat", lon="lon", hover_name="Hochschule",
                        size="count", color="count", color_continuous_scale=px.colors.cyclical.Phase, zoom=5, #height=500,
                        labels={
                                        "count": "Anzahl",
                                        "lat":"Latitude",
                                        "lon":"Longitude"
                                             }
                        )
fig4.update_layout(mapbox_style="open-street-map", 
                      mapbox=dict(
                            #accesstoken=mapbox_access_token,
                            bearing=0,
                            center=dict(
                                    lat=51.10,
                                    lon=10.27
                                            )),
                   clickmode='event+select'
                        )  
fig4.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig4.update_traces(marker_sizemin = 5, marker_sizeref = 10)
#st.plotly_chart(fig4, use_container_width=True)

select=1000
selected_points = plotly_events(fig4)

if selected_points: 
        a=selected_points[0]
        select = a['pointNumber']  

if select != 1000:
        uni = df_uni.iloc[select]['Hochschule']
        link2 = df_uni.iloc[select]['url']
        st.info(f"Zu den im Set enthaltenen Hochschulschriften der [{uni}](%s)" % link2)
else:
        st.write(" ")
        
st.write(" ")
st.write(" ") 
        
st.markdown(" ##### Informationen zu dieser Visualisierung")
st.markdown("Die Übersicht Universitäten zeigt die Anzahl der im Datenset enthaltenen Hochschulschriften nach verantwortlicher Hochschule. Die "
           "hierzu benötigten Informationen wurden aus dem Feld 'Hochschulschriftenvermerk' entnommen. Da die Angabe der Hochschule in diesem Feld jedoch "
           "nicht normiert ist, musste eine automatisierte Datenbereinigung sowie Zuordnung vorgenommen werden. Das Set enthält weit überwiegend Daten zu "
           "Dissertationen sowie Habilitationen, weshalb die angegebenen Hochschulen mit einer Liste der Hochschulen in Deutschland, die über "
           "das Promotionsrecht verfügen, abgeglichen wurden (Liste  von [hochschulkompass.de](https://www.hochschulkompass.de/home.html), verantwortet durch die Hochschulrektorenkonferenz)."
           " Der Abgleich erfolgt über Schlüsselbegriffe bzw. Schlüsselphrasen, da im Hochschulschriftenvermerk "
           "häufig nicht der offizielle Name der jeweiligen Institution angegeben ist, sondern lediglich ein Ortsname sowie Abkürzungen wie bspw. 'Uni.', "
           " 'Hochsch.', etc. Meist lässt sich auf diese Art eine eindeutige Identifizierung vornehmen, eine geringe Fehlerquote ist möglich. "
           " Auch wurden in geringem Umfang Schätzungen aufgrund von Stichproben genutzt: so wurden bspw. die glücklicherweise wenigen Einträge der Form 'Berlin, Uni.' (ohne weitere Spezifikation) der 'Freien Universität Berlin' zugeordnet, "
           " da stichprobenartige Untersuchungen ergaben, dass Hochschulschriften der HU Berlin Teile des Namens oder die Abkürzung 'HU' enthielten, "
           " während alle überprüften Hochschulschriften mit dem Vermerk 'Berlin, Uni.' der FU Berlin zuzuordnen waren. " )
st.markdown("Alle Hochschulschriften, die einer Hochschule außerhalb Deutschlands zuzuordnen sind, wurden für diese Übersicht nicht berücksichtigt. "
            "Auch konnten nicht alle Tippfehler im Hochschulschriftenvermerk abgefangen werden, so dass dadurch einzelne Schriften in der Anzeige "
            "ebenfalls keine Berücksichtigung finden konnten. Dies betrifft jedoch lediglich 464 der 295.199 Datensätze (0,15%).")
