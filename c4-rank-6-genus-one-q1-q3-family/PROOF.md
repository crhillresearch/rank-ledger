# Proof notes: a C4 rank-six family from the q1 and q3 covers

I use Elkies's discriminant-163 K3 surface and its four known sections. Two
short quadratic covers add one section each. Their common genus-one base has
at least 24 rational points, which proves it has positive rank. The result is
an infinite family with exact C4 torsion and rank **at least six**.

This is a rank lower bound. The four inherited sections rely on the published
Elkies–Klagsbrun independence theorem. The arithmetic for the two new
sections is replayed by `verify.py`. I do not claim an exact generic rank or
a new rank record.

## Theorem

Define

\[
 a(t)=(8t-1)(32t+7),\qquad b(t)=8(t+1)(15t-8)(31t-7)
\]

and let

\[
 E_t:\quad y^2=x^3+(a(t)^2-8b(t))x^2+16b(t)^2 x.
\]

Let

\[
\begin{aligned}
 q_1(t)&=11076t^2+2620t+665,\\
 q_3(t)&=22276t^2+352t+8701,
\end{aligned}
\]

and define the smooth projective curve \(C/\mathbb Q\) by its function field

\[
 K=\mathbb Q(t)\left(\sqrt{q_1(t)},\sqrt{q_3(t)}\right).
\]

**The family \(E/K\) has at least six independent rational sections; the parameter curve \(C\) has genus one and infinitely many rational points. There are therefore infinitely many distinct smooth elliptic curves over \(\mathbb Q\), with exact rational torsion \(\mathbb Z/4\mathbb Z\) and rank at least six.**

The independence of the **four inherited sections** is cited from Elkies–Klagsbrun (2020); all additional identities and elementary certificate computations in this packet are independently checked by `verify.py`.

## 1. Four inherited sections and C4 torsion

The parent model is the discriminant-163 K3 fibration used by Elkies–Klagsbrun. In Tate coordinates it reads

\[
 Y^2+aXY+abY=X^3+bX^2.
\]

The coordinate transformation

\[
 x=4(X+b),\qquad y=4(2Y+a(X+b))
\]

gives the displayed short model. The rational point

\[
 T=(4b,4ab),\qquad 2T=(0,0),\qquad 4T=O
\]

has exact order four on the generic fiber.

To specify the four published nontorsion sections, put \(Z_i=2Y_i+a(X_i+b)\) and use

\[
\begin{array}{ll}
X_1=-\frac{15}{4}(t+1)(31t-7)(32t+7), &
Z_1=\frac{19}{4}(t+1)(31t-7)(32t+7)(127t-44),\\[2pt]
X_2=(8t-1)(15t-8)(31t-7)(32t+7), &
Z_2=(8t-1)(15t-8)(16t+1)(31t-7)(32t+7)(46t-15),\\[2pt]
X_3=-(t+1)(8t-1)(15t-8)(32t+7), &
Z_3=(t+1)(8t-1)(14t-9)(15t-8)(16t-7)(32t+7),\\[2pt]
X_4=-4(t+1)(2t+5)(15t-8)(32t+7), &
Z_4=4(t+1)(8t+7)(15t-8)(32t+7)(56t^2+8t-57).
\end{array}
\]

The four short-model sections are \((4(X_i+b),4Z_i)\). The verifier checks all four point identities exactly. Their **independence** is a cited published result, rather than a newly calculated Shioda matrix in this packet.

## 2. The two new quadratic sections

Over the first quadratic function field, define

\[
\boxed{
 P_1=\bigl(36(15t-8)(31t-7),\;12(15t-8)(31t-7)(8t-1)\sqrt{q_1(t)}\bigr).
}
\]

Over the second, define

\[
\boxed{
 P_3=\bigl(-196(t+1)(31t-7),\;28(t+1)(31t-7)(8t-1)\sqrt{q_3(t)}\bigr).
}
\]

Direct expansion proves

\[
\begin{aligned}
(y_1/\sqrt{q_1})^2 q_1 &=x_1^3+(a^2-8b)x_1^2+16b^2x_1,\\
(y_3/\sqrt{q_3})^2 q_3 &=x_3^3+(a^2-8b)x_3^2+16b^2x_3.
\end{aligned}
\]

