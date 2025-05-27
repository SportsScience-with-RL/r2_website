import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import glob

def parcours_timeline_fr():
    exp = {
        'Année': [2013, 2014, 2014, 2015, 2015, 2015, 2016, 2016, 2018, 2018, 2020, 2021, 2021, 2022, 2022,
                  2023, 2023.5, 2023, 2023.5, 2023.5, 2024, 2024],
        'Exp_Et': ['RAC Rugby', 'Université Paris V Descartes', 'Racing 92', 'Université de Poitiers', 'CREPS de Montpellier',
                   'ASBH', 'Université de Montpellier', 'Hurricanes', 'TrainingLoad Pro', 'Collège Sainte-Anne', 'Centre Universitaire de Santé McGill',
                   'Harvard University', 'Brûleurs de loups', 'CentraleSupélec', 'FFR XIII', 'Trimane', 'RCT',
                   'INS QC', 'Boxe Canada', 'Badminton QC', 'INS QC', 'Soccer QC'],
        'Poste': ['Préparateur physique', 'Licence STAPS Entrainement sportif', 'Assistant Prép. physique (CDF)',
                  'DU Evaluation et Préparation physique', 'Certificat de compétences de préparateur physique pour sportifs de haut niveau', 'Assistant Prép. physique (Pro)',
                  "DU Optimisation de la préparation physique par les techniques d'haltérophilie et de force", 'Data Analyst - Sports Science<br>Assistant Prép. physique',
                  "Quantification des efforts, analyse et interprétations, programmation des stratégies d'entrainement et de réhabilitation, reporting, monitoring, datamining", 'Responsable Préparation physique',
                  'Analyste bases de données', 'Introduction à la Data Science avec Python',
                  'Data Scientist R&D<br>Responsable Prép. physique (Pro & CDF)', 'Maitrise Science des données en partenariat avec OpenClassrooms', 'Data Analyst - Sports Science',
                  'Data Scientist - Performance sportive', "Partenariat du club pour développer l'application", 'Data Scientist - Sport & Medicine', "Mise à jour d'une application de monitoring quotidien", 
                  "Création d'applications<br>- Application de tagging pour saisie de statistque en match<br>- Application d'analyse des saisies statistiques de match", 'Data Scientist', 'Gestionnaire de données'],
        'Projet': ['', '', '', '', '', '', '',
                   "Gestion de la structuration des données pour monitoring quotidien<br>- Extraction, transformation, chargement (ETL) des données<br>- Analyses descriptives, longitudinales (séries temporelles)<br>- Reporting quotidien",
                   '', '',
                   "Gestion de la base de données de la chaine d'approvisionnement<br>- Création d'une base de données pour la gestion des stocks et la distribution des entrepôts<br>- Mise à jour et reporting quotidien",
                   '',
                   "Gestion de la structuration des données pour monitoring quotidien et analyse par cycle<br>- Extraction, transformation, chargement (ETL) des données<br>- Analyses descriptives, longitudinales (séries temporelles)<br>- Machine learning (clustering, réduction de dimension)<br>- Reporting quotidien, hebdomadaire et mensuel",
                   '',
                   "Gestion de la structuration et déploiement des données pour monitoring quotidien<br>- Extraction, transformation, chargement (ETL) des données<br>- Analyses descriptives, longitudinales (séries temporelles)<br>- Reporting quotidient et rapport bilan post-compétition",
                   "Développement d'une application analytique pour structures sportives<br>- Développement logiciel support pour clubs sportifs<br>- Conception et développement des traitements de collecte, contrôle et stockage des données<br>- Réalisation de dashboards de pilotage<br>- Analyses statistiques et machine learning",
                   '', 
                   "Structuration du département de Sciences des données<br>- Audit et nettoyage des banques de données scientifiques<br>- Restructuration et/ou développement de solutions logiciels pour optimiser le workflow des données<br>- Développement de modèles facilitant l'interprétation des données ou à des fins de prédictions",
                   '', '', '', ''],
        'Valeur_graph': [1, -1, 1, -1, -2, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 2, 1.7, 2.3, 1, 2],
        'Line_x0': [2013, 2014, 2014, 2015, 2015, 2015, 2016, 2016, 2018, 2018, 2020, 2021, 2021, 2022, 2022,
                    2023, 2023.25, 2023, 2023.18, 2023.18, 2024, 2024],
        'Line_x1': [2013, 2014, 2014, 2015, 2015, 2015, 2016, 2016, 2018, 2018, 2020, 2021, 2021, 2022, 2022,
                    2023, 2023.35, 2023, 2023.38, 2023.38, 2024, 2024],       
        'Line_y0': [0, 0, 0, 0, -1.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1.3, 2, 2, 0, 1.3],
        'Line_y1': [.7, -.7, .7, -.7, -1.7, .7, -.7, .76, -.79, .7, .7, -.7, .7, -.7, .7, .7, 1, 1.7, 1.7, 2.3, .7, 1.7]
       }

    exp_df = pd.DataFrame(exp)

    fig = px.scatter(exp_df, x='Année', y='Valeur_graph')

    for i, row in exp_df.iterrows():
        logo = row['Exp_Et']
        if row['Exp_Et'] in ['RCT', 'Boxe Canada', 'Badminton QC', 'Soccer QC']:
            size = .3
        else:
            size = .6

        fig.add_layout_image(
            dict(source=Image.open(f'logo/{logo}.png'),
                 xref='x', yref='y',
                 xanchor='center', yanchor='middle',
                 x=row['Année'], y=row['Valeur_graph'],
                 sizex=size, sizey=size,
                 sizing='contain',
                 layer='above'))
        fig.add_shape(type='line',
                      xref='x', yref='y',
                      x0=row['Line_x0'], x1=row['Line_x1'],
                      y0=row['Line_y0'], y1=row['Line_y1'],
                      line=dict(color='#000000', width=1))
        
    fig.add_shape(type='line',
                  xref='x', yref='y',
                  x0=2012, x1=2024.5,
                  y0=0, y1=0,
                  line=dict(color='#4b75f6', width=2.5))
        
    fig.update_xaxes(showgrid=False, title=None)
    fig.update_yaxes(showgrid=False, showticklabels=False, title=None)
    fig.update_layout(plot_bgcolor='#747779', paper_bgcolor='#747779', xaxis=dict(tickvals=[2013, 2014, 2015, 2016, 2018, 2020, 2021, 2022, 2023]))
    fig.update_traces(customdata=exp_df, hovertemplate='<b>%{customdata[1]}</b><br><br>%{customdata[2]}<br><br>%{customdata[3]}',
                      hoverlabel=dict(bgcolor='#000000'))

    return fig


def parcours_timeline_eng():
    exp = {
        'Année': [2013, 2014, 2014, 2015, 2015, 2015, 2016, 2016, 2018, 2018, 2020, 2021, 2021, 2022, 2022,
                  2023, 2023.5, 2023, 2023.5, 2023.5, 2024, 2024],
        'Exp_Et': ['RAC Rugby', 'Université Paris V Descartes', 'Racing 92', 'Université de Poitiers', 'CREPS de Montpellier',
                   'ASBH', 'Université de Montpellier', 'Hurricanes', 'TrainingLoad Pro', 'Collège Sainte-Anne', 'Centre Universitaire de Santé McGill',
                   'Harvard University', 'Brûleurs de loups', 'CentraleSupélec', 'FFR XIII', 'Trimane', 'RCT',
                   'INS QC', 'Boxe Canada', 'Badminton QC', 'INS QC', 'Soccer QC'],
        'Poste': ['Strength & Conditioning Coach', 'Bachelor of Sciences: Applied Sports Science', 'Assistant Strength & Conditioning Coach (Academy))',
                  'University Diploma - Strength & Conditioning', 'Certificate - S&C coaching for high level athletes', 'Assistant S&C Coach (Pro)',
                  'University Diploma -  Olympic lifting and Power lifting techniques for S&C', 'Data Analyst - Sports Science<br>Assistant S&C Coach',
                  "Quantification of efforts, analysis and interpretations, programming of training and rehabilitation strategies, reporting, monitoring, data-mining", 'Lead Strength & Conditioning Coach',
                  'Databases Analyst', 'Introduction to Data Science with Python',
                  'Data Scientist R&D<br>Lead S&C Coach (Pro & Academy)', 'Master Data Science (OpenClassrooms partnership)', 'Data Analyst - Sports Science',
                  'Data Scientist - Sport Performance', 'Club partnership to develop the application', 'Data Scientist - Sport & Medicine', 'Updating a daily monitoring application', 
                  'Applications creation<br>- Tagging application for game stats recording<br>- Game statistics analysis application', 'Data Scientist', 'Data Manager'],
        'Projet': ['', '', '', '', '', '', '',
                   'Data structuring management for daily monitoring<br>- Data Extraction, transformation, Loading (ETL)<br>- Descriptive and longitudinal analyses (timeseries)<br>- Daily reporting',
                   '', '',
                   'Supply chain database management<br>- Creation of a database for inventory management and warehouse distribution<br>- Daily update and reporting',
                   '',
                   'Data structuring management for daily monitoring and cycle analysis<br>- Data Extraction, transformation, Loading (ETL)<br>- Descriptive and longitudinal analyses (timeseries)<br>- Machine learning (clustering, dimensionality reduction)<br>- Daily, weekly and monhtly reporting',
                   '',
                   'Management of data structuring and deployment for daily monitoring<br>- Data Extraction, transformation, Loading (ETL)<br>- Descriptive and longitudinal analyses (timeseries)<br>- Reporting quotidient et rapport bilan post-compétition',
                   'Development of an analytical application for sports organizations<br>- Development of support software<br>- Design and development of data collection, control and storage processes<br>- Production of steering dashboards<br>- Statistical analysis and machine learning',
                   '', 
                   'Structuring the Data Science department<br>- Auditing and cleaning of scientific databases<br>- Restructuring and development of software solutions to optimize data workflow<br>- Development of models facilitating the interpretation of data or for prediction purposes',
                   '', '', '', ''],
        'Valeur_graph': [1, -1, 1, -1, -2, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, 1, 1, 2, 1.7, 2.3, 1, 2],
        'Line_x0': [2013, 2014, 2014, 2015, 2015, 2015, 2016, 2016, 2018, 2018, 2020, 2021, 2021, 2022, 2022,
                    2023, 2023.25, 2023, 2023.18, 2023.18, 2024, 2024],
        'Line_x1': [2013, 2014, 2014, 2015, 2015, 2015, 2016, 2016, 2018, 2018, 2020, 2021, 2021, 2022, 2022,
                    2023, 2023.35, 2023, 2023.38, 2023.38, 2024, 2024],       
        'Line_y0': [0, 0, 0, 0, -1.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1.3, 2, 2, 0, 1.3],
        'Line_y1': [.7, -.7, .7, -.7, -1.7, .7, -.7, .76, -.79, .7, .7, -.7, .7, -.7, .7, .7, 1, 1.7, 1.7, 2.3, .7, 1.7]
       }

    exp_df = pd.DataFrame(exp)

    fig = px.scatter(exp_df, x='Année', y='Valeur_graph')

    for i, row in exp_df.iterrows():
        logo = row['Exp_Et']
        if row['Exp_Et'] in ['RCT', 'Boxe Canada', 'Badminton QC', 'Soccer QC']:
            size = .3
        else:
            size = .6

        fig.add_layout_image(
            dict(source=Image.open(f'logo/{logo}.png'),
                 xref='x', yref='y',
                 xanchor='center', yanchor='middle',
                 x=row['Année'], y=row['Valeur_graph'],
                 sizex=size, sizey=size,
                 sizing='contain',
                 layer='above'))
        fig.add_shape(type='line',
                      xref='x', yref='y',
                      x0=row['Line_x0'], x1=row['Line_x1'],
                      y0=row['Line_y0'], y1=row['Line_y1'],
                      line=dict(color='#000000', width=1))
        
    fig.add_shape(type='line',
                  xref='x', yref='y',
                  x0=2012, x1=2024.5,
                  y0=0, y1=0,
                  line=dict(color='#4b75f6', width=2.5))
        
    fig.update_xaxes(showgrid=False, title=None)
    fig.update_yaxes(showgrid=False, showticklabels=False, title=None)
    fig.update_layout(plot_bgcolor='#747779', paper_bgcolor='#747779', xaxis=dict(tickvals=[2013, 2014, 2015, 2016, 2018, 2020, 2021, 2022, 2023]))
    fig.update_traces(customdata=exp_df, hovertemplate='<b>%{customdata[1]}</b><br><br>%{customdata[2]}<br><br>%{customdata[3]}',
                      hoverlabel=dict(bgcolor='#000000'))

    return fig