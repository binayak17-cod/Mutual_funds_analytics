
import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    layout="wide"
)

st.title("📊 Mutual Fund Analytics Dashboard")
st.write("Capstone Project I - Exploratory Data Analysis")

# Absolute path to charts folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
charts_folder = os.path.abspath(
    os.path.join(BASE_DIR, "..", "charts")
)

st.write(f"Charts Folder: {charts_folder}")

if not os.path.exists(charts_folder):
    st.error(f"Charts folder not found: {charts_folder}")
    st.stop()

files = sorted(
    [f for f in os.listdir(charts_folder) if f.endswith(".png")]
)

if len(files) == 0:
    st.warning("No PNG charts found in charts folder.")
else:
    for file in files:

        chart_name = (
            file.replace(".png", "")
                .replace("_", " ")
                .title()
        )

        st.subheader(chart_name)

        image_path = os.path.join(
            charts_folder,
            file
        )

        image = Image.open(image_path)

        st.image(
            image,
            use_container_width=True
        )

        st.markdown("---")