This is a symbolic rational-function identity in \(\mathbb Q[t]\), not evidence inferred from numeric specializations.

The quadratic discriminants and resultant are

\[
\begin{aligned}
\operatorname{disc}(q_1)&=-22597760,\\
\operatorname{disc}(q_3)&=-775170000,\\
\operatorname{Res}(q_1,q_3)&=7880681899492416\neq 0.
\end{aligned}
\]

Thus each quadratic is squarefree, their four geometric roots are distinct, and their squareclasses are independent in \(\mathbb Q(t)^*/\mathbb Q(t)^{*2}\). Consequently the compositum has Galois group \((\mathbb Z/2\mathbb Z)^2\).

## 3. Independence of all six sections

At \(t_0=7/3\), the two branch conditions become

\[
q_1(t_0)=259^2,\qquad q_3(t_0)=(1085/3)^2.
\]

The two new points specialize to

\[
 P_1(t_0)=(63504,\ 96857712),\qquad
 P_3(t_0)=(-384160/9,\ 3155874400/81).
\]

The fiber is smooth. Exact finite-field counts give

\[
 \#E_{t_0}(\mathbb F_{19})=24,\qquad
 \#E_{t_0}(\mathbb F_{41})=44.
\]

Both primes are of good reduction. Rational torsion has order dividing \(\gcd(24,44)=4\). Since the known section \(T\) has order four, the fiber's torsion group is exactly C4. Its finite torsion points have \(x\)-coordinates \(0\) and \(4b(t_0)=188160\). Neither new point has either coordinate, so each is **nontorsion**.

Let \(\sigma_1\) negate \(\sqrt{q_1}\) while fixing \(\sqrt{q_3}\), and let \(\sigma_3\) negate \(\sqrt{q_3}\) while fixing \(\sqrt{q_1}\). Since the short-model \(x_i\) are rational functions of \(t\),

\[
\sigma_1(P_1)=-P_1,\quad \sigma_1(P_3)=P_3,\qquad
\sigma_3(P_3)=-P_3,\quad \sigma_3(P_1)=P_1.
\]

Both automorphisms fix the four inherited sections. If there were an integral relation among the six, applying \(\sigma_1-1\) would give a nonzero integer multiple of \(2P_1\) equal to zero, forcing the coefficient of \(P_1\) to vanish. Similarly \(\sigma_3-1\) forces the coefficient of \(P_3\) to vanish. The remaining relation is among the four published independent sections and is trivial. Thus

\[
\boxed{\operatorname{rank} E(K)\ge 6.}
\]

This is an independence argument *without* claiming the new points are independent from every possible unlisted section, nor that the generic rank is exactly six.

## 4. The parameter curve is genus one of positive rank

Each squarefree degree-two cover branches at two distinct geometric points of \(\mathbb P^1_t\), and their branch loci are disjoint. The combined degree-four Galois cover \(C\to\mathbb P^1_t\) has four branch values, each contributing two ramified points. Riemann–Hurwitz gives

\[
2g(C)-2=4(-2)+4(2)=0\quad\Longrightarrow\quad g(C)=1.
\]

The six distinct rational values

\[
\boxed{
 t=\frac73,\ -\frac{53}{7},\ -\frac{287}{367},\ -\frac{283}{368},\ -\frac{83}{848},\ -\frac{317}{1191}
}
\]

satisfy \(q_1(t)\in\mathbb Q^{\times2}\) and \(q_3(t)\in\mathbb Q^{\times2}\). They are all smooth parameters. Each has four distinct lifts \((t,\pm\sqrt{q_1(t)},\pm\sqrt{q_3(t)})\) to \(C(\mathbb Q)\). Therefore \(C\) has **at least 24 distinct rational points**.

A genus-one curve with a rational point is an elliptic curve over \(\mathbb Q\). Mazur's torsion theorem bounds its rational torsion subgroup by 16 points. Since 24 distinct rational points are displayed, at least one has infinite order. Thus **\(C(\mathbb Q)\) is infinite**. This avoids depending on an auxiliary Jacobian computation.

## 5. Infinitely many fibers have exact rational C4 torsion and rank >=6

