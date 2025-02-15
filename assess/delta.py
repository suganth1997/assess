r"""This module contains functions that compute the coefficients in analytical
solution to the Stokes equations in cylindrical and spherical shell domains
with a delta function RHS forcing term, which in the 2D cylindrical shell
domain takes the form:

.. math::

  f = -g \delta(r-r') cos(n\varphi) \hat{r}

where r is the radius (distance from origin), :math:`\varphi` is the angle with
the x-axis, :math:`r'` is the radius of the density anomaly, and
:math:`\hat{r}` is the outward pointing radial unit vector. The magnitude g,
degree l and wave number n can be chosen arbitrarily. Similarly in a 3D
spherical domain we consider the forcing term

.. math::

  f = -g \delta(r-r') Y_{lm}(\theta,\varphi) \hat{r}

where :math:`\theta` and :math:`\varphi` are the co-latitude and longitude
respectively, and :math:`Y_{lm}` is Laplace's spherical harmonic function of
degree l and order m.

We consider the following cases:

  cylinder_delta_fs: cylindrical, with free-slip boundary condition at r=Rm and r=Rp
  cylinder_delta_ns: cylindrical, with zero-slip boundary conditions at r=Rm and r=Rp
  sphere_delta_fs:   spherical, with free-slip boundary condition at r=Rm and r=Rp
  sphere_smooh_ns:    spherical, with zero-slip boundary condition at r=Rm and r=Rp

The functions below take the following parameters:

   :param Rp:   outer radius
   :param Rm:   inner radius
   :param rp:   radius of density anomaly with Rm<rp<Rp
   :param n:    wave number (2D cylindrical only)
   :param l:    spherical degree (3D only)
   :param g:    scalar magnitude of forcing
   :param nu:   viscosity
   :param sign: +1 or -1 for the upper (r>rp) and lower (r<rp) half of the solution

and return four coefficients A, B, C, D for the linear combination of
biharmonic spherical functions that constitute the analytical solution.

This module has been automatically generated by extracting the solutions from
the latex source of the associated paper. If sign=+1 we use the following
substitutions

  alpha_pm = Rp/rp, alpha_mp = Rm/rp, pm=+1, mp=-1

i.e. we take the top case for the symbols \alpha_\pm, \alpha_\mp, \pm, and \mp
in the paper to obtain :math:`A_+, B_+, C_+,` and :math:`D_+` corresponding to
the upper half of the domain. If sign=-1 we have

  alpha_pm = Rm/rp, alpha_mp = Rp/rp, pm=-1, mp=+1

to obtain the :math:`A_-, B_-, C_-,` and :math:`D_-` coefficients of the lower
half of the solution.
"""


def coefficients_cylinder_delta_fs(Rp, Rm, rp, n, g, nu, sign):
    alpha_pm, alpha_mp = [Rp/rp, Rm/rp][::int(sign)]
    pm = sign

    A = -0.125*(alpha_mp**(2*n - 2) - 1)*g*pm*rp**(-n + 2)/((alpha_mp**(2*n - 2) - alpha_pm**(2*n - 2))*(n - 1)*nu)
    B = -0.125*(alpha_mp**(2*n + 2) - 1)*alpha_pm**(2*n + 2)*g*pm*rp**(n + 2)/((alpha_mp**(2*n + 2) - alpha_pm**(2*n + 2))*(n + 1)*nu)
    C = 0.125*(alpha_mp**(2*n + 2) - 1)*g*pm/((alpha_mp**(2*n + 2) - alpha_pm**(2*n + 2))*(n + 1)*nu*rp**n)
    D = 0.125*(alpha_mp**(2*n - 2) - 1)*alpha_pm**(2*n - 2)*g*pm*rp**n/((alpha_mp**(2*n - 2) - alpha_pm**(2*n - 2))*(n - 1)*nu)
    return A, B, C, D


