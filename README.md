# MachineLearning-Project_4

# Part 1: Business case

Is it possible to predict whether a review is positive or negative?

We think that this topic is interesting, because it can help sites predict the tone of a review. This prediction might also be useful to predict the tone of an e-mail or any other written review. The sites can then use this to delete reviews or comments if they are negative/bad (now how ethical this is, is a different matter).

We can use binary classification for this problem, because a review can be either be negative or positive. We also have to do some kind of preproccesing with the words so they can be used with binary classification. For this we can use tools such as countvectorizer etc.

# Part 2: Data

<https://www.kaggle.com/nicolasgervais/rotten-tomatoes-480000-labeled-critic-reviews>

This dataset contains 480000 critic reviews from Rotten Tomatoes. The dataset consist of two columns — freshness and review.
Freshness indicates if the review is negative or positive.

You can use the downloader.py to download the dataset.


# Part 3: Data content and format

This dataset can help us train a model which will be able to predict if a review is negative or positive. This is due to the dataset consisting of negative and positive reviews. We can use SVM, K-Neighbours or Decision Tree classifiers.
We have not worked so much with text classification, so we might have to learn some new preprocessing techniques.
