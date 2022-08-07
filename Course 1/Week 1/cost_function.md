# The Cost Function

<img width="706" alt="image" src="https://user-images.githubusercontent.com/43887905/183281419-8fe16b26-f7f1-4519-bba5-95c55f908a7b.png">

 — We want to choose *w* and *b* values that fit as much as possible our training set, so the difference between *y* and *ŷ* is minimal
 <img width="443" alt="image" src="https://user-images.githubusercontent.com/43887905/183281469-1122e669-f055-496d-b4c0-c52a847c462d.png">

<img width="315" alt="image" src="https://user-images.githubusercontent.com/43887905/183281495-455a22f4-c971-4937-a22a-d4dc0ad856fd.png">

— The sustraction is the error, we compute the square error across the entire data set, and we divided by *m* (number of training samples) by convention, to avoid the function to grow with many cases. We also divide by 2 by convention because it will be useful for us later on.
