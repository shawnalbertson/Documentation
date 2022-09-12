Index Notation
==============

.. math::
    a_i b_i = \sum_{i=1}^3 a_i b_i

SCALAR
------
:math:`a_ib_i`

Row x column results in scalar of rank 0

DYADIC
------
:math:`a_ib_j`

Column by row results in ixj matrix of rank 2

*Rank* corresponds to number of free indices

Index Killer
-------------
.. math::
    a_i \delta_{ij} = a_j

Multiplying a row vector by the identity matrix turns it into a column vector.

Identity matrix a.k.a. "kronecker delta"
\left\{
    \begin{array}{lr}
        if i=j & \delta_{ij} = 1 \\
        if i\neq j \delta_{ij} = 0
    \end{array}

Del operator
-------------

.. math::
    \symbf{∇} = \left\( \frac{\partial}{\partial x_1}, \frac{\partial}{\partial x_2}, \frac{\partial}{\partial x_3} \right\) = \frac{\partial}{\partial x_i}