The map \(t:C\to\mathbb P^1\) is nonconstant and finite, so infinitely many rational points of \(C\) produce infinitely many distinct rational \(t\)-values. The elliptic surface is nonisotrivial: \(b(t)\) has a simple zero at \(t=-1\) while \(a(-1)\neq0\), so the \(j\)-invariant is nonconstant. The specialization theorem preserves the six-section subgroup for all but finitely many rational points of \(C\).

To ensure **exact C4 torsion** (rather than merely the contained C4) for infinitely many fibers, note that \(C\) and the fiber at \(t_0=7/3\) have good reduction at both \(p=19\) and \(p=41\). The verifier checks the distinct branch loci modulo those primes and the fiber's point counts \(24\) and \(44\).

Choose any non-torsion point \(R\in C(\mathbb Q)\), whose existence was just proved, and the rational base point \(P_0\in C(\mathbb Q)\) above \(t_0\). The reduction maps from \(C(\mathbb Q)\) to \(C(\mathbb F_{19})\) and \(C(\mathbb F_{41})\) have finite images. There is therefore a positive integer \(M\) for which \(MR\) reduces to zero in both groups. The infinitely many points

\[
 P_0+nMR,\qquad n\in\mathbb Z,
\]

have the same reductions as \(P_0\) at 19 and 41, so their \(t\)-coordinates have the same reductions as \(t_0\). Each corresponding elliptic fiber is good at these primes and has group orders 24 and 44, so its rational torsion group has order at most four. The exhibited order-four section forces torsion **exactly C4**. All but finitely many of these infinitely many points also preserve rank >=6, completing the proof.

## 6. What is not proved

- **No new numerical rank record:** the known C4 infinite-family lower bound is already at least six.
- **No originality claim:** a different pair of quadratic formulas does *not* by itself rule out an isomorphism or base-change equivalence with previously published families.
- **No exact generic rank calculation:** only rank >=6 is established.
- **No seventh section:** none is present in this packet.
- **Parent rank-four independence is cited** from Elkies–Klagsbrun rather than independently certified by this verifier.

## Earlier C4 rank-six work

This is the same parent surface and four inherited sections that Elkies gave
in his [2007 lectures](https://arxiv.org/abs/0709.2908), with the corrected
parent equation printed by [Elkies and Klagsbrun in 2020](https://www.math.auckland.ac.nz/~sgal018/ANTS/papers/Elkies-Klagsbrun.pdf).
Elkies also described rank-six families made by pairing quadratic sections,
but did not print the pairs there.

[Dujella and Peral's 2021 survey](https://web.math.pmf.unizg.hr/~duje/pdf/DujellaPeralConstruction.pdf),
§4, prints these **same two quadratic covers** as entries 4 and 7 of its
substitution list:

\[
t=-\frac{u^2-212u+596}{4(u^2-11076)},\qquad
t=-\frac{u^2-350u+21924}{u^2-22276}.
\]

Taking the discriminant in \(u\) of each equation \(N(u)-tD(u)=0\) gives
exactly \(64q_1(t)\) and \(4q_3(t)\), respectively. The cover coordinates
are related by \(u=(106+4\sqrt{q_1})/(1+4t)\) and
\(u=(175+\sqrt{q_3})/(1+t)\). `verify.py` checks these identities. My earlier
comparison applied the leading minus sign to only the first term of each
numerator; that error produced the false claim that the covers differed.
The 2021 text says that several pairings yield rank-six families but does
not identify every pair there. I cannot claim this pair as an original
construction.

Their [2022 rank-six paper](https://web.math.pmf.unizg.hr/~duje/pdf/Rank6-TorsionZ4.pdf)
uses two covers with rational branch points and obtains a rational parameter
for its common family. Both quadratics here have negative discriminant, so
their branch points are nonreal, and their common base has genus one. Thus
these are different explicit covers over \(t\). A more indirect equivalence
of the resulting elliptic families has not been ruled out.

The pair in this entry differs from the pair in the neighboring C4
entry: those two branch quadratics have positive discriminant, while both
quadratics here have negative discriminant.

## Reproducibility

Run `sage -python verify.py`. The SageMath script checks the fields in
`data/rank6-family-certificate.json`, all four inherited point identities,
both new section identities, the branch loci, six rational parameters,
finite-field orders, and the arithmetic witnesses used above. The equations
are split across the named JSON files in `data/`; worked specializations are
in `data/specializations.csv`.
