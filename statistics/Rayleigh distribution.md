This probability density function describes the probability of a given wave height for narrow banded spectra, although it works fairly well for even broad banded spectra
$$p(H) = \frac{H}{4\sigma^2}\exp{\frac{-H^2}{8\sigma^2}}$$
It can be rewritten as 
$$p(H) = \frac{2H}{H_{RMS}^2}\exp\left(-\left(\frac{H}{H_{RMS}}\right)^2\right)$$
So, for a Rayleigh distribution of wave heights H, and variance of the surface elevation $\sigma$
$$H_{RMS}^2 = 8\sigma^2$$

![[images/Pasted image 20230327085706.png]]
## probabilty of exceedence
The probability that a wave **exceeds** a certain height depends on the height and the standard deviation $\sigma$
$$P\left(H^{\prime}>H\right)=1-P\left(H^{\prime}<H\right)=1-\int_0^H p(H) d H=e^{-\frac{H^2}{8 \sigma^2}}$$
To solve the integral for the Rayleigh distribution, use [[../math/calculus/integration#by substitution]]
$$u = \frac{H^2}{8\sigma^2} \rightarrow p(u) = e^{-u}du$$

$$\int_0^H p(u) du = \left.-e^{-u}\right|_0^{\frac{H^2}{8\sigma^2}}$$

$$1-\left[\int_0^H p(u) du\right] = 1-\left[-e^{-\frac{H^2}{8\sigma^2}} -1\right] = e^{-\frac{H^2}{8 \sigma^2}} = P(H)$$
The height of the wave with probability of exceedence $P$ (that is, there is a probability $P$ that a wave will exceed this height) is
$$H = 2\sigma\sqrt{2\log\left(\frac{1}{P}\right)}$$
For example, the height of the wave that 1/3 of waves are expected to surpass is
$$H_{1/3} = 2\sigma\sqrt{2\log(3)} = 2.96\sigma$$
## H 1/3
The average of the tallest 1/3 waves can be found by integrating (verified numerically)
$$H_{1/3}=\frac{\int_{H33\%}^{\infty}HP(H)dH}{\int_{H33\%}^{\infty}P(H)dH} = 4.004\sigma$$
This numerical coincidence is why we sometimes say 
$$H_{1/3} = 4\sigma$$
