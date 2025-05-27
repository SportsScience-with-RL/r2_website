import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

def page_fr(graph):
    menu = option_menu(menu_title='',
                   options=['Qui suis-je ?', 'Prestations', 'Parcours/Projets', 'Contact'],
                   icons=['person-bounding-box', 'cart-plus', 'collection', 'chat-left-text'],
                   default_index=1, orientation='horizontal')

    if menu == 'Qui suis-je ?':
        _, main, _ = st.columns([.25/2, .75, .25/2])
        with main:
            st.write('')
            _, ci, _, ct = st.columns([.1, .2, .05, .65])
            with ci:
                st.image('img/RL.png', width=200)
            with ct:
                st.write('')
                st.write('')
                st.markdown("""<div style="text-align: justify;">Je m'appelle Raphaël Lagarde.
                            Issu d'une formation universitaire dans le domaine sportif (STAPS : Sciences et Techniques des Activités Physiques et Sportives), j'ai commencé ma carrière professionnelle en tant préparateur physique.
                            Grand amoureux du sport, que j'ai pratiqué depuis l'enfance (badminton, hockey sur gazon et en salle, capoeira), je voulais continuer mes études supérieures dans cette voie là.</div>""", unsafe_allow_html=True)
            
            ct, _, ci = st.columns([.65, .05, .3])
            with ct:
                st.write('')
                st.markdown("""<div style="text-align: justify;">J'ai débuté donc ma carrière dans le rugby (elle continuera principalement dans cette discipline) au niveau amateur et j'évolue au fur et à mesure jusqu'au niveau niveau professionnel en Nouvelle Zélande (Hurricanes).
                            C'est d'ailleurs lors de cette expérience au pays du long nuage blanc que je découvre l'utilisation des données et qui va faire naitre une véritable passion ajoutée à celle du sport.
                            Au début je me forme seul à ce nouveau domaine, puis j'ai l'occasion de suivre des cours/séminaires et finalement d'obtenir une formation diplômante.
                            Aujourd'hui, je voue un réel engouement à ces données, je suis en admiration devant les possibilités offertes par leur utilisation aussi bien sur l'information obtenue que sur la technique pure comme la manipulation de celles-ci.</div>""", unsafe_allow_html=True)
            with ci:
                st.write('')
                st.write('')
                st.image('img/IMG_NZ.jpg')
            st.markdown("""<div style="text-align: justify;"><br>Pour en apprendre plus sur mon parcours, vous pouvez vous rendre à l'onglet <b>Parcours/Projets</b>.</div>""", unsafe_allow_html=True)
            st.write('')
            st.write('')
            st.subheader('Mon expertise')
            st.write('')
            st.markdown("""<div style="text-align: justify;">Ma volonté de me lancer comme freelance/consultant est venue depuis mon expérience à l'INS Québec.
                        Travailler sur plusieurs projets et plusieurs sports a été très enrichissant et stimulant. M'ouvrir à des contrats de consultant va me permettre de continuer à collaborer avec une multitude de structures/personnes et m'enrichir des contextes tous uniques.
                        <br><br>Mon expertise métier est évidemment celle du sport. Ce domaine m'a permis de m'intéresser et de composer avec d'autres domaines : la physiologie, la santé, la médecine, la psychologie ou encore la sociologie.
                        C'est par la richesse de ces domaines "sous-jacents" que mon expertise métier peut s'appliquer à bien d'autres spécialités.
                        <br><br>Mon expertise technique accorde une importance au cycle de vie de la donnée en adoptant les meilleures pratiques : sa mesure, son stockage, sa transformation éventuelle, son accessibilité, sa sécurité, sa visualisation, son analyse et finalement son interprétation. 
                        <br><br>La combinaison de ces deux expertises me permet de proposer des outils propres à chacun : j'ai la conviction que toute structure, selon son contexte (budget), peut et doit avoir accès à des solutions technologiques.
                        Mes prestations s'organisent autour de trois axes pouvant se compléter :
                        <br>- Développement de solutions technologiques
                        <br>- Accompagnement de projet
                        <br>- Formation
                        <br><br>Pour découvrir les différentes prestations proposées, vous pouvez vous rendre à l'onglet <b>Prestations</b>.</div>""", unsafe_allow_html=True)

    elif menu == 'Prestations':
        _, main, _ = st.columns([.25/2, .75, .25/2])
        with main:
            st.write('')
            st.markdown("""<div style="text-align: justify;">Mes offres de prestations sont la combinaison d'une expertise métier dans le sport, la santé et les sciences sociales ; et d'une expertise technique adoptant continuellement les meilleures pratiques. Mes services s'organisent autour de trois axes pouvant se compléter :
                        <br>- Développement de solutions technologiques
                        <br>- Accompagnement de projet
                        <br>- Formation</div>""", unsafe_allow_html=True)
            st.write('')
            with st.expander('**DEVELOPPEMENT DE SOLUTIONS TECHNOLOGIQUES**'):
                st.write('')
                st.markdown("""<div style="text-align: justify;">Cette prestation concerne la création et le développement de solutions analytiques et de visualisation. Cela peut comprendre :
                            <br>- La création de tableaux de bord
                            <br>- La création de pipeline pour automatiser des calculs, des agrégations etc.
                            <br>- La création d'une application permettant d'envoyer des données vers une base de données
                            <br>- La création d'application répondant à des besoins spécifiques
                            <br>- Etc.</div>""", unsafe_allow_html=True)
                st.markdown("""<div style="text-align: justify;"><br><b>Exemples de cas de figure :</b></div>""", unsafe_allow_html=True)
                st.markdown("""<div style="text-align: right;"><br><i>"Nous recoltons nos données dans une base de données et nous souhaitons créer un outil nous permettant de visualiser, analyser et interpréter"
                            <br><br><i>"Nous avons un processus, se faisant à la main, pour alimenter notre base de données principale. Cependant c'est assez chronophage, nous souhaitons automatiser le processus à l'aide d'une pipeline"
                            <br><br><i>"Actuellement nos données sont stockées dans des tableurs Excel ou Sheet. Nous aimerions une technologie pour le stockage et l'accès de nos données. Nous souhaitons également intégrer une ou plusieurs pipelines pour automatiser le traitement de nos données (calculs etc.)"
                            <br><br>"Nous utilisons déjà un outil pour récolter certaines données. Cependant nous aimerions développer un outil plus modulable répondant davantage à nos besoins"
                            <br><br>"Nous souhaitons développer un outil nous permettant de récupérer de l'information et des données sur X situation"</i></div>""", unsafe_allow_html=True)
                st.write('')
            with st.expander('**ACCOMPAGNEMENT**'):
                st.write('')
                st.markdown("""<div style="text-align: justify;">Cette prestation concerne l'accompagnement d'une structure avec des outils et solutions déjà en place ou l'accompagnement avec le développement de solutions souhaitées par la structure et/ou proposées ci-dessus. Cela peut comprendre :
                            <br>- Audit de la structure
                            <br>- Apport d'expérience et expertise supplémentaires sur les processus déjà en place
                            <br>- Production de rapports hebdomadaires, mensuels etc.
                            <br>- Accompagnement scientifique et statistique sur projet de mémoire
                            <br>- Revue statistique de projet de mémoire
                            <br>- Etc.</div>""", unsafe_allow_html=True)
                st.markdown("""<div style="text-align: justify;"><br><b>Exemples de cas de figure :</b></div>""", unsafe_allow_html=True)
                st.markdown("""<div style="text-align: right;"><br><i>"Nous souhaitons avoir un oeil extérieur sur nos pratiques. Nous souhaitons une certaine expertise métier et technique pour un avis constructif et suivre d'éventuels axes d'amélioration"
                            <br><br><i>"Notre budget ne nous permet pas d'employer quelqu'un pour gérer notre pôle Data. Nous souhaitons donc nous attacher les services d'un consultant"
                            <br><br>"Je suis athlète individuel et je cherche un professionnel pour s'occuper de mon suivi"
                            <br><br><i>"Je prépare un mémoire pour mon diplôme et je souhaite un accompagnement dans ma réflexion et mes analyses statistiques"
                            <br><br>"Je viens de finaliser la rédaction de mon mémoire et je souhaite avoir une relecture de ma partie analyse statistique"</i></div>""", unsafe_allow_html=True)
                st.write('')
            with st.expander('**FORMATION**'):
                st.write('')
                st.markdown("""<div style="text-align: justify;">Cette prestation concerne l'encadrement d'apprentissages orientés sur l'utilisation des données. Cela peut comprendre :
                            <br>- Apprentissage de langage de programmation
                            <br>- Formation interne de la structure
                            <br>- Création d'E-book en accompagnement de la formation
                            <br>- Formation de groupes et/ou en solitaire : cas pratiques du domaine souhaité, exercices, suivi etc.
                            <br>- Etc.</div>""", unsafe_allow_html=True)
                st.markdown("""<div style="text-align: justify;"><br><b>Exemples de cas de figure :</b></div>""", unsafe_allow_html=True)
                st.markdown("""<div style="text-align: right;"><br><i>"Je souhaite apprendre Python en étant encadré par quelqu'un"
                            <br><br><i>"Je souhaite appprendre la programmation. Il y a beaucoup d'offres sur internet et je crains d'être un peu laissé à moi-même"
                            <br><br><i>"Nous souhaitons former nos staffs en interne sur la thématique X avec l'utilisation des données"
                            <br><br>"Nous cherchons un intervenant sur la thématique X pour notre organisme de formation"
                            <br><br>"Je souhaite en apprendre davantage sur l'utilisation des données dans mon domaine avec de vrais cas pratiques"</i></div>""", unsafe_allow_html=True)
                st.write('')
            st.write('')
            st.markdown('''<style>p {text-align: center;}</style>''', unsafe_allow_html=True)
            st.success('''**Les prestations sont facturables pour toutes les structures et personnes quelle que soit leur situation géographique.**''')
            st.write('')
            st.info('''Vous pouvez me contacter pour toute demande de prestation non répertoriée ci-dessous.
                    Il s'agit d'une liste non exhaustive permettant d'avoir une vision globale des offres proposées.
                    Dans l'onglet **Parcours/Projets** se trouvent quelques exemples de solutions réalisées.
                    \n**DEMANDE DE PRESTATION**
                    \nPour une demande de prestation ou d'information complémentaire, suivez l'onglet **Contact**.
                    Vous pourrez m'y expliquer votre projet et la prestation vous intéressant dès cette prise de contact. Je vous ferai suivre un formulaire me permettant d'avoir un maximum d'informations, afin d'organiser une **première rencontre**.
                    Celle-ci est **gratuite** et **sans engagement** : elle nous permettra de convenir des modalités de la collaboration et/ou des étapes du projet.
                    \n**TARIFS**
                    \nN'hésitez pas à me communiquer votre budget lors la prise de contact (il sera demandé dans le formulaire). Les prix sont **adaptés** à vos besoins, au projet, sa durée etc. et surtout votre **contexte/budget**.''')
            st.write('')
            st.subheader('Stack technique principale')
            st.write('')
            cp, cr, cns, ce, cst, csh, cpbi = st.columns(7)
            cp.image('img/stack/python.png', width=90)
            cr.image('img/stack/r.png', width=90)
            cns.image('img/stack/nosql.png')
            ce.image('img/stack/excel.png')
            cst.image('img/stack/streamlit.png')
            csh.image('img/stack/shiny.png')
            cpbi.image('img/stack/powerbi.png')

    elif menu == 'Parcours/Projets':
        _, main, _ = st.columns([.25/2, .75, .25/2])
        with main:
            st.subheader('Mon Parcours')
            st.write('')
            st.markdown("""<div style="text-align: justify;">Ci-dessous vous pouvez trouver la chronologie de mon parcours de formation et professionnel.
                        En vous plaçant sur les logos des différentes structures et institutions vous verrez apparaitre le poste occupé (accompagné des responsabilités, des missions ; ou thématique de la formation suivie).</div>""", unsafe_allow_html=True)
            st.write('')
            st.write('')
        st.plotly_chart(graph, use_container_width=True)
        st.write('')
        st.write('')
        _, main, _ = st.columns([.25/2, .75, .25/2])
        with main:
            st.subheader('Mes Projets')
            st.write('')
            st.markdown("""<div style="text-align: justify;">Ci-dessous vous pouvez trouver des exemples de projets professionnels et personnels réalisés.
                        Ceux-ci permettent d'avoir une idée des produits et solutions réalisables à travers les différentes prestations.</div>""", unsafe_allow_html=True)
            st.write('')
            st.write('---')
            st.write('')
            st.success('**ATHLETE MANAGEMENT SYSTEM (AMS)**')
            c_ams = st.columns(4)
            c_ams[0].info('**CENTRALISER**')
            c_ams[1].info('**VISUALISER**')
            c_ams[2].info('**INFORMER**')
            c_ams[3].info('**REGULER**')
            st.markdown("""<div style="text-align: justify;">- Création d'un AMS permettant de centraliser un maximum de données pour leur visualisation et analyse.
                        <br>- Visualisations et informations de groupes/d'équipe et individuel.
                        <br>- Suivi longitudinal des marqueurs choisis.
                        <br>- Suivi des variations.
                        <br>- Extraction des données en fichier brut.</div>""", unsafe_allow_html=True)
            cv1, _, cv2 = st.columns([.45, .1, .45])
            with cv1:
                st.write('')
                st.video(open('video/ams.mp4', 'rb').read())
            with cv2:
                st.video(open('video/neuro.mp4', 'rb').read())
            st.write('')
            st.write('---')
            st.write('')
            st.warning('**GPS - SUIVI & PROGRAMMATION DE SEANCE**')
            c_gps = st.columns(3)
            c_gps[0].info('**SUIVRE**')
            c_gps[1].info('**PROGRAMMER**')
            c_gps[2].info('**REGULER**')
            st.markdown("""<div style="text-align: justify;">- Création d'un tableau de bord pour suivi des marqueurs choisis.
                        <br>- Visualisations et informations de groupes/d'équipe et individuel.
                        <br>- Suivi longitudinal des marqueurs choisis.
                        <br>- Suivi des variations.
                        <br>- Création d'une application de programmation de séance (% en rapport à match(s) référence(s)).</div>""", unsafe_allow_html=True)
            st.write('')
            ci, _, cv = st.columns([.45, .1, .45])
            with ci:
                st.image('img/projets/gps.PNG')
            with cv:
                st.video(open('video/gps.mp4', 'rb').read())
            st.write('')
            st.write('---')
            st.write('')
            st.success('**WELLNESS/MARQUEURS QUALITATIFS - SUIVI & QUESTIONNAIRE**')
            c_w = st.columns(4)
            c_w[0].info('**RECOLTER**')
            c_w[1].info('**SUIVRE**')
            c_w[2].info('**ANALYSER**')
            c_w[3].info('**REGULER**')
            c1, _, c2 = st.columns([.55, .1, .35])
            with c1:
                st.markdown("""<div style="text-align: justify;">- Création d'un tableau de bord pour suivi type Wellness.
                            <br>- Visualisations et informations de groupes/d'équipe et individuel.
                            <br>- Suivi longitudinal des marqueurs.
                            <br>- Suivi des variations.
                            <br>- Création de questionnaire sur-mesure (choix des marqueurs).</div>""", unsafe_allow_html=True)
                st.write('')
                st.image('img/projets/wellness.png', width=500)
            with c2:
                st.write('')
                st.write('')
                st.image('img/projets/questionnaire.PNG', width=300)
            st.write('')
            cv1, ct, cv2 = st.columns([.4, .2, .4])
            with cv1:
                st.video(open('video/clustering.mp4', 'rb').read())
            with ct:
                st.markdown("""<div style="text-align: center;">Identification de groupes et caractéristation des groupes</div>""", unsafe_allow_html=True)
            with cv2:
                st.video(open('video/clustering2.mp4', 'rb').read())
            st.write('')
            st.write('---')
            st.write('')
            ct, _, ci = st.columns([.45, .05, .5])
            with ci:
                st.image('img/projets/tagging.png')
            with ct:
                st.write('')
                st.write('')
                st.write('')
                st.write('')
                st.markdown("""<div style="text-align: justify;">- Création d'une application de saisie (tagging) de compétition.
                            <br>- Identification des situations de compétitions.
                            <br>- Identification des gestes techniques.
                            <br>- Disposition et boutons de tagging sur-mesure.</div>""", unsafe_allow_html=True)
            st.write('')
            cv1, ct, cv2 = st.columns([.4, .2, .4])
            with cv1:
                st.video(open('video/6nations.mp4', 'rb').read())
            with ct:
                st.markdown("""<div style="text-align: center;">Analyses de compétition</div>""", unsafe_allow_html=True)
            with cv2:
                st.video(open('video/ffr13.mp4', 'rb').read())

    elif menu == 'Contact':
        st.write('')
        _, main, _ = st.columns([.25/2, .75, .25/2])
        with main:
            code_li = '''from linkedin import profile, page
            \nprint(profile)\nprint(page)'''
            code_mail = '''library(email)
            \nprint(address)'''
            code_wa = '''SELECT whatspp_number, canadian_number\nFROM phone_numbers'''
            cc, ci, ct = st.columns([.4, .1, .5])
            with cc:
                st.write('')
                st.code(code_li, language='python')
            with ci:
                st.write('')
                st.write('')
                st.image('img/contact/LinkedIn.png', width=90)
            with ct:
                st.info("**https://www.linkedin.com/in/raphael-lagarde-511b40100/**")
                st.info("**https://www.linkedin.com/company/r2traininghub/**")
            # st.write('---')
            # cc, ci, ct = st.columns([.4, .1, .5])
            # with cc:
            #     st.code(code_mail, language='r')
            # with ci:
            #     st.image('img/contact/mail.png')
            # with ct:
            #     st.write('')
            #     st.warning("**datadella.consulting@gmail.com**")
            st.write('---')
            cc, ci, ct = st.columns([.4, .1, .5])
            with cc:
                st.write('')
                st.code(code_wa, language='sql')
            with ci:
                st.write('')
                st.image('img/contact/whatsapp.png')
            with ct:
                st.success('''**(+33) 7 67 60 57 92**
                           \n**(+1) 514 558 5015**''')
            st.write('---')
            cl, ci, ct = st.columns([.55, .05, .4])
            with cl:
                st.image('img/contact/loc.png')
                st.write('**Montréal QC, Canada**')
            with ci:
                st.image('img/contact/github.png', width=40)
            with ct:
                st.write('https://github.com/SportsScience-with-RL')
