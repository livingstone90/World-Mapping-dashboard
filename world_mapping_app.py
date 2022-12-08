import plotly.express as px
import geopandas as gpd
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import os


st.title("World Mapping")

world_cord = pd.read_csv("D:/Dashboard/world_mapping/world_country.csv")

EA_cord = pd.read_csv("./data/east_africa.csv")

# px.set_mapbox_access_token(open("open-street-map").read())
#fig = go.Figure()
fig = px.scatter_mapbox(world_cord,
                        lat=world_cord.latitude,
                        lon=world_cord.longitude,
                        hover_name="country",
                        zoom=1)
fig.update_layout(mapbox_style='open-street-map')
fig.update_layout(height=500, width=1000)
# fig.write_image("images/fig1.png")
# fig.show()

st.plotly_chart(fig,  use_container_width=False)

with st.expander("Expand for East Africa Map"):
    fig = px.scatter_mapbox(EA_cord,
                            lat=EA_cord.latitude,
                            lon=EA_cord.longitude,
                            hover_name="country",
                            color_continuous_scale=px.colors.cyclical.IceFire, size_max=15,
                            zoom=5)
    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(height=500, width=1000)
    # fig.write_image("images/fig1.png")
    # fig.show()

    st.plotly_chart(fig,  use_container_width=False)
    st.write('Expand to view')
