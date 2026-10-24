# Proof notes: nineteen sections from two quadratic covers

## What is proved

We have an elliptic curve over the function field of a genus-one curve whose
Mordell–Weil group contains nineteen independent rational sections. The
parameter curve has a rational point of infinite order. Consequently there
are infinitely many elliptic curves over **Q** with rank at least nineteen.
They can be chosen to have trivial rational torsion.

This proves a lower bound. It does not determine the exact generic rank or
the exact rank of any particular specialization.

The complete Weierstrass equations, all section coordinates, and the height
matrices are in the four JSON files under `data/`. The short Sage
program `verify.py` reads only those files and rechecks the identities and
height calculations; no Rank Hunter database or plugin is needed.

## The surface and two quadratic covers

Write the parent elliptic surface as

```
E_t: y^2 = x^3 + A(t)x + B(t).
```

The exact coefficients `A(t), B(t)` and seventeen sections `P1,...,P17`
are in `data/parent-rank17.json` (`jacobian_model` and
`neighbor_sections`). This model arose in our work from a 2-neighbor
construction seeded by ICARM #3900. The coefficients are large; the JSON
lists every coefficient and every rational-function numerator and
denominator without rounding or abbreviation.

The two extra sections arise over the following quadratic extensions:

```
q1(t) = 30015061720809 t^2 - 20692173881368 t + 3538696407184,
q2(t) = 46784549960425 t^2 - 29557331565600 t + 4702049024256,

C1: r1^2 = q1(t),       C2: r2^2 = q2(t).
```

Both polynomials are squarefree and they have no common root. Thus their
square classes are independent in `Q(t)*/Q(t)*2`. Their compositum has
Galois group `(Z/2Z)^2`. Its smooth parameter curve `C` is given by the
two equations `r1^2=q1(t), r2^2=q2(t)`. The four distinct branch points
give total ramification eight in the degree-four map `C -> P1_t`;
Riemann–Hurwitz gives genus one.

At the rational parameter

```
t0 = 15122/33609,
r1 = 6185869062/11203,
r2 = 31426768294/33609,
```

both cover equations hold. This is a rational point on `C`.

## A point of infinite order on the parameter curve

For an explicit genus-one model, use the first conic to write

```
t = N(u)/D(u),       r1 = W(u)/D(u),

N(u) = 14974938550/289 + (550744148/17)u + 4995486u^2,
D(u) = 1957773675/17 + 74456844u + 11774081u^2,
W(u) = 18377134456116150/289
       + (591506630529100/17)u + 4746709944790u^2.
```

The identity `q1(N/D) = (W/D)^2` holds exactly. The second cover becomes

```
w^2 = F(u),       F(u) = D(u)^2 q2(N(u)/D(u)).
```

`F` is a squarefree quartic with square constant term. All five exact
coefficients are in `data/pair.json`. Write
`F(u)=a u^4+b u^3+c u^2+d u+e^2`, taking the positive rational square
root `e` of the constant term. Its Jacobian model used here is

```
E0: Y^2 = X^3 + c X^2 + (bd-4ae^2)X
                     + e^2 b^2 + a d^2 - 4ac e^2.
```

The exact coefficients and point `P=(X,Y)` are recorded in `data/pair.json`
as `auxiliary_a_invariants` and `auxiliary_point`. The birational map is

```
X = [2e(w+e)+du]/u^2,
Y = [(X^2-4ae^2)u-(Xd+2e^2b)]/(2e).
```

The verifier checks this identity symbolically. Under the inverse map,
the recorded point `P` has `u=0`, hence `t=t0`.

At good primes 31 and 37, the group orders of `E0` are respectively 30
and 32. Rational torsion therefore has order dividing two. Direct addition
gives `2P != O`, so `P` has infinite order. In particular `C(Q)` is infinite.

## Independence of the nineteen sections

The parent model has squarefree discriminant of degree 24: its singular
fibers are all type I1. The exact Shioda height matrix of the seventeen
displayed parent sections is positive definite with determinant 1152.
In these minimal models with only I1 fibers, the verifier obtains the
canonical height of a section from the pole degrees of its exact
`x`-coordinate:

```
h(P) = max(deg numerator(x(P)), deg denominator(x(P)) + 2 chi),
<P,Q> = [h(P+Q)-h(P)-h(Q)]/2,
```

where `chi=2` for the parent and `chi=4` for either degree-two pullback.
It checks the discriminant and degree hypotheses before using this formula.

Each quadratic cover pulls these seventeen sections back and adds one
explicit section, called `S1` or `S2`. The full coordinate expressions are
in `data/cover-4339.json` and `data/cover-36773.json`; in each file the first
seventeen entries of `neighbor_sections` are the inherited sections, and the
last entry is the new one. Both pullback models have squarefree discriminant
of degree 48, so again every singular fiber is I1 and no reducible-fiber
correction is omitted from the height pairing.

For each cover, `verify.py` recomputes the complete eighteen-by-eighteen
height matrix from the section coordinates and checks it against the matrix
stored with the model. Both matrices are positive definite and have
determinant **452984832**. The upper-left seventeen-by-seventeen block is
twice the parent height matrix, as expected for a degree-two base change.

Let `sigma_i` be the deck involution of the `i`th quadratic cover. Direct
substitution in the coordinates verifies that it fixes all seventeen
inherited sections, while

```
height(S1 - sigma_1(S1)) = 12,
height(S2 - sigma_2(S2)) = 12.
```

These differences are nontorsion. Over the biquadratic function field,
extend `sigma_1` to fix `sqrt(q2)` and `sigma_2` to fix `sqrt(q1)`.
If an integer relation among `P1,...,P17,S1,S2` existed, applying
`sigma_1-1` would leave only a multiple of the first nontorsion difference;
its coefficient must be zero. Applying `sigma_2-1` does the same for the
second. The remaining relation is among the seventeen parent sections and
is zero because their height matrix is positive definite. Hence all nineteen
sections are independent over `Q(C)`.

## Infinitely many trivial-torsion specializations

The auxiliary point `P` maps to `t0=15122/33609`. The fiber `E_t0` has
good reduction at 31, 37, and 59, with group orders

```
#E_t0(F_31) = 42,     #E_t0(F_37) = 46,     #E_t0(F_59) = 71.
```

Their greatest common divisor is one, so `E_t0(Q)` has trivial torsion.
At the same three primes, `E0` has good reduction and group orders
`30, 32, 72`. Their least common multiple is 1440. For every integer
`n = 1 (mod 1440)`, the reduction of `nP` equals that of `P` at all three
primes. The map `E0 -> P1_t` is regular at these reductions, so the fiber
at `t(nP)` has the same three reductions as `E_t0`. Its rational torsion is
therefore trivial as well.

There are infinitely many such `nP` because `P` has infinite order.
The family is nonconstant, and the specialization theorem retains the
nineteen independent sections for all but finitely many of these points.
Thus infinitely many elliptic curves over `Q` have trivial torsion and
rank at least nineteen.

## How to check the packet

From this directory, with SageMath installed:

```
sage -python verify.py
```

The program checks the parent and pullback Weierstrass equations, all 53
section identities, the three exact height matrices, both cover maps, the
quartic-to-Jacobian identity, the infinite-order point, both deck actions,
and the finite-field orders used for the torsion argument. It takes about
two seconds on our machine. A successful run ends with:

```
CERTIFIED: infinitely many trivial-torsion curves have rank at least 19 (by specialization)
```

The four `data/*.json` files contain the exact arithmetic inputs; `verify.py`
does not query an external service or database. `SHA256SUMS` records their
checksums.
