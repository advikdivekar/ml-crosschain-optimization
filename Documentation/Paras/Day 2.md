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

---

## Number of Features

We define:

- \(n\) = number of **features** in a supervised learning problem  

So the feature vector has dimension:

\[
x =
\begin{bmatrix}
x_0 \\
x_1 \\
\vdots \\
x_n
\end{bmatrix}
\]

Where:
- \(x_0 = 1\) (bias term)
- \(x_1, x_2, \ldots, x_n\) are the actual input features

Accordingly, the parameter vector \(\theta\) also has \(n + 1\) elements.

---

## 3. Choosing the Parameters \(\theta\)

The goal of learning is to choose the parameter vector \(\theta\) such that the hypothesis:

\[
h(x) = \theta^T x
\]

is as close as possible to the true output \(y\) for all training examples.

In other words:

> We want to choose \(\theta\) so that the predicted values \(h(x)\) are as close as possible to the actual values \(y\) in the training set.


J (Q) = 1/2 <img width="445" height="114" alt="image" src="https://github.com/user-attachments/assets/c55191c2-8cc4-4512-bfe1-db3d3f4357a6" />

This equation is used for finding out the minmisation of the concept of J(Q).

---

## 4. Implementing an Algorithm to Minimize \(J(\theta)\)

To find the best parameters \(\theta\), we need to minimize the **cost function** \(J(\theta)\).  
This tells us how wrong our predictions are.

We do this using an optimization algorithm called **Gradient Descent**.

---

### Gradient Descent

We start with an initial value of the parameter vector \(\theta\).  
Then, we repeatedly update \(\theta\) in a way that reduces the value of the cost function \(J(\theta)\).

In each step, we move \(\theta\) in the direction that makes \(J(\theta)\) smaller.

In simple terms:

> Start with some \(\theta\), and keep changing it until the hypothesis \(h(x)\) fits the training data as well as possible.
<img width="153" height="50" alt="image" src="https://github.com/user-attachments/assets/8616ae43-e145-4164-a7c8-3c7a0289f0e3" />

We keep updating the parameter vector \(\theta\) in order to **reduce the cost function** \(J(\theta)\).

In **each step of Gradient Descent**, the training set is kept **fixed**.  
Only the parameters \(\theta\) are changed.

So the process is:

> Keep changing \(\theta\) to make \(J(\theta)\) smaller, while the training data remains the same.

One step can be implented as follows:
<img width="353" height="104" alt="image" src="https://github.com/user-attachments/assets/54901f82-20f9-45f1-b5ef-6dd1535556be" />

here, alpha = learning rate.

<img width="484" height="138" alt="image" src="https://github.com/user-attachments/assets/4e059160-7f9b-4441-974c-3453c2225aa9" />

<img width="488" height="105" alt="image" src="https://github.com/user-attachments/assets/6d168ace-8ca0-41cc-8c09-3a097d83e28b" /> 

---

## Gradient Descent Update Rule

The Gradient Descent algorithm works by **repeating updates until convergence**.  
For each update, we update every parameter:

\[
j = 0, 1, 2, \ldots, n
\]

If we do this, we will eventually find a **good set of parameters** \(\theta\) that fits the training data well.

---

## Cost Function Properties

If the cost function \(J(\theta)\) is defined for **linear regression** as the **sum of squared errors**, then:

\[
J(\theta)
\]

is a **quadratic function**.

This means:
- It has **no local minima**
- It has **only one global minimum**

So Gradient Descent will always converge to the **best possible solution**.

---

## Batch Gradient Descent

Linear Regression with Gradient Descent is still one of the **most widely used learning algorithms** today.

Gradient Descent is also called **Batch Gradient Descent** because:

> In each update, the algorithm uses **all** training examples to compute the gradient.

The entire training set is called a **batch**.

This can become slow when:
- The dataset is very large
- We need to scan through **all examples** many times

---

## Stochastic Gradient Descent (Alternative)

To avoid processing the entire dataset each time, we use an alternative called  
**Stochastic Gradient Descent (SGD)**.

It works as follows:

\[
\textbf{Repeat:}
\]

\[
\text{for } i = 1 \text{ to } m:
\]

\[
\theta_j := \theta_j - \alpha \big( h_\theta(x^{(i)}) - y^{(i)} \big) x_j^{(i)}
\]

Where:
- \(\alpha\) = learning rate  
- \(m\) = number of training examples  
- \(x^{(i)}, y^{(i)}\) = the \(i^{th}\) trainin

<img width="327" height="238" alt="image" src="https://github.com/user-attachments/assets/a244b0ae-a6a5-4c1d-9771-67d63c36553a" />


---

## Stochastic Gradient Descent (SGD)

This algorithm is called **Stochastic Gradient Descent**.

Instead of scanning through the **entire dataset** to compute each update, SGD uses an **inner loop** that goes through:

\[
i = 1 \text{ to } m
\]

and performs a Gradient Descent step using **only one training example at a time**.

This makes the algorithm much faster for very large datasets.

---

## Convergence Behavior

- **Batch Gradient Descent** moves smoothly toward the **global minimum** and eventually stops there.
- **Stochastic Gradient Descent** does **not converge exactly** to the minimum.  
  Instead, it keeps **oscillating** around the minimum due to the randomness of single-example updates.

---

## Monitoring Convergence

To determine when to stop Gradient Descent, we plot:

\[
J(\theta) \text{ vs. time (iterations)}
\]

When the cost function stops decreasing significantly, we stop the algorithm.

---

## Why Linear Regression is Nice

One of the best properties of **Linear Regression** is that:

- \(J(\theta)\) has **no local optima**
- It has only **one global minimum**

So we have fewer convergence and debugging problems compared to many other learning algorithms.

---

## Iterative Nature of Gradient Descent

Gradient Descent is an **iterative algorithm**.  
It must be run for **many steps** in order to approach the global minimum.

---

## Closed-Form Solution for Linear Regression

For **linear regression**, there is actually a way to compute the **global minimum directly**, without using Gradient Descent at all.

This is known as the **Normal Equation**, which solves for \(\theta\) in a single step.


<img width="312" height="226" alt="image" src="https://github.com/user-attachments/assets/3781b1d9-f218-4e4e-8bb2-6768107e8e9d" />

<img width="242" height="73" alt="image" src="https://github.com/user-attachments/assets/ad4e7412-90e3-4d1d-bacf-07d69739c5ba" />


