# Proof notes: a C4 family of rank at least 6

I use Elkies's discriminant-163 K3 surface and four sections as the starting
point. Two quadratic covers supply one more section each. Their common
genus-one base has infinitely many rational points, and the six sections are
independent. That gives infinitely many curves over **Q** with torsion exactly
`Z/4Z` and rank **at least six**.

This is a lower bound. The four inherited sections rely on the published
Elkies–Klagsbrun independence result. `verify.py` replays the arithmetic for
the two new sections. I do not claim exact generic rank or a rank record.

## Theorem

Let

\[
 a(t)=(8t-1)(32t+7),\qquad
 b(t)=8(t+1)(15t-8)(31t-7)
\]

and consider the elliptic surface

\[
 E_t:\quad y^2=x^3+(a(t)^2-8b(t))x^2+16b(t)^2x.
\]

Put

\[
\begin{aligned}
q_A(t)&=22485609t^2+2061276t-291164,\\
q_B(t)&=20497165225t^2+22061649540t+4379105124,
\end{aligned}
\]

and let \(C\) be the smooth projective curve whose function field is

\[
 K=\mathbb Q(t)(\sqrt{q_A(t)},\sqrt{q_B(t)}).
\]

**Then:**

1. \(C\) has genus one and infinitely many rational points;
2. \(E(K)\) contains **six independent sections** and has rational torsion **exactly** \(\mathbb Z/4\mathbb Z\);
3. infinitely many distinct smooth specializations \(E_{t_0'}/\mathbb Q\) have torsion exactly \(\mathbb Z/4\mathbb Z\) and rank at least six.

These are lower-bound statements; no claim is made that the function-field rank is exactly six.

## 1. The four inherited sections

The Tate model of the parent fibration is

\[
Y^2+aXY+abY=X^3+bX^2.
\]

The change of coordinates

\[
x=4(X+b),\qquad y=4\bigl(2Y+a(X+b)\bigr)
\]

gives the short model stated above. In the Tate model, \((0,0)\) has order four. In the short model its image is

\[
T=(4b,4ab),\qquad 2T=(0,0).
\]

Elkies–Klagsbrun [EK2020, §11] give four independent sections with the following Tate-model \(X\)-coordinates:

\[
\begin{aligned}
X_1&=-\frac{15}{4}(t+1)(31t-7)(32t+7),\\
X_2&=(8t-1)(15t-8)(31t-7)(32t+7),\\
X_3&=-(t+1)(8t-1)(15t-8)(32t+7),\\
X_4&=-4(t+1)(2t+5)(15t-8)(32t+7).
\end{aligned}
\]

For reproducibility, set \(Z_i=2Y_i+a(X_i+b)\). One choice of the four square roots is

\[
\begin{aligned}
Z_1&=\frac{19}{4}(t+1)(31t-7)(32t+7)(127t-44),\\
Z_2&=(8t-1)(15t-8)(16t+1)(31t-7)(32t+7)(46t-15),\\
Z_3&=(t+1)(8t-1)(14t-9)(15t-8)(16t-7)(32t+7),\\
Z_4&=4(t+1)(8t+7)(15t-8)(32t+7)(56t^2+8t-57).
\end{aligned}
\]

The exact identities

\[
Z_i^2=(X_i+b)\{4X_i^2+a^2(X_i+b)\}
\]

are checked in `verify.py`, as are the short-Weierstrass equations for \((4(X_i+b),4Z_i)\). **The independence of these four inherited sections is the published Elkies–Klagsbrun result**; it is used as a prior theorem, not silently assumed as a consequence of point identity checks.

## 2. The 2-neighbor and two new quadratic sections

Set \(g(t)=(15t-8)(31t-7)\), so \(b=8(t+1)g\). Introduce

\[
u=\frac{X+b}{g},\qquad v=\frac{2Y+a(X+b)}{g}.
\]

Their defining equation simplifies **identically** to the quartic genus-one fibration

\[
\tag{1}
v^2=\mathcal F(u,t)
:=u^2a(t)^2+4u g(t)\bigl(u-8(t+1)\bigr)^2.
\]

In terms of the original short Weierstrass model, any rational solution of (1) gives

\[
\tag{2}
(x,y)=(4u g(t),\;4g(t)v).
\]

Three explicit rational points on the quartic \(\mathcal F(u,t)\) are

\[
\begin{array}{lll}
T_0=8/15, & V_0=u\,a(8/15), & \\
T_1=7/31, & V_1=u\,a(7/31), & \\
T_2=(32u-361)/(60u+361), &
V_2=19u(4u-25)(1424u-61731)/(60u+361)^2. &
\end{array}
\]

For signs \(\epsilon=(\epsilon_0,\epsilon_1,\epsilon_2)\), let \(L_\epsilon(u,t)\) denote the unique degree-at-most-two Lagrange interpolation polynomial in \(t\) taking the three values \(\epsilon_i V_i\) at \(T_i\):

\[
\tag{3}
L_\epsilon(u,t)=\sum_{i=0}^2\epsilon_iV_i\prod_{\substack{0\le j\le2\\j\ne i}}
\frac{t-T_j}{T_i-T_j}.
\]

Since \(L_\epsilon(u,t)^2-\mathcal F(u,t)\) vanishes at the three interpolated points, its fourth intersection with (1) gives another rational point. Two sign selections produce the degree-two maps

\[
\tag{4}
t_A(u)=\frac{2268u^2-33518u+135424}{10044u^2-51735u-135424},
\qquad\epsilon_A=(+,+,-),
\]

and

\[
\tag{5}
t_B(u)=\frac{17500u^2-1395458u+5234944}{77500u^2+2403465u-5234944},
\qquad\epsilon_B=(+,-,+).
\]

In both cases, exact polynomial arithmetic gives

\[
\tag{6}
\mathcal F(u,t_i(u))=L_{\epsilon_i}(u,t_i(u))^2.
\]

Consequently, **explicit sections on the two degree-two parameter covers** are

\[
\tag{7}
S_i(u)=\bigl(4u g(t_i(u)),\;4g(t_i(u))L_{\epsilon_i}(u,t_i(u))\bigr),
\quad i\in\{A,B\}.
\]

This is a complete exact rational-function specification of their coordinates; no unspecified point search or numerical root selection is needed.

Write \(t_i(u)=N_i(u)/D_i(u)\). Directly taking the discriminant in \(u\) of \(N_i(u)-tD_i(u)\) yields

\[
\tag{8}
\operatorname{disc}_u(N_A-tD_A)=19^2 q_A(t),\qquad
\operatorname{disc}_u(N_B-tD_B)=19^2 q_B(t).
\]

Thus \(\mathbb Q(u_i)\cong\mathbb Q(t)(\sqrt{q_i(t)})\). The verifier checks (4)–(8) exactly.

## 3. Independence of the two new directions

Both \(q_A,q_B\) are squarefree quadratics with no common root. Their square classes are therefore independent in \(\mathbb Q(t)^*/\mathbb Q(t)^{*2}\); the compositum \(K\) has Galois group \((\mathbb Z/2\mathbb Z)^2\).

Use the common rational parameter

\[
\tag{9}
t_0=-\frac{38323}{227116}.
\]

The two branch conditions become squares:

\[
\sqrt{q_A(t_0)}=\frac{7996847}{227116},\qquad
\sqrt{q_B(t_0)}=\frac{7997834207}{227116}.
\]

The two solutions of \(t_A(u)=t_0\) are

\[
\frac{25344}{4831},\quad\frac{43861}{8100};
\]

those of \(t_B(u)=t_0\) are

\[
\frac{25344}{4831},\quad\frac{38996243}{1437500}.
\]

Let \(P_i\) and \(P_i^\sigma\) denote the two corresponding specialized points from (7). They lie on the same smooth rational elliptic curve \(E_{t_0}\). Exact group operations in `verify.py` give

\[
\tag{10}
4(P_A-P_A^\sigma)\ne O,\qquad
4(P_B-P_B^\sigma)\ne O.
\]

At the good primes 13 and 19,

\[
\#E_{t_0}(\mathbb F_{13})=20,\qquad
\#E_{t_0}(\mathbb F_{19})=16.
\]

Hence rational torsion on this fiber has order dividing four. The point \(T\) already has order four, so torsion is exactly C4. Equation (10) then proves that the two anti-invariant differences are **nontorsion**. A torsion section would specialize to a torsion point, so the generic anti-invariants are also nontorsion.

Let \(\sigma_A\) act by negating \(\sqrt{q_A}\) while fixing \(\sqrt{q_B}\), and let \(\sigma_B\) act conversely. They fix the four inherited sections; \(\sigma_A\) fixes \(S_B\) and \(\sigma_B\) fixes \(S_A\). If

\[
\sum_{i=1}^4 n_iP_i+m_AS_A+m_BS_B=O,
\]

then applying \(\sigma_A-1\) shows \(m_A=0\) using the first nontorsion difference. Applying \(\sigma_B-1\) gives \(m_B=0\). The remaining relation is trivial because the original four sections are independent. Hence

\[
\boxed{\operatorname{rank}E(K)\ge6.}
\]

## 4. Genus one and a rational point of infinite order

The four roots of \(q_Aq_B\) are distinct. Each is a branch point of inertia two in the degree-four Galois cover \(C\to\mathbb P^1_t\), contributing two to the total ramification. Riemann–Hurwitz gives

\[
2g(C)-2=4(-2)+4(2)=0,
\qquad \boxed{g(C)=1}.
\]

Here is an explicit model proving that \(C(\mathbb Q)\) is infinite. Parametrize the first conic as

\[
\tag{11}
t=\frac{N(U)}{D(U)},\qquad \sqrt{q_A(t)}=\frac{W(U)}{D(U)},
\]

where

\[
\begin{aligned}
N(U)&=U^2+67036U+1228566528,\\
D(U)&=-U^2+103470U+5440794624,\\
W(U)&=4487U^2+351019008U+6252877099008.
\end{aligned}
\]

The identity \(q_A(N/D)D^2=W^2\) holds over \(\mathbb Q[U]\). The second condition becomes

\[
\tag{12}
w^2=F(U):=D(U)^2q_B(N(U)/D(U))
=a_4U^4+b_3U^3+c_2U^2+d_1U+e^2,
\]

with the **exact** coefficients, in descending order,

\[
\begin{aligned}
a_4&=2814620809,\\
b_3&=2645678061026000,\\
c_2&=387659239878453786688,\\
d_1&=19157729911799232946176000,\\
e&=555011422875648.
\end{aligned}
\]

(The constant coefficient is \(e^2=308037679522451368069671419904\).)

The genus-one curve (12) is birational to the elliptic curve

\[
\tag{13}
J:\quad Y^2=X^3+c_2X^2+(b_3d_1-4a_4e^2)X
+(e^2b_3^2+a_4d_1^2-4a_4c_2e^2)
\]

by the explicit map

\[
\tag{14}
X=\frac{2e(w+e)+d_1U}{U^2},\qquad
Y=\frac{(X^2-4a_4e^2)U-(Xd_1+2e^2b_3)}{2e}.
\]

An inverse on a dense open set is

\[
U=\frac{2eY+Xd_1+2e^2b_3}{X^2-4a_4e^2},\qquad
w=\frac{XU^2-d_1U}{2e}-e.
\]

Both the curve identity and the inverse are checked using exact rational arithmetic.

The quartic has the rational point

\[
\tag{15}
(U,w)=\left(-\frac{1083392}{25},\frac{13302924837367808}{625}\right),
\]

whose image on (13) is

\[
\tag{16}
R=\bigl(-101444794609024256688,\;
16067387279706471686378520000\bigr).
\]

The auxiliary Jacobian has good-reduction point counts

\[
\#J(\mathbb F_{37})=30,\quad
\#J(\mathbb F_{41})=48,\quad
\#J(\mathbb F_{43})=56.
\]

Rational torsion on \(J\) therefore has order dividing \(\gcd(30,48,56)=2\). Since \(R\) has nonzero \(Y\)-coordinate, it is not a point of order two; hence \(R\) is nontorsion. Thus **\(C(\mathbb Q)\) is infinite**.

## 5. Exact C4 torsion on infinitely many rational fibers

A single fiber with torsion C4 is not by itself enough to establish exact torsion on infinitely many fibers; this step uses a congruence argument on the auxiliary genus-one curve.

Let \(Q_0\in C(\mathbb Q)\) have the values in (9), with the indicated positive square roots. On the quartic model it has

\[
U_0=-\frac{95385600}{1907},\qquad
w_0=D(U_0)\frac{7997834207}{227116}.
\]

The corresponding point on \(J\) is defined and the rational maps to and from \(J\) are regular at its reductions at \(p=43,47,53\). The verifier checks all relevant denominators and the nonzero inverse-map denominator at these primes.

At these three primes both \(J\) and the rational fiber \(E_{t_0}\) have good reduction, with

| \(p\) | \(\#J(\mathbb F_p)\) | \(\#E_{t_0}(\mathbb F_p)\) |
|---:|---:|---:|
| 43 | 56 | 36 |
| 47 | 52 | 56 |
| 53 | 56 | 48 |

Put

\[
M=\operatorname{lcm}(56,52,56)=728.
\]

Identify \(C\) with \(J\) using \(Q_0\) as origin, and let \(R\in J(\mathbb Q)\) be the nontorsion point (16). For every integer \(n\), the point

\[
Q_n=Q_0+nMR
\]

has the same reduction as \(Q_0\) at each of the three good primes. Since the map \(t:C\to\mathbb P^1\) is regular at these reductions,

\[
t(Q_n)\equiv t_0\pmod{43,47,53}.
\]

For all \(n\) for which the fiber is smooth, its reductions at these three primes are consequently identical to those of \(E_{t_0}\). Its rational torsion order divides

\[
\gcd(36,56,48)=4.
\]

Since each smooth fiber retains its explicit rational point of order four, its torsion is **exactly C4**. The \(Q_n\) are distinct because \(R\) is nontorsion; because \(t\) is a nonconstant finite map, infinitely many distinct rational values \(t(Q_n)\) occur.

The family is non-isotrivial: its \(j\)-invariant has a pole at \(t=-1\), where \(b(-1)=0\) and \(a(-1)\ne0\). The specialization theorem for elliptic surfaces preserves the six independent sections outside a finite exceptional set among the rational points of \(C\) of increasing height. The infinite sequence \(Q_n\) therefore contains infinitely many fibers having **rank at least six** and **torsion exactly C4**.

This proves the theorem.

## 6. Verification and reproducibility

Run `sage -python verify.py` with SageMath. The verifier reads the named JSON
files in `data/`, checks `rank6-family-certificate.json`, reconstructs all
rational-function sections, and checks:

1. Four inherited point identities (independence taken from [EK2020]);
2. the exact 2-neighbor quartic and three initial sections;
3. both interpolation maps, exact square identities and quadratic discriminants;
4. distinct squarefree quadratic branch loci;
5. common-fiber square roots, good reduction, the order-four point, and the two nontorsion anti-invariant differences;
6. conic parametrization, square quartic and exact quartic-to-Jacobian map;
7. the rational infinite-order Jacobian witness and good-prime group orders;
8. congruence-prime regularity, the torsion-preserving progression \(M=728\), and nonconstant \(j\).

All calculations use integer and rational arithmetic. The program does **not** accept a heuristic Mestre–Nagao score, a numerical height estimate, or an unverified rank claim as proof.

## Source

The parent surface and four inherited sections are Elkies's construction,
printed in [EK2020]. The independence of those four sections is used here as
a published result. The two new covers and their checks are given above.
This proof establishes rank at least six, not an exact-rank or priority claim.

### Reference

- [EK2020] N. D. Elkies and Z. Klagsbrun, *New rank records for elliptic curves having rational torsion*, **Observations on Number Theory and Related Fields**, 2020. <https://msp.org/obs/2020/4-1/obs-v4-n1-p15-s.pdf>
