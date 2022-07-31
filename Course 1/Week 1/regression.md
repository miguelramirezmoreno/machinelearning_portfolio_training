# Linear regression

<img width="728" alt="image" src="https://user-images.githubusercontent.com/43887905/182031128-2597c0ff-93c3-498f-a606-3cc72e0c7162.png">

## Concepts

### Training set
Data used to train the model

### Variables
  - *x* is the input variable, or feature
   -  *y* is the output/target variable.
   -  *m* total number of training samples, each pair of *x* and *y*
   -  (*x*<sup>(i)</sup>, *y*<sup>(i)</sup>) referes to the *i*th pair. Note that the parenthesis indicates it is not exponential, just an index.

## How we train the model
- The algorythm is fed with training set
- The algorhythm produces a hypothesis, or function *f*, the function takes *x* and generates (*y*)hat, the estimated value of *y*. We never refer to (*y*)hat as the target variable, that is just *y*.
- *f<sub>(w,b)</sub>*(x) = wx + b = (y)hat = *f(x)*. It determines a linear function. The algorythm determines the values of w and b. It may be a different function of course, but then it would not be linear regression. This is also named *univariate linear regression*. 
<img width="371" alt="image" src="https://user-images.githubusercontent.com/43887905/182044041-71ea724f-d8d1-46c0-a266-a53fb80047fe.png">





## The cost function
