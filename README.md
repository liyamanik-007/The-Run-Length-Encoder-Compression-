
# RLE Text Compressor

A small interactive web app that demonstrates **Run-Length Encoding (RLE)** using Python and Streamlit.

## Features

- Enter text in a web interface
- Compress consecutive repeated characters
- View original and compressed character counts
- See whether the output is shorter or longer
- Learn how the algorithm works

## Run locally

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the app:

   ```bash
   streamlit run app.py
   ```

Streamlit will print a local URL, usually `http://localhost:8501`, which you can open in your browser.

## Deploy on Streamlit Community Cloud

1. Push `app.py`, `requirements.txt`, and `README.md` to a GitHub repository.
2. Sign in to Streamlit Community Cloud with your GitHub account.
3. Choose **Create app** and select your repository and branch.
4. Set the main file path to `app.py`.
5. Deploy the app and wait for the build to finish.

## How RLE works

For input `aaabbccccd`, the output is `3a2b4c1d`: three `a` characters, two `b` characters, four `c` characters, and one `d` character.

## Limitations

RLE is useful when the input has consecutive repeated characters, but it may make other strings longer. This demonstration compares character counts, not actual file sizes in bytes. The simple count-plus-character format is not unambiguous for all possible inputs, so it should not be treated as a general-purpose compression format.

## Technology

- Python
- Streamlit
