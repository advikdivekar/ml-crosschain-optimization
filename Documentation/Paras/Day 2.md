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
