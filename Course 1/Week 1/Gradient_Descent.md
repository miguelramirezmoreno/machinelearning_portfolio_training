# Gradient descent

An algorythm to systematically find *w* and *b* values that results in the smalles possible *J*.
  - Usually we start with values of 0 (convention).
  - Some cost function have intricate shapes (e.g. with neural networks)
  <img width="599" alt="image" src="https://user-images.githubusercontent.com/43887905/183286649-39a670b5-19e5-4ac5-926d-60a436d9a2c1.png">

  - There are hills and valleys, and each step takes us closer towards the minimum. But there are things to consider:
   -  The starting point may lead you to a different local minimum
   -  The step size can cause you to miss a minimum

## Implementing gradient descent algorythm

We update the parameter w by adjusting the previous value with the derivate. In coding, for *w* it is:
<img width="303" alt="image" src="https://user-images.githubusercontent.com/43887905/183286772-939aaf7e-93e4-45e0-9aa8-85dc86fce377.png">
  - Sometimes we write "==" for truth assertions (a=c, but a cannot neber be a+1 in truth assertion, but it can be in code assigment, as it happens with the gradient descent algorythm).
  - α is the learning rate (usually between 0 and 1).
  - α multiplies the (partial) derivative of *J*.
 An for *b* it is:
 <img width="259" alt="image" src="https://user-images.githubusercontent.com/43887905/183286894-c266c25c-096c-46bc-9f41-956c6d9050b2.png">
 
  - We repeat until both converge, where the parameters no longer change much with each step.
  - As we are updating *w* and *b* we need to simultaneously update both parameters
<img width="750" alt="image" src="https://user-images.githubusercontent.com/43887905/183286960-1a97d5d9-b44b-49ac-8245-6be56eaded4c.png">

  - This way, temp_w is a different value from the w that follows. In the incorrect example we have updated *w* before updating *b*, so the *w* terms in the second adn third line are different.
  - We can interpret the partial derivative as the slope of the tangent line to the function in that position (y/x in math notation), positive if the curve is climbing and negative if it is trouting. So the algorythm substracts if slope is positive, and sums if it is negative. If we pass the minimum, the algorythm backtracks. 
  <img width="741" alt="image" src="https://user-images.githubusercontent.com/43887905/183287204-4f5ffd5f-1f53-4f93-ab0b-d8cba1236d40.png">

  - What about the learning rate?
    -  α too small and the algorythm will be slow, it will need many more steps to reach the minimum.
    -  α too large, the algorythm may skip the minimum (overshoot) or fail to converge, even diverge.
    -  What happens if *J(w)* is already in a local minimum? There the slope is 0, so gradient descent leaves *w* unchanged, so we are stuck in the local minimum!
    
    
   - Applied to linear regression:
   
   <img width="770" alt="image" src="https://user-images.githubusercontent.com/43887905/183287496-59b07956-30b4-441e-9f01-4c8e1aa5688b.png">

   <img width="747" alt="image" src="https://user-images.githubusercontent.com/43887905/183287465-d4ed5429-ed6d-4ac6-9f2e-7b016b018893.png">





