# Classification
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
