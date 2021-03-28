### First Order System

### Second Order System
- Underdamped second order systems
    - Rise time: time to go from 0.1 - 0.9 of final value (fv)

Related by a table between omega and zeta


| $T_r * \omega_n$ | $\zeta$ |
| ------- | ----------- |
| 1.104 | 0.1 |
| 1.638 | 0.5 |
| 2.883 | 0.9 |

Peak time: time to reach first peak
$$T_p = \frac{\pi}{\omega_n \sqrt{1 - \zeta^2}}$$
- When $\zeta >= 1$, no peak!

Percent overshoot: amount that system goes past fv
$$\%OS = \frac{c_{max} - c_{final}}{c_{max}} * 100$$
$$c_{max} = 1 + e^{-(\zeta \pi / \sqrt{1 - \zeta^2})}$$
$c_{final} = 1$ (for the step function)
$$\%OS = e^{-(\zeta \pi / \sqrt{1 - \zeta^2})} * 100$$
- Can also describe $\zeta$ in terms of $\%OS$
$$\zeta=\frac{-\ln (\% O S / 100)}{\sqrt{\pi^{2}+\ln ^{2}(\% O S / 100)}}$$
- Settling time: time to reach oscillations within +/- 2% fv
$$T_s = \frac{4}{\zeta \omega_n}$$