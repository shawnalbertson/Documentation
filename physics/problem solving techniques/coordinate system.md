A frame of reference in which Newton's laws of motion can be applied. Momentum is conserved in the absence of an external force.

### inertial vs. relative
From a meteorological standpoint, an inertial coordinate system has origin on the earth's axis of rotation and is fixed relative to the stars. A non inertial or relative coordinate system chosen at some place on the planet is subject to apparent forces such as the [[Coriolis force]]

Rotating frames of reference are non-inertial, thus we detect fictitious forces in them
### rotating reference frames
To understand the accelerations in a global frame of reference $G$, based on the accelerations in rotating frame $R$, first consider that the velocity of a particle in the global reference ($\mathbf{v}_G$) is dependent on the velocity in the rotating reference frame ($\mathbf{v}_R$), as well as the rotational velocity of the rotating frame ($\omega$) and the vector placing the origin of the rotating frame to the origin of the global frame ($\mathbf{r}$).

$$\mathbf{v}_G = \mathbf{v}_R + \mathbf{\omega} \times \mathbf{r}$$
To find the global accelerations, we take the time derivative of this equation. The first part giving
$$\frac{d}{dt}\mathbf{v}_R = \mathbf{a}_R + \omega\times\mathbf{v}_R$$
The second part giving
$$\frac{d}{dt}\left(\omega \times \mathbf{r}\right) = \frac{d\omega}{dt} \times \mathbf{r} + \omega \times \frac{d\mathbf{r}}{dt}$$
$$\frac{d\mathbf{r}}{dt} = \mathbf{v}_R + \omega\times\mathbf{r}$$
And combining everything,
$$\mathbf{a}_G = \mathbf{a}_R + 2\omega\times\mathbf r + \omega \times \omega \times \mathbf r + \frac{d\omega}{dt} \times \mathbf{r}$$
Where the first term is the acceleration in the rotating frame, the second term is the coriolis acceleration, the third term is the centripetal acceleration, and the last is the acceleration due to acceleration of the rotating frame.

frame of reference
cartesian, cylindrical, spherical
inertial, noninertial