# Proof notes: an S3 genus-one C4 family of rank at least 6

I pull the Elkies–Klagsbrun C4 surface back along an explicit cubic. Its
splitting field has a genus-one base with infinitely many rational points.
The three conjugate points from the cubic give two new independent sections
alongside the four published parent sections. The conclusion is a rank lower
bound, not an exact-rank or priority claim.

## Theorem

Set

\[
 a(t)=(8t-1)(32t+7),\quad b(t)=8(t+1)(15t-8)(31t-7),
\]
\[
 E_t:\quad y^2=x^3+(a(t)^2-8b(t))x^2+16b(t)^2x.
\]

Let \(H(U,t)=N(U)-tD(U)\), where

\[
\begin{aligned}
N(U)={}&14907321U^3-392116761U^2+3433897552U-9026551296,\\
D(U)={}&24(31965219U^2-66155603U-1665613632).
\end{aligned}
\]

Let \(C\) be the smooth projective curve with function field the splitting field of \(H(U,t)\) over \(\mathbb Q(t)\). Then \(C\) is a genus-one curve with infinitely many rational points; the extension has Galois group \(S_3\), and \(E(\mathbb Q(C))\) has rank at least six and torsion exactly \(\mathbb Z/4\mathbb Z\). Consequently, infinitely many pairwise distinct elliptic curves over \(\mathbb Q\) have rank at least six and torsion exactly C4. The four inherited independent sections use [EK2020, §11].

## 2. The four inherited sections and C4 torsion

Set \(g(t)=(15t-8)(31t-7)\). The parent surface is the discriminant-163 C4 K3 used in Elkies–Klagsbrun [EK2020, §11]. Its Tate form is

\[
Y^2+aXY+abY=X^3+bX^2.
\]

The coordinate change \(x=4(X+b)\), \(y=4(2Y+a(X+b))\) gives the above Weierstrass model and the order-four torsion point \(T=(4b,4ab)\), with \(2T=(0,0)\).

The four published independent parent sections have Tate x-coordinates

\[
\begin{aligned}
X_1&=-\tfrac{15}{4}(t+1)(31t-7)(32t+7),\\
X_2&=(8t-1)(15t-8)(31t-7)(32t+7),\\
X_3&=-(t+1)(8t-1)(15t-8)(32t+7),\\
X_4&=-4(t+1)(2t+5)(15t-8)(32t+7).
\end{aligned}
\]

Define \(Z_i=2Y_i+a(X_i+b)\). For exact reproducibility choose

\[
\begin{aligned}
Z_1&=\tfrac{19}{4}(t+1)(31t-7)(32t+7)(127t-44),\\
Z_2&=(8t-1)(15t-8)(16t+1)(31t-7)(32t+7)(46t-15),\\
Z_3&=(t+1)(8t-1)(14t-9)(15t-8)(16t-7)(32t+7),\\
Z_4&=4(t+1)(8t+7)(15t-8)(32t+7)(56t^2+8t-57).
\end{aligned}
\]

The four sections on \(E_t\) are \((x_i,y_i)=(4(X_i+b),4Z_i)\). `verify.py` checks all identities exactly. **Their rank-four independence uses the published EK2020 theorem** and is not inferred merely from the identities.

## 3. A cubic multisection of the 2-neighbor fibration

Introduce the neighbor coordinates

\[
 U=\frac{X+b}{g},\qquad V=\frac{2Y+a(X+b)}{g}.
\]

Then the neighbor equation is

\[
 V^2=\mathcal F(U,t)=U^2a(t)^2+4U g(t)(U-8(t+1))^2.
\]

Write

\[
 K(U)=31965219U^2-66155603U-1665613632,
\]
\[
\begin{aligned}
J_5(U)={}&888912877588164U^5-10646406622659951U^4\\
&-960018782069421396U^3+12164159827914309855U^2\\
&-9247249925793225856U-202923579084549844992.
\end{aligned}
\]

The rational functions

