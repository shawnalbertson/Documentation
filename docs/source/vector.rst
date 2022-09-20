Vector math
===========
*Rank* corresponds to number of free indices

Index notation
###############
.. math::
    a_i b_i = \sum_{i=1}^3 a_i b_i

Dot product
------
:math:`a_ib_i`

Row vector x column vector results in SCALAR of rank 0


Dyadic
------
:math:`a_ib_j`

Column by row results in ixj matrix of rank 2


Index Killer
-------------

.. math::
    a_i \delta_{ij} = a_j

Multiplying a row vector by the identity matrix turns it into a column vector.

Identity matrix a.k.a. "kronecker delta"

.. math::
    \left\{
        \begin{array}{lr}
            if i=j & \delta_{ij} = 1 \\
            if i\neq j \delta_{ij} = 0
        \end{array}
    \right\}

Del operator
############
A vector of spatial derivatives

.. math::
    \symbf{∇} = \frac{\partial}{\partial x_1}, \frac{\partial}{\partial x_2}, \frac{\partial}{\partial x_3} \right\) = \frac{\partial}{\partial x_i}

The gradient is the del operator on a scalar field showing the rate of change of the scalar in each direction. For example, the pressure in a fluid :math:`\symbf{∇}\rho`

To find the derivative in a given direction, take the dot product of the gradient with an arbitrary normal vector.

.. math::
    \frac{\partial \rho}{\partial \mathbf{n}} = \symbf{∇}\rho \cdot \mathbf{n} = \frac{\partial \rho}{\partial x_i}\mathbf{n}_i

Divergence
----------

Dot product of del operator with a vector

.. math::
    \symbf{∇} \cdot \mathbf{a} = \frac{\partial a_i}{\partial x_i}

on a vector
-----------

If applied directly to a vector without a dot product, a matrix is produced

.. math::
    \symbf{∇}\mathbf{a} = \frac{\partial a_i}{\partial x_j}

curl of curl
------------

.. math::
    \boldsymbol{a} \times(\boldsymbol{b} \times c)=\boldsymbol{b}(\boldsymbol{a} \cdot \boldsymbol{c})-\boldsymbol{c}(\boldsymbol{a} \cdot \boldsymbol{b})

*proof*

.. math::
    \begin{aligned}
    \boldsymbol{d} &=\boldsymbol{a} \times(\boldsymbol{b} \times \boldsymbol{c}) \\
    d_m &=\epsilon_{m n i} a_n\left(\epsilon_{i j k} b_j c_k\right) \\
    &=\epsilon_{i m n} \epsilon_{i j k} a_n b_j c_k \\
    &=\left(\delta_{m j} \delta_{n k}-\delta_{m k} \delta_{n j}\right) a_n b_j c_k \\
    &=b_m a_k c_k-c_m a_j b_j \\
    &=[\boldsymbol{b}(\boldsymbol{a} \cdot \boldsymbol{c})]_m-[\boldsymbol{c}(\boldsymbol{a} \cdot \boldsymbol{b})]_m
    \end{aligned}