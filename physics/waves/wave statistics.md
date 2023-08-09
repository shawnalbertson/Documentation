Two main methods
1. Wave-by-wave analysis which treats time series as a sequence of individual waves with respective heights and periods
2. spectral analysis which treats surface as a summation of an infinite number of sine waves with varying frequencies

Assume
stationary, ergodic

# wave-by-wave analysis

$$H_{1/3} = \frac{1}{N/3}\Sigma_{i=1}^{N/2}H_i$$
$$H_{RMS} = \sqrt{\frac{1}{N}\Sigma_{i=1}^N H_i^2}$$

In this case the wave heights are the wave heights measured on a wave-by-wave basis. It is worth noting that on a continuous basis, the RMS is the same as the standard deviation for a mean centered time series

# spectral analysis
The spectral approach assumes that the surface is represented by an infinite sum of sine and cosine waves.
Consider the [[statistics/statistical quantities#variance]] of each harmonic component (mean-centered) with amplitude $a$ has variance $1/2 a^2$. The total variance is then 
$$\Sigma^n \frac 1 2 a_n^2$$
The variance density spectrum gives the variance density per unit frequency. It can be related to the energy [[wave energy#by variance]]
$$\lim _{\Delta f \rightarrow 0} \frac{1 / 2 a_n^2}{\Delta f}=E\left(f_n\right)$$
Integrating across the spectrum (aka the finding the zero moment) recovers the variance of the original signal equal to the mean square wave elevation
$$\int_0^{\infty}E(f) = \sigma^2 = m_0 = \overline{\eta^2}$$
In this way, the zero moment and standard deviation are related by 
$$\sigma = \sqrt{m_0}$$




# significant wave height
The significant wave height is the average of the 1/3 tallest waves. It is a summary statistic first introduced by Sverdrup and Munk (1947), which is related to the wave height which would be reported by a trained observer watching the sea surface over several periods. Thus, it is an empirical concept which is still used because of its tangible connection to reality. There are several ways to compute significant wave height, both with a wave-by-wave analysis and a spectral analysis. The simplest method is by taking the average of the tallest 1/3 waves measured on a wave by wave basis.
$$H_s = \frac{1}{N/3}\Sigma_{i=1}^{N/2}H_i$$
Where $N$ is the number of waves recorded, and $H_i$ the wave heights sorted from highest to lowest.

**[[statistics/Rayleigh distribution]]**
If we assume a Rayleigh distribution, we can also restate this summary statistic in several ways, and compute signficant wave height based on the standard deviation $\sigma$
$$H_{1/3} = 4\sigma$$
where $\sigma$ is the standard deviation of the time series, according to the formulation in [[statistics/Rayleigh distribution#H 1/3]]. Noticing the relationship to the zero moment by the variance of each spectral component, this is equivalent to 
$$H_{1/3} = 4\sqrt{m_0}$$
There is also a relationship to $H_{rms}$, the root mean square of the individual wave heights, such that
$$H_{1/3} = H_s = \sqrt{2} H_{rms}$$
Which again points to the conclusion that 
$$H_{rms}^2 = 8\sigma^2$$


## comparing $H_s$
$H_{m0}$ slightly over estimates $H_{1/3}$, by about 5%, according to https://support.nortekgroup.com/hc/en-us/articles/360029507012-What-is-the-difference-between-Hm0-and-Hs-

# Relevant distributions for waves
Surface elevation time series $\eta(t)$ is a **Gaussian** process aka normal distribution
Individual wave heights follow a **Rayleigh** distribution
Spectral energy/ variance follows the **JONSWAP** spectrum

### references
this was the most useful, stepping me through each process fairly thoroughly
https://geo.libretexts.org/Bookshelves/Oceanography/Coastal_Dynamics_(Bosboom_and_Stive)/03%3A_Ocean_waves/3.04%3A_Short-term_wave_statistics/3.4.4%3A_Short-term_wave_height_distribution?readerView

lowkey really good info in the Appendix
http://www.coastalwiki.org/wiki/Statistical_description_of_wave_parameters

naval academy
https://www.usna.edu/NAOE/_files/documents/Courses/EN330/Rayleigh-Probability-Distribution-Applied-to-Random-Wave-Heights.pdf

http://falk.ucsd.edu/pdf/Lectures6_7.pdf
