import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

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


with st.sidebar:  
    st.write("Datensätze im Set: ", complete) 
    st.write("Stand der Daten: 03.11.2022")
    st.write("Zuletzt aktualisiert: 22.11.2022") 

    
dissyears = pd.read_json("data/diss_years.json")


st.subheader("Anzahl der Online-Hochschulschriften im Bestand ab 1990: ")

st.write("Klicken Sie auf die blau unterlegte Anzahl der Dissertationen eines Jahres, um sich die hier erfassten Titel dieses Erscheinungsjahres "
         " im Katalog der DNB anzeigen zu lassen. Da die Katalogdaten im Unterschied zum Datenset immer tagesaktuell sind, kommt es zu Abweichungen "
         " zwischen der Gesamtzahl der Hochschulschriften im Katalog und in der Visualisierung.")

dissyears["url"] = "https://portal.dnb.de/opac.htm?method=simpleSearch&cqlMode=true&query=catalog=dnb.hss+location=onlinefree+jhr="+dissyears["years"].astype(str)

fig2 = px.bar(dissyears, x="years", y = "count", labels={'years':'Jahr', 'count':'Anzahl'}, color='count', height=500)
update = (len(dissyears["years"]))

for i in range (0,update):     
    fig2.add_annotation(      
            x = dissyears["years"].values[i],
            y = dissyears["count"].values[i],
            textangle = 90,
            text = f"""<a href="{dissyears["url"].values[i]}" target="_blank">{dissyears["count"].values[i]}</a>""",
            showarrow=True,
            arrowhead=1,                        
        )
fig2.update_traces(showlegend=False)
st.plotly_chart(fig2, use_container_width=True)

st.markdown(" ##### Informationen zu dieser Visualisierung:")
st.markdown('Das Datenset "Freie Online-Hochschulschriften" enthält Datensätze über alle in der DNB gesammelten Hochschulschriften, die online frei verfügbar sind. '
            "Es enthält dabei auch Datensätze über entsprechende Publikationen, die Jahre nach ihrem Erscheinen digitalisiert worden sind. Das Set enthält daher auch Datensätze "
            "von Publikationen, die vor dem Beginn der Sammlung digitaler Hochschulschriften veröffentlicht wurden. Da auch Hochschulschriften aus den Jahren vor 1990 "
            "digitalisiert wurden und entsprechend im Datenset enthalten sind, diese aber einen vergleichsweisen geringen Teil ausmachen, die Übersichtlichkeit der Darstellung "
            "allerdings bei Ausweitung der Visualisierung auf alle im Set enthaltenen Erscheinungsjahre sehr leidet, wurde die Darstellung der Publikationsjahre auf die Erscheinungsjahre ab 1990 "
            "beschränkt. Enstprechend liegen dieser Darstellung 294.809 Publikationen zugrunde. ") 
    

        
 
