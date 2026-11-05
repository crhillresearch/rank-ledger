#!/usr/bin/env sage -python
"""Exact replay of the C4 genus-one rank >= 6 proof with SageMath.

Run: sage -python verify.py

The four parent sections are independently known by the theorem of Elkies
and Klagsbrun (2020); their defining identities are checked here. The rank-4
assertion is a cited published theorem, not re-proved by this script.
"""
import json
from fractions import Fraction as Q
from functools import reduce
from math import gcd, isqrt, lcm
from pathlib import Path
import sympy as S
from sage.all import EllipticCurve, GF, QQ, ZZ

HERE = Path(__file__).resolve().parent
def read(name):
    return json.loads((HERE / 'data' / name).read_text())

PARENT = read('parent-c4-k3.json')
COVERS = read('quadratic-covers.json')
FIBER = read('common-fiber.json')
BASE = read('genus-one-base.json')
CERT = read('rank6-family-certificate.json')
DATA = PARENT | COVERS | FIBER | BASE
assert CERT['data_files'] == ['parent-c4-k3.json', 'quadratic-covers.json',
                              'common-fiber.json', 'genus-one-base.json']
assert CERT['parent_rank_lower_bound'] == 4
assert CERT['rank_lower_bound'] == 6
assert CERT['torsion_subgroup'] == 'C4'
assert CERT['parameter_base_genus'] == 1
assert CERT['base_field'] == 'Q(t)(sqrt(qA),sqrt(qB))'
assert CERT['independent_square_classes'] is True
assert CERT['auxiliary_positive_rank_proved'] is True
assert CERT['infinitely_many_rank6_specializations'] is True
assert CERT['exact_generic_rank_claimed'] is False
t, u, w = S.symbols('t u w')

def rat(x):
    v = S.Rational(str(x))
    return Q(int(S.numer(v)), int(S.denom(v)))

def frac(x):
    z = S.cancel(x)
    assert not z.free_symbols, z
    return rat(z)

def poly(items, var):
    return sum(S.Rational(str(c))*var**i for i, c in enumerate(items))

def check(label, test):
    if not test:
        raise AssertionError(label)
    print('PASS:', label, flush=True)

def sqrtrational(x):
    x = Q(x)
    if x < 0:
        return None
    n, d = isqrt(x.numerator), isqrt(x.denominator)
    return Q(n,d) if n*n == x.numerator and d*d == x.denominator else None

def good_count(a2, a4, a6, p):
    a2,a4,a6 = [Q(v) for v in (a2,a4,a6)]
    assert all(x.denominator % p for x in (a2,a4,a6)), f'nonintegral at p={p}'
    discr = 16*(a2*a2*a4*a4 - 4*a4*a4*a4 - 4*a2*a2*a2*a6 -27*a6*a6 +18*a2*a4*a6)
    assert discr.denominator % p and discr.numerator % p, f'bad reduction at p={p}'
    def red(q):
        return (q.numerator%p)*pow(q.denominator,-1,p)%p
    c, A, B = [red(z) for z in (a2,a4,a6)]
    squares = {n*n%p for n in range(p)}
    order = 1
    for x in range(p):
        z = (x*x*x+c*x*x+A*x+B)%p
        order += 1 if z == 0 else (2 if z in squares else 0)
    return order

def add(P, R, a2, a4):
    if P is None:
        return R
    if R is None:
        return P
    x,y = P
    z,v = R
    if x == z and y == -v:
        return None
    if x == z:
        if y == 0:
            return None
        m = (3*x*x+2*a2*x+a4)/(2*y)
    else:
        m = (v-y)/(z-x)
    nx = m*m-a2-x-z
    ny = -m*(nx-x)-y
    return (nx,ny)

def neg(P):
    return None if P is None else (P[0],-P[1])

def mul(P, n, a2, a4):
    out = None
    while n:
        if n & 1:
            out = add(out,P,a2,a4)
        P = add(P,P,a2,a4)
        n //= 2
    return out

# Original K3 and four published independent rational sections.
a = (8*t-1)*(32*t+7)
g = (15*t-8)*(31*t-7)
b = 8*(t+1)*g
A = S.expand(a*a-8*b)
B = S.expand(16*b*b)
assert S.expand(S.sympify(PARENT['a'], locals={'t': t})-a) == 0
assert S.expand(S.sympify(PARENT['b'], locals={'t': t})-b) == 0
assert S.expand(S.sympify(PARENT['g'], locals={'t': t})-g) == 0
source = DATA['four_Elkies_Klagsbrun_Tate_x_coordinates']
xs = [S.sympify(v,locals={'t':t}) for v in source]
zs = [
    S.Rational(19,4)*(t+1)*(31*t-7)*(32*t+7)*(127*t-44),
    (8*t-1)*(15*t-8)*(16*t+1)*(31*t-7)*(32*t+7)*(46*t-15),
    (t+1)*(8*t-1)*(14*t-9)*(15*t-8)*(16*t-7)*(32*t+7),
    4*(t+1)*(8*t+7)*(15*t-8)*(32*t+7)*(56*t*t+8*t-57)
]
for i,(x,z) in enumerate(zip(xs,zs),1):
    assert S.expand(z*z-(x+b)*(4*x*x+a*a*(x+b))) == 0
    X,Y=4*(x+b),4*z
    assert S.expand(Y*Y-X**3-A*X*X-B*X) == 0
check('four published parent sections satisfy their equations', True)

# Geometrically exact 2-neighbor and its rational sections.
F = S.expand(u*u*a*a+4*u*g*(u-8*(t+1))**2)
Ts = [S.Rational(8,15), S.Rational(7,31), (32*u-361)/(60*u+361)]
Vs = [u*a.subs(t,Ts[0]), u*a.subs(t,Ts[1]),
      19*u*(4*u-25)*(1424*u-61731)/(60*u+361)**2]
for ti,vi in zip(Ts,Vs):
    assert S.cancel(F.subs(t,ti)-vi*vi) == 0
check('2-neighbor quartic and three rational section identities', True)

def interpolation(signs):
    return S.cancel(sum(signs[j]*Vs[j]*S.prod(
        (t-Ts[k])/(Ts[j]-Ts[k]) for k in range(3) if k != j)
        for j in range(3)))

def section_at(name, uu, time):
    M = DATA['neighbor_chord_maps'][name]
    yy = interpolation(M['interpolation_signs'])
    gg = frac(g.subs(t,time))
    vv = frac(yy.subs({t:S.Rational(time.numerator,time.denominator),
                       u:S.Rational(uu.numerator,uu.denominator)}))
    return (4*uu*gg,4*gg*vv)

quad = {}
for name in ('A','B'):
    M = DATA['neighbor_chord_maps'][name]
    N,D = [poly(M[k],u) for k in ('numerator_low_to_high','denominator_low_to_high')]
    q = poly(DATA['branch_polynomials'][name],t)
    V = interpolation(M['interpolation_signs'])
    assert S.cancel(F.subs(t,N/D)-V.subs(t,N/D)**2) == 0
    disc = S.discriminant(N-t*D,u)
    assert S.expand(disc-19**2*q) == 0
    quad[name]=(N,D,q,V)
check('both quadratic maps and both full section identities', True)
qA,qB=quad['A'][2],quad['B'][2]
assert S.gcd(qA,S.diff(qA,t)) == 1
assert S.gcd(qB,S.diff(qB,t)) == 1
assert S.gcd(qA,qB) == 1
check('distinct squarefree degree-two branch loci (genus-one compositum)', True)

# A smooth common fiber supplies exact C4 torsion and nonzero anti-invariants.
common = DATA['common_rational_fiber']
t0=rat(common['t'])
assert str(t0) == CERT['common_fiber_t']
qAv=frac(qA.subs(t,S.Rational(t0.numerator,t0.denominator)))
qBv=frac(qB.subs(t,S.Rational(t0.numerator,t0.denominator)))
assert sqrtrational(qAv)==rat(common['sqrt_qA'])
assert sqrtrational(qBv)==rat(common['sqrt_qB'])
a0,b0=[frac(z.subs(t,S.Rational(t0.numerator,t0.denominator))) for z in (a,b)]
A0,B0=a0*a0-8*b0,16*b0*b0
orders={int(p):v for p,v in common['good_prime_orders'].items()}
assert orders == {int(p):v for p,v in CERT['common_fiber_good_prime_orders'].items()}
for p,expected in orders.items():
    assert good_count(A0,B0,0,p)==expected
check('common-fiber point counts and good reduction at 13, 19, 43, 47, 53', True)
assert gcd(orders[13],orders[19]) == 4
assert CERT['common_fiber_torsion_order_bound'] == 4
T4=(4*b0,4*a0*b0)
assert mul(T4,2,A0,B0)==(Q(0),Q(0))
assert mul(T4,4,A0,B0) is None
E0 = EllipticCurve(QQ, [0, QQ(A0.numerator)/A0.denominator, 0,
                         QQ(B0.numerator)/B0.denominator, 0])
assert E0([QQ(T4[0].numerator)/T4[0].denominator,
           QQ(T4[1].numerator)/T4[1].denominator]).order() == 4
for p in (13, 19):
    assert E0.change_ring(GF(p)).cardinality() == orders[p]
check('the common smooth fiber has torsion exactly C4', True)
for name in ('A','B'):
    assert name in CERT['cover_anti_invariant_witnesses']
    N,D,q,V=quad[name]
    rootlist = [rat(z) for z in DATA['neighbor_chord_maps'][name]['roots_at_test_t']]
    assert rootlist[0]!=rootlist[1]
    pp=[]
    for root in rootlist:
        U=S.Rational(root.numerator,root.denominator)
        assert frac((N-t0*D).subs(u,U)) == 0
        P=section_at(name,root,t0)
        x,y=P
        assert y*y == x**3+A0*x*x+B0*x
        pp.append(P)
    R=add(pp[0],neg(pp[1]),A0,B0)
    assert R is not None and mul(R,4,A0,B0) is not None
    assert CERT['anti_invariant_fourfold_nonzero'][name] is True
    print(f'PASS: cover {name} anti-invariant is nontorsion (4*(P-sigma P) != O)',flush=True)

# A rational genus-one quartic and its elliptic Jacobian.
cov = DATA['conic_parametrization']
N,D,W=[poly(cov[k],u) for k in ('N_low_to_high','D_low_to_high','W_low_to_high')]
assert S.expand(S.together(qA.subs(t,N/D)*D**2-W**2)) == 0
qBP = S.Poly(qB,t)
Fquart = S.Poly(S.expand(qBP.nth(2)*N*N + qBP.nth(1)*N*D + qBP.nth(0)*D*D),u)
assert [int(Fquart.nth(i)) for i in range(5)] == list(map(int,cov['quartic_low_to_high']))
f=[int(x) for x in cov['quartic_low_to_high']]
e=int(cov['quartic_constant_square_root'])
assert e*e==f[0]
a4q,b3,c2,d1=f[4],f[3],f[2],f[1]
J2 = c2
J4 = b3*d1-4*a4q*e*e
J6 = e*e*b3*b3+a4q*d1*d1-4*a4q*c2*e*e
assert [J2,J4,J6]==list(map(int,cov['jacobian_a2_a4_a6']))
# Confirm quartic-to-Jacobian rational map as an identity modulo w^2=F.
XX = (2*e*(w+e)+d1*u)/u**2
YY = ((XX**2-4*a4q*e*e)*u-(XX*d1+2*e*e*b3))/(2*e)
residual=S.together(YY**2-XX**3-J2*XX**2-J4*XX-J6).as_numer_denom()[0]
assert S.Poly(residual,w).rem(S.Poly(w*w-Fquart.as_expr(),w)).is_zero
check('conic parametrization and exact quartic-to-Jacobian identity', True)
uv,wv=rat(cov['infinite_point_quartic_U']),rat(cov['infinite_point_quartic_w'])
assert wv*wv == sum(Q(f[i])*uv**i for i in range(5))
Jpoint=(frac(XX.subs({u:S.Rational(uv.numerator,uv.denominator),
                       w:S.Rational(wv.numerator,wv.denominator)})),
        frac(YY.subs({u:S.Rational(uv.numerator,uv.denominator),
                       w:S.Rational(wv.numerator,wv.denominator)})))
