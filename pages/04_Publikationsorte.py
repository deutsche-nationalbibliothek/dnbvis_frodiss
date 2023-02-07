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
        </style>
        """,
        unsafe_allow_html=True,
    )


testcolor = ['#ff6900', '#fcb900', '#7bdcb5', '#00d084', '#8ed1fc',
            '#0693e3', '#abb8c3', '#eb144c', '#f78da7', '#9900ef']

with st.sidebar:  
    st.write("Datensätze im Set: ", complete) 
    st.write("Stand der Daten: 03.11.2022")
    st.write("Zuletzt aktualisiert: 22.11.2022") 


st.subheader("Übersicht Publikationsorte") 

st.write("Klicken Sie auf einen Publikationsort, um einen Link zu den Titeln im Katalog zu generieren. ")
st.write("Der Link wird im Anschluss unter der Karte angezeigt. ")

df = pd.read_json("data/geoplaces.json", encoding="utf-8")

df["url"] = "https://portal.dnb.de/opac.htm?method=simpleSearch&cqlMode=true&query=catalog=dnb.hss+location=onlinefree+"+df["Place"].astype(str)
update = (len(df["Place"]))

    
fig3 = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="Place", hover_data=['count'],
                        size="count", color="count", color_continuous_scale=px.colors.cyclical.IceFire, zoom=5, height=500)
fig3.update_layout(mapbox_style="open-street-map", 
                      mapbox=dict(
                            bearing=0,
                            center=dict(
                                    lat=51.10,
                                    lon=10.27
                                            )),
                   clickmode='event+select'
                        )  
fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig3.update_traces(marker_sizemin = 5, marker_sizeref = 10)

template = """
<b>Anzahl:</b> %{customdata[0]}<br>
<extra></extra>
"""

fig3.update_traces(hovertemplate = template)


selected_points = plotly_events(fig3)
select = 1000

if selected_points: 
        a=selected_points[0]
        select = a['pointNumber']  

if select != 1000:
        place = df.iloc[select]['Place']
        link = df.iloc[select]['url']
        st.info(f"Zu den Publikationen aus [{place}](%s)" % link)
else:
        st.write(" ")
        

st.write(" ")

st.markdown(" ##### Informationen zu dieser Visualisierung") 
st.markdown("Für diese Ansicht wurden vor allem die Angaben zum Publikationsort in den Datensätzen genutzt. Da Angaben hierzu jedoch häufig fehlten, "
            " wurden die Ortsinformationen ergänzend aus dem Hochschulschriftenvermerk genutzt. Dies ist möglich, weil Hochschulschriften in der Regel auf den "
            " Repositorien der promovierenden bzw. habilitierenden Hochschule veröffentlicht werden und damit in der Regel der Publikationsort auch dem Hochschulstandort entspricht. ")
st.markdown("Die Ortsangaben wurden anschließend bereinigt und vereinheitlicht, um eine automatisierte Georeferenzierung für die Kartendarstellung durchführen zu können. ")
