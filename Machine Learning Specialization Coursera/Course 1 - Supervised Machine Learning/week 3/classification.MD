# Classification; logistic regression
 - When we want to answer a simple question. Is this email spam? Is the transaction legal? Is the tumour malignant?
 - Binary classification, *y* can be only one of two values, or classes or categories: no/false/0, versus yes/true/1. Bad/good can be used too, but these words carry a bias (e.g., with malignant tumour we won't say "good" for the true.
 - We can use symbols to show the two different classes:

<img width="776" alt="image" src="https://user-images.githubusercontent.com/43887905/184878655-be40378d-5448-4c99-bff0-b4ac5630ab08.png">

  - intuition suggest that we can try to use linear regression, trying to find a threshold after which 0 becomes 1.
  
  <img width="640" alt="image" src="https://user-images.githubusercontent.com/43887905/184878883-d7f9bd58-2ec3-49a6-9a2f-f3edec33e362.png">

  - But we have a big problem sometimes, adding more cases displaces the threshold boundary, and misclassifies existing data:
<img width="842" alt="image" src="https://user-images.githubusercontent.com/43887905/184879048-b7807365-4526-4808-88ae-5e58631df446.png">
  - Hence, linear regression works sometimes, but it is not universal. We need a new system


# Logistic regression
  - Despite the name, is is **not** regression, the name is due to historical reasons.
  - Based on the logistic/sigmoid function, which has output between 0 and 1. The imput,z, is derived from x, but it can have positive or negative values.
  
 <img width="619" alt="image" src="https://user-images.githubusercontent.com/43887905/185188583-3d40784f-4ee2-47fe-ba9e-186a79de8782.png">
  - A positive Z makes *g(z)* to become 1, and a negative Z makes *g(z)* closer to zero.
  - If Z=0, *g(z)* = 0.5.
  - The algorythm is build this way:
<img width="340" alt="image" src="https://user-images.githubusercontent.com/43887905/185189504-7328ec12-d4cc-4b9d-aa8f-10422c7a59fb.png">
  -*g(z)* tells us the probability that class is 1 (true) given the parameters *w* and *b* and the input *x*.So p(y=0)= 1-p(y=1)
  
# Decision boundary
  - We assign the prediction to be 1 once *g(z)* crosses a boundary.
  - If the threshold is 0.5, it means that the prediction will be 1 whenever w * x +b is greater than zero, or 0 if below 0.
  <img width="859" alt="image" src="https://user-images.githubusercontent.com/43887905/185196408-77708e11-f4f0-4005-a85a-e27a58d80124.png">
  -  The purple line is the decision boundary, assuming that both *w* equal to 1 and that *b* = -3 in this example.
  -  But the decison boundary may not be a line:
 <img width="950" alt="image" src="https://user-images.githubusercontent.com/43887905/185196928-0b3ccff1-3b60-4980-a282-3580e66ced3d.png">
<img width="951" alt="image" src="https://user-images.githubusercontent.com/43887905/185214187-8ca420bd-305f-4a56-ac4e-80c39ab63f4d.png">


# Cost function
  -  We cannot use the same ecuation, or plotting *H* against *w,b* we get a non convex function with losts of local minima.
  -  For a given case, we define the Loss, *L*(*f<sub>w,b</sub> (x<sup>(i)</sup>), y<sup>(i)</sup>)* = (1/2) * (*f<sub>w,b</sub> (x<sup>(i)</sup>)* - *y<sup>(i)</sup>*)<sup>2</sup> .
  -  Including the sigmoid function, the logistic loss function takes different ecuations whether *y* = 0 or 1. Both give a convex function, just like we wanted.
  <img width="739" alt="image" src="https://user-images.githubusercontent.com/43887905/185329163-bfca234b-4bb5-4e58-8a55-0fddca42ab2b.png">

  -  If y = 1, let's see what happens plotting log(*f*) (we are only interested in the 0-1 range).
<img width="997" alt="image" src="https://user-images.githubusercontent.com/43887905/185330158-0286c46a-f626-4a27-9331-da4ffa725744.png">
  -  Loss tends to 0 as we approach yo *f* = 1, as it tends to 0, loss tends to infinite.

  -  If y = 0, the opposite occurs:
<img width="662" alt="image" src="https://user-images.githubusercontent.com/43887905/185331799-d95c2843-08b3-4bbd-8c04-accb000c6eb0.png">

  -  The loss function can also be written with the formula:
 <img width="784" alt="image" src="https://user-images.githubusercontent.com/43887905/185796039-6caea6ec-84ca-4d3d-837b-76bd3016b3c7.png">

  -  (As *y* is always either 1 or 0)
  -  Cost function, applying the same method than in linear regression and moving the "-" outside, results in:
<img width="774" alt="image" src="https://user-images.githubusercontent.com/43887905/185796282-645c463e-b613-4ab2-8a91-d1948cbf2d3f.png">

  -  
