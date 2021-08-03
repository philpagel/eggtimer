#!/usr/bin/python3
import click
from math import log, pi


def BoilingTime(m, t0, t1, e, r=2 / 3):
    """returns the boiling time [s] for the egg

     m:    mass [g]
     t0:   egg temperature at time 0
     t1:   target egg temperature
     e:    elevation [m]
     r:    fraction of yolk compared to egg mass

     All temperatures in °C
"""
    c = 3.7  # specific heat capacity
    rho = 1.038  # density
    kappa = 5.4e-3  # thermal conductivity

    # compute boiling time
    TW = boiltemp(e)
    lmbda = (c * rho ** (1 - r)) / (kappa * pi ** 2 * (4 * pi / 3) ** r)
    boiltime = lmbda * m ** r * log(0.76 * (t0 - TW) / (t1 - TW))

    return boiltime


def airpressure(h=0):
    "return atmospheric pressure at altitude h [m]"

    return 1013.25 * (1 - (0.0065 * h) / 288.15) ** 5.255


def boiltemp(e=0):
    "return boiling temperature at elevation e [m]"

    Hmv = 40.657e3  # enthalpy of vaporization
    R = 8.314  # gas constant
    T0 = 373.15  # boiling temperature at sea level [K]
    P0 = 1013.25
    P1 = airpressure(e)

    T1 = Hmv / (R * log(P0 / P1) + Hmv / T0)

    return T1 - 273.15


def ms(seconds):
    """return the tupple (minutes, seconds) that corresponds to `seconds`
    """

    seconds = int(round(seconds))
    m = round(seconds // 60)
    s = round(seconds % 60)

    return (m, s)


@click.command()
@click.option("-m", "--mass", "m", default=70, help="Egg mass [g]")
@click.option("-s", "--t0", "t0", default=6, help="Starting temperature [°C]")
@click.option("-t", "--t1", "t1", default=70, help="Target temperature [°C]")
@click.option("-e", "--elevation", "e", default=0, help="Elevation over sea level [m]")
def main(m, t0, t1, e):

    min, sec = ms(BoilingTime(m=m, t0=t0, t1=t1, e=e))
    print(f"Egg mass:      {m} g")
    print(f"Starting temp: {t0} °C")
    print(f"Target temp:   {t1} °C")
    print(f"Elevation:     {e} m")
    print(f"Boiling time:  {min}:{sec} (min:sec)")


if __name__ == "__main__":
    main()
