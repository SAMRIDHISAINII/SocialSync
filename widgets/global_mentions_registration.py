

import streamlit as st
from resources.config import settings_core


settings = settings_core()
from resources.global_mentions import global_mention


def app():

    ########## NEW GLOBAL MENTIONS
    #####

    ## Title
    st.markdown("#### New Global ID")

    ## Global IDs 
    gID_input = st.text_input(label="Global ID",value=settings.new_global_id_message, key="global_id_new_register")
    
    ## Create Setting Layout
    col1, col2 = st.columns(2)

    ## Platform
    with col1:
        gID_platform_data = st.text_input(label="Platform", value=settings.new_gid_mention_platform_message, key=f"global_id_new_register_platform")

    ## Platform ID
    with col2:
        gID_platform_data_id = st.text_input(label="Platform ID", value=settings.new_gid_mention_platform_id_message, key=f"global_id_new_register_platform_ID")

    ## Dividers
    st.markdown(f"-----")

    ## Check for new data
    if not settings.new_gid_mention_platform_id_message == gID_platform_data_id and not settings.new_gid_mention_platform_message == gID_platform_data and not gID_input == settings.new_global_id_message:

        # Log Data
        return global_mention(gID_input,[[gID_platform_data,gID_platform_data_id]])

    ## No New Data
    else:

        ## Log None
        return False