# Data Science

Data Science is a repository that contains my resources for learning, teaching, and developing materials related to Data Science and (mostly Python-based) programming. The more advanced AI/ML Concepts will be implemented in the Artificial Intelligence folder, which can also be located on this github. 

# Coding Projects Overview
1. Deteminining Popularity of Rising Pop Music Artists with Scraped Spotify Data and NLP Sentiment Analysis (2020)
2. Project 5: Estimating Flood Depths of Submerged Vehicles with Convolutional Neural Networks (2020)

## Deteminining Popularity of Rising Pop Music Artists with Scraped Spotify Data and NLP Sentiment Analysis (2020)

### Problem Statement
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

### Executive Summary
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

## Project: Estimating Flood Depths of Submerged Vehicles with Convolutional Neural Networks (cNN)

### Problem Statement

Both a car insurance company and a motor-vehicle owner have a vested commercial interest in being able to estimate a car's damages caused by natural disasters, floods in particular. The United States 2020 Census recognizes floods as the most common natural disaster in the country, and cars are particularly vulnerable to flood damages due to their internal technologies. The 2019 Mississippi River Floods resulted in 20 Billion Dollars of damages alone. 

As a result of these factors, we need to be able to use Visual APIs, Machine Learning, and Neural Networks to systematically label the depths of flooded motor vehicles. Which APIs and forms of Machine Learning will we use to recognize our target variable "flood depth?" More importantly, how accurately can we estimate flood depth, considering the baseline flood depth predictions are only 20% accurate for this type of model.

### Executive Summary
- After extensive research, we decided to use the Google Vision API to specifically identify flooded from non-flooded cars. 
- We created a dataset of flooded and non-flooded cars from public domain image sources. 
- Next, we used Google Vision’s API to label specific objects like “wheel,” “window,” etc. in our dataset.
- Then, we trained the Google Vision API to recognize flooded cars as different objects from non-flooded cars.
- To enlarge our dataset, we used Image Augmentation to visually bootstrap our images. 
- We assigned Flood Height to these images.
- Finally, we inputted our processed flooded vehicles through our Convolutional Neural Network, successfully estimating flood height with visual images.

## Exercises

Individual Python Exercises that demonstrate various mathematical concepts that we can implement in Python functions (as well as in Java, C++, etc.)

## Contributing

Pull requests are not generally welcome for developing this material, as the material is developed only by James Pecore as a resource.
That said, pull requests from prospective employers or from students looking to analyze the code used and its functionality are certainly welcome.

## License

Inspirations for the Material
[Columbia University, Computer Science Alum 2023](https://datascience.columbia.edu/education/#:~:text=Ours%20is%20one%20of%20the,science%20programs%20in%20the%20world.)
[General Assembly, Data Science Alum 2020](https://generalassemb.ly/education/data-science/new-york-city)
[Inspirit AI, Instructor 2021-2023](https://www.inspiritai.com/)
["Artificial Intelligence, A Modern Approach", Tony Dear](https://aima.cs.berkeley.edu/)