# Geospatial Analysis of Brazilian E-Commerce (Olist Dataset)

This project explores the geographical distribution of customers and sellers in Brazil using the Olist dataset. The goal is to gain spatial insight for customer segmentation, shipping efficiency, and logistics strategy.

---

## Dataset

This project uses a subset of the [Olist dataset from Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), particularly:

- `olist_customers_dataset.csv`
- `olist_sellers_dataset.csv`
- `olist_geolocation_dataset.csv`

---

## Project Goal

Understand customer–seller distribution across Brazil:
- Where are most customers and sellers located?
- How far are sellers from their customers?
- How does geography impact logistics?

---

## Project Structure

| Folder | Description |
|--------|-------------|
| `data/` | Raw CSV files |
| `notebooks/` | Jupyter notebooks for EDA and distance analysis |
| `dashboard/` | Streamlit dashboard for interactive map |
| `src/` | Optional Python modules |
| `sql/` | Optional SQL-based exploration |
| `README.md` | Documentation (this file) |

---

## EDA Highlights

- Join customer & seller zip codes with their lat/lng using geolocation dataset
- Plot customer & seller distribution on Brazil map
- Calculate great-circle distance between customers and sellers
- Observe delivery distance patterns (many sellers located far from buyers)

![Map Example](![alt text](image.png))

---

## Streamlit Dashboard

A Streamlit dashboard is available to explore the location data interactively.

### To Run:

```bash
cd dashboard
streamlit run app.py
```

You can change the number of sampled points from the sidebar.