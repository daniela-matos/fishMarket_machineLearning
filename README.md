
## Fish Market 

The goal of this homework is to training a regression model to predict the weight of a fish.
First, I looked at how fish measurements were made and then I researched how is the best way to predict the weight of a fish based on its measurements. 
The research showed that we should never use a cross lenght to weight a fish. So I didn't use the Length 3 in my model.
Also, the research showed that the best way to predict the weight is using the formula (length x girth x girth)/800.
Since I don't have the girth measurement in the dataset, I added a column Girth with an approximate number (Length2 * Width).
I tested Multilinear Regression, Polynomial Regression, SVR, Decision Tree and Random Florest. Multilinear Regression is the one that showed to be best model.


### Technology

* Python (Pandas, Numpy, Scikit-learn)


### Additional Research

https://www.almanac.com/content/how-estimate-weight-fish

https://www.koaw.org/measuring-fishes

### 

