## by substitution
Integration by substitution is somewhat simpler, and can be done for certain problems that allow this formulation. For example, this looks integral looks somewhat scary
$$\int x e^{x^2}dx$$
But there is a simple substitution which makes the problem easily and quickly tractable
$$u = x^2, \quad du = 2xdx, \quad xdx = \frac{1}{2}du$$
$$\frac{1}{2}\int e^u du = \frac{1}{2} e^u + c = \frac{1}{2} e^{x^2}$$

## by parts

$$\int u dv = uv - \int v du$$

On the other hand, this problem looks somewhat innocuous but requires integration *by parts*
$$\int x e^{6x} dx$$
$$u = x, \quad du = dx$$
$$dv = e^{6x}, \quad v = \frac1 6e^{6x}$$
$$uv - \int v du = \frac1 6 xe^{6x} - \int \frac1 6e^{6x} dx$$
Finally,
$$\int x e^{6x} dx= \frac1 6 xe^{6x} -  \frac1 {36}e^{6x}$$




**References**
https://tutorial.math.lamar.edu/classes/calcii/integrationbyparts.aspx
