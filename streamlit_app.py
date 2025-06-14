import streamlit as st
from api_client import get_ppt_json
from ppt_generator import create_ppt
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="PPT Generator Bot", layout="centered")

st.title("📊 AI Presentation Generator")
st.markdown("Enter a topic and get a PowerPoint presentation with 7–9 slides!")

# Input from user
topic = st.text_input("📝 Enter Topic for Presentation:")

# Generate button
if st.button("🎯 Generate PPT"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating slides..."):
            try:
                slides_json = get_ppt_json(topic)
                ppt_path = create_ppt(slides_json, topic)
                st.success("✅ Presentation Created!")

                # Provide download button
                with open(ppt_path, "rb") as f:
                    st.download_button(
                        label="📥 Download PPT",
                        data=f,
                        file_name=os.path.basename(ppt_path),
                        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                    )
            except Exception as e:
                st.error(f"❌ Failed to create PPT: {e}")
