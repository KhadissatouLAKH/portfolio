import streamlit as st

st.title("Khadissatou LAKH")

st.header("Profil 👤 ")
st.write("Technicienne supérieure en géomatique, passionnée par l'exploitation des données spatiales. De l’acquisition de données sur le terrain à leur intégration en base de données. Je traduis la donnée brute en cartes prêtes à l'emploi et rend l'information géographique accessible et stratégique pour vos projets d'aménagement.")


with st.sidebar:
    st.header("Coordonnées")
    st.write("* Téléphone 📞: +221 78 917 10 57")
    st.write("* Email 📧: diatoulakh4@email.com")
    st.write("* Adresse 🏠 : Dieuppeul Derklé")
    
    st.header("Education 🎓")
    st.write("* BTS en Géomatique 2026/2027")
    st.write("* Bac L2  2024/2025")
    


st.header("Compétences 🚀")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Logiciels & Outils informatiques")
    st.write("- **SIG :** QGIS, ArcGIS")
    st.write("- **2D & 3D :** AutoCAD, **Sketchup**")
    st.write("- **Bureautique :** Google Workspace")

with col2:
    st.subheader("Missions techniques")
    st.write("- **Code :** Programmation Python")
    st.write("- **Données :** Traitement CSV, TXT, KML")
    st.write("- **Terrain :** Numérisation & Cartographie")



st.header("Projet Académiques📂 ")
st.write("Réalisation d'une carte thématique de la région de Saint-Louis sur ArcGIS")
st.write("Cartographie numérique du quartier [Dieuppeul Derkle] sur Qgis")
st.write("""
- Création d'une base de données géographique sur Qgis et ArcMap.
- **Numérisation structurée :** Création de couches vectorielles (points, lignes, polygones) sous QGIS.
- **Topologie :** Respect des règles de saisie pour assurer la précision des données.
""")
