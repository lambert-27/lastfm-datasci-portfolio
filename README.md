# **Data Science and Machine Learning 1 - Year 4**
## Last.FM Personal Scrobble History Portfolio Repository
*By Mark Lambert - C00192497*

*Lecturer: Ben O'Shaughnessey*

*Submission Date: 27th November 2026*

*Start Date: 17th October 2026*

---

This portfolio explores my personal Last.Fm listening history using data collection, cleaning and merging with an external dataset for extended features. 

It asks whether the release year of the music I listen to changes over time, and whether time of day helps predict which of my most-played artists I will listen to.

## Notebooks

| Notebook | Purpose |
| --- | --- |
| [`LastFMDataCollection.ipynb`](LastFMDataCollection.ipynb) | Retrieves recent and loved tracks from the Last.Fm API, cleans and aggregates the data, merges with another dataset for extended features|
| [`LastFMLinearRegression.ipynb`](LastFMLinearRegression.ipynb) | Uses linear regression to explore weekly changes in the average release decade of scrobbled music. |
| [`LastFMLogisticRegression.ipynb`](LastFMLogisticRegression.ipynb) | Uses time of day to predict the listened-to artist among the ten most-played artists in the dataset. |

## Data

The `datasets/` directory contains the collected and processed data used by the notebooks. This includes raw scrobbles, daily aggregates, loved-track data and extended features from a Spotify dataset retrieved from [HuggingFace]((https://huggingface.co/datasets/GD-Studio/embeat_45m_spotify_tracks))

The data collection notebook makes requests to the Last.fm API. To run it, provide your own API key and Last.fm username through a local `lastfm_creds.py` module. 

Keep API credentials private and out of version control.

## Installation
1. Clone the repository and move into its folder:

   ```powershell
   git clone https://github.com/lambert-27/LastFM---Data-Science-ML-Portfolio.git
   cd LastFM---Data-Science-ML-Portfolio
   ```

3. Open the notebooks in JupyterLab or PyCharm. To start JupyterLab from the repository folder:

   ```powershell
   jupyter lab
   ```

To run the data collection notebook, create a local `lastfm_creds.py` with your own Last.fm API key and username.

Keep this file and its credentials private.

## Author

**Mark Lambert · C00192497**

- Personal email: [marklambert123@gmail.com](mailto:marklambert123@gmail.com)
- SETU email: [c00192497@setu.ie](mailto:c00192497@setu.ie)
