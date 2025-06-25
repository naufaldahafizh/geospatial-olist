import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Load data customer dan seller yang sudah diberi lat/lng
@st.cache_data
def load_data():
    df_customers = pd.read_csv("./data/olist_customers_dataset.csv")
    df_sellers = pd.read_csv("./data/olist_sellers_dataset.csv")
    df_geo = pd.read_csv("./data/olist_geolocation_dataset.csv")

    # Zip-code → koordinat
    df_geo_grouped = df_geo.groupby("geolocation_zip_code_prefix")[["geolocation_lat", "geolocation_lng"]].mean().reset_index()
    df_geo_grouped.columns = ["zip_code_prefix", "lat", "lng"]

    df_customers["zip_code_prefix"] = df_customers["customer_zip_code_prefix"]
    df_sellers["zip_code_prefix"] = df_sellers["seller_zip_code_prefix"]

    df_customers = df_customers.merge(df_geo_grouped, on="zip_code_prefix", how="left")
    df_sellers = df_sellers.merge(df_geo_grouped, on="zip_code_prefix", how="left")

    return df_customers, df_sellers

# Load data
df_customers, df_sellers = load_data()
df_customers = df_customers.dropna()
df_sellers = df_sellers.dropna()

# Sidebar
st.sidebar.title("Geospatial Analysis")
sample_size = st.sidebar.slider("Jumlah sample untuk visualisasi", 100, 3000, 1000)

# Peta
st.title("Peta Persebaran Customer & Seller")
m = folium.Map(location=[-14.2350, -51.9253], zoom_start=4)

@st.cache_data
def get_sample(df_customers, df_sellers, sample_size):
    cust_sample = df_customers.sample(n=sample_size, random_state=42)
    seller_sample = df_sellers.sample(n=sample_size, random_state=42)
    return cust_sample, seller_sample

cust_sample, seller_sample = get_sample(df_customers, df_sellers, sample_size)

# Tambahkan marker customer (biru)
for _, row in cust_sample.iterrows():
    folium.CircleMarker(
        location=(row["lat"], row["lng"]),
        radius=2,
        color='blue',
        fill=True,
        fill_opacity=0.3
    ).add_to(m)


# Tambahkan marker seller (merah)
for _, row in seller_sample.iterrows():
    folium.CircleMarker(
        location=(row["lat"], row["lng"]),
        radius=2,
        color='red',
        fill=True,
        fill_opacity=0.3
    ).add_to(m)

# Tampilkan peta
st_data = st_folium(m, width=700, height=500)

st.markdown("**Biru**: Customer • **Merah**: Seller")