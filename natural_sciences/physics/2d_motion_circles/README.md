![circular kinematics basics](https://tikz.net/files/kinematics_circular-001.png)

linear and angular kinematics are pretty much the same

_linear kinematics_:
1. $\overline{v} = \frac{\Delta x}{t}$ 
2. $\overline{a} = \frac{\Delta v}{t}$
3. $\frac{\Delta x}{t} = \frac{v_f + v_0}{2}$

_angular kinematics_:
1. $\overline{\omega} = \frac{\Delta \theta}{t}$
2. $\overline{\alpha} = \frac{\Delta \omega}{t}$
3. $\frac{\Delta \theta}{t} = \frac{\omega_f + \omega_0}{2}$

### variables

1. $\theta$ = angular displacement (measured in rad)
2. $s$ = arc length (not shown on the picture; it's the number of meters an
   object -- the red circle -- has traveled in $m$). calculated like so: $s
   = r \Delta \theta$
3. $\omega$ = angular velocity (angular displacement per time, measured in
   $\frac{rad}{s}$).  calculated like so: $\omega = \frac{\Delta \theta}{t}$
4. $v$ = arc speed (speed of an object travelling on the arc). calculated like
   so: $v = r \omega = \frac{r \Delta \theta}{t} = \frac{s}{t}$
5. $\alpha$ = angular acceleration (change in angular velocity over time).
   calculated like so: $\alpha = \frac{\Delta \omega}{t}$
6. $a_t$ = arc/tangential acceleration (__NOT CENTRIPETAL ACCELERATION__; not
   shown on the picture above). $a = r \alpha$
7. $a_c$ = centripetal acceleration. $a_c = \frac{v^2}{r}$
8. $a$ = total acceleration. because the tangential and centripetal accelerations
   form a right-angle triangle, the pythagorean theorem can be used:
   $a^2 = a_t^2 + a_c^2$

![oscillating pendulum showing tangential and centripetal acceleration](https://upload.wikimedia.org/wikipedia/commons/2/24/Oscillating_pendulum.gif)

here, the change in $v$ is _tangential acceleration_, whereas the $a$ shown is
the _centripetal acceleration_. if an object is moving in circle with unchanging
angular acceleration, its tangential acceleration is 0. however, any object
moving on a circle is _always_ centripetally accelerating, because it is always
turning.

## simple reasoning

essentially, remember this:
1. angular displacement is $\theta$
2. angular velocity (change in angular displacement over time) is $\omega$
3. angular acceleration (change in angular velocity over time) is $\alpha$
4. angular and linear kinematics are calculated in the same manner
5. to calculate the relations to the arc/distance an object travels instead of
   the angle, multiply it by the radius (i.e. arc length = $r \theta$,
   arc velocity = $r \omega$, arc/tangential acceleration = $r \alpha$)
6. centripetal acceleration = $\frac{v^2}{r}$
