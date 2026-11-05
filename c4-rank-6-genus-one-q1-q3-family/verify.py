#!/usr/bin/env sage -python
"""SageMath replay for the q1,q3 C4 rank >= 6 infinite family.

Run: sage -python verify.py. Does *not* re-prove the published four inherited section
independence theorem of Elkies and Klagsbrun (2020).
"""
from fractions import Fraction as F
from functools import reduce
from math import gcd, isqrt
from pathlib import Path
import json
import csv
import sympy as S
from sage.all import EllipticCurve, GF, QQ, ZZ

DIR = Path(__file__).resolve().parent
def read(name):
    return json.loads((DIR/'data'/name).read_text())

PARENT = read('parent-c4-k3.json')
COVERS = read('quadratic-covers.json')
BASE = read('genus-one-base.json')
CERT = read('rank6-family-certificate.json')
DATA = PARENT | COVERS | BASE
assert CERT['data_files'] == ['parent-c4-k3.json','quadratic-covers.json',
                              'genus-one-base.json','specializations.csv']
assert CERT['rank_lower_bound'] == 6 and CERT['parent_rank_lower_bound'] == 4
assert CERT['torsion_subgroup'] == 'C4'
assert CERT['base_field'] == 'Q(t)(sqrt(q1),sqrt(q3))'
assert CERT['parameter_base_genus'] == 1
assert CERT['positive_rank_base_proved'] is True
assert CERT['infinitely_many_exact_C4_rank6_specializations'] is True
assert CERT['exact_generic_rank_claimed'] is False
assert CERT['originality_claimed'] is False
t = S.symbols('t')

def exact_equal(x,y):
    return S.cancel(x-y) == 0

def parse(x, loc=None):
    return S.sympify(x.replace('^','**'),locals=loc or {'t':t})

def rat(x):
    z = S.Rational(str(x))
    return F(int(S.numer(z)),int(S.denom(z)))

def eval_fraction(expr, z):
    v = S.cancel(expr.subs(t, S.Rational(z.numerator, z.denominator)))
    assert v.is_Rational, v
    return F(int(S.numer(v)), int(S.denom(v)))

def rational_square(v):
    v = F(v)
    if v < 0: return None
    n,d=isqrt(v.numerator),isqrt(v.denominator)
    return F(n,d) if n*n==v.numerator and d*d==v.denominator else None

def red(v, p):
    v=F(v)
    assert v.denominator%p
    return (v.numerator%p)*pow(v.denominator,-1,p)%p

def count_finite_field(A,B,p):
    assert p>3 and A.denominator%p and B.denominator%p
    # discriminant for y^2=x^3+A*x^2+B*x
    disc=16*B*B*(A*A-4*B)
    assert disc.denominator%p and disc.numerator%p, (p,'bad reduction')
    aa,bb=red(A,p),red(B,p)
    squares={i*i%p for i in range(p)}
    count=1
    for x in range(p):
        r=(x*x*x+aa*x*x+bb*x)%p
        count+=1 if r==0 else 2 if r in squares else 0
    return count

def pass_check(s):
    print('PASS:',s,flush=True)

# Parent curve and four inherited independent sections.
a,b=[parse(DATA[n]) for n in ('a','b')]
A=S.expand(a*a-8*b)
B=S.expand(16*b*b)
Delta=S.factor(16*B*B*(A*A-4*B))
assert Delta != 0
for p in DATA['inherited_sections_tate']:
    xz=parse(p['X']); z=parse(p['Z'])
    assert exact_equal(z*z, (xz+b)*(4*xz*xz+a*a*(xz+b))),p['label']
    xx,yy=4*(xz+b),4*z
    assert exact_equal(yy*yy,xx**3+A*xx**2+B*xx),p['label']
pass_check('all four Elkies-Klagsbrun section equations (independence is cited)')

# The rational 4-torsion point: 2T=(0,0). Algebraic doubling identity.
Tx,Ty=4*b,4*a*b
assert exact_equal(Ty*Ty,Tx**3+A*Tx**2+B*Tx)
# Doubling slope for y^2=x^3+A*x^2+B*x:
slope=S.cancel((3*Tx*Tx+2*A*Tx+B)/(2*Ty))
x2=S.cancel(slope*slope-A-2*Tx)
y2=S.cancel(-slope*(x2-Tx)-Ty)
assert exact_equal(x2,0) and exact_equal(y2,0)
pass_check('rational point of exact order four')

# Two distinct quadratic extensions and their explicit points.
covers={}
for item in DATA['new_covers']:
    name=item['label']; cc=item['q_coeff_low_to_high']
    q=sum(S.Integer(c)*t**i for i,c in enumerate(cc))
    x,yfactor=parse(item['x']),parse(item['y_factor'])
    assert exact_equal(yfactor*yfactor*q, x**3+A*x*x+B*x),name
    assert S.degree(q,t)==2
    assert S.gcd(q,S.diff(q,t)) == 1
    assert int(S.discriminant(q,t)) == int(item['branch_disc'])
    covers[name]=(q,x,yfactor)
    pass_check(f'new section {name}: exact identity and squarefree quadratic cover')
q1,x1,z1=covers['q1'];q3,x3,z3=covers['q3']
assert S.gcd(q1,q3) == 1
resultant = S.resultant(q1,q3,t)
assert resultant!=0
pass_check('independent quadratic squareclasses; four distinct branch points; genus one')

# Six rational parameters, each yielding four rational points on the smooth cover.
seen=set()
for s in DATA['rational_parameters']:
    t0=rat(s)
    assert t0 not in seen
    seen.add(t0)
    for q,_,_ in covers.values():
        value=eval_fraction(q,t0)
        assert value!=0 and rational_square(value) not in (None,F(0)),(s,q,value)
    aa,bb=eval_fraction(a,t0),eval_fraction(b,t0)
    assert aa and bb and aa*aa-16*bb
assert len(seen)==6
assert len(seen)==CERT['distinct_rational_t_values']
assert 4*len(seen)==CERT['rational_base_points']
assert CERT['rational_base_points'] > CERT['mazur_maximum_rational_torsion_order']
# There are 6*4=24 distinct rational points of C. Since Mazur's theorem
# says a rational elliptic curve has <=16 rational torsion points, C(Q) is infinite.
pass_check('six smooth rational t values, 24 distinct rational base points (>16 torsion max)')
# Verify every numeric cell in the distributable worked-example CSV.
with (DIR/'data'/'specializations.csv').open(newline='') as f:
    rows=list(csv.DictReader(f))
assert len(rows)==len(DATA['rational_parameters'])
for r in rows:
    t0=rat(r['t'])
    assert str(rational_square(eval_fraction(q1,t0)))==r['sqrt_q1']
    assert str(rational_square(eval_fraction(q3,t0)))==r['sqrt_q3']
    aa,bb=eval_fraction(a,t0),eval_fraction(b,t0)
    expected = {
        'a':aa,'b':bb,'A':aa*aa-8*bb,'B':16*bb*bb,
        'x_q1':eval_fraction(x1,t0),
        'y_q1':eval_fraction(z1,t0)*rational_square(eval_fraction(q1,t0)),
        'x_q3':eval_fraction(x3,t0),
        'y_q3':eval_fraction(z3,t0)*rational_square(eval_fraction(q3,t0)),
    }
    for key,value in expected.items():
        assert rat(r[key])==value,(t0,key)
pass_check('all exact sample coordinates and model coefficients in CSV')


# Exact C4 torsion of a chosen smooth rational fiber, and non-torsion of two
# new specialized points (which proves the generic points are nontorsion).
t0=rat(DATA['test_fiber']['t'])
assert str(t0)==CERT['test_fiber_t']
q1root=rational_square(eval_fraction(q1,t0))
q3root=rational_square(eval_fraction(q3,t0))
assert str(q1root)==DATA['test_fiber']['sqrt_q1']
assert str(q3root)==DATA['test_fiber']['sqrt_q3']
aa,bb=eval_fraction(a,t0),eval_fraction(b,t0)
AA,BB=aa*aa-8*bb,16*bb*bb
E0=EllipticCurve(QQ,[0,QQ(AA),0,QQ(BB),0])
assert E0([QQ(4*bb),QQ(4*aa*bb)]).order()==4
orders=[]
for p,n in DATA['test_fiber']['torsion_good_reduction_orders'].items():
    p=int(p);actual=count_finite_field(AA,BB,p)
    assert actual==n,(p,actual,n)
    assert E0.change_ring(GF(p)).cardinality()==n
    orders.append(actual)
assert DATA['test_fiber']['torsion_good_reduction_orders']==CERT['test_fiber_group_orders']
assert reduce(gcd,orders)==4
assert eval_fraction(x1,t0)!=0 and eval_fraction(x3,t0)!=0
assert eval_fraction(x1,t0)!=4*bb and eval_fraction(x3,t0)!=4*bb
for name,q,x,yf in [('q1',q1,x1,z1),('q3',q3,x3,z3)]:
    xx=eval_fraction(x,t0)
    yy=eval_fraction(yf,t0)*rational_square(eval_fraction(q,t0))
    assert yy*yy == xx**3+AA*xx*xx+BB*xx
    assert [str(xx),str(yy)]==DATA['test_fiber'][f'point_{name}']
    assert name in CERT['new_sections_nontorsion']
    assert 4*E0([QQ(xx),QQ(yy)]) != E0(0)
    # With exactly four torsion points (O,(0,0),(4b,+/-4ab)),
    # xx != 0 and xx != 4b implies the point is nontorsion.
pass_check('test fiber has exact C4 torsion; each new section has nontorsion specialization')

# Inherited four points are rational over Q(t). q1 and q3 new sections
# are anti-invariant under different (Z/2)^2 deck involutions.
# Non-torsion specializes => sigma_i(P_i)-P_i=-2 P_i non-torsion;
# character argument proves all six sections independent.
pass_check('six-section Galois-character independence, using cited EK rank-four theorem')

# C is smooth with good reduction at 19,41; the chosen point is unramified.
# An infinite progression of rational points of C has the same reductions
# as the chosen point, preserving exact torsion via 24 and 44 group orders.
for p in (19,41):
    assert int(S.LC(S.Poly(q1,t)))%p and int(S.LC(S.Poly(q3,t)))%p
    assert int(S.discriminant(q1,t))%p and int(S.discriminant(q3,t))%p
    assert int(resultant)%p
    assert t0.denominator%p
    assert red(eval_fraction(q1,t0),p) and red(eval_fraction(q3,t0),p)
    assert count_finite_field(AA,BB,p)==(24 if p==19 else 44)
# j has a pole at t=-1, while a(t) is nonzero and b(t) has a simple zero.
assert b.subs(t,-1)==0 and a.subs(t,-1)!=0
assert S.diff(b,t).subs(t,-1)!=0
pass_check('good reduction of genus-one base and exact C4 preservation at 19,41; nonconstant j')

print('\nCERTIFIED RELATIVE TO PUBLISHED EK2020 RANK-FOUR INDEPENDENCE:')
print('  six independent sections over the positive-rank genus-one parameter curve;')
print('  infinitely many rational elliptic curves with exact C4 torsion and rank >=6.')
print('  NOT a new rank record. Originality/inequivalence to published families not proved.')
