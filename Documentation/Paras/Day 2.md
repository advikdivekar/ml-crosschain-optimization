14 Feb, 2026 12:11 PM

Notes of Day 2:

1. In process of Supervised learning is that - you will be given a test data set. That test dataset will be put into a Leanring algorithm like in the example discussed to give predictions about the housing prices and by convention this outputs the hypothesis.
The job of the hypothesis is to give the size of the new house and the price of that new house.
Therefore , the job of the Learning algorithm is to input a training set and output hypothesis and the job the hypothesis is to give the give the size of the house and what it thinks should be the price of the house.

2. When desinging a learning algorithm, the way you go about structuring a machine learning algo is important like - what is  data set? What is the hypothesis? and many more. These are the key decisions you have to make in pretty bmuch every supervised learning. 
When designing a learning algorithm:
-> The first thing you need to ask is how am i going to represent the hypothesis H?
and in linear regression we are going to say that the hypotesis is going to be - h (x) = Qo + Q1x, which means that the input size x and the output number as a linear function of size x.
More generally, when we have more input data, in the given exmaple, such as,  number of bedrooms as well as the size of the house, then we have two nput features, x1 - the size of the house ad x2 is the number of bedrooms. Then the equation becomes - h(x) = Qo + Q1x1 + Q2x2.
In order to simplify this notation, making it a little more comapact, 
<img width="327" height="88" alt="image" src="https://github.com/user-attachments/assets/c1779f02-bd6d-4e90-829a-5143093e46af" />
<img width="227" height="85" alt="image" src="https://github.com/user-attachments/assets/8d1ec6db-64f7-473b-b249-dcd1792f3b78" />
<img width="142" height="110" alt="image" src="https://github.com/user-attachments/assets/4ebe75a7-98d4-4a96-91e3-c5e95b15fbee" /> <img width="139" height="157" alt="image" src="https://github.com/user-attachments/assets/acc7716a-76d2-44a8-9e20-213ae3174c97" />

so here the theta becomes a three dimensional parameter and the features become a three - dimensional feature where:
Xo = 1, X1 = size of the house and X2 = number of bedrooms in the house 

Q = 'parameters' 
m = number of training examples
x = inputs/ features
y = output/ target variable
(x, y) = one training example
x^(i), y^(i) = i^th training example 