\[
 t(U)=\frac{N(U)}{24K(U)},\qquad
 V(U)=\frac{U(U-9)J_5(U)}{9K(U)^2}
\]

satisfy \(\mathcal F(U,t(U))=V(U)^2\) identically. For any root \(U_i\) of \(H(U,t)=0\), we therefore obtain a point on the original elliptic curve:

\[
 \boxed{P_i=(4U_i g(t),\;4g(t)V(U_i)).}
\]

Thus each of the three roots supplies a section after passing to the splitting field.

## 4. Galois closure and genus one

The exact cubic discriminant is

\[
\begin{split}
\operatorname{disc}_U H(U,t)=43796088116928(&1682330950211090408678592t^4\\
&+2032853295795148379391696t^3\\
&+53691289761921871193523t^2\\
&+1391585322280210990012t\\
&-132998306248524640756).
\end{split}
\]

The quartic factor has four simple roots; consequently the irreducible cubic has non-square discriminant and Galois group \(S_3\) over \(\mathbb Q(t)\). The sixfold Galois closure has four transposition branch values, so Riemann–Hurwitz gives \(2g-2=-12+4\cdot3=0\) and \(g=1\).

A concrete model of this Galois closure is

\[
 \boxed{w^2=G(U)=\sum_{i=0}^4 c_iU^i},
\]
where

```
c0 =  1136913313078118744985600
c1 = -596318731133167069975680
c2 =  101870134810871311417329
c3 = -7358395974814467407682
c4 =  211744205635877094609
```

The quartic is squarefree and has rational point \((0,e)\) where \(e=1066261371840\), \(e^2=c_0\).

For a fixed root \(U\), factor \(H(Z,t(U))=(Z-U)(A_3 Z^2+B_2 Z+C_2)\). Here

\[
 A_3=14907321,\qquad B_2=-392116761-767165256t(U)+14907321U.
\]

The quadratic discriminant satisfies the exact identity

\[
 B_2^2-4A_3 C_2=\frac{477603^2 G(U)}{K(U)^2}.
\]

Hence the remaining two cubic roots are

\[
 U_{\pm}=\frac{-B_2\pm477603\,w/K(U)}{2A_3}.
\]

This identifies \(\mathbb Q(U,w)\) with the splitting field: all three roots are explicit rational functions on the quartic model.

## 5. Non-torsion rational point on the parameter curve

With \(c_i\) as above, the quartic has the elliptic Weierstrass model

\[
 J:\quad Y^2=X^3+c_2X^2+(c_3c_1-4c_4e^2)X
 +(e^2c_3^2+c_4c_1^2-4c_4c_2e^2).
\]

An explicit birational transformation (verified as a polynomial identity modulo \(w^2-G(U)\)) is

\[
 X=\frac{2e(w+e)+c_1U}{U^2},\qquad
 Y=\frac{(X^2-4c_4e^2)U-(Xc_1+2e^2c_3)}{2e}.
\]

Its rational inverse on a dense open is

\[
 U=\frac{2eY+Xc_1+2e^2c_3}{X^2-4c_4e^2},\qquad
 w=\frac{XU^2-c_1U}{2e}-e.
\]

The quartic rational point

\[
 (U,w)=\left(\frac{7288}{837},-\frac{4303028078006840}{25947}\right)
\]

with the indicated negative sign maps to

\[
 R=\left(-\frac{35818210150996569947911185120}{829921},
 -\frac{414949679159040119391810475552836641085600}{756058031}\right).
\]

