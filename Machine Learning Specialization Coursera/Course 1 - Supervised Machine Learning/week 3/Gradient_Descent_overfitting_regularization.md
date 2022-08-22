# Gradient descent implementation

- Same rationale, we want probability of y = 1 given the parameters.
- We again need to use gradient descent using partial derivates to adjust parameters simultaneously.
- Applying  partial derivate:
<img width="578" alt="image" src="https://user-images.githubusercontent.com/43887905/185799964-dd7dce34-9743-449d-9296-75e1eae8c8dc.png">
- Applying  partial derivate:

 
# Underfitting and overfitting
<img width="821" alt="image" src="https://user-images.githubusercontent.com/43887905/185801581-1aabfc8f-e7bc-4bf8-bdba-c225e37efc4b.png">
- An algorythm that is underfitting the training data has a high bias (e.g., a line against a diff distribution).
- Notice that this is a different use of the word bias. It means the training data has a pattern the algorythm is missing, is unrelated to biased algorythms we usually heard about.
- The oposite happens when we use a 4th order polynomial, and the algorythm overfits the data. Then the algorythm has high variance.
- The middle example we use a cuadratic function, fits training set well, and we say this algorythm generalizes well.
<img width="828" alt="image" src="https://user-images.githubusercontent.com/43887905/185801704-6cbe2738-1b71-42b8-8633-00733d279874.png">

# How do we address overfitting?
- Overfit is often a consecuence of too many features but insufficient data. Removing features helps with this case.
  - The disadvantage is that useful features may be lost.
- Regularization reduces the size of parameters without eliminating features.

# Regularization
- Reducing the contribution of feature(s) *w*
- We regularize by looking at the mininum of the cost function, but summing up an operation involving the troubling features.
- This way, the whole model is penalized unless those features are reduced. So how do we implement this? Using lambda times the sum of *w*<sup>2</sup> and dividing by 2m.
- We add ALL the features *w*. By convention, we do not penalize *b*.
- *lambda* is the regularization parameter, always > 0
<img width="822" alt="image" src="https://user-images.githubusercontent.com/43887905/185867556-bf49b212-bcf8-4107-a3d2-972ef2112d3c.png">
- If lambda is 0, model overfits, if lambda is too big, it underfits.


## Regularized linear regression

- Gradient descent ecuation changes *w<sub>j</sub> (*b* remains the sane)
<img width="986" alt="image" src="https://user-images.githubusercontent.com/43887905/185871416-bbc04e7e-fe67-4352-a8f8-e9b7435ce269.png">
- And the detailed explanation of the new partial derivate:
<img width="932" alt="image" src="https://user-images.githubusercontent.com/43887905/185872869-559b5455-abb5-4f74-9f99-7367d1f46364.png">

## Regularized logistic regression
- Gradient updates in a similar manner to linear regression, except that now *f(x)* is the logistic function.
<img width="716" alt="image" src="https://user-images.githubusercontent.com/43887905/185873657-aff8fa21-ec03-4252-9576-7511e1197141.png">
