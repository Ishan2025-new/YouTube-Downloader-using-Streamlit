# YouTube Downloader App using Streamlit

A simple Streamlit web app that downloads a YouTube video from a provided URL and lets you download it from the browser.

## Features

- Enter a YouTube video URL in the sidebar
- Download the video on the server using `yt_dlp`
- Serve the downloaded file as a browser download button
- Automatically cleans up the downloaded file after serving

## Files

- `app.py` - Main Streamlit app interface
- `download_config.py` - Video download helper using `yt_dlp`
- `environment.yml` - Conda environment definition with required packages
- `downloads/` - Output folder for temporarily saved downloads

## Requirements

- Python 3.14
- Streamlit
- yt_dlp
- Conda (recommended) or a compatible Python environment manager

## Setup

1. Create and activate the Conda environment:

```bash
conda env create -f environment.yml
conda activate yt_downloader
```

2. Install dependencies if needed:

```bash
pip install streamlit yt_dlp
```

## Run the app

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

## Usage

1. Paste the YouTube video URL into the sidebar input.
2. Click **Start Download**.
3. Wait for the download to complete.
4. Click the download button to save the video locally.

## Notes

- The app downloads the video to the `downloads/` folder.
- The file is removed from the server after it has been prepared for browser download.
- Playlists are not supported; only single video URLs are downloaded.

## License

This project is provided as-is for learning and personal use.
