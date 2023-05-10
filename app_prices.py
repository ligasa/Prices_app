

import streamlit as st
import pandas as pd

import streamlit as st

st.markdown("""
    <style>
        /* nastavení overflow pro celou stránku */
        html {
            overflow: auto;
            -webkit-overflow-scrolling: touch;
        }

        /* zrušení overflow pro vaši aplikaci */
        .streamlit-embed-wrapper {
            overflow: visible;
        }
    </style>
""", unsafe_allow_html=True)

# vložte sem kód vaší Streamlit aplikace

# Načtení datasetu
df = pd.read_excel("prices.xlsx")
df['Cena_2023'] = df['Cena_2023'].round(0).astype(int)
df['Cena_2020'] = df['Cena_2020'].round(0).astype(int)

st.markdown('<style>body {background-color: #F6F6F6;}</style>', unsafe_allow_html=True)

# Přidání nadpisu
st.title("Dokážete uhodnout průměrnou cenu zboží v březnu 2020?")

icons = {
    "Chléb kmínový (1 kg)": "icons/bread.png",
    "Hovězí maso zadní bez kosti (1 kg)": "icons/beef.png",
    "Vejce (10 ks)": "icons/eggs.png",
    "Benzín (1 l)": "icons/petrol.png",
    "Pivo výčepní, světlé, lahvové (0,5 l)": "icons/beer.png",
    "Polotučné mléko pasterované (1 l)": "icons/milk.png",
    "Cukr krystalový (1 kg)": "icons/sugar.png",
    "Máslo (250 g)": "icons/butter.png",
    "Kuřata kuchaná celá (1 kg)": "icons/chicken.png",
    "Brambory (1 kg)": "icons/potatos.png",
    "Vaječné těstoviny (1 kg)": "icons/pasta.png",
    # atd.
}

# Vytvoření sliderů a tlačítek
for index, row in df.iterrows():
    st.write(f"## {row['potravina']}")
    st.image(icons[row['potravina']], width=50)
    slider_val = st.slider(
        "Jaká byla cena zboží v roce 2020?",
        min_value = int(row["Cena_2020"] * 0.3),
        max_value=int(row["Cena_2020"] * 2.4),
        value=int(row["Cena_2023"]),
        step=1,
        key=row['potravina'],
        format="%d Kč"
    )
    # Zvýraznění aktuální ceny na slideru
    st.write(f"Aktuální cena: {row['Cena_2023']} Kč")
    st.markdown(
        f'<style>.streamlit-slider {{ background-color: lightgray !important }} .streamlit-slider-value[data-bk="{slider_val}"] {{ background-color: red !important }}</style>',
        unsafe_allow_html=True,
    )
    if st.button(f"Hádat cenu!", key=f"button_{row['potravina']}"):
        # Porovnání cen a výpis výsledků
        st.write("### Výsledek:")
        if slider_val == row["Cena_2020"]:
            st.write(f"Uhodli jste cenu! Cena byla {row['Cena_2020']} Kč.")
        elif slider_val > row["Cena_2020"]:
            rozdil = round(slider_val - row["Cena_2020"], 2)
            st.write(f"Zadali jste cenu o {rozdil} Kč vyšší než byla cena v roce 2020. Zboží tehdy stálo {row['Cena_2020']} Kč.")
        else:
            rozdil = round(row["Cena_2020"] - slider_val, 2)
            st.write(f"Zadali jste cenu o {rozdil} Kč nižší než byla cena v roce 2020. Zboží tehdy stálo {row['Cena_2020']} Kč.")
 
# Přidání informací o autorovi a zdroji dat
st.markdown('')
st.markdown("""<div style="text-align: right">Autor: Aleš Ligas | Zdroj: Český statistický úřad</div>""", unsafe_allow_html=True)
