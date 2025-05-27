import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

def page_eng(graph):
    menu = option_menu(menu_title='',
                   options=['Who am I?', 'Services', 'Career/Projects', 'Contact'],
                   icons=['person-bounding-box', 'cart-plus', 'collection', 'chat-left-text'],
                   default_index=1, orientation='horizontal')

    if menu == 'Who am I?':
        _, main, _ = st.columns([.25/2, .75, .25/2])
        with main:
            st.write('')
            _, ci, _, ct = st.columns([.1, .2, .05, .65])
            with ci:
                st.image('img/RL.png', width=200)
            with ct:
                st.write('')
                st.write('')
                st.markdown("""<div style="text-align: justify;">My name is Raphaël Lagarde.
                            With a university degree in sports (Applied Sports Science), I started my professional career as a strength and conditioning coach.
                            Great lover of sport, which I have practiced since childhood (badminton, field and indoor hockey, capoeira). I wanted to continue my higher education in that direction.</div>""", unsafe_allow_html=True)
            
            ct, _, ci = st.columns([.65, .05, .3])
            with ct:
                st.write('')
                st.markdown("""<div style="text-align: justify;">I began my career in rugby (it will continue mainly in this sport) at amateur level and gradually progressed to professional level in New Zealand (Hurricanes).
                            It was during this experience in the land of the long white cloud that I discovered the use of data. This is where my passion appeared in addition to the one for sport.
                            At first, I trained myself in this new field, then I undertook courses/seminars and finally to graduate a degree.
                            Today I'm fascinated by the possibilities offered by the use and integration of data, both in terms of the information obtained and the pure technique such as data manipulation.</div>""", unsafe_allow_html=True)
            with ci:
                st.write('')
                st.write('')
                st.image('img/IMG_NZ.jpg')
            st.markdown("""<div style="text-align: justify;"><br>To learn more about my journey, you can go to the <b>Career/Projects</b> tab.</div>""", unsafe_allow_html=True)
            st.write('')
            st.write('')
            st.subheader('My expertise')
            st.write('')
            st.markdown("""<div style="text-align: justify;">My desire to lauch myself as a freelance/consultant came since my experience at INS Québec.
                        Working on several projects and several sports was very enriching and stimulating.
                        Opening up to consultancy contracts will enable me to continue collaborating with a multitude of structures and people, and to enrich my knowledge of unique contexts.
                        <br><br>My business expertise is obviously in sports.
                        And this field has enabled me to take an interest in and work with other fields: physiology, health, medicine, psychology and sociology.
                        It's because of the richness of these "underlying" fields that my business expertise can be applied to many other areas.
                        <br><br>My technical expertise focuses on the data lifecycle while adopting best practices: measurement, storage, transformation, accessibility, security, visualization, analysis and interpretation. 
                        <br><br>The combination of these two expertises enables me to offer unique solutions to each individual: I'm convinced that any structure, depending on its context (budget), can and should have access to technological solutions.
                        My services are organized around three axes which can complement each other:
                        <br>- Development of technological solutions
                        <br>- Project support
                        <br>- Education/training
                        <br><br>To find out about the different services offered, please go to the <b>Services</b> tab.</div>""", unsafe_allow_html=True)

    elif menu == 'Services':
        _, main, _ = st.columns([.25/2, .75, .25/2])
        with main:
            st.write('')
            st.markdown("""<div style="text-align: justify;">My offers are the combination of a professional expertise in sport, health and social sciences; and a technical expertise continually adopting best practices.
                        My services are organized around three axes which can complement each other:
                        <br>- Development of technological solutions
                        <br>- Project support
                        <br>- Education/training</div>""", unsafe_allow_html=True)
            st.write('')
            with st.expander('**DEVELOPMENT OF TECHNOLOGICAL SOLUTIONS**'):
                st.write('')
                st.markdown("""<div style="text-align: justify;">This service covers the creation and development of analytical and visualization solutions. This may include:
                            <br>- Dashboard creation
                            <br>- Creation of pipelines to automate calculations, aggregations, etc.
                            <br>- Creation of an application to send data to a database
                            <br>- Creation of applications to meet specific needs
                            <br>- Etc.</div>""", unsafe_allow_html=True)
                st.markdown("""<div style="text-align: justify;"><br><b>Examples of scenarios:</b></div>""", unsafe_allow_html=True)
                st.markdown("""<div style="text-align: right;"><br><i>"We collect our data in a database and would like to create a tool that allows us to visualize, analyze and interpret it"
                            <br><br><i>" We have a manual process for feeding our main database. However, this is rather time-consuming, so we'd like to automate the process using a pipeline"
                            <br><br><i>"Currently our data is stored in Excel or Sheet spreadsheets. We'd like a technology for storing and accessing our data. We would also like to integrate one or more pipelines to automate the processing of our data (calculations etc.)"
                            <br><br>"We already use a tool to collect certain data. However, we'd like to develop a more modular tool that better meets our needs"
                            <br><br>"We would like to develop a tool to retrieve information and data on X situation"</i></div>""", unsafe_allow_html=True)
                st.write('')
            with st.expander('**PROJECT SUPPORT**'):
                st.write('')
                st.markdown("""<div style="text-align: justify;">This service concerns the support of a structure with tools and solutions already in place, or support with the development of solutions desired by the structure and/or proposed above. This may include:
                            <br>- Structure audit
                            <br>- Additional experience and expertise on existing processes
                            <br>- Production of weekly and monthly reports, etc.
                            <br>- Scientific and statistical support for Master projects
                            <br>- Statistical review of Master projects
                            <br>- Etc.</div>""", unsafe_allow_html=True)
                st.markdown("""<div style="text-align: justify;"><br><b>Examples of scenarios:</b></div>""", unsafe_allow_html=True)
                st.markdown("""<div style="text-align: right;"><br><i>"We're looking for an outside perspective on our practices. We would like some business and technical expertise to give us a constructive opinion and to monitor possible areas for improvement"
                            <br><br><i>"Our budget doesn't allow us to employ someone to manage our Data department. We are therefore looking to hire the services of a consultant"
                            <br><br>"I am an individual athlete and I am looking for a professional to manage my monitoring"
                            <br><br><i>"I'm preparing a dissertation for my degree and would like support in my thinking and statistical analysis"
                            <br><br>"I have just finished writing my dissertation and would like to have my statistical analysis section proofread"</i></div>""", unsafe_allow_html=True)
                st.write('')
            with st.expander('**EDUCATION/TRAINING**'):
                st.write('')
                st.markdown("""<div style="text-align: justify;">This service concerns the supervision of apprenticeships focused on the use of data. This may include:
                            <br>- Learning a programming language
                            <br>- Staff training
                            <br>- Creation of E-book supporting the training courses
                            <br>- Group and/or individual training: case studies in the desired field, exercises, follow-up, etc.
                            <br>- Etc.</div>""", unsafe_allow_html=True)
                st.markdown("""<div style="text-align: justify;"><br><b>Examples of scenarios:</b></div>""", unsafe_allow_html=True)
                st.markdown("""<div style="text-align: right;"><br><i>"I'd like to learn Python under someone's supervision"
                            <br><br><i>"I want to learn programming. There are a lot of offers on the internet and I'm afraid I'll be left on my own"
                            <br><br><i>"We would like to train our staff to the use of data on the X topic"
                            <br><br>"I'd like to learn more about the use of data in my field, with real case studies"</i></div>""", unsafe_allow_html=True)
                st.write('')
            st.markdown('''<style>p {text-align: center;}</style>''', unsafe_allow_html=True)
            st.success('''**Services are billable for all structures and individuals, regardless of their geographical location.**''')
            st.write('')
            st.info('''You can contact me for any service not listed below.
                    This is a non-exhaustive list to give you an overview of the services we offer.
                    In the **Career/Projects** tab, you'll find examples of solutions I've implemented.
                    \n**SERVICE REQUEST**
                    \nTo request a service or additional information, follow the **Contact** tab.
                    You can tell me about your project and the service you're interested in as soon as you get in touch.
                    I'll send you a form so that I can get as much information as possible in order to schedule a first meeting.
                    This first meeting is **free** and **without commitment**: it will enable us to agree on the terms of the collaboration and/or the stages of the project.
                    \n**PRICES**
                    \nPlease let me know your budget when you contact me (it will be requested in the form). Prices are **adapted** to your needs, the project, its duration, etc. and above all your **context/budget**.''')
            st.write('')
            st.subheader('Main Tech Stack')
            st.write('')
            cp, cr, cns, ce, cst, csh, cpbi = st.columns(7)
            cp.image('img/stack/python.png', width=90)
            cr.image('img/stack/r.png', width=90)
            cns.image('img/stack/nosql.png')
            ce.image('img/stack/excel.png')
            cst.image('img/stack/streamlit.png')
            csh.image('img/stack/shiny.png')
            cpbi.image('img/stack/powerbi.png')

    elif menu == 'Career/Projects':
        _, main, _ = st.columns([.25/2, .75, .25/2])
        with main:
            st.subheader('My Path')
            st.write('')
            st.markdown("""<div style="text-align: justify;">Below you can find a chronology of my training and professional career.
                        By placing your cursor over the logos of the various structures and institutions, you'll see the position held as well as the responsibilities and missions or the training course followed.</div>""", unsafe_allow_html=True)
            st.write('')
            st.write('')
        st.plotly_chart(graph, use_container_width=True)
        st.write('')
        st.write('')
        _, main, _ = st.columns([.25/2, .75, .25/2])
        with main:
            st.subheader('My Projects')
            st.write('')
            st.markdown("""<div style="text-align: justify;">Below you'll find examples of the professional and personal projects I've carried out.
                        These projects give an idea of the products and solutions that can be achieved through the various services I offer.</div>""", unsafe_allow_html=True)
            st.write('')
            st.write('---')
            st.write('')
            st.success('**ATHLETE MANAGEMENT SYSTEM (AMS)**')
            c_ams = st.columns(4)
            c_ams[0].info('**CENTRALIZE**')
            c_ams[1].info('**VISUALIZE**')
            c_ams[2].info('**INFORM**')
            c_ams[3].info('**MANAGE**')
            st.markdown("""<div style="text-align: justify;">- Creation of an AMS to centralize a maximum amount of data for visualization and analysis.
                            <br>- Group/team and individual visualizations and information.
                            <br>- Longitudinal monitoring of selected markers.
                            <br>- Timeseries analysis
                            <br>- Extraction of raw data.</div>""", unsafe_allow_html=True)
            cv1, _, cv2 = st.columns([.45, .1, .45])
            with cv1:
                st.write('')
                st.video(open('video/ams.mp4', 'rb').read())
            with cv2:
                st.video(open('video/neuro.mp4', 'rb').read())
            st.write('')
            st.write('---')
            st.write('')
            st.warning('**GPS - MONITORING & SESSION PLANNER**')
            c_gps = st.columns(3)
            c_gps[0].info('**MONITOR**')
            c_gps[1].info('**PROGRAM**')
            c_gps[2].info('**MANAGE**')
            st.markdown("""<div style="text-align: justify;">- Creation of a dashboard to monitor selected markers.
                            <br>- Group/team and individual visualizations and information.
                            <br>- Longitudinal monitoring of selected markers.
                            <br>- Timeseries analysis
                            <br>- Creation of a session programmer application (% in relation to match(es) reference(s)).</div>""", unsafe_allow_html=True)
            st.write('')
            ci, _, cv = st.columns([.45, .1, .45])
            with ci:
                st.image('img/projets/gps.PNG')
            with cv:
                st.video(open('video/gps.mp4', 'rb').read())
            st.write('')
            st.write('---')
            st.write('')
            st.success('**WELLNESS/QUESTIONNAIRE - MONITORING**')
            c_w = st.columns(4)
            c_w[0].info('**COLLECT**')
            c_w[1].info('**MONITOR**')
            c_w[2].info('**ANALYZE**')
            c_w[3].info('**MANAGE**')
            c1, _, c2 = st.columns([.55, .1, .35])
            with c1:
                st.markdown("""<div style="text-align: justify;">- Creation of a Wellness dashboard.
                            <br>- Group/team and individual visualizations and information.
                            <br>- Longitudinal monitoring of markers.
                            <br>- Timeseries analysis
                            <br>- Creation of customized questionnaires (choice of markers).</div>""", unsafe_allow_html=True)
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
                st.markdown("""<div style="text-align: center;">Group identification and characterization</div>""", unsafe_allow_html=True)
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
                st.markdown("""<div style="text-align: justify;">- Creation of a competition tagging application.
                            <br>- Identify competition situations.
                            <br>- Identification of technical actions.
                            <br>- Custom layout and tagging buttons.</div>""", unsafe_allow_html=True)
            st.write('')
            cv1, ct, cv2 = st.columns([.4, .2, .4])
            with cv1:
                st.video(open('video/6nations.mp4', 'rb').read())
            with ct:
                st.markdown("""<div style="text-align: center;">Competition analysis</div>""", unsafe_allow_html=True)
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
            code_wa = '''SELECT whatsapp_number, canadian_number\nFROM phone_numbers'''
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
            st.write('---')
            # cc, ci, ct = st.columns([.4, .1, .5])
            # with cc:
            #     st.code(code_mail, language='r')
            # with ci:
            #     st.image('img/contact/mail.png')
            # with ct:
            #     st.write('')
            #     st.warning("**datadella.consulting@gmail.com**")
            # st.write('---')
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
            cl, ci, ct = st.columns([.6, .05, .35])
            with cl:
                st.image('img/contact/loc.png')
                st.write('**Montréal QC, Canada**')
            with ci:
                st.image('img/contact/github.png', width=40)
            with ct:
                st.write('https://github.com/SportsScience-with-RL')
