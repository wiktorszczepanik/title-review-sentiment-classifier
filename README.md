## Title Review Sentiment Classifier

This repository contains a sentiment classification model designed to analyze and classify product title reviews from various e-commerce platforms. The model utilizes various data processing techniques and machine learning algorithms to determine the sentiment of reviews, achieving an accuracy of **0.91**.

### Trained Models

The trained models are located in the ***models/*** directory and are saved with the `.pkl` extension. These include:

- `count_vectorizer.pkl`: The vectorizer used for transforming text data into numerical format.
- `logistic_regression_classifier.pkl`: The logistic regression model used for sentiment classification.

### Command Line Program

A command-line program is included in this repository to allow for manual testing and checking of the classifier. This program enables users to input reviews and receive sentiment predictions directly from the model.

```plaintext
$ python3 sentiment-cli.py 
>>> Perfect for a Watch Newbie Seeking Analog Simplicity!
Positive
>>> Didn't like was damaged 
Negative
```

### Dataset

The dataset used in this project consists of 34,686,770 Amazon reviews from 6,643,669 users on 2,441,053 products. It is sourced from Kaggle and is licensed under the **CC0 1.0 Public Domain**.

### Installation

```bash
git clone https://github.com/wiktorszczepanik/title-review-sentiment-classifier.git
cd title-review-sentiment-classifier
pip install -r requirements.txt
```

### Third-Party Licenses

This project uses the following third-party library:

- `langid.py` by Marco Lui – for license details, see the `THIRD_PARTY_LICENSES.txt` file.
