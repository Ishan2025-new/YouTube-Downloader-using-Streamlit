import streamlit as st
from download_config import download_youtube_video
import os

st.set_page_config(page_title="Youtube Video Downloader", page_icon="📼", layout='wide')
st.title("RC Youtube Video Downloader")
st.caption("Enter the URL in the sidebar and press the button")

video_url = st.sidebar.text_input("Enter the video url:")
button = st.sidebar.button("Start Download")
if video_url and button:
    download_file_path = download_youtube_video(video_url)
    if download_file_path:
        try:
            with open(download_file_path, "rb") as f:
                video_bytes = f.read()
            file_name = os.path.basename(download_file_path)
            st.download_button(
                label='Click to Download the Video', 
                data=video_bytes, 
                file_name=file_name,
                mime='video/mp4')
            st.success("Downloaded Video Successfully")
            os.remove(download_file_path)
        except Exception as e:
            st.error(f"Could Prepare the file {e}")
else:
    st.warning("Please Enter the URL")