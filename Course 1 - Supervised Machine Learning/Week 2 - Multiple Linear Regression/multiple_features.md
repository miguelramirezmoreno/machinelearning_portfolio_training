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


