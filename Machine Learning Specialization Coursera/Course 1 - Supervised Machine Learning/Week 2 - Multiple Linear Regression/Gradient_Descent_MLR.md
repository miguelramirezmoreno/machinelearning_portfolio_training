# Gradient descent for multiple linear regression

  - We start with a vector $\vec{w}$ of lenght *n* (*b* remains a number).

  - *f<sub>w,b</sub>* = dot product of $\vec{w}$ and $\vec{x}$ vectors plus *b*
  - *J(w,b)*

<img width="627" alt="image" src="https://user-images.githubusercontent.com/43887905/184096251-3891275c-4a93-422d-928a-de674f232983.png">

<img width="628" alt="image" src="https://user-images.githubusercontent.com/43887905/184096571-f5df581d-351a-48a8-b0dc-5e3892a2709f.png">

## Alternatives for gradient descent: Normal Ecuation
  - The **normal ecuation** only works for linear regression. Solves for w,b without iterations.
  - Of course, the con is that it does not generalise to other learning algorythms. It is also very slow with many features (>10,000).
  - It can be used in machine learning libraries that implement linear regression.