def coefficients_cylinder_delta_ns(Rp, Rm, rp, n, g, nu, sign):
    alpha_p, alpha_m = [Rp/rp, Rm/rp]
    alpha_pm, alpha_mp = [Rp/rp, Rm/rp][::int(sign)]
    pm, mp = sign, -sign

    A = -0.125*(((alpha_m**2 - alpha_p**2)*n - (n + 1)*pm + 1/alpha_m**(2*n) - 1/alpha_p**(2*n))*(n - 1) + (alpha_m**2/alpha_p**(2*n) - alpha_p**2/alpha_m**(2*n))*n + (n**2*(alpha_m/alpha_p)**(2*mp) - (alpha_m/alpha_p)**(2*n*pm))*pm)*g*rp**(-n + 2)/((n**2*(alpha_m/alpha_p - alpha_p/alpha_m)**2 - ((alpha_m/alpha_p)**n - 1/(alpha_m/alpha_p)**n)**2)*(n - 1)*nu)
    B = -0.125*(((alpha_m**2 - alpha_p**2)*n - (n - 1)*pm - alpha_m**(2*n) + alpha_p**(2*n))*(n + 1) - (alpha_m**2*alpha_p**(2*n) - alpha_m**(2*n)*alpha_p**2)*n + (n**2*(alpha_m/alpha_p)**(2*mp) - (alpha_m/alpha_p)**(2*mp*n))*pm)*g*rp**(n + 2)/((n**2*(alpha_m/alpha_p - alpha_p/alpha_m)**2 - ((alpha_m/alpha_p)**n - 1/(alpha_m/alpha_p)**n)**2)*(n + 1)*nu)
    C = -0.125*((n**2*(alpha_m/alpha_p)**(2*pm) - (alpha_m/alpha_p)**(2*n*pm))*mp - (mp*(n - 1) + n*(1/alpha_m**2 - 1/alpha_p**2) - 1/alpha_m**(2*n) + 1/alpha_p**(2*n))*(n + 1) - n*(1/(alpha_m**(2*n)*alpha_p**2) - 1/(alpha_m**2*alpha_p**(2*n))))*g/((n**2*(alpha_m/alpha_p - alpha_p/alpha_m)**2 - ((alpha_m/alpha_p)**n - 1/(alpha_m/alpha_p)**n)**2)*(n + 1)*nu*rp**n)
    D = -0.125*((n**2*(alpha_m/alpha_p)**(2*pm) - (alpha_m/alpha_p)**(2*mp*n))*mp - (mp*(n + 1) + n*(1/alpha_m**2 - 1/alpha_p**2) + alpha_m**(2*n) - alpha_p**(2*n))*(n - 1) + n*(alpha_m**(2*n)/alpha_p**2 - alpha_p**(2*n)/alpha_m**2))*g*rp**n/((n**2*(alpha_m/alpha_p - alpha_p/alpha_m)**2 - ((alpha_m/alpha_p)**n - 1/(alpha_m/alpha_p)**n)**2)*(n - 1)*nu)
    return A, B, C, D


def coefficients_sphere_delta_fs(Rp, Rm, rp, l, g, nu, sign):
    alpha_pm, alpha_mp = [Rp/rp, Rm/rp][::int(sign)]
    pm = sign

    A = -0.5*(alpha_mp**(2*l - 1) - 1)*g*pm*rp**(-l + 2)/((alpha_mp**(2*l - 1) - alpha_pm**(2*l - 1))*(2*l + 1)*(2*l - 1)*nu)
    B = -0.5*(alpha_mp**(-2*l - 3) - 1)*g*pm*rp**(l + 3)/((alpha_mp**(-2*l - 3) - alpha_pm**(-2*l - 3))*(2*l + 3)*(2*l + 1)*nu)
    C = 0.5*(alpha_mp**(2*l + 3) - 1)*g*pm/((alpha_mp**(2*l + 3) - alpha_pm**(2*l + 3))*(2*l + 3)*(2*l + 1)*nu*rp**l)
    D = 0.5*(alpha_mp**(-2*l + 1) - 1)*g*pm*rp**(l + 1)/((alpha_mp**(-2*l + 1) - alpha_pm**(-2*l + 1))*(2*l + 1)*(2*l - 1)*nu)
    return A, B, C, D


def coefficients_sphere_delta_ns(Rp, Rm, rp, l, g, nu, sign):
    alpha_p, alpha_m = [Rp/rp, Rm/rp]
    alpha_pm, alpha_mp = [Rp/rp, Rm/rp][::int(sign)]
    pm, mp = sign, -sign

    A = -0.5*(alpha_m**2 - alpha_p**2 - (2*l + 1)*mp*(alpha_m/alpha_p)**(2*mp)/(2*l - 1) - (2*l + 3)*pm/(2*l + 1) + 2*(alpha_m**(-2*l - 1) - alpha_p**(-2*l - 1))/(2*l + 1) + 2*(alpha_m**2*alpha_p**(-2*l - 1) - alpha_m**(-2*l - 1)*alpha_p**2)/(2*l - 1) - 4*pm*(alpha_m/alpha_p)**((2*l + 1)*pm)/((2*l + 1)*(2*l - 1)))*g*rp**(-l + 2)/(((2*l + 1)**2*(alpha_m**2/alpha_p**2 + alpha_p**2/alpha_m**2) - 2*(2*l + 3)*(2*l - 1) - 4*(alpha_m/alpha_p)**(2*l + 1) - 4*(alpha_m/alpha_p)**(-2*l - 1))*nu)
    B = -0.5*(alpha_m**2 - alpha_p**2 - (2*l + 1)*mp*(alpha_m/alpha_p)**(2*mp)/(2*l + 3) - (2*l - 1)*pm/(2*l + 1) - 2*(alpha_m**2*alpha_p**(2*l + 1) - alpha_m**(2*l + 1)*alpha_p**2)/(2*l + 3) - 2*(alpha_m**(2*l + 1) - alpha_p**(2*l + 1))/(2*l + 1) - 4*pm*(alpha_m/alpha_p)**((2*l + 1)*mp)/((2*l + 3)*(2*l + 1)))*g*rp**(l + 3)/(((2*l + 1)**2*(alpha_m**2/alpha_p**2 + alpha_p**2/alpha_m**2) - 2*(2*l + 3)*(2*l - 1) - 4*(alpha_m/alpha_p)**(2*l + 1) - 4*(alpha_m/alpha_p)**(-2*l - 1))*nu)
    C = 0.5*((2*l + 1)*pm*(alpha_m/alpha_p)**(2*pm)/(2*l + 3) + (2*l - 1)*mp/(2*l + 1) - 2*(alpha_m**(-2*l - 1) - alpha_p**(-2*l - 1))/(2*l + 1) + 4*mp*(alpha_m/alpha_p)**((2*l + 1)*pm)/((2*l + 3)*(2*l + 1)) + 2*(alpha_m**(-2*l - 1)/alpha_p**2 - alpha_p**(-2*l - 1)/alpha_m**2)/(2*l + 3) + 1/alpha_m**2 - 1/alpha_p**2)*g/(((2*l + 1)**2*(alpha_m**2/alpha_p**2 + alpha_p**2/alpha_m**2) - 2*(2*l + 3)*(2*l - 1) - 4*(alpha_m/alpha_p)**(2*l + 1) - 4*(alpha_m/alpha_p)**(-2*l - 1))*nu*rp**l)
    D = 0.5*((2*l + 1)*pm*(alpha_m/alpha_p)**(2*pm)/(2*l - 1) + (2*l + 3)*mp/(2*l + 1) + 2*(alpha_m**(2*l + 1) - alpha_p**(2*l + 1))/(2*l + 1) + 4*mp*(alpha_m/alpha_p)**((2*l + 1)*mp)/((2*l + 1)*(2*l - 1)) - 2*(alpha_m**(2*l + 1)/alpha_p**2 - alpha_p**(2*l + 1)/alpha_m**2)/(2*l - 1) + 1/alpha_m**2 - 1/alpha_p**2)*g*rp**(l + 1)/(((2*l + 1)**2*(alpha_m**2/alpha_p**2 + alpha_p**2/alpha_m**2) - 2*(2*l + 3)*(2*l - 1) - 4*(alpha_m/alpha_p)**(2*l + 1) - 4*(alpha_m/alpha_p)**(-2*l - 1))*nu)
    return A, B, C, D

def coefficients_cylinder_delta_nsfs(Rp, Rm, Rd, n, g, nu, sign):
    Ap =  -1 / nu / Rd ** (-n + 2) / Rd ** n / (Rp ** (-n + 2) * Rm ** n * n - Rm ** (-n + 2) * Rp ** n * n - Rp ** (-n + 2) * Rm ** n + Rm ** (-n + 2) * Rp ** n) * (Rd ** (-n + 2) * Rm ** n - Rm ** (-n + 2) * Rd ** n) * g * Rd ** 2 * Rp ** (-n + 2) / 8
    Bp = -Rp ** (n + 2) * (Rm ** (-n) * Rd ** (n + 2) - Rm ** (n + 2) * Rd ** (-n)) * g * Rd ** 2 / nu / Rd ** (n + 2) / Rd ** (-n) / (Rm ** (-n) * Rp ** (n + 2) * n - Rm ** (n + 2) * Rp ** (-n) * n + Rm ** (-n) * Rp ** (n + 2) - Rm ** (n + 2) * Rp ** (-n)) / 8
    Cp = Rp ** (-n) * (Rm ** (-n) * Rd ** (n + 2) - Rm ** (n + 2) * Rd ** (-n)) * g * Rd ** 2 / nu / Rd ** (n + 2) / Rd ** (-n) / (Rm ** (-n) * Rp ** (n + 2) * n - Rm ** (n + 2) * Rp ** (-n) * n + Rm ** (-n) * Rp ** (n + 2) - Rm ** (n + 2) * Rp ** (-n)) / 8
    Dp = 1 / nu / Rd ** (-n + 2) / Rd ** n / (Rp ** (-n + 2) * Rm ** n * n - Rm ** (-n + 2) * Rp ** n * n - Rp ** (-n + 2) * Rm ** n + Rm ** (-n + 2) * Rp ** n) * (Rd ** (-n + 2) * Rm ** n - Rm ** (-n + 2) * Rd ** n) * Rp ** n * g * Rd ** 2 / 8
    
    Am = (Rp ** (-n + 2) * Rd ** n - Rd ** (-n + 2) * Rp ** n) / nu / Rd ** (-n + 2) / Rd ** n / (Rp ** (-n + 2) * Rm ** n * n - Rm ** (-n + 2) * Rp ** n * n - Rp ** (-n + 2) * Rm ** n + Rm ** (-n + 2) * Rp ** n) * g * Rd ** 2 * Rm ** (-n + 2) / 8
    Bm = -Rm ** (n + 2) * (Rp ** (-n) * Rd ** (n + 2) - Rp ** (n + 2) * Rd ** (-n)) * g * Rd ** 2 / nu / Rd ** (n + 2) / Rd ** (-n) / (Rm ** (-n) * Rp ** (n + 2) * n - Rm ** (n + 2) * Rp ** (-n) * n + Rm ** (-n) * Rp ** (n + 2) - Rm ** (n + 2) * Rp ** (-n)) / 8
    Cm = (Rp ** (-n) * Rd ** (n + 2) - Rp ** (n + 2) * Rd ** (-n)) * Rm ** (-n) * g * Rd ** 2 / nu / Rd ** (n + 2) / Rd ** (-n) / (Rm ** (-n) * Rp ** (n + 2) * n - Rm ** (n + 2) * Rp ** (-n) * n + Rm ** (-n) * Rp ** (n + 2) - Rm ** (n + 2) * Rp ** (-n)) / 8
    Dm = -Rm ** n * (Rp ** (-n + 2) * Rd ** n - Rd ** (-n + 2) * Rp ** n) / nu / Rd ** (-n + 2) / Rd ** n / (Rp ** (-n + 2) * Rm ** n * n - Rm ** (-n + 2) * Rp ** n * n - Rp ** (-n + 2) * Rm ** n + Rm ** (-n + 2) * Rp ** n) * g * Rd ** 2 / 8

    if sign > 0:
        return Ap, Bp, Cp, Dp
    else:
        return Am, Bm, Cm, Dm

