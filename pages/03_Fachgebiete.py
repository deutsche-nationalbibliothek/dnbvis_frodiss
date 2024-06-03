import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from streamlit_plotly_events import plotly_events
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("pages", "data")

#file location paths:
style = "data/style.css"  # online version
#style = dir_path + "\data\style.css" # offline version
#overview = dir_path + "\data\overview.csv"
overview = "data/overview.csv"
diss_ddc = "data/diss_ddc.json"

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
 
dissddc = pd.read_json(diss_ddc, encoding="utf-8")
df = pd.read_json(diss_ddc, dtype = str)


zero = dissddc[dissddc["Parent_no"].astype(str).str.startswith('0')]
first = dissddc[dissddc["Parent_no"].astype(str).str.startswith('1')]
second = dissddc[dissddc["Parent_no"].astype(str).str.startswith('2')]
third = dissddc[dissddc["Parent_no"].astype(str).str.startswith('3')]
fourth = dissddc[dissddc["Parent_no"].astype(str).str.startswith('4')]
fifth = dissddc[dissddc["Parent_no"].astype(str).str.startswith('5')]
sixth = dissddc[dissddc["Parent_no"].astype(str).str.startswith('6')]
seventh = dissddc[dissddc["Parent_no"].astype(str).str.startswith('7')]
eigth = dissddc[dissddc["Parent_no"].astype(str).str.startswith('8')]
ninth = dissddc[dissddc["Parent_no"].astype(str).str.startswith('9')]
    
    
pub_000 = zero['count'].sum()
conv_pub_000 = f'{pub_000:,}'.replace(',', '.')
pub_100 = first['count'].sum()
conv_pub_100 = f'{pub_100:,}'.replace(',', '.')
pub_200 = second['count'].sum()
conv_pub_200 = f'{pub_200:,}'.replace(',', '.')
pub_300 = third['count'].sum()
conv_pub_300 = f'{pub_300:,}'.replace(',', '.')
pub_400 = fourth['count'].sum()
conv_pub_400 = f'{pub_400:,}'.replace(',', '.')
pub_500 = fifth['count'].sum()
conv_pub_500 = f'{pub_500:,}'.replace(',', '.')
pub_600 = sixth['count'].sum()
conv_pub_600 = f'{pub_600:,}'.replace(',', '.')
pub_700 = seventh['count'].sum()
conv_pub_700 = f'{pub_700:,}'.replace(',', '.')
pub_800 = eigth['count'].sum()
conv_pub_800 = f'{pub_800:,}'.replace(',', '.')
pub_900 = ninth['count'].sum()
conv_pub_900 = f'{pub_900:,}'.replace(',', '.')

overview_ddc = pd.DataFrame({'Anzahl': [pub_000,pub_100,pub_200,pub_300,pub_400,pub_500,pub_600,pub_700,pub_800,pub_900], 
                         'DDC':['000','100','200','300','400','500','600','700','800','900']})


records_ddc = int(overview['records_hss'].values[-1] - overview['no_ddc'].values[-1]) 
records_ddc = f'{records_ddc:,}'.replace(',', '.')
ddc_missing_at_first = int(overview['ddc_missing_at_first'].values[-1])
ddc_missing_at_first = f'{ddc_missing_at_first:,}'.replace(',', '.')
missing = int(overview['no_ddc'].values[-1])

# --------- DDC -----------------

st.subheader("Übersicht Fachgebiete")

st.markdown("Diese Übersicht gliedert die Daten entsprechend der Fachgebiete der 10 DDC-Hauptklassen. Die Auswahl einer Hauptklasse führt zu einer detaillierteren Ansicht. "
            "Mehr Informationen zu den DDC-Klassen finden Sie unter [www.dnb.de/ddcuebersichten](https://www.dnb.de/ddcuebersichten).")
    
st.markdown("###### Wählen Sie im Auswahlmenü ein Fachgebiet zur genaueren Ansicht oder klicken Sie auf eine farbige Kachel, um zu den entsprechenden Publikationen im "
            " DNB-Katalog zu gelangen:")
subject = st.selectbox(
     'Auswahlmenü Fachgebiete: ',
     ('Übersicht', 'Alle Fachgebiete', '000 - Allgemeines, Informatik, Informationswissenschaft', '100 - Philosophie und Psychologie', '200 - Religion', '300 - Sozialwissenschaften',
      '400 - Sprache', '500 - Naturwissenschaften und Mathematik', '600 - Technik, Medizin, angewandte Wissenschaften', '700 - Künste und Unterhaltung',
     '800 - Literatur', '900 - Geschichte und Geografie')
    )
    
