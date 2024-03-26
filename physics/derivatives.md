_limits_ are based on the idea that if you have an equation on a graph, you can
predict what it's going to look like at one point, just by knowing what it
looks like at the surrounding points.

_an interval_ is just a range on a graph. it's the space between two points on
the horizontal axis (e.g. 15 to 20 seconds).

the idea of derivatives is that you can use infinitely tiny intervals to figure
out exactly how an equation is changing at any moment. in this sense, 
velocity is the derivative of position/displacement (velocity describes change
in position with respect to time) and acceleration is the derivative of
velocity (acceleration describes change in velocity with respect to time).

in other words, derivative represents the rate at which a function is changing
at any given point. if you have a function $f(x)$, its derivative, denoted
as $f'(x)$, or $\frac{df}{dx}$, gives you the rate of change of $f(x)$
with respect to $x$.

in other other words, $\frac{dx}{dt}$ is the derivative of x with respect to t.

the process of finding derivatives is called _differentiation_.
there are various techniques and rules for finding derivatives of different
types of functions, for example the __power rule__.
1. _leibniz's notation_: if $f(x) = x^n$, then $f'(x) = n x^{n-1}$
2. _lagrange's notation_: if $f = x^n$, then $\frac{df}{dx} = n x^{n-1}$

both notations are cringe but you should use them both anyway :^)

### Examples

1.  $x = 7t^6$  
1.1 $\frac{dx}{dt} = 42t^5$
2.  $x = t^\frac{1}{2}$  
2.1 $\frac{dx}{dt} = \frac{1}{2} t^{-\frac{1}{2}}$
3.  $x = t^{-2}$  
3.1 $\frac{dx}{dt} = -2t^{-3}$  
3.2 $\frac{dx}{dt} = -\frac{2}{t^3}$

### Trigonometry

![sin cos tan](https://andymath.com/wp-content/uploads/2019/07/Righttriangletrigonomety.jpg)

![derivative of sin](https://www.storyofmathematics.com/wp-content/uploads/2021/03/visualizing-the-derivative-of-sine-along-with-the-function-of-sine.png)

tracking the turning points of the curve (in this case, $sin(x)$ ), every ~180
degrees (e.g. -90 and 90). here, the function isn't changing at all (is constant)
and therefore its derivative is 0. from -270 to -90, $sin(x)$ is decreasing,
therefore its derivative will be negative. from -90 to 90, it is increasing,
causing its derivative to be positive.

1. $f'(sin(x)) = cos(x)$
1. $f'(cos(x)) = (-sin(x))$
2. $f'(-sin(x)) = (-cos(x))$
3. $f'(-cos(x)) = sin(x)$
