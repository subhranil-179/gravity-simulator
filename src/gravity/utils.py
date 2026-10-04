from .constants import G

def calc_g_force(m1, m2, r):
    f = G*(m1*m2)/(r**(2))
    return f