st.write(" ")

st.write(" ") 
# --- Data ---- 
    
def show_ddc():         
        col1, col2 = st.columns([1, 6])     
    
        with col1:
                st.write("")
                st.write("")
                st.markdown("[![Foo](https://i.creativecommons.org/l/by-nc-nd/3.0/88x31.png)](http://creativecommons.org/licenses/by-nc-nd/3.0/)") 
        
        
        with col2:     
                st.caption("This work is licensed under a Creative Commons Attribution-Noncommercial-No Derivative Works 3.0 Unported License "
                "by OCLC Online Computer Library Center, Inc. All copyright rights in the Dewey Decimal Classification system are "
                "owned by OCLC. Dewey, Dewey Decimal Classification, DDC, OCLC and WebDewey are registered trademarks of OCLC. ")
    

        
    
    
if subject == "Übersicht": 
# --- boxes
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        colour = (254,107,72)
        fontsize = 16
        ddc_main = "Allgemeines, Informatik, Informationswissenschaft"
        #lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'
        i = conv_pub_000
        
        htmlstr = f"""<a href="https://portal.dnb.de/opac/simpleSearch?query=catalog%3Ddnb.hss+AND+hss%3Ddiss*+AND+location%3Donlinefree+AND+hsg%3D0*&cqlMode=true" target="new" style="text-decoration:none">
                        <p style='background-color: rgb({colour[0]}, {colour[1]}, {colour[2]}); 
                        font-size: {fontsize}px; 
                        color: black;
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height: 20px;'>
                        {ddc_main}</style><br>
                        <span style='font-size: 22px; line-height: 35px;'><b>{i}</b></style></span></p></a>"""

        st.markdown(htmlstr, unsafe_allow_html=True)
    
    
    with col2: 
        colour = (163,184,0)
        fontsize = 16
        ddc_main = "Philosophie und Psychologie"
        i = conv_pub_100

        htmlstr = f"""<a href="https://portal.dnb.de/opac/simpleSearch?query=catalog%3Ddnb.hss+AND+hss%3Ddiss*+AND+location%3Donlinefree+AND+hsg%3D%28100+OR+110+OR+120+OR+130+OR+140+OR+150+OR+160+OR+170+OR+180+OR+190%29&cqlMode=true" target="new" style="text-decoration:none">
                        <p style='background-color: rgb({colour[0]}, {colour[1]}, {colour[2]});
                        font-size: {fontsize}px; 
                        color: black;
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:20px;'>
                        {ddc_main}<br></style><BR>
                        <span style='font-size: 22px; line-height: 35px;'><b>{i}</b><br></style></span></p></a>"""

        st.markdown(htmlstr, unsafe_allow_html=True)
        
    with col3:
        colour = (153,153,255)
        fontsize = 16
        ddc_main = "Religion"
        i = conv_pub_200

        htmlstr = f"""<a href="https://portal.dnb.de/opac/simpleSearch?query=catalog%3Ddnb.hss+AND+hss%3Ddiss*+AND+location%3Donlinefree+AND+hsg%3D2*&cqlMode=true" target="new" style="text-decoration:none">
                        <p style='background-color: rgb({colour[0]}, {colour[1]}, {colour[2]}); 
                        font-size: {fontsize}px; 
                        color: black;
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:20px;'>
                        {ddc_main}<br>
                        </style><BR><span style='font-size: 22px; line-height: 35px;'><b>{i}</b></style></span></p></a>"""

        st.markdown(htmlstr, unsafe_allow_html=True)

   
    twocol1, twocol2, twocol3 = st.columns(3)
      
    with twocol1: 
        colour = (0,141,188)
        fontsize = 16
        ddc_main = "Sozialwissenschaften"
        i = conv_pub_300
        
        htmlstr = f"""<a href="https://portal.dnb.de/opac/simpleSearch?query=catalog%3Ddnb.hss+AND+hss%3Ddiss*+AND+location%3Donlinefree+AND+hsg%3D3*&cqlMode=true" target="new" style="text-decoration:none">
                        <p style='background-color: rgb({colour[0]}, {colour[1]}, {colour[2]}); 
                        font-size: {fontsize}px; 
                        color: black;
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:20px;'>
                        {ddc_main}<br></style><BR>
                        <span style='font-size: 22px; line-height: 35px;'><b>{i}</b></style></span></p></a>"""
     
        st.markdown(htmlstr, unsafe_allow_html=True)
        
    with twocol2: 
        colour = (255,200,31)
        fontsize = 16
        ddc_main = "Sprache"
        i = conv_pub_400
        
        htmlstr = f"""<a href="https://portal.dnb.de/opac/simpleSearch?query=catalog%3Ddnb.hss+AND+hss%3Ddiss*+AND+location%3Donlinefree+AND+hsg%3D4*&cqlMode=true" target="new" style="text-decoration:none">
                        <p style='background-color: rgb({colour[0]}, {colour[1]}, {colour[2]}); 
                        font-size: {fontsize}px; 
                        color: black;
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:20px;'>
                        {ddc_main}<br></style><BR>
                        <span style='font-size: 22px; line-height: 35px;'><b>{i}</b></style></span></p></a>"""
     
        st.markdown(htmlstr, unsafe_allow_html=True)
        
        
    with twocol3: 
        colour = (255,51,51)
        fontsize = 16
        ddc_main = "Naturwissenschaften und Mathematik"
        i = conv_pub_500
        
        htmlstr = f"""<a href="https://portal.dnb.de/opac/simpleSearch?query=catalog%3Ddnb.hss+AND+hss%3Ddiss*+AND+location%3Donlinefree+AND+hsg%3D5*&cqlMode=true" target="new" style="text-decoration:none">
                        <p style='background-color: rgb({colour[0]}, {colour[1]}, {colour[2]}); 
                        font-size: {fontsize}px; 
                        color: black;
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:20px;'>
                        {ddc_main}</style><BR>
                        <span style='font-size: 22px; line-height: 35px;'><b>{i}</b></style></span></p></a>"""
     
        st.markdown(htmlstr, unsafe_allow_html=True)
        
        
    threecol1, threecol2, threecol3 = st.columns(3)
      
    with threecol1: 
        colour = (255,184,77)
        fontsize = 16
        ddc_main = "Technik, Medizin, angewandte Wissenschaften"
        i = conv_pub_600
        
        htmlstr = f"""<a href="https://portal.dnb.de/opac/simpleSearch?query=catalog%3Ddnb.hss+AND+hss%3Ddiss*+AND+location%3Donlinefree+AND+hsg%3D6*&cqlMode=true" target="new" style="text-decoration:none">
                        <p style='background-color: rgb({colour[0]}, {colour[1]}, {colour[2]}); 
                        font-size: {fontsize}px;
                        color: black;
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:20px;'>
                        {ddc_main}</style><BR>
                        <span style='font-size: 22px; line-height: 35px;'><b>{i}</b></style></span></p></a>"""
     
        st.markdown(htmlstr, unsafe_allow_html=True)
        
        
    with threecol2: 
        colour = (51,204,204)
        fontsize = 16
        ddc_main = "Künste und Unterhaltung"
        i = conv_pub_700
        
        htmlstr = f"""<a href="https://portal.dnb.de/opac/simpleSearch?query=catalog%3Ddnb.hss+AND+hss%3Ddiss*+AND+location%3Donlinefree+AND+hsg%3D7*&cqlMode=true" target="new" style="text-decoration:none">
                        <p style='background-color: rgb({colour[0]}, {colour[1]}, {colour[2]});
                        color: black;
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:20px; '>
                        {ddc_main}<br></style><BR>
                        <span style='font-size: 22px; line-height:35px'><b>{i}</b></style></span></p></a>"""
     
        st.markdown(htmlstr, unsafe_allow_html=True)
        
    with threecol3: 
        colour = (122,219,112)
        fontsize = 16
        ddc_main = "Literatur"
        i = conv_pub_800
        
        htmlstr = f"""<a href="https://portal.dnb.de/opac/simpleSearch?query=catalog%3Ddnb.hss+AND+hss%3Ddiss*+AND+location%3Donlinefree+AND+hsg%3D8*&cqlMode=true" target="new" style="text-decoration:none">
                        <p style='background-color: rgb({colour[0]}, {colour[1]}, {colour[2]}); 
                        font-size: {fontsize}px; 
                        color: black;
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:20px;'>
                        {ddc_main}<br></style><BR>
                        <span style='font-size: 22px; line-height: 35px;'></b>{i}</b></style></span></p></a>"""
     
        st.markdown(htmlstr, unsafe_allow_html=True)
        
    fourcol1, fourcol2, fourcol3 = st.columns(3)
      
    with fourcol1: 
        colour = (255,153,255)
        fontsize = 16
        ddc_main = "Geschichte und Geografie"
        i = conv_pub_900
        
        htmlstr = f"""<a href="https://portal.dnb.de/opac/simpleSearch?query=catalog%3Ddnb.hss+AND+hss%3Ddiss*+AND+location%3Donlinefree+AND+hsg%3D9*&cqlMode=true" target="new" style="text-decoration:none">
                        <p style='background-color: rgb({colour[0]}, {colour[1]}, {colour[2]}); 
                        font-size: {fontsize}px; 
                        color: black;
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:20px;'>
                        {ddc_main}<br></style><BR>
                        <span style='font-size: 22px; line-height: 35px;'><b>{i}</b></style></span></p></a>"""
     
        st.markdown(htmlstr, unsafe_allow_html=True)
        
    with fourcol2: 
        colour = (255,255,255)
        fontsize = 16
        ddc_main = "Ohne Fachgebiet"
        i = missing
        
        htmlstr = f"""<a href="https://portal.dnb.de/opac/simpleSearch?query=catalog%3Ddnb.hss+AND+hss%3Ddiss*+AND+location%3Donlinefree+AND+NOT+%28hsg%3D0*+OR+hsg%3D1*+OR+hsg%3D2*+OR+hsg%3D3*+OR+hsg%3D4*+OR+hsg%3D5*+OR+hsg%3D6*+OR+hsg%3D7*+OR+hsg%3D8*+OR+hsg%3D9*%29&cqlMode=true" target="new" style="text-decoration:none">
                        <p style='background-color: rgb({colour[0]}, {colour[1]}, {colour[2]}); 
                        font-size: {fontsize}px; 
                        color: black;
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:20px;
                        border-style: solid;
                        border-width: 1px;'>
                        {ddc_main}<br></style><BR>
                        <span style='font-size: 22px; line-height: 35px;'><b>{i}</b></style></span></p>"""
     
        st.markdown(htmlstr, unsafe_allow_html=True)
      
        
    st.write(" ")    
    st.caption(" Klicken Sie auf eine farbige Kachel, um sich die hier erfassten Titel dieses Fachgebiets "
         " im neuen Katalog der DNB anzeigen zu lassen. Da die Katalogdaten im Unterschied zum Datenset immer tagesaktuell sind und andere "
         " Suchindizes genutzt werden, kommt es bei der Treffermenge zu leichten Abweichungen zwischen der Gesamtzahl der jeweiligen Hochschulschriften "
         " im Katalog und in der Visualisierung.   ")    
    st.write(" ")  
        
        
elif subject == "Alle Fachgebiete":    
        
    st.write("Visuelle Darstellung der Verteilung auf die 10 DDC-Hauptklassen:")        
        
    fig_all = px.bar(overview_ddc, x='DDC', y='Anzahl',         
                color='DDC',
                labels={'DDC':'DDC Hauptklasse'}, height=400, 
                color_discrete_map={
                        '000': '#FE6B48',
                        '100': '#A3B800',
                        '200': '#0046C4',
                        '300': '#008DBC',
                        '400': '#FFC81F',
                        '500': '#E62D2D',
                        '600': '#DDCD69',
                        '700': '#007DEE',
                        '800': '#F3A161',
                        '900': '#B233D5',
                      }    
                    )
    #st.plotly_chart(fig_all, use_container_width=True)    
    
    selected_points = plotly_events(fig_all)
    if selected_points:
        a=selected_points[0]
        select = a['x']
        print(select)
    else:
        select = 0

            
#--------------------------
        
elif subject == "000 - Allgemeines, Informatik, Informationswissenschaft": 
    
    st.info("Klicken Sie auf die einzelnen Elemente im inneren Ring, um eine detailliertere Darstellung der Teilmengen "
            "sehen zu können. Bewegen Sie Ihren Cursor auf ein Elemente, um Zusatzinformationen zu erhalten." ) 

    df_000 = df[df["Parent_no"].str.startswith('0')]
               
    fig = px.sunburst(df_000, path=['DDCsecond_title', 'Sachgebiet'], values='count', 
                  custom_data=['Parent_title', 'count', 'Parent_no', 'DDCthird'],
                  height = 750, color_discrete_sequence=px.colors.sequential.Viridis)
    fig.update_traces(texttemplate="%{label}<br>%{percentEntry:.2%}",
                        insidetextorientation='auto',  
                        hovertemplate="<br>".join([
                        "DDC-Sachgruppe: %{label}",
                        "DDC: %{customdata[3]}",
                        "Anzahl: %{customdata[1]}",
                        "Anteil: %{percentEntry:.2%}",   
                        "DDC-Klassen: %{customdata[2]}, %{customdata[0]}"]),
                        sort=False,
                        #rotation=180,
                        textfont_size=12
                 )

    st.plotly_chart(fig, use_container_width=True)
    show_ddc()
    
       
