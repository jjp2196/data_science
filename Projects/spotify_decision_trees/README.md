# (Capstone) Project 6: Determining Popularity of Rising Pop Music Artists with Scraped Spotify Data and NLP Sentiment Analysis

## Problem Statement
1. Spotify uses its popularity parameter in order to rank songs, albums, and artists. This "popularity" metric is based on how often users stream songs from Spotify.

2. But how does this stream-popularity metric compare with other metrics for popularity?
    - This metric only shows how popular very recent artists are in general (not popularity according to genre or popularity by song/lyrical content).

3. As a result, historically VERY popular classic songs (by Earth, Wind, & Fire, The Beatles, and other "classic groups") are overlooked. Additionally, artists who are VERY popular in their genre become ignored due to higher weight artists from higher popularity genres like "pop."

4. We need a new metric for popularity. In fact, we need more than one new popularity metric and a logic to guide our new metrics for popularity, in addition to a way of evaluating our old metric's effectiveness.

So:

1. Can we predict a song's popularity by stream count accurately using Regression Modeling?

2. Can we predict whether a song is popular by stream count using Classification Modeling?

3. What can we say about a song's popularity based on aspects of the music itself: like danceability, energy, and acousticness?

4. What can we say about a song’s popularity based on the content of an artist's lyrics--the verbal connotations and vibe of the poetry?

5. How do each of these factors influence our ability to predict the popularity of an artist or song?

6. Finally, when using Regression modeling, Classification modeling, and NLP Clustering to predict the popularity of a musical artist, how can evaluate whether or not to trust Spotify's ranking of popularity?

7. What other metrics of popularity should we define and recommend that Spotify and other top streaming sites adopt? What is our reasoning?

## Executive Summary

![](./spotify_images/1_exec_sum.png)

Spotify Song Attributes
1. First (for Song Attributes), I scrape ten different playlists off of Spotify full of 700 "Rising" songs from 2020. I clean the data, removing NAN values and duplicates for the songs. Spotify has a built in popularity function based on number of streams. This is ordered_playlist. Then, I import a dataframe of 232,000 songs from 2018-2020 made by a prominent Kaggle musical data scientist, Zaheen Hamidani, to the small dataset. I clean this data, dropping NAN values and duplicates. Next, I concatenate this songlist to ordered_songlist. At last, I name this large dataframe of roughly 150,000 songs as giant_ordered_playlist.
2. Second, I build a wide variety of Regression Models that try to accurately predict a song's "stream-popularity" based off of the song's musical attributes (like energy, valence, modality, time signature, and other characteristics). I will also use many different Classification Models to measure whether we can predict that a song is popular (above 75% popularity on a scale of 0 to 100) based off of these same song attributes.
3. Finally, I interpret the differences between the stream-based popularity metric and this song-attribute-based popularity metric, generating reasons for incongruities and making conclusions about the effectiveness of our popularity metric.

Genius Lyric Attributes
3. First (for Lyric Attributes), I use the shorter list of playlist songs (just 700 songs from ordered_playlist) from Spotify as a basis for which lyrics to scrape. I scrape the lyrics for each of these songs off of Genius' lyric library.
4. Second, I use sentiment analysis and NLP (CountVectorizer) to perform EDA on the most common words/sentiments for each song.
5. Finally, I try to evaluate whether there is a correlation between most common words and song sentiment with its popularity.

Lyric Clustering Processing (Completed Stretch Goal)
6. First (for Lyrics), I use Spacey to convert the lyrics of the 300 most common words in each song of ordered_playlist into vectors. These word vectors are arranged by their similarity to one another on a large coordinate plane.
7. Finally, I try to evaluate whether there is a correlation between a group of lyrics' content and their artist's stream-popularity. I conclude that yes, there IS a clear relationship between a song's stream-popularity and lyrical content. Though, for further research, I would like to pursue Hypothesis Testing to be certain of this relationship being a correlation at a statistically significant level.

## Project 6 Contents:

1. Webscraping Spotify and Genius
2. Exploratory Data Analysis: Song Attributes
3. Exploratory Data Analysis: Lyrics and Sentiment Analysis
4. Regression Modeling: Song Attributes
5. Classification Modeling: Song Attributes
6. Clustering Song Lyrics

## Project 6 Visualizations:

![](./spotify_images/2_popularity_by_distribution.png)

---

![](./spotify_images/3_energy_loudness_danceability.png)

---

![](./spotify_images/4_liveness_tempo.png)

---

![](./spotify_images/5_regression.png)

---

![](./spotify_images/6_classification.png)

---

![](./spotify_images/7_clustering.png)

---

## Conclusions

### Recommendation 1: All-Time Stream Popularity
- A new popularity metric based on:
- “Total Number of Streams of All Time”
- This will let us grade older songs comparably with newer songs
- We could compare historical trends in music with current trends without improper scaling worries from Stream Popularity

### Recommendation 2: Personal Popularities
- Bring back a 5-Star or “One-to-Ten” review system for each user’s songs
- This will let us assess what styles each individual user prefers
- This will allow us to create a Regression Model and Recommender System for the user for their highest rated songs, improving user turnout

### Recommendation 3: Song Features Review
- Create an optional Features Review section for each song in Spotify
- Vectorize the words used in Features Review
- Create Sentiment Analyses with these Vectors
- Create a recommender system with these Vectorized Sentiments

### Recommendation 4: Individual Research
- Artists with educational backgrounds in Music like Charlie Puth, Lizzo, and Lady Gaga have degrees in music from established music universities like Berklee, MSM, NYU, and University of Houston
- Research should be done individually at a certain point on who to promote after you've narrowed down artists to your "Top Five"

## Further Research and Future Projects

1. Using Parallel Programming (AWS) not Serial Programming (Jupyter, Google)
- Processing all 150,000 song lyrics
- Extending NLP Sentiment Lists and Performing Sentiment Analysis on all 150,000 song lyrics
- Performing NLP Clustering with SpaCy on all 150,000 song lyrics
2. Using Public Opinion on Pop Songs for Sentiment Analysis
- Scraping News/Twitter/Reddit/Tumblr/etc. Posts for All Songs
- Using NLP to Determine if Public Opinion Towards Artist is Negative, Neutral, or Positive
3. Using Song Attributes & Reviews to Create a Recommender System for Songs
- Publish online or submit to Record Labels / Streaming Companies

## Sources
- General Assembly Data Science Immersive 2020
- Cho, Youngmin P. "Quantify Music and Audio." NYC Data Science Academy, 3 June 2019, nycdatascience.com/blog/student-works/web-scraping/spotify-x-billboard/.
- Georgieva, Elena, lecturer. "HitPredict: Using Spotify Data to Predict Billboard Hits." ICML 2020, researcher by Nicholas Burton and Marcella Suta, Stanford University, 18 July 2020.
- Gingeleski, Ashley. "Spotify Web API: How to Pull and Clean Top Song Data Using Python." Ashley Gingeleski, 11 Nov. 2019, ashleygingeleski.com/2019/11/11/spotify-web-api-how-to-pull-and-clean-top-song-data-using-python/.
- Hamidani, Zaheen. Kaggle, 2019, www.kaggle.com/zaheenhamidani/ultimate-spotify-tracks-db.
- Itsaam. "History and Development of Compression." Music Tech Student, 11 Aug. 2013, musictechstudent.co.uk/music-technology/history-and-development-of-compression/.
- Loot, Rare. "Extracting Spotify data on your favourite artist via Python." Medium, 30 Dec. 2018, medium.com/@RareLoot/extracting-spotify-data-on-your-favourite-artist-via-python-d58bc92a4330.
- Passy, Jacob. "How Spotify influences what songs become popular (or not)." MarketWatch, 18 June 2018, www.marketwatch.com/story/how-spotify-influences-what-songs-become-popular-or-not-2018-06-18.
- Pierre, Sadrach. "Analysis of Top 50 Spotify Songs using Python." Medium, Towards Data Science, 27 Dec. 2019, towardsdatascience.com/analysis-of-top-50-spotify-songs-using-python-5a278dee980c.
- Sahu, Apratim. "Country-wise visual analysis of music taste using Spotify’s API & Seaborn in Python." Medium, Towards Data Science, 12 June 2020, towardsdatascience.com/country-wise-visual-analysis-of-music-taste-using-spotify-api-seaborn-in-python-77f5b749b421.
- SpaCy. spacy.io/. Sept. 2020.
- Spotify for Developers. Spotify, developer.spotify.com/dashboard/. Sept. 2020.
- Spotipy: Read the Docs. Spotipy, spotipy.readthedocs.io/en/2.16.0/. Sept. 2020.
- Tweepy Documentation. Tweepy, docs.tweepy.org/en/latest/. Sept. 2020.
