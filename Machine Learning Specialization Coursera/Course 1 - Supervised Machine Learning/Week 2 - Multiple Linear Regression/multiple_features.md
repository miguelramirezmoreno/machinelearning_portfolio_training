# Multiple features in multiple linear regression

Now we have multiple features, such as:

| Feature 1| Feature2 | Feature3 | Feature4 | Output |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| *x<sub>1</sub>*| *x<sub>2</sub>* | *x<sub>3</sub>*|*x<sub>4</sub>* | *y* |
| Size in feet<sup>2</sup>| Number of bedrooms | Number of floors|Age of home in years | Price in $ |

 - *x<sub>j</sub>*, or *j<sup>th</sup>* feature, is a column. In this case, *j* = 1, 2, 3 or 4.
 - *n* is the number of features. In this case, *n* = 4.
 - *x<sup>(i)</sup>* contains the features of the *i<sup>th</sup>* training example, each of the rows. It does not contain *y*. It is a row vector.
 - *x<sub>j</sub><sup>(i)</sup>* is the value of feature *j* in the *i<sup>th</sup>* training example.
 - *j* or feature is subscript, *i* or training example is superscript. *x* in the latter sometimes has an arrow, to further stress it is a vector.

The new model has multiple *w*, as many as features *j* (or the value of n). All the *w*s make a row vector. So the parameters of the model are the vector *w* and *b* (independent.

<img width="373" alt="image" src="https://user-images.githubusercontent.com/43887905/183463407-fb08f9ca-0628-47bb-ab30-21a1892f5cc0.png">

Hence, *f<sub>w,b</sub>*(x) = w ∙ x + *b*. Notice the **dot product**.

<img width="588" alt="image" src="https://user-images.githubusercontent.com/43887905/183464523-7ea72641-4a24-4878-af95-ee95c3c7ee35.png">


# Vectorization

 - Makes coding shorter.
 - Increases efficiency.
 - Allows to use specific libraries and GPU hardware.
 
 For the given set
 <img width="348" alt="image" src="https://user-images.githubusercontent.com/43887905/183465822-7b38944d-84a0-419d-a24f-a574dd900d84.png">
 
## Vectorization of the model

In Python with numpy:
```
w = np.array( [1.0, 2.5, -3.3])
b = 4
x = np.array([10, 20, 30])
```

Implementation without vectorization:
```
f = w[0] * x[0] +
    w[1] * x[1] +
    w[2] * x[2] + b
```
With summ loop but still no vectorization:
```
f = 0
  for j in range(0,n):
    f = f + w[j] *x[j]
  f = f + b
```
*note* the 0 in range is not necessary, range(n) means from n to n-1 by default.

With vectorization:
```
f = np.dot(w,x) + b
```

Vectorized operation runs all the training cases in parallel, a loop goes one by one. This is critical with big datasets.

## Vectorization of gradient descent

For w = (*w<sub>1</sub> *w<sub>2</sub> ... *w<sub>16</sub>) and *b* parameters, and the derivative d= (*d<sub>1</sub> *d<sub>2</sub> ... *d<sub>16</sub>).
```
w = np.array([0.5, 1,3, ... 3.4])
d = np.array([0.3, 0.2, ... 0.4])
```

We want to compute *w<sub>j</sub>* = *w<sub>j</sub>* - 0.1*d<sub>j</sub>* 
for *j* = 1...16 (0.1 is the learning rate).

Without vectorization: 
```
for j in range(0,16):
    w[j] = w[j] - 0.1 * d[j]
```
With vectorization:
```
w = w - 0.1 * d
```
