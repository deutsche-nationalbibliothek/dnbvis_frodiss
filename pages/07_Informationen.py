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


testcolor = ['#ff6900', '#fcb900', '#7bdcb5', '#00d084', '#8ed1fc',
            '#0693e3', '#abb8c3', '#eb144c', '#f78da7', '#9900ef']

with st.sidebar:  
    
    st.write("Datensätze im Set: ", complete) 
    st.write("Stand der Daten: 03.11.2022")
    st.write("Zuletzt aktualisiert: 22.11.2022") 


st.subheader("Über diese Visualisierung")

st.markdown('Die Anwendung visualisiert das Datenset "Freie Online-Hochschulschriften" der Deutschen Nationalbibliothek. Sie soll einen ersten visuellen Eindruck '
            " der Online-Dissertationen im Bestand der DNB geben, und zusätzlich verdeutlichen, "
            " wie auf der Basis vorhandener Katalogdaten mit einfachen Mitteln und verhältnismäßig geringem Aufwand Erkenntnisse über ausgewählte "
            " Publikationstypen, deren Entwicklung, Verbreitung und sprachliche Vielfalt gewonnen und graphisch dargestellt werden können. Mit den "
            " Online-Dissertationen ist ein Anfang gemacht. Eine Fortsetzung mit Bestandsanalysen zu anderen Publikationstypen, Zeiträumen und inhaltlichen " 
            " Schwerpunkten ist wünschenswert.")

st.markdown("Die Anwendung enthält mehrfach Links auf den Katalog der Deutschen Nationalbibliothek, die es ermöglichen sollen, die den Visualisierungen "
            "zugrundeliegenden Publikationen genauer zu erkunden. Bitte beachten Sie dabei, dass die Anzahl der in dieser Anwendung dargestellten Publikationen von der im "
            "DNB-Katalog angezeigten Trefferanzahl abweichen kann. Grund dafür ist, dass diese Anwendung auf einem Datenabzug eines bestimmten Datums "
            " basiert, während der Katalog der DNB die Sammlung tagesaktuell wiedergibt.") 

st.markdown(" #### Methodik")
          
st.markdown("Im Datenset enthalten sind derzeit ingesamt 295.756 Datensätze. Von diesen verfügen 295.199 "
            "über einen [Hochschulschriftenvermerk](https://www.dnb.de/DE/Service/Hilfe/HilfeNP/_content/Ablieferung/Monografienn/hochschulschriftenvermerkAblieferung8_akk.html). "
            "Bei den 557 Datensätzen ohne Hochschulschriftenvermerk handelt es sich zumeist um übergeordnete "
            "Datensätze monographischer Reihen, in denen entsprechende Hochschulschriften erschienen sind. Diese Datensätze wurden für die weitere "
            "Darstellung des Sets entsprechend nicht berücksichtigt." ) 

st.write("Für die visuelle Darstellung der Daten aus dem Datenset der Deutschen Nationalbibliothek mussten diese bereinigt und angepasst werden. "
         " Diese Arbeiten erfolgten hauptsächlich maschinell, indem bspw. eckige Klammern um Jahreszahlen entfernt oder Eintragungen älterer Sachgruppen "
        " auf die DDC gemappt wurden. Mehr Informationen hierzu finden Sie jeweils unter den einzelnen Visualisierungen.") 

st.write("Das Datenset liegt im MARC21-XML-Format vor, aus dem die für die unterschiedlichen Visualisierungen notwendigen Informationen gefiltert "
         " und als JSON-Dateien gespeichert wurden. Diese dienen als Basis für die verschiedenen Python-Skripte, auf denen die Visualisierungen basieren. ")
st.write("Die Anwendung wurde mit dem Python-Framework [Streamlit](https://streamlit.io/) geschrieben, die verschiedenen Visualisierungen basieren auf "
         " [Plotly](https://plotly.com/python/). ")
st.markdown(" #### Lizenz) 
st.write("Die für diese Anwendung genutzten Skripte und JSON-Dateien sind auf [Github](https://github.com/deutsche-nationalbibliothek/dnbvis_frodiss) verfügbar. "
         " Diese Skripte und Daten stehen unter CC0 Lizenz und können frei weitergenutzt werden. ")


st.markdown(" #### Kontakt") 
st.markdown(" Bei Fragen oder Anmerkungen wenden Sie sich bitte an Stephanie Palek: s.palek@dnb.de") 
    

    
