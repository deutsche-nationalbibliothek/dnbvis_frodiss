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
timestamp = overview['timestamp'].values[-1]
update = overview['update'].values[-1]

with st.sidebar:
        
        st.write("Datensätze im Set: ", complete)     
        st.write("Stand der Daten: ", timestamp)
        st.write("Zuletzt aktualisiert: ", update)
        st.markdown('#') 
        st.markdown('#') 
        
        
        github_logo_black = "GitHub_Logo.png"
        github_logo_white = "GitHub_Logo_white.png"
        
        with st.container():
                column1, column2 = st.columns(2)
                
                column1.write("[DNBVIS_frodiss auf GitHub](https://github.com/deutsche-nationalbibliothek/dnbvis_frodiss)")
                column2.markdown('<style>img {width: 75px; display: block; margin-left: auto; margin-right: auto; margin-top: 10px;}</style><a href="https://github.com/deutsche-nationalbibliothek/dnbvis_frodiss", target="new"><img src="https://raw.githubusercontent.com/deutsche-nationalbibliothek/dnbvis_frodiss/main/GitHub_Logo.png"></a>', unsafe_allow_html=True)
                
#----------------        
    
    


st.subheader("Übersicht Publikationsorte") 

st.write("Klicken Sie auf einen Publikationsort, um einen Link zu den Titeln im Katalog zu generieren.")
st.write("Der Link wird im Anschluss unter der Karte angezeigt. ")

df = pd.read_json("data/geoplaces.json", encoding="utf-8")

df["url"] = "https://portal.dnb.de/opac.htm?method=simpleSearch&cqlMode=true&query=catalog=dnb.hss+location=onlinefree+"+df["Place"].astype(str)
update = (len(df["Place"]))

    
fig3 = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name="Place", 
                         size="count", color="count", color_continuous_scale=px.colors.cyclical.IceFire, zoom=5, 
                         height=500, labels={
                                        "count": "Anzahl",
                                        "lat":"Latitude",
                                        "lon":"Longitude"
                                             }
                        )
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
st.markdown("Ausschlaggebend für die örtliche Zuordnung ist die Angabe des Publikationsortes, oder, falls diese Information nicht vorhanden war, der Sitz der für die Publikation "
            "verantwortlichen Hochschule. Dieser wurde dem Hochschulschriftenvermerk entnommen. Dies ist möglich, weil freie Online-Hochschulschriften in der Regel auf den "
            " Repositorien der promovierenden bzw. habilitierenden Hochschule veröffentlicht werden und damit der Publikationsort überwiegend auch dem Hochschulstandort entspricht. "
            " Der Fokus dieser Darstellung liegt dabei auf dem Publikationsort, der aber durchaus auch im Ausland liegen kann, sofern bspw. der Verlag seinen Hauptsitz im Ausland hat. ")
st.markdown("Die Ortsangaben wurden anschließend bereinigt und vereinheitlicht, um eine automatisierte Georeferenzierung für die Kartendarstellung durchführen zu können. ")
