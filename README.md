# Data Science

Data Science is a repository that contains my resources for learning, teaching, and developing materials related to Data Science and (mostly Python-based) programming. The more advanced AI/ML Concepts will be implemented in the Artificial Intelligence folder, which can also be located on this github. 

## Exercises

Individual Python Exercises that demonstrate various mathematical concepts that we can implement in Python functions (as well as in Java, C++, etc.)

## License

Inspirations for the Material
1. [Columbia University, Computer Science Alum 2023](https://datascience.columbia.edu/education/#:~:text=Ours%20is%20one%20of%20the,science%20programs%20in%20the%20world.)
2. [General Assembly, Data Science Alum 2020](https://generalassemb.ly/education/data-science/new-york-city)
3. [Inspirit AI, Instructor 2021-2023](https://www.inspiritai.com/)
4. ["Artificial Intelligence, A Modern Approach", Tony Dear](https://aima.cs.berkeley.edu/)

# Coding Projects Overview
1. Estimating Flood Depths of Submerged Vehicles with CNNs

## Project: Estimating Flood Depths of Submerged Vehicles with CNNs

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
