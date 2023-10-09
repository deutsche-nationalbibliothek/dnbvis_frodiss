import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("pages", "data")

#file location paths:
style = dir_path + "\style.css"
overview = dir_path + "\overview.csv"

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
    
    


st.subheader("Über DNBVIS_frodiss")

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
st.markdown(" #### Lizenz") 
st.write("Die für diese Anwendung genutzten Skripte und JSON-Dateien sind auf [Github](https://github.com/deutsche-nationalbibliothek/dnbvis_frodiss) verfügbar. "
         " Diese Skripte und Daten stehen unter CC0 Lizenz und können frei weitergenutzt werden. ")


st.markdown(" #### Kontakt") 
st.markdown(" Bei Fragen oder Anmerkungen wenden Sie sich bitte an Stephanie Palek: s.palek@dnb.de") 
    

    
