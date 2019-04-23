# MachineLearning-Project_4

# Part 1: Business case

Is it possible to predict if a review is negative or positiv?

We think that this topic is interesting, because it can help sites predict the tone of a review. This prediction might also be useful to predict the tone of a mail or any other written review. The sites can then use this to delete review or comments if they are negative/bad.

We can use binary classification for this problem, because a review can be negativ or positiv. We also have to do somekind of preproccesing with the words so they can be used with binary classification. For this we can use tools as countvectorizer etc.

# Part 2: Data

<https://www.kaggle.com/nicolasgervais/rotten-tomatoes-480000-labeled-critic-reviews>

This dataset contains  480,000 critic reviews from Rotten Tomatoes. The dataset consist of 2 columns freshness and review.
Freshness indicates if the review is negative or positiv.

You can use the downloader.py to download the dataset.


# Part 3: Data content and format

This dataset can help us train a model which will be able to predict if a review is negative or positiv. This is due to the dataset consisting of negative and positiv review's. We can use SVM, K-Neighbours and Decision tree.
We have not worked so much with text classification, so we might have to learn some new preprocessing techniques.
