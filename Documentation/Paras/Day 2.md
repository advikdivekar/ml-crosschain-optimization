# 14 Feb, 2026 — 12:11 PM  
## Notes of Day 2

---

## 1. Supervised Learning

In the process of **supervised learning**, you are given a **training dataset**.  
This dataset is fed into a **learning algorithm**, which produces a **hypothesis**.

The purpose of the hypothesis is to:
- Take the **size of a new house**
- Predict the **price of that house**

Therefore:

> The job of the **learning algorithm** is to take a training set and output a hypothesis.  
> The job of the **hypothesis** is to map input features (house size, etc.) to a predicted price.

---

## 2. Designing a Learning Algorithm

When designing a learning algorithm, the way you structure it is very important.  
Some key questions are:

- What is the **dataset**?
- What is the **hypothesis**?
- How will the hypothesis be represented?

These are decisions you make in almost every supervised learning problem.

---

### Representing the Hypothesis

The first question to ask is:

> **How am I going to represent the hypothesis \(H\)?**

In **linear regression**, we represent the hypothesis as:

\[
h(x) = \theta_0 + \theta_1 x
\]

Where:
- \(x\) = input (house size)  
- \(h(x)\) = predicted house price  
- \(\theta_0, \theta_1\) = model parameters  

This means the output is a **linear function** of the input.

---

### Multiple Input Features

When we have more than one input feature, for example:
- \(x_1\) = size of the house  
- \(x_2\) = number of bedrooms  

The hypothesis becomes:

\[
h(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2
\]

This allows the model to use **multiple factors** to predict the house price.

To simplify this notation and make it more compact, we use vectorized forms in machine learning.

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
