torque = otáčivý moment

if a force acts on an object off the center of its mass, the object will rotate
around the center of its mass.

formula for the center of mass is $X = \frac{\displaystyle \sum m_i x_i}{\displaystyle \sum m_i}$.

formula for torque is $\tau = F r$, unit is _Newton-meter_. more generally,
since we only care about the force that is perpendicular to the center of mass,
or the pivot, if the force is applied at an angle, a $\sin$ function will reveal
the perpendicular component. that is, the equation in its more general form
is $\tau = F r \sin{\theta}$

altough the equation is the same as work,
it _isn't_ work -- work is force applied over distance in the same direction $d$
(translation), whereas torque is force applied over circular path (rotation),
distance $d$ from the center, in a perpendicular fashion.
torque is the rotational analogue of linear force.

using torque, one can derive angular acceleration like so:
1. $\tau = F r$
2. tangential acceleration = $r \alpha$
2. $F_t = ma_t$
3. $\tau = rma_t$
4. $\tau = r m r \alpha$
5. $\tau = r^2 m \alpha$
6. $\alpha = \frac{\tau}{mr^2}$

so, angular acceleration is $\alpha = \frac{\sum \tau_i}{\sum m_i r_i^2}$

that is to say: since in normal acceleration, $\frac{F}{m}$, the mass acts as
inertia, in this case, $m r^2$ is _rotational inertia of a disc_. you can use this knowledge
to derive the formula for rotational/angular kinetic energy: if kinetic energy is
$\frac{mv^2}{2}$, where mass is the inertia, if you replace the inertia with
rotational inertia and the velocity with angular velocity, you get $\frac{mr^2 \omega^2}{2}$

so, rotational kinetic energy of a disc is $\frac{mr^2 \omega^2}{2}$

angular momentum is $m v_t r$, where tangential velocity can be replaced with
$\omega r$, therefore, angular momentum of a disc is $m r^2 \omega$

inertia for each rotating object can be different; that is, torque exercises
that require the calculation of rotational dynamics must specify the inertia
for said object. otherwise, always assume a disc: $I = m r^2$
