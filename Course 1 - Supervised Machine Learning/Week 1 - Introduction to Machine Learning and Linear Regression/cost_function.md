# The Cost Function

<img width="706" alt="image" src="https://user-images.githubusercontent.com/43887905/183281419-8fe16b26-f7f1-4519-bba5-95c55f908a7b.png">

 - We want to choose *w* and *b* values that fit as much as possible our training set, so the difference between *y* and *ŷ* is minimal

 <img width="443" alt="image" src="https://user-images.githubusercontent.com/43887905/183281469-1122e669-f055-496d-b4c0-c52a847c462d.png">

<img width="315" alt="image" src="https://user-images.githubusercontent.com/43887905/183281495-455a22f4-c971-4937-a22a-d4dc0ad856fd.png">

— The sustraction is the error, we compute the square error across the entire data set, and we divided by *m* (number of training samples) by convention, to avoid the function to grow with many cases. We also divide by 2 by convention because it will be useful for us later on.

Our goal is to minimize *J(w,b)*. Let's start with the simplified function, where *b* = 0, so *w* is our only parameter, then we can introduce *x* in the cost function ecuation. This line crosses the origin
<img width="695" alt="image" src="https://user-images.githubusercontent.com/43887905/183281679-c9d2cc4f-af4c-42cc-9963-4cab05d82961.png">

<img width="704" alt="image" src="https://user-images.githubusercontent.com/43887905/183281737-b23323bc-99c4-412a-8257-883f1ae14a7a.png">

—Important: each data point in *J(w)* represents a different ecuation/graph for *f<sub>w</sub>(x)*. If we keep our training set but change *w*:

<img width="700" alt="image" src="https://user-images.githubusercontent.com/43887905/183281901-7c786501-0fd4-454c-a672-830026103a48.png">

<img width="705" alt="image" src="https://user-images.githubusercontent.com/43887905/183281916-5b199b9c-50dd-4933-89f9-9918a9967085.png">

If we test all the possible values, we end up with the cost function graph:

<img width="340" alt="image" src="https://user-images.githubusercontent.com/43887905/183281931-f5f24bf9-78ff-49ca-835d-14138eb28cdb.png">

For a given dataset and only that dataset, we want to reach the valley, that is minimize *J*.

If we add B, the function looks different, the bowl shape extends to the third dimension, but there is still a valley to reach:

<img width="632" alt="image" src="https://user-images.githubusercontent.com/43887905/183282071-e6459e4d-7325-4c06-8744-701e810aa37b.png">

We can also represent it in 2d, much as the geographic maps connects the points with the same height. At the contour plot, every dot within a given ellipse have the same *J* value, as an output of different combinations of *w* and *b*.
<img width="541" alt="image" src="https://user-images.githubusercontent.com/43887905/183282127-de20727e-485d-45a0-9cef-4de9051b4e4d.png">


 

 
