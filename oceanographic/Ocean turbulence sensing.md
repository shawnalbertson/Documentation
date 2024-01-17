Lueck 2022a
- Epsilon $\epsilon$ : The rate of viscous dissipation of TKE. Units $W kg^{-1}$
- Estimating the rate of viscous dissipation of turbulence kinetic energy provides a means to estimate diapycnal eddy diffusivity
- Airfoil Shear probes
	- measure the variance of microstructure shear, providing one component of the fluctuation of velocity orthogonal to its direction of profiling
	- measures frequencies higher than 0.1 Hz, wavenumber resolution of 150 cpm (counts per minute)
	- Resolves fluctuations near Kolmogorov scale, $L_K \equiv \left(\nu^3/ \epsilon \right)^{1/4}$
- In isotropic turbulence, rate of dissipation related to shear variance by 
	$$\epsilon = \frac{15}{2} \nu \overline{\left( \frac{\partial w}{\partial x}\right)^2} = \frac{15}{2} \nu \int_0^\infty \phi(k)dk \approx \frac{15}{2} \nu \int_0^{k_u}\phi(k)dk$$
	- with $\nu$ kinematic viscocity, $w$ velocity component normal to profiling direction, $x$ the direction of profiling, $\phi(k)$ the spectrum of shear, $k$ is wavenumber in the $x$ direction, $k_u$ the upper wavenumber estimate
- High wavenumbers are cut off as they usually consist of electrical noise
- Measurement errors are accounted for by comparing to known spectra (Nasmyth, Oakey)
- Two methods
	- The usual method of spectral integration
		- good control over wavenumber range
		- bad control over spatial range, because a lot of data has to be used
	- The direct variance method (first component of equation)
		-  excellent control of spatial scale, no control over wavenumber range

How is kolmogorov length calculated?
