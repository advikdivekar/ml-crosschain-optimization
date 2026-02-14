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

---

## Vectorized Representation

When we use multiple input features, we introduce a **parameter vector** and a **feature vector**.

We define the feature vector as:

\[
x =
\begin{bmatrix}
x_0 \\
x_1 \\
x_2
\end{bmatrix}
\]

Where:
- \(x_0 = 1\) (bias term)  
- \(x_1\) = size of the house  
- \(x_2\) = number of bedrooms  

The parameter vector is:

\[
\theta =
\begin{bmatrix}
\theta_0 \\
\theta_1 \\
\theta_2
\end{bmatrix}
\]

So the hypothesis becomes:

\[
h(x) = \theta^T x
\]

This means the hypothesis is the **dot product** of the parameter vector and the feature vector.

---

## Training Set Notation

We use the following notation in supervised learning:

- \(\theta\) = model parameters  
- \(m\) = number of training examples  
- \(x\) = input features  
- \(y\) = output (target variable)  

A single training example is written as:

\[
(x, y)
\]

The \(i^{th}\) training example is written as:

\[
(x^{(i)}, y^{(i)})
\]

This notation allows us to refer to any specific example in the dataset when training the model.

n = number of features you have for the supervised learning problems

3. Choosing parameters theta :
Choose theta such that h(x) and y for training examples.

J (Q) = 1/2 <img width="445" height="114" alt="image" src="https://github.com/user-attachments/assets/c55191c2-8cc4-4512-bfe1-db3d3f4357a6" />

This equation is used for finding out the minmisation of the concept of J(Q).

4. Implementing an algorithm to see how does minimization of J(Q) takes place:
Using the algorithm - Gradient descent.
We satrt with the value of Q <img width="153" height="50" alt="image" src="https://github.com/user-attachments/assets/8616ae43-e145-4164-a7c8-3c7a0289f0e3" />

Keep changing Q to reduce J (Q).
Each separate Gradient descent in as follows -  in this example the traing set is fixed. 
One step can be implented as follows:
<img width="353" height="104" alt="image" src="https://github.com/user-attachments/assets/54901f82-20f9-45f1-b5ef-6dd1535556be" />

here, alpha = learning rate.

<img width="484" height="138" alt="image" src="https://github.com/user-attachments/assets/4e059160-7f9b-4441-974c-3453c2225aa9" />


