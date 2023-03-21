import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

logo = "https://files.dnb.de/DFG-Viewer/DNB-Logo-Viewer.jpg"
st.set_page_config(page_title='DNBVIS_frodiss', page_icon = logo) # , layout = 'wide')

def local_css(file):
        with open(file) as f:
                st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("data/style.css")



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
                
        
    
  #-----------------  

    
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
            "Es enthält dabei auch Datensätze über entsprechende Publikationen, die Jahre nach ihrem Erscheinen digitalisiert und "
            "vor dem Beginn der Sammlung digitaler Hochschulschriften veröffentlicht wurden. "
            "Digitalisierte Hochschulschriften mit einem Erscheinungsdatum vor 1990 sind daher in sehr geringem Umfang ebenfalls im Set enthalten. " 
            "Für eine möglichst übersichtliche Darstellung der Publikationsjahre wurde diese auf die Erscheinungsjahre ab 1990 "
            "beschränkt. Enstprechend liegen dieser Darstellung 294.809 Publikationen zugrunde. ") 
    

        
 