At good primes 31 and 37 the auxiliary Jacobian has \(\#J(\mathbb F_{31})=27\), \(\#J(\mathbb F_{37})=48\). Thus rational torsion has order dividing three. But the reduction of \(3R\) modulo 37 is \((16,14)\ne O\). Hence \(R\) is non-torsion and \(C(\mathbb Q)\) is infinite.

## 6. Smooth fiber and two independent new directions

The completely split fiber at \(t=7/31\) is singular. To test the new point differences, take the rational point \(Q_0=2R\) on \(J\), map it back to \((U_0,w_0)\) using the inverse transformation, and define \(t_0=t(U_0)\). This fiber is smooth, and

\[
 t_0=\frac{130519437860157186821597294459066332383618071691490258658519095434629198880463674413145236626613}
 {4301276332085122997006195014178083644951481670132363892520027987669029420687377301897137198019584}.
\]

The exact three roots \(U_1,U_2,U_3\) and the exact three corresponding rational points \(P_i\) are recorded in `data/witness.json`; `verify.py` reconstructs each and checks its Weierstrass identity.

At this **smooth** rational fiber, exact finite-field computations give

| Good prime \(p\) | \(\#E_{t_0}(\mathbb F_p)\) |
|---:|---:|
| 43 | 56 |
| 59 | 72 |
| 73 | 76 |

Their gcd is 4. The fiber has the visible point \(T=(4b(t_0),4a(t_0)b(t_0))\) of order 4, hence its rational torsion is **exactly C4**.

For the point difference \(P_1-P_2\), the exact group law followed by reduction gives

\[
\boxed{4(P_1-P_2)\bmod43=(9,38)\ne O.}
\]

Since rational torsion at the smooth fiber has order dividing four, \(P_1-P_2\) is non-torsion. A torsion generic section would specialize to a torsion point, so the generic difference is non-torsion.

The Galois group \(S_3\) permutes \(P_1,P_2,P_3\). The map from its rational 3-dimensional permutation module to \(E(\mathbb Q(C))\otimes\mathbb Q\) therefore takes the standard 2-dimensional irreducible representation nontrivially (because \(P_1-P_2\) is non-torsion). By irreducibility, its image has dimension two. The four Elkies–Klagsbrun parent directions are Galois-invariant, so these two new directions are independent of them:

\[
\boxed{\operatorname{rank}E(\mathbb Q(C))\ge4+2=6.}
\]

## 7. Infinite specializations with exact C4 torsion

The auxiliary elliptic curve has good-reduction orders

| \(p\) | \(\#J(\mathbb F_p)\) | \(\#E_{t_0}(\mathbb F_p)\) |
|---:|---:|---:|
| 43 | 45 | 56 |
| 59 | 72 | 72 |
| 73 | 72 | 76 |

Set \(M=\operatorname{lcm}(45,72,72)=360\), and take

\[
 Q_n=Q_0+nMR=(2+360n)R\in J(\mathbb Q).
\]

Since \(R\) is non-torsion, the points \(Q_n\) are distinct. Each reduces to the same point as \(Q_0\) modulo 43, 59, and 73. `verify.py` checks the regularity and nonvanishing denominator conditions of the maps at these reductions. Thus the fibers at \(t(Q_n)\) have the same good reductions, so rational torsion has order dividing \(\gcd(56,72,76)=4\). The explicit order-four section persists, giving **exactly C4** on every good member of the progression.

The rational map \(t:C\to\mathbb P^1\) is finite nonconstant, so infinitely many distinct rational values occur. The parent's \(j\)-invariant is nonconstant (it has a pole at \(t=-1\)); hence infinitely many non-isomorphic curves occur. Silverman's specialization theorem preserves the six independent sections for all but finitely many points in this infinite progression. Therefore infinitely many rational elliptic curves have C4 torsion and rank at least six.

## Reproducibility and scope

Run `python verify.py` from this folder. It checks the identities and finite-field witnesses exactly. The four inherited sections are independent by [EK2020, §11]; checking that they lie on the curve alone would not establish their independence. The argument proves rank at least six over the genus-one function field and on infinitely many rational fibers. It does not establish exact generic rank or publication priority.

## References

- [EK2020] Noam D. Elkies and Zev Klagsbrun, *New rank records for elliptic curves having rational torsion*, 2020, Section 11, https://msp.org/obs/2020/4-1/obs-v4-n1-p15-s.pdf
- C. R. Hill, Rank Ledger, original C4 rank-6 quadratic-cover proof packet, https://github.com/crhillresearch/rank-ledger/tree/main/c4-rank-6-genus-one-family
