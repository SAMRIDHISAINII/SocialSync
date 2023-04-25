
import streamlit as st
import numpy as np
import pandas as pd
import time
import os
import pathlib
from resources.setup import setup_check, initialize_settings, check_first_time_setup, initialize_app


## Checking for first time setup, will generate settings file & only allow for first time setup screen
setup_check()
if check_first_time_setup():
    initialize_settings()


## Continue the imports
from resources.page_manager import PageManager
from resources.config import settings_core




settings = settings_core()
app = PageManager()




st.set_page_config(page_title="SocialSync", page_icon=None, layout='centered', initial_sidebar_state='auto', menu_items={'Get help':None,'Report a Bug':"https://github.com/Visualistic-Studios/Media-Manager/issues",'About':"https://github.com/Visualistic-Studios/Media-Manager/",})
st.header("SocialSync")


########## ADD PAGES HERE
#####

##### First Time Setup
if check_first_time_setup():

    ##### IMPORT PAGES
    from pages import app_setup

    ##### LOAD PAGES
    app.add_page("App Setup", app_setup.app)

##### Regular Application 
else:
    ##### IMPORT PAGES
    from pages import new_posts, settings_page
    
    ##### LOAD PAGES
    app.add_page("New Posts", new_posts.app)
    app.add_page("Settings", settings_page.app)


app.run()