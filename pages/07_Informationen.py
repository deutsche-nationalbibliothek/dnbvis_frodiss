import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
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
                
#----------------        
    
    


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
st.markdown(" #### Lizenz") 
st.write("Die für diese Anwendung genutzten Skripte und JSON-Dateien sind auf [Github](https://github.com/deutsche-nationalbibliothek/dnbvis_frodiss) verfügbar. "
         " Diese Skripte und Daten stehen unter CC0 Lizenz und können frei weitergenutzt werden. ")


st.markdown(" #### Kontakt") 
st.markdown(" Bei Fragen oder Anmerkungen wenden Sie sich bitte an Stephanie Palek: s.palek@dnb.de") 
    

    
