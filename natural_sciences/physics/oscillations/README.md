### displacement function

function for simple harmonic oscillation is $x(t) = A \sin(\omega t)$. if the
angular velocity is not known but the period is, it can be derived as
$x(t) = A \sin(\frac{2 \pi}{T} t)$, where $A$ is the amplitude (how far from
the equilibrium does the object move), $T$ is the period ($2 \pi$ is one whole
cycle -- divided by $T$, this is how long one cycle takes), $t$ is the time at
which we are measuring the object's position $x$.

the derived function for simple harmonic motion is
$x(t) = A \cos(\omega t + \varphi)$, where $\varphi$ (the _phase constant_)
determines the starting position on the $\cos$ wave (it shifts the wave to the
sides), resulting in the following equation:
$sin(\omega t) = \cos(\omega t - \frac{\pi}{2})$

using this information, one can substitute $\cos(\varphi)$ for:
1. $\cos$, if it starts farthest from the equilibrium ($A$ far)
   ($-\cos$ if it starts on one side, $+\cos$ if it starts on the other)
2. $\sin$ is used, if it starts at the equilibrium
   ($-\sin$ if it moves towards one side, $+\sin$ if it moves towards the other)

#### the pendulum

position from the equilibrium is not all that important, so the displacement
function uses $\theta$ instead of $x$;
$\theta (t) = \theta_max cos(\omega t + \varphi)$

### restoring force

equation for the restoring force $F$ proportional to the displacement $x$ is
described by hooke's law: $F = -kx$, where $F$ is the restoring force (acting
on the object to pull/push it to the equilibrium), $k$ is a positive spring
constant (how 'stiff' the spring is) and $x$ is the displacement from the
equilibrium.

in a pendulum, the restoring force is provided by gravity. an analogy to the
spring constant therefore results in the following equation: $k = \frac{mg}{L}$,
where $L$ is the length of the pendulum.
replacing the spring constant with the pendulum equivalent therefore results
in the following equation for pendulums: $F = -\frac{mg}{L} x$

## period

amplitude doesn't affect the period at all (imagine gain pedals).

period formulae go like so:
1. for the spring: $T = 2 \pi \sqrt{\frac{m}{k}}$.
2. $T = 2 \pi \sqrt{\frac{m}{\frac{mg}{L}}} = 2 \pi \sqrt{\frac{L}{g}}$

given these equations, one can see that the period is affected by:
1. for the spring, _the mass_ and the _spring constant_
2. for the pendulum, _the length_ and the _gravitational acceleration_
4. $T = 2 \pi \sqrt{\frac{m}{k}}$

calculus is required to derive these equations, so either:
1. remember them
2. forget them
3. derive them (which would be too complicated and time consuming for entrance
   exams, so literally just choose either of the other two)

## takeaway

1. $x(t) = A \cos(\omega t + \varphi)$
   OR $\theta (t) = \theta_max \cos(\omega t + \varphi)$
2. $T = 2 \pi \sqrt{\frac{m}{k}}$ OR $T = 2 \pi \sqrt{\frac{L}{g}}$
3. $F = -kx$
4. for pendulums; $k = \frac{mg}{L}$
