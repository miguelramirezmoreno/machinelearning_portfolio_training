# Feature scaling

  - Useful with great disparity in the range of our features.
  - Normally, we adjust the different size *w<sub>j</sub>*, or a variable with a bigger range (size in square feet) has a desproporcionate effect compared with a "smaller one" (number of bedrooms).
  - Parameter range is inverse to feature range. In the scatterplot, the feature may barely change in hte axis, but *w* has a way more profound impact on **J<sub>w,b</sub>**

<img width="814" alt="image" src="https://user-images.githubusercontent.com/43887905/184530216-01aeef36-0474-47e8-89b1-e915b654dc21.png">
  - If features are rescaled, then the parameters have similar range and impact:

<img width="754" alt="image" src="https://user-images.githubusercontent.com/43887905/184530239-eae341ad-0857-4f20-a505-11f72c9cf774.png">
  
  ##Scaling procedure
  
  - Dividing by the maximum value
  - Mean normalization: ( *x<sub>1</sub>* - *π<sub>1</sub>*)/range (maximum - minimum).
    - This way the range includes negative values.
  - Z-score normalization. We need the standard deviation, σ, for each feature:  ( *x<sub>1</sub>* - *π<sub>1</sub>*)/*σ<sub>1</sub>*.
    - This way the range also includes negative values.
  - We want to have all features within similar ranges, -1 to +3, -3 to +3 and -0.3 to +0.3 are acceptable with each other. But -100 to +100 would require rrescaling.
    - Rescaling **is never bad**, though.

# Checking gradient descent for convergence
