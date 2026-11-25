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

It also asks how well a track's energy predicts its loudness, what drives the number of songs I scrobble per day and whether a tracks audio features can predict the time of day I listened to it

## Notebooks

| Notebook | Purpose |
| --- | --- |
| [`LastFMDataSciencePortfolio.ipynb`](portfolio/LastFMDataSciencePortfolio.ipynb) | The combined portfolio notebook, covering data collection, cleaning and all models |
| [`model_notebooks/`](portfolio/model_notebooks/) | This is where the initial work was done for each model and the combined portfolio notebook is derived from here |


## Models and Results

All models were ran on a snapshot of the data pulled, which holds 17,999 plays over 331 days. Plays are matched to Spotify auddio features by cleaned artist and track name and about 81% of plays (14,611) matched

| Model | Question | Result |
| --- | --- | --- |
| Linear Regression | Does the average release year change by week? | No meaningful change (Slope of 0.0332 years p/ week, R-squared 0.024 |
| Linear and Polynomial Regression | How well does energy predict loudness? | Linear scored 0.6086, cubic improved by 6.6 percentage points |
| Linear Regression | How many songs do I scrobble per day? | Model performed worse than the baseline |
| Logistic Regression | Can time of day predict which of my top 10 artists I play? | Only Arctic Monkeys and Tame Impala are every predicted |
| K-means with 4 Clusters | Do my tracks cluster by audio features? | Silhouette of 0.203, clusters overlap |
| Decision Tree | Can audio features predict the time of day I listened? | Scored 6 points above always guessing evening baseline of 0.406. Morning and night never predicted |

Across the models the output is weak, which can largely be attributed to the lack of data. A longer period of scrobbled data would give better, more accurate results

## Data

The `datasets/` directory contains the collected and processed data used by the notebooks: `scrobbles.csv` and `scrobbled_merged_with_hugging_face.csv`, source for Spotify dataset: [Embeat Spotify tracks dataset on Hugging Face](https://huggingface.co/datasets/GD-Studio/embeat_45m_spotify_tracks). Shared name-cleaning functions live in `portfolio/data_clean.py`

The project specification is in `documentation/`. I’ve also kept a short [diary](documentation/WORKLOG.md) with weekly notes on how the portfolio has progressed through development

The data collection section of the notebook makes requests to the Last.fm API and Hugging Face. To run it, provide your own API key, Last.fm username and Hugging Face token through a local `portfolio/lastfm_creds.py` module

Keep API credentials private and out of version control

From 1st December 2026 Last.fm will require a Pro subscription to generate a new API key, see [here](https://support.last.fm/t/api-keys-will-require-pro-from-1st-december/121030). The included CSV files mean the analysis can be run without making any API calls

## Limitations 

- Because the data is my own listening and only covers 331 days none of the results can be generalised to a broader audience. SSeasonal patterns also can't be checked because of the short time-frame.
- I mostly listen to full albums in order, so scrobbles are mostly runs of the same artists rather than spontaneous, independent choices between plays
- Night plays are only 402, so any results for the Night class are unreliable
- Matching to Spotify for features is done by cleaning the name, so some plays may be missed entirely or matched to a different version of the track
- Spotify audio features are model estimated, meaning sevral overlap

  
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

