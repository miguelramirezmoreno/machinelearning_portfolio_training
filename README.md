# Machine Learning

These are my personal notes from Andrew Ng's [coursera specialization](https://www.coursera.org/specializations/machine-learning-introduction).

According to Samuels, Machine learning is *the field of study that gives computers the ability to learn without being explicitly programmed*.

## Types of machine learning
- Supervised; most common in real world applications. (course 1, 2)
- Unsupervised (course 3)
- Reccomender systems
- Reinformecement learning

## Supervised learning
- Algorythm that learns X (input) to Y (output)
- Learns from being given the right answers (labels), we always start with example datasets. Then, the model is presented against new data
  - Regression: housing price prediction, finding a relationship between house size in feet^2 and price in $1000s. With regression we get infinitely possible outputs.
  - Classification: breast cancer detection, finite number of output (yes/no, 0/1). Class or category mean the same thing. There can be more than two categories. We find a boundary whose shape depends on the number of inputs.


| Input (X)| Output (Y) | Application  |
| ----------- | ----------- | ----------- |
| email | spam?(0/1) | Spam filter |
| audio | text transcripts | speech recognition |
| English | Spanish | translation |

## Unsupervised learning
- We give data with no label, no right answers, no y output in the dataset.
- We find a hidden pattern, or obscure feature. The algorythm figures it out alone what is interesting
  - Clustering. What google news does, or DNA microarray, or grouping customers in market segments.
  - Anomaly detection. Detect unusual events (e.g. fraud detection)
  - Dimensionality reduction. Reduce the complexity of a dataset without losing actual information.
