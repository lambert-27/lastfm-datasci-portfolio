# **Data Science and Machine Learning 1 - Year 4 Portfolio**
## Work Log
*By Mark Lambert - C00192497 | [LinkedIn](https://www.linkedin.com/in/mark-lambert-27tw721921/) | [GitHub](https://github.com/lambert-27)* | [Personal Email](mailto:marklambert123@gmail.com)

*Lecturer: Ben O'Shaughnessey*

*Submission date: 27 November 2026*

*Start Date: 6th October 2026*

---

This log is a summary of my weekly progress on the Data Science & Machine Learning 1 portfolio

| Week | Date | Work Completed |
| :--- | :--- | :--- |
| 1 | 06 Oct 2026 | Project setup. Tidied up specification. Began initial data collection from the Last.fm API, including `getLovedTracks` |
| 2 | 13 Oct 2026 | Aggregated scrobble data and merged with a temporary Spotify dataset from Kaggle. Restructured the portfolio into separate notebooks for data collection and modeling |
| 3 | 20 Oct 2026 | Found a better Spotify dataset on Hugging Face. Implemented a chunked merging strategy to handle the large file size. Added README and LICENCE. Began building the main linear regression notebook |
| 4 | 27 Oct 2026 | Tidied markdown and comments across notebooks. Added a second linear model based<br/> on the PythonDataScienceHandbook example. Fixed bugs in the logistic regression notebook and polished all code for the draft submission. Extracted common data cleaning code into `data_clean.py`. Refactored the huggingface data loading by using `streaming=True` rather than loading downloaded dataset directly from disk (it's 12GB total) |
| 5 | 02 Nov 2026 | Restructured project directory, moved notebooks and python modules into `portfolio` and save data pulled into the `datasets` folder. Added a small guide to the logistic regression notebook on the variable names. Worked on a metal vs not metal logistic regression model |
| 6 | 09 Nov 2026| Began decision tree models after Ben's recommendation. Refactored notebooks and familiarised myself with random forests. Implemented a more cohesive decision tree that asks can audio features predict the time of day I listen to a given track |
| 7 | 16 Nov 2026 | Made a single unified notebook that runs through data collection, processing and analysis with models. Worked on a better clustering model that ties in with the decision tree section. Began refining notebook to adhere to the CA guidelines by reformatting markdown, fixed some bugs in code |
