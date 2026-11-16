# **Data Science and Machine Learning 1 - Year 4**
## Last.FM Personal Scrobble History Portfolio Repository
*By Mark Lambert - C00192497 | [LinkedIn](https://www.linkedin.com/in/mark-lambert-27tw721921/) | [GitHub](https://github.com/lambert-27)* | [Personal Email](mailto:marklambert123@gmail.com)


*Lecturer: Ben O'Shaughnessey*

*Submission Date: 27th November 2026*

*Start Date: 17th October 2026*

[Weekly diary](documentation/WORKLOG.md)

---

This portfolio explores my personal Last.fm listening history through data collection, cleaning and a merge with an external dataset for extra track features

It asks whether the release year of the music I listen to changes over time, if the time of day helps predict which of my most-played artists I will listen to, and whether my tracks group into clusters based on their audio features

## Notebooks

| Notebook | Purpose |
| --- | --- |
| [`LastFMDataSciencePortfolio.ipynb`](LastFMDataSciencePortfolio.ipynb) | The combined portfolio notebook, covering data collection, cleaning and all models end to end |
| [`model_notebooks/`](model_notebooks/) | This is where the initial work was done for each model and the combined portfolio notebook is derived from here |

## Data

The `datasets/` directory contains the collected and processed data used by the notebooks: `scrobbles.csv` and `scrobbled_merged_with_hugging_face.csv`, source for Spotify dataset: [Embeat Spotify tracks dataset on Hugging Face](https://huggingface.co/datasets/GD-Studio/embeat_45m_spotify_tracks). Shared name-cleaning functions live in `portfolio/data_clean.py`

The project specification is in `documentation/`. I’ve also kept a short [diary](documentation/WORKLOG.md) with weekly notes on how the portfolio has progressed through development

The data collection notebook makes requests to the Last.fm API and Hugging Face. To run it, provide your own API key, Last.fm username and Hugging Face token through a local `portfolio/lastfm_creds.py` module

Keep API credentials private and out of version control

## Installation
1. Clone the repository and move into its folder:

   ```powershell
   git clone https://github.com/lambert-27/lastfm-datasci-portfolio.git
   cd lastfm-datasci-portfolio
   ```
2. Install the project dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Open the notebooks in JupyterLab or PyCharm. Run JupyterLab from the repository folder so the notebook paths and `portfolio` imports resolve correctly:

   ```powershell
   jupyter lab
   ```

To run the data collection notebook, create a local `portfolio/lastfm_creds.py` or edit the `portfolio/lastfm_creds.py.example` file with your own Last.fm API key, username, and Hugging Face API key:

```python
API_KEY = "your_api_key"
USERNAME = "your_username"
HF_KEY = "your_huggingface_api_key"
```

Keep this file and its credentials private. The regression notebooks can be run with the included datasets and do not require API credentials

## Author

**Mark Lambert · C00192497**

- Personal email: [marklambert123@gmail.com](mailto:marklambert123@gmail.com)
- SETU email: [c00192497@setu.ie](mailto:c00192497@setu.ie)