#_____________
elif subject == "100 - Philosophie und Psychologie": 
        
    st.info("Klicken Sie auf die einzelnen Elemente im inneren Ring, um eine detailliertere Darstellung der Teilmengen "
            "sehen zu können. Bewegen Sie Ihren Cursor auf ein Elemente, um Zusatzinformationen zu erhalten." ) 

    
    df_000 = dissddc[dissddc["Parent_no"].astype(str).str.startswith('1')]
            
    fig = px.sunburst(df_000, path=['DDCsecond_title', 'Sachgebiet'], values='count', 
                  custom_data=['Parent_title', 'count', 'Parent_no'],
                  height = 750, color_discrete_sequence=px.colors.sequential.Aggrnyl)
    fig.update_traces(texttemplate="%{label}<br>%{percentEntry:.2%}",
                        #insidetextorientation='radial',
                        hovertemplate="<br>".join([
                        "DDC-Sachgruppe: %{label}",
                        "Anzahl: %{customdata[1]}",
                        "Anteil: %{percentEntry:.2%}",   
                        "DDC-Hauptklasse: %{customdata[2]} - %{customdata[0]}"]),
                        sort=False,
                        rotation=180,
                        textfont_size=12
                 )

    st.plotly_chart(fig, use_container_width=True)
    show_ddc()
    

#___________________________________

elif subject == "200 - Religion": 
        
    st.info("Klicken Sie auf die einzelnen Elemente im inneren Ring, um eine detailliertere Darstellung der Teilmengen "
            "sehen zu können. Bewegen Sie Ihren Cursor auf ein Elemente, um Zusatzinformationen zu erhalten." ) 

    
    df_000 = dissddc[dissddc["Parent_no"].astype(str).str.startswith('2')]
            
    fig = px.sunburst(df_000, path=['DDCsecond_title', 'Sachgebiet'], values='count', 
                  custom_data=['Parent_title', 'count', 'Parent_no'],
                  height = 750, color_discrete_sequence=px.colors.sequential.ice)
    fig.update_traces(insidetextorientation='radial', texttemplate="%{label}<br>%{percentEntry:.2%}",
                 hovertemplate="<br>".join([
                        "DDC-Sachgruppe: %{label}",
                        "Anzahl: %{customdata[1]}",
                        "Anteil: %{percentEntry:.2%}",   
                        "DDC-Hauptklasse: %{customdata[2]} - %{customdata[0]}"]),
                        sort=False,
                        rotation=180,
                        textfont_size=12
                 )

    st.plotly_chart(fig, use_container_width=True)
    show_ddc()
   

#___________________________________

elif subject == "300 - Sozialwissenschaften": 
    
    st.info("Klicken Sie auf die einzelnen Elemente im inneren Ring, um eine detailliertere Darstellung der Teilmengen "
            "sehen zu können. Bewegen Sie Ihren Cursor auf ein Elemente, um Zusatzinformationen zu erhalten." ) 

    df_000 = dissddc[dissddc["Parent_no"].astype(str).str.startswith('3')]
            
    fig = px.sunburst(df_000, path=['DDCsecond_title', 'Sachgebiet'], values='count', 
                  custom_data=['Parent_title', 'count', 'Parent_no'],
                  height = 750, color_discrete_sequence=px.colors.sequential.deep)
    fig.update_traces(insidetextorientation='radial', texttemplate="%{label}<br>%{percentEntry:.2%}",
                 hovertemplate="<br>".join([
                        "DDC-Sachgruppe: %{label}",
                        "Anzahl: %{customdata[1]}",
                        "Anteil: %{percentEntry:.2%}",   
                        "DDC-Hauptklasse: %{customdata[2]} - %{customdata[0]}"]),
                        sort=False,
                        rotation=180,
                        textfont_size=12
                 )

    st.plotly_chart(fig, use_container_width=True)
    show_ddc()
    

#___________________________________

elif subject == "400 - Sprache": 
        
    st.info("Klicken Sie auf die einzelnen Elemente im inneren Ring, um eine detailliertere Darstellung der Teilmengen "
            "sehen zu können. Bewegen Sie Ihren Cursor auf ein Elemente, um Zusatzinformationen zu erhalten." ) 

    
    df_000 = dissddc[dissddc["Parent_no"].astype(str).str.startswith('4')]
            
    fig = px.sunburst(df_000, path=['DDCsecond_title', 'Sachgebiet'], values='count', 
                  custom_data=['Parent_title', 'count', 'Parent_no'],
                  height = 750, color_discrete_sequence=px.colors.sequential.solar)
    fig.update_traces(insidetextorientation='radial', texttemplate="%{label}<br>%{percentEntry:.2%}",
                 hovertemplate="<br>".join([
                        "DDC-Sachgruppe: %{label}",
                        "Anzahl: %{customdata[1]}",
                        "Anteil: %{percentEntry:.2%}",   
                        "DDC-Hauptklasse: %{customdata[2]} - %{customdata[0]}"]),
                        sort=False,
                        rotation=180,
                        textfont_size=12
                 )

    st.plotly_chart(fig, use_container_width=True)
    show_ddc()
    
#___________________________________

elif subject == "500 - Naturwissenschaften und Mathematik": 
    
    st.info("Klicken Sie auf die einzelnen Elemente im inneren Ring, um eine detailliertere Darstellung der Teilmengen "
            "sehen zu können. Bewegen Sie Ihren Cursor auf ein Elemente, um Zusatzinformationen zu erhalten." ) 

    df_000 = dissddc[dissddc["Parent_no"].astype(str).str.startswith('5')]
            
    fig = px.sunburst(df_000, path=['DDCsecond_title', 'Sachgebiet'], values='count', 
                  custom_data=['Parent_title', 'count', 'Parent_no'],
                  height = 750, color_discrete_sequence=px.colors.sequential.Inferno)
    fig.update_traces(insidetextorientation='radial', texttemplate="%{label}<br>%{percentEntry:.2%}",
                 hovertemplate="<br>".join([
                        "DDC-Sachgruppe: %{label}",
                        "Anzahl: %{customdata[1]}",
                        "Anteil: %{percentEntry:.2%}",   
                        "DDC-Hauptklasse: %{customdata[2]} - %{customdata[0]}"]),
                        sort=False,
                        rotation=180,
                        textfont_size=12
                 )

    st.plotly_chart(fig, use_container_width=True)
    show_ddc()
    

#___________________________________

elif subject == "600 - Technik, Medizin, angewandte Wissenschaften": 
    
    st.info("Klicken Sie auf die einzelnen Elemente im inneren Ring, um eine detailliertere Darstellung der Teilmengen "
            "sehen zu können. Bewegen Sie Ihren Cursor auf ein Elemente, um Zusatzinformationen zu erhalten." ) 

    df_000 = dissddc[dissddc["Parent_no"].astype(str).str.startswith('6')]
            
    fig = px.sunburst(df_000, path=['DDCsecond_title', 'Sachgebiet'], values='count', 
                  custom_data=['Parent_title', 'count', 'Parent_no'],
                  height = 750, color_discrete_sequence=px.colors.diverging.Fall)
    fig.update_traces(insidetextorientation='radial', texttemplate="%{label}<br>%{percentEntry:.2%}",
                 hovertemplate="<br>".join([
                        "DDC-Sachgruppe: %{label}",
                        "Anzahl: %{customdata[1]}",
                        "Anteil: %{percentEntry:.2%}",   
                        "DDC-Hauptklasse: %{customdata[2]} - %{customdata[0]}"]),
                        sort=False,
                        rotation=180,
                        textfont_size=12
                 )

    st.plotly_chart(fig, use_container_width=True)
    show_ddc()
    
#___________________________________

elif subject == "700 - Künste und Unterhaltung": 
    
    st.info("Klicken Sie auf die einzelnen Elemente im inneren Ring, um eine detailliertere Darstellung der Teilmengen "
            "sehen zu können. Bewegen Sie Ihren Cursor auf ein Elemente, um Zusatzinformationen zu erhalten." ) 

    df_000 = dissddc[dissddc["Parent_no"].astype(str).str.startswith('7')]
            
    fig = px.sunburst(df_000, path=['DDCsecond_title', 'Sachgebiet'], values='count', 
                  custom_data=['Parent_title', 'count', 'Parent_no'],
                  height = 750, color_discrete_sequence=px.colors.sequential.haline)
    fig.update_traces(insidetextorientation='radial', texttemplate="%{label}<br>%{percentEntry:.2%}",
                 hovertemplate="<br>".join([
                        "DDC-Sachgruppe: %{label}",
                        "Anzahl: %{customdata[1]}",
                        "Anteil: %{percentEntry:.2%}",   
                        "DDC-Hauptklasse: %{customdata[2]} - %{customdata[0]}"]),
                        sort=False,
                        rotation=180,
                        textfont_size=12
                 )

    st.plotly_chart(fig, use_container_width=True)
    show_ddc()
    

#___________________________________

elif subject == "800 - Literatur": 
    
    st.info("Klicken Sie auf die einzelnen Elemente im inneren Ring, um eine detailliertere Darstellung der Teilmengen "
            "sehen zu können. Bewegen Sie Ihren Cursor auf ein Elemente, um Zusatzinformationen zu erhalten." ) 

    df_000 = dissddc[dissddc["Parent_no"].astype(str).str.startswith('8')]
            
    fig = px.sunburst(df_000, path=['DDCsecond_title', 'Sachgebiet'], values='count', 
                  custom_data=['Parent_title', 'count', 'Parent_no'],
                  height = 750, color_discrete_sequence=px.colors.sequential.thermal)
    fig.update_traces(insidetextorientation='radial', texttemplate="%{label}<br>%{percentEntry:.2%}",
                 hovertemplate="<br>".join([
                        "DDC-Sachgruppe: %{label}",
                        "Anzahl: %{customdata[1]}",
                        "Anteil: %{percentEntry:.2%}",   
                        "DDC-Hauptklasse: %{customdata[2]} - %{customdata[0]}"]),
                        sort=False,
                        rotation=180,
                        textfont_size=12
                 )

    st.plotly_chart(fig, use_container_width=True)
    show_ddc()
    

#___________________________________


elif subject == "900 - Geschichte und Geografie": 
    
    st.info("Klicken Sie auf die einzelnen Elemente im inneren Ring, um eine detailliertere Darstellung der Teilmengen "
            "sehen zu können. Bewegen Sie Ihren Cursor auf ein Elemente, um Zusatzinformationen zu erhalten." ) 

    df_000 = dissddc[dissddc["Parent_no"].astype(str).str.startswith('9')]
            
    fig = px.sunburst(df_000, path=['DDCsecond_title', 'Sachgebiet'], values='count', 
                  custom_data=['Parent_title', 'count', 'Parent_no'],
                  height = 750, color_discrete_sequence=px.colors.sequential.Agsunset)
    fig.update_traces(insidetextorientation='radial', texttemplate="%{label}<br>%{percentEntry:.2%}",
                 hovertemplate="<br>".join([
                        "DDC-Sachgruppe: %{label}",
                        "Anzahl: %{customdata[1]}",
                        "Anteil: %{percentEntry:.2%}",   
                        "DDC-Hauptklasse: %{customdata[2]} - %{customdata[0]}"]),
                        sort=False,
                        rotation=180,
                        textfont_size=12
                 )

    st.plotly_chart(fig, use_container_width=True)
    
    show_ddc()

#___________________________________



else:
    
    st.write("Data missing")
        
                  
st.write(" ")
st.write(" ")
            
st.markdown(" ##### Informationen zu dieser Visualisierung:")
st.markdown(f"Für die Übersicht nach Fachgebieten konnten insgesamt {records_ddc} Datensätze berücksichtigt werden. Hiervon verfügte ein Großteil "
            f" über einen entsprechenden Eintrag einer DDC-Klasse, bei einigen Datensätzen war ein solcher Eintrag jedoch zunächst nicht vorhanden. "
            " Sofern vorhanden, wurden hierfür Einträge älterer DNB-Sachgruppen herangezogen und anhand bestehender Mappings bzw. Konkordanzlisten "
            " einer DDC-Klasse zugeordnet. Dadurch konnten weitere Datensätze nachträglich mit DDC-Klassen angereichert werden. Für "
            f" {missing} Datensätze, die keinen Eintrag zu einem Fachgebiet enthielten, war dies nicht möglich. ") 
