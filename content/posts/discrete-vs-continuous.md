---
title: "Discrete Vs Continuous"
author: Cheese-Cracker (Chinmay Hebbar)
created: Wed Jan 26 23:59:48 IST 2022
excerpt: 'Dive into the abstract feelings of things being continuous and discrete, with various examples.'
date: 2022-01-26
description: Continuous Vs Discrete
tags: [ "signalprocessing", "math", "mentalmodels", "numericalmethods",]
categories: [ "ideas" ]
imgs: ['/plots/des/DvsC.jpg']
toc: true
---

## Introduction

In this post, we delve into the **mental model** (or abstract feeling) of things being __continuous Vs discrete__.
In the direction of continuous vs discrete ideas, we look into signal processing, numerical methods and random ideas.
<div align="center">
<img height="300" src="/plots/des/DvsC.jpg"> </img>

<small> Poster originally by mathbytori.blogspot.com </small>
</div>

> Throughout this post, the terms 'discrete' and 'continuous' are somewhat loosely defined.

A simple intuition on continuous and discrete would give us,

| Discrete | Continuous |
| :---: | :---: |
| Distinct, seperate and countable | Fluid, mostly singular |
| Dotted Line  | Normal straight Line |
| Scattered | Unionized |
| Set of Integers $Z$:  Distinct points on the number line | Set of Real Numbers $\Re$: Continuous line on the number line |
| Sets not dense <small>(in any metric space)</small> |  Set is dense <small>(in any metric space)</small>|
| Non-seperable Metric Space<small>(like discrete metric space)</small> |  Seperable Metric Space |
| Discrete Probability Distribution | Continuous Probability Distributions |
| Histograms | Kernel Density Estimates |
| Digital Image Processing | Analog Image Processing |
| Discrete Delaunay Triangulations | Continuous Voronoi Diagrams |
| Discrete Time Signals | Continuous Time Signals |
| Sum of many discrete rectangles | Area under a continuous curve |
| Discrete Factorials | Continuous Gamma Function |
| Discrete Transforms | Continuous Transforms |
| Discrete Recurrence Relations | Continuous Differential Equations |


> A common trend to notice is that **discrete** things tend to take a **finite or countable** set of values.

---

## Discrete Signals Vs Continuous Signals

Moving to more concrete definitions,
Let us take the example of Continuous vs Discrete in the context of Signals.
This divides us into four parts shown below,
<div align="center">
<img height="400" src="/plots/des/4SignalDiagram.jpg" alt="Four Divisions of Signals"> </img>

<small> Clockwise: CT Analog, CT Digital, DT Digital, DT Analog</small>
</div>

The differentiating factors are,
- Discrete time (DT) Vs Continuous time (CT)
- Analog signal Vs Digital signal

Here, digital signal and analog signals are both continuous in time but the
CT digital signal has only a discrete set of values for the ouput $y(t)$.

> In this post, the ideas of 'digital' and 'discrete' may be mixed because 'digital' signals are still discrete in the y-axis.

---

## Area under a Continuous Curve Vs Sum of many Discrete Rectangles


Considering the area under the curve for any continuous function $y(t)$,
the area is given by $\int_{t_0}^{t_n} y(t)$

However, if we consider the digital equivalent of this function (by quantizing the input), the area under the curve can just be the sum of distinct rectangles.

So we get,
$\int_{t_0}^{t_n} y(t) = \sum_{i=0}^{n-1} y(t_i)$.

<div align="center">
<img height="300" src="/plots/des/MidRiemann2.svg"> </img>

<small> Wikipedia: Riemann Sum (taking midpoints)</small>
</div>

Taking the value at each midpoints and summing the rectangles we get,
$$\int \limits_a^b m(x)dx = \lim_{n \rightarrow \infty} \frac{|b - a|}{n} \sum_{k = 1}^{n} m(a + k \frac{|b - a|}{2n})$$
So, as we make the partition intervals smaller ($\lim_{n \rightarrow \infty} \frac{1}{n}$), this sum becomes closer to the actual integral.


> A [mid-riser or mid-tread quantizer](https://en.wikipedia.org/wiki/Quantization_(signal_processing)#Mid-riser_and_mid-tread_uniform_quantizers) in signal processing, would be analogous to a Riemann sum except for one point. The quantizer divides the signal $y(t)$ into discrete bins (and reconstructs). However, the riemann sum would divide the input $t$ into discrete bins.

<div align="center">
<img src="/plots/des/QuantizationLevels4.png"> </img>

<small> Wikipedia: Quantization of Signal with 4 Levels</small>
</div>

Instead of partitioning the continuous function into __rectangles__, we could take the function values at two points and break it into __trapezoids__. (Trapezoidal Rule)

<div align="center">
<img height="300" src="/plots/des/TrapRiemann2.png"> </img>

<small> Wikipedia: Trapezoidal Rule </small>
</div>

Similarly, we can approximate with even more function points to get the other [Newton Cotes Formulas](https://en.wikipedia.org/wiki/Newton%E2%80%93Cotes_formulas).

So, all these summations functions are approximations to integrations (each with a same or faster convergence).

---

## Discrete Factorials Vs Continuous Gamma Function

Considering another seqn of numbers,
$$1, 1, 2, 6, 24, 120, 720 ...$$
Can you guess the sequence?

For any given sequence in $N$, there will always be infinitely many continuous functions in $\Re$, that satisfy the sequence.

But one special function that represents this is the __gamma__ function,
$$ \Gamma(z) = \int_0^{\infty} x^{z-1} e^{-x}dx$$

Here,
$$ \Gamma (n + 1) = n!$$
thus captures the **factorial function**.

(Note that however the gamma function is continuous only in $\Re^{+}$.)

For many sequences which are a discrete recurrence relation, a continuous generating function can be also found.

---

## Discrete Vs Continuous - Fourier-Like Transforms

Another interesting and useful concept when dealing with signal processing, is the __fourier transforms__.
It is a very essential way to transfer a random signal (think square, triangular, wavy, crazy or any time-based oscillation)
into a mixture of sine ways of different frequencies.
3blue1brown has an amazing [visual introduction to the fourier transform](https://odysee.com/@3Blue1Brown:b/but-what-is-the-fourier-transform-a:b).

When considering fourier transforms, there are numerous generalization for different signals.
The types of transform depends on the 4 differentiating factors,
1. Discrete Signal or Continuous Signal
2. Periodic Signal or Aperiodic (Infinite Period) Signal
3. Transform or Inverse Transform (Analysis or Synthesis)
4. Imaginary exponent Vs Complex(re + im) exponent in equation


Considering the __normal transform in real domain__, varying points __1__ and __2__, we get the following table,

<div align="center">
<img height="250" src="/plots/des/SeriesVsTransform.png"> </img>

<small> Fourier Series Vs Fourier Transform</small>
</div>

Similar to the CTFT and DTFT, there is also inverse CTFT and inverse DTFT.
This [article](https://medium.com/sho-jp/fourier-transform-101-part-4-discrete-fourier-transform-8fc3fbb763f3) has a nice table,

<div align="center">
<img height="500" src="/plots/des/Medium-FT.jpeg"> </img>

<small> Medium: Fourier Transform Table</small>

<small>'Complex Fourier Series' is the same as 'Continuous Time Fourier Series'</small>
</div>

Switching the last parameter __4__ from purely imaginary to complex exponents, give us
two new transforms -
- Laplace Transform (Continuous Domain)
- Z - Transform     (Discrete Domain)

> In the transforms, the real component gives us the $e^x$ curves and the complex exponent gives us the $e^{ix} = cos(x) + isin(x)$ curves.

#### An ugly inconsistency

Considering the laplace transform to be,
$$ X(s) = \int_{-\infty}^{\infty} x(t) e^{-st} dt $$
An intuitive definition of Z-transform would be,
$$ X(z) = \sum_{-\infty}^{\infty} x[n] e^{-zn} $$
where z just like s would be defined by $z = \sigma + i\omega$

Unfortunately, due to ease of usage in digital signal processing the definition of z-transform was made rather unintuitive.
Hence, it is given by,
$$X(z) = \sum_{-\infty}^{\infty} x[n] z^{n} $$
where $z = e^{sT}$ (instead of $z=sT$)

From this we see the mapping,

**$j\omega$ axis for the Laplace transform $=$ unit circle for the Z transform**

See [this thread](https://dsp.stackexchange.com/questions/72140/why-not-use-the-same-standard-exponentials-for-both-continuous-and-discrete-ti/72143#72143) to know more.
Another [stackexchange thread](https://math.stackexchange.com/questions/3169159/why-define-the-z-transform-differently-from-the-laplace-transform), also points out why the laplace transform cannot be defined the other way around.

---

## Discrete Recurrence Relations Vs Continuous Differential Equations

Consider two alien species in two different planets with no natural predators
and sufficient resources to grow.
1. The first alien species breeds naturally with its growth twice its current population (population growth rate 200%).
2. The second alien species reproduces using binary fission. So, one alien essentially splits into two new alien creatures. And all the alien species undergoes this binary fission every new years' eve.

Both these cases could be modelled as,
1. $y' = 2y$ where $y$ is the population, and $y'$ is it's derivative (the population growth rate).
2. $a_n = 2 a_{n-1}$ where $a_n$ is the population in year $n$

Notice that in case of __alien species no. 1__ we are modelling it as a __continuous differential equation__ whereas in the case of __alien species no. 2__ we are modelling it as a __discrete recurrence relation__.


In case of alien species no. 1,
we have to solve the differential equation which gives us,
$$y = a_0 e^{2t}$$
where $a_0$ is a constant representing the original population of aliens.

So if there where 1 million aliens, originally,
there would $e^2 \approx  7.34$ million aliens after just one year.

For alien species no. 2,
it is relatively straightforward to see that a population of 1 million aliens would be 2 million after the first year.

It is also intuitive to notice that after any $n$ years the solution to this is,
$$ a_n = a_0 2^n $$

This similarity between the population growth equations can be seen better by modelling the recurrence relation as an diferential equation.

Consider the population after 3 years, it is 4 times the population after year 1 so,

$$a_3 = 2 * ( 2 * a_1 )$$
$$a_3  - a_1 = (2^2 - 1) a_1$$

So from this we could say for any general points a_{n+k} and a_n,

$$ \Delta y \approx \Delta a_n = a_{n + k} - a_n = (2^k - 1) * a_n $$
$$ \Delta t \approx \Delta n = (n + k) - n = k $$

$$ \lim_{\Delta n \rightarrow 0} \frac{\Delta a_n}{\Delta n} = \lim_{\Delta k \rightarrow 0 } \frac{(2^k - 1) * a_n}{k}$$

Taking derivative on both numerator and denominator with the [El 'Hospital' rule](https://en.wikipedia.org/wiki/L'H%C3%B4pital's_rule),

$$ \lim_{\Delta n \rightarrow 0} \frac{\Delta a_n}{ \Delta n} = ln(2) a_n $$

Modelling $a_n$ as $y$ and $n$ as $t$ we have,

$$ y' = ln(2) y $$
$$ y = a_0 e^{ln(2) t} = a_0 2^t $$

Or better expressed as,

$$ a_n = a_0 2^n $$

Another way to look at the two alien species is that,
1. The 1st alien species is a 100% compound interest which is [continuous compounded](https://en.wikipedia.org/wiki/Compound_interest#Continuous_compounding).
2. The 2nd alien species is a 100% compound interest which is compounded annually.

Note that instead if we take any other coeffecient too this would work!

#### For 2nd Order and above

It also works similarly for second order differential equations and second order recurrence relations.
The technique to solve 2nd order ODE and 2nd order RR are the same,
1. Put the solution as $y = C_0 e^{rt}$ or $a_n = \alpha^n = e^{ln(\alpha)n}$
2. Solve the quadratic equation or "characteristic equation" that transpires to get the general solution
3. Find the particular solution, this could be with the help of specific boundary conditions etc. and combine.

Without getting into too much detail,
For the general solution of 2nd order ODE with distinct roots,
$$ y = C_1 e^{r_1 t} + C_2 e^{r_2 t}$$
and for repeated root,
$$ y = C_1 e^{r_1 t} + C_2 t e^{r_2 t}$$


For the general solution of a 2nd order recurrence relation with distinct roots,
$$ y = C_1 r_1^n + C_2 r_2^n = C_1 e^{ln(r_1) n} + C_2 e^{ln(r_2) n}$$
and for repeated root,
$$ y = C_1 r_1^n + C_2 n r_2^n = C_1 e^{ln(r_1) n} + C_2 n e^{ln(r_2) n}$$

## Other Interesting References

- Can't find a [generating function for factorials](https://math.stackexchange.com/questions/126803/generating-function-for-the-factorial-sequence)
- A [philosophical and cognitive science view](http://philsci-archive.pitt.edu/4692/1/AnalogDigitalContinuousDiscrete.pdf) of analog, digital, continuous and discrete.
- [Baby Steps of Statistics](https://medium.com/greyatom/baby-steps-of-statistics-part-1-c76bafb30288)
- [Fourier Transforms 101](https://medium.com/sho-jp/fourier-transform-101-part-4-discrete-fourier-transform-8fc3fbb763f3)
- For mental models in other domains, refer [Farnam Street Blog](https://fs.blog/mental-models/) or [Super Thinking Book](https://www.goodreads.com/book/show/41181911-super-thinking)
- Try to find an anology for discrete vs continuous, with separable and non-separable spaces. Good Resources: [Separable Spaces](https://en.wikipedia.org/wiki/Separable_space), [Discrete-like non-separable subspaces in separable spaces](https://math.stackexchange.com/questions/3946786/example-of-non-separable-subspace-of-a-separable-hausdorff-space), [Database of Topological Counterexamples](https://topology.jdabbs.com/properties)