assert [str(z) for z in Jpoint]==cov['jacobian_infinite_point_XY']
assert [str(z) for z in Jpoint]==CERT['auxiliary_nontorsion_point_XY']
assert Jpoint[1]**2==Jpoint[0]**3+J2*Jpoint[0]**2+J4*Jpoint[0]+J6
jac_orders={int(p):v for p,v in cov['good_prime_orders'].items()}
assert jac_orders == {int(p):v for p,v in CERT['auxiliary_jacobian_good_prime_orders'].items()}
for p,expected in jac_orders.items():
    assert good_count(J2,J4,J6,p)==expected
assert gcd(jac_orders[37],jac_orders[41],jac_orders[43]) == 2
assert CERT['auxiliary_jacobian_torsion_order_bound'] == 2
assert Jpoint[1] != 0
J_sage = EllipticCurve(QQ, [0, ZZ(J2), 0, ZZ(J4), ZZ(J6)])
R_sage = J_sage([QQ(Jpoint[0].numerator)/Jpoint[0].denominator,
                 QQ(Jpoint[1].numerator)/Jpoint[1].denominator])
assert R_sage != J_sage(0) and 2*R_sage != J_sage(0)
for p in (37, 41, 43):
    assert J_sage.change_ring(GF(p)).cardinality() == jac_orders[p]
check('auxiliary Jacobian point is nontorsion (torsion order divides 2)', True)

# Verify that an explicit rational common-base point is regular at the
# reduction primes used to preserve exact C4 torsion along an infinite orbit.
u0=rat(cov['common_fiber_parameter_U0'])
nu0s=S.Rational(u0.numerator,u0.denominator)
assert frac((N/D).subs(u,nu0s)) == t0
assert frac((W/D).subs(u,nu0s)) == rat(common['sqrt_qA'])
D0=frac(D.subs(u,nu0s))
w0=D0*rat(common['sqrt_qB'])
assert w0*w0 == sum(Q(f[i])*u0**i for i in range(5))
J0x = frac(XX.subs({u:S.Rational(u0.numerator,u0.denominator),
                     w:S.Rational(w0.numerator,w0.denominator)}))
J0y = frac(YY.subs({u:S.Rational(u0.numerator,u0.denominator),
                     w:S.Rational(w0.numerator,w0.denominator)}))
assert J0y**2==J0x**3+J2*J0x**2+J4*J0x+J6
inverse_den = J0x*J0x-4*a4q*e*e
assert inverse_den != 0
assert (2*e*J0y+J0x*d1+2*e*e*b3)/inverse_den == u0
for p in (43,47,53):
    for value in (u0,D0,w0,J0x,J0y,inverse_den):
        assert value.denominator%p, f'parameter pole at p={p}'
    assert u0.numerator%p and D0.numerator%p and e%p and inverse_den.numerator%p
assert gcd(orders[43],orders[47],orders[53]) == 4
step=lcm(jac_orders[43],jac_orders[47],jac_orders[53])
assert step==cov['torsion_preserving_progression_step']==728
assert step==CERT['torsion_preserving_progression_step']
check('infinite progressions preserve the exact C4 torsion via 43,47,53', True)
# Nonconstant j: B has zero at t=-1 and is not identically zero,
# but t=0 is nonsingular; hence j has a pole at t=-1.
assert b.subs(t,-1)==0 and b.subs(t,0)!=0
assert (a*a-16*b).subs(t,-1)!=0
check('j-invariant nonconstant and specialization theorem applicable', True)

print('\nCERTIFIED (relative to Elkies–Klagsbrun parent rank-4 theorem):')
print('  over a positive-rank genus-one base, C4 torsion and rank >= 6;')
print('  infinitely many distinct rational C4 curves have rank >= 6.')
print('  Does NOT establish novelty or an improvement over the existing bound.')
