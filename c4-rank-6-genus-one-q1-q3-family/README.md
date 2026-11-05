# Another C4 family of rank at least 6: the q1 and q3 covers

I start with the same Elkies discriminant-163 K3 surface as in the [other C4
entry](../c4-rank-6-genus-one-family/). This time the two new sections come
from particularly short quadratic formulas:

$$
q_1(t)=11076t^2+2620t+665,\qquad
q_3(t)=22276t^2+352t+8701.
$$

Their common parameter curve has genus one. I found six rational values of
`t` that each lift to four points on it. Those 24 points force the parameter
curve to have positive rank, so this construction gives infinitely many
rational curves with **exact C4 torsion and rank at least 6**.

The four starting sections are Elkies's, and I use their published
independence theorem. This is a rank lower bound, not a new rank record or an
exact generic-rank calculation. Elkies described the rank-six pairing idea
in 2007 without printing his pairs, so I do not claim priority for this pair.

## Check it

The [proof note](PROOF.md) gives the argument. [`data/`](data/) holds the
parent and cover equations, six worked specializations, and a rank-six
certificate. Run the SageMath verifier from this directory:

```bash
sage -python verify.py
```

If SageMath is in a Conda environment, activate it and run `python verify.py`.
The verifier uses SageMath and its bundled SymPy for exact arithmetic.
`SHA256SUMS` records hashes of the entry files.
