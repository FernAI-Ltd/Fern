import streamlit as st
import pandas as pd
from PIL import Image
import random

# Dummy classifier – randomly tags each image for now
def classify_image(image):
    return random.choice(["deer", "fox", "blank"])

# App Title
st.title("FERN AI – Camera Trap Classifier (Prototype)")

# Upload section
uploaded_files = st.file_uploader("Upload your camera trap images", type=['jpg', 'jpeg', 'png'], accept_multiple_files=True)

if uploaded_files:
    results = []

    for uploaded_file in uploaded_files:
        image = Image.open(uploaded_file)
        label = classify_image(image)
        results.append({"Image Name": uploaded_file.name, "Species": label})

    # Display results
    df = pd.DataFrame(results)
    st.subheader("Classification Results")
    st.dataframe(df)

    # Summary count
    summary = df['Species'].value_counts().reset_index()
    summary.columns = ['Species', 'Count']
    st.subheader("Summary")
    st.dataframe(summary)

    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Results as CSV", data=csv, file_name="fern_ai_results.csv", mime="text/csv")
else:
    st.info("Upload one or more JPG or PNG camera trap images to begin.")