def coefficients_sphere_delta_nsfs(Rp, Rm, Rd, l, g, nu, sign):
    Ap = -Rd ** 2 * g * (2 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) * l + 2 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) * l - 2 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2) * l - 2 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) * l + Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) + 2 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) - Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) - Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2) + Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) - 2 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** (-l - 1) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2)) / (8 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l ** 3 - 8 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l ** 3 + 4 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l ** 2 + 8 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) * l ** 2 - 8 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) * l ** 2 - 4 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l ** 2 - 2 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l + 2 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l - Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) - 2 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) + 2 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) + Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1)) / Rd ** (-l + 1) / Rd ** (l + 2) / Rd ** (-l - 1) / Rd ** l / nu / 2
    Bp =  -(2 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) * l + 2 * Rm ** l * Rm ** (l + 2) * Rp ** l * Rp ** (-l + 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) * l - 2 * Rm ** l * Rm ** (l + 2) * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) * l - 2 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2) * l + Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) + 3 * Rm ** l * Rm ** (l + 2) * Rp ** l * Rp ** (-l + 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) - Rm ** l * Rm ** (l + 2) * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) - 2 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) + 2 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) - 3 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2)) / Rd ** l * g * Rd ** 2 / nu / Rd ** (-l - 1) / Rd ** (l + 2) / Rd ** (-l + 1) / (4 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l ** 2 - 4 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l ** 2 + 4 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l + 4 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) * l - 4 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) * l - 4 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l + Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) + 2 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) - 2 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) - Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1)) / (3 + 2 * l) / 2
    Cp = Rd ** 2 * g * (2 * Rm ** l * Rm ** (-l - 1) * Rp ** l * Rp ** (-l + 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) * l + 2 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) * l - 2 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2) * l - 2 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) * l + 3 * Rm ** l * Rm ** (-l - 1) * Rp ** l * Rp ** (-l + 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) - 2 * Rm ** l * Rm ** (-l - 1) * Rp ** (-l - 1) * Rp ** (-l + 1) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) + 2 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) + Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) - 3 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2) - Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1)) / Rd ** l / nu / Rd ** (-l - 1) / Rd ** (l + 2) / Rd ** (-l + 1) / (4 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l ** 2 - 4 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l ** 2 + 4 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l + 4 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) * l - 4 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) * l - 4 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l + Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) + 2 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) - 2 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) - Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1)) / (3 + 2 * l) / 2
    Dp = (2 * Rm ** l * Rm ** (-l - 1) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) * l + 2 * Rm ** l * Rm ** (l + 2) * Rp ** l * Rp ** (-l - 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) * l - 2 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) * l - 2 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2) * l + 2 * Rm ** l * Rm ** (-l - 1) * Rp ** l * Rp ** (l + 2) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) - Rm ** l * Rm ** (-l - 1) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) + Rm ** l * Rm ** (l + 2) * Rp ** l * Rp ** (-l - 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) + Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) - 2 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2) - Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2)) / (8 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l ** 3 - 8 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l ** 3 + 4 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l ** 2 + 8 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) * l ** 2 - 8 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) * l ** 2 - 4 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l ** 2 - 2 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l + 2 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l - Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) - 2 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) + 2 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) + Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1)) / Rd ** (-l + 1) / Rd ** (l + 2) / Rd ** (-l - 1) / Rd ** l / nu * g * Rd ** 2 / 2
    
    Am = -1 / (8 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l ** 3 - 8 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l ** 3 + 4 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l ** 2 + 8 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) * l ** 2 - 8 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) * l ** 2 - 4 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l ** 2 - 2 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l + 2 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l - Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) - 2 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) + 2 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) + Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1)) / Rd ** (-l + 1) / Rd ** (l + 2) / Rd ** (-l - 1) / Rd ** l / nu * (2 * Rm ** (-l - 1) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) * l - 2 * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2) * l + 2 * Rm ** (l + 2) * Rp ** l * Rp ** (-l - 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) * l - 2 * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) * l + 2 * Rm ** (-l - 1) * Rp ** l * Rp ** (l + 2) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) - Rm ** (-l - 1) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) - Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2) + Rm ** (l + 2) * Rp ** l * Rp ** (-l - 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) + Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) - 2 * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2)) * g * Rd ** 2 * Rm ** (-l + 1) / 2
    Bm = -Rm ** (l + 2) * (2 * Rm ** l * Rp ** l * Rp ** (-l + 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) * l - 2 * Rm ** l * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) * l + 2 * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) * l - 2 * Rm ** (-l + 1) * Rp ** l * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2) * l + 3 * Rm ** l * Rp ** l * Rp ** (-l + 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) - 2 * Rm ** l * Rp ** (-l - 1) * Rp ** (-l + 1) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) - Rm ** l * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) + Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) + 2 * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) - 3 * Rm ** (-l + 1) * Rp ** l * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2)) * g * Rd ** 2 / (4 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l ** 2 - 4 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l ** 2 + 4 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l + 4 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) * l - 4 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) * l - 4 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l + Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) + 2 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) - 2 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) - Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1)) / (3 + 2 * l) / Rd ** (-l + 1) / Rd ** (l + 2) / Rd ** (-l - 1) / nu / Rd ** l / 2
    Cm = (2 * Rm ** l * Rp ** l * Rp ** (-l + 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) * l - 2 * Rm ** l * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) * l + 2 * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) * l - 2 * Rm ** (-l + 1) * Rp ** l * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2) * l + 3 * Rm ** l * Rp ** l * Rp ** (-l + 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) - 2 * Rm ** l * Rp ** (-l - 1) * Rp ** (-l + 1) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) - Rm ** l * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) + Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) + 2 * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) - 3 * Rm ** (-l + 1) * Rp ** l * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2)) * Rm ** (-l - 1) * g * Rd ** 2 / (4 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l ** 2 - 4 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l ** 2 + 4 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l + 4 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) * l - 4 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) * l - 4 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l + Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) + 2 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) - 2 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) - Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1)) / (3 + 2 * l) / Rd ** (-l + 1) / Rd ** (l + 2) / Rd ** (-l - 1) / nu / Rd ** l / 2
    Dm = 1 / (8 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l ** 3 - 8 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l ** 3 + 4 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l ** 2 + 8 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) * l ** 2 - 8 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) * l ** 2 - 4 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l ** 2 - 2 * Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * l + 2 * Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1) * l - Rm ** l * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) - 2 * Rm ** l * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) + 2 * Rm ** (-l - 1) * Rm ** (-l + 1) * Rp ** l * Rp ** (l + 2) + Rm ** (l + 2) * Rm ** (-l + 1) * Rp ** l * Rp ** (-l - 1)) / Rd ** (-l + 1) / Rd ** (l + 2) / Rd ** (-l - 1) / Rd ** l / nu * Rm ** l * (2 * Rm ** (-l - 1) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) * l - 2 * Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2) * l + 2 * Rm ** (l + 2) * Rp ** l * Rp ** (-l - 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) * l - 2 * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) * l + 2 * Rm ** (-l - 1) * Rp ** l * Rp ** (l + 2) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) - Rm ** (-l - 1) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (l + 2) * Rd ** (-l + 1) - Rm ** (-l - 1) * Rp ** (l + 2) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2) + Rm ** (l + 2) * Rp ** l * Rp ** (-l - 1) * Rd ** (-l - 1) * Rd ** (l + 2) * Rd ** (-l + 1) + Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (l + 2) * Rd ** l * Rd ** (-l - 1) * Rd ** (-l + 1) - 2 * Rm ** (l + 2) * Rp ** (-l - 1) * Rp ** (-l + 1) * Rd ** l * Rd ** (-l - 1) * Rd ** (l + 2)) * g * Rd ** 2 / 2
    
    if sign > 0:
        return Ap, Bp, Cp, Dp
    else:
        return Am, Bm, Cm, Dm
