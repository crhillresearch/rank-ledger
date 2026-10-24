# From 17 to 19

I started with an elliptic surface carrying 17 independent sections. Two
quadratic covers each gave me one more. Together, they give **19 independent
sections** over the function field of a genus-one curve.

The genus-one parameter curve has a rational point of infinite order. That
means this construction produces infinitely many elliptic curves over
$\mathbb Q$ with rank at least 19. Infinitely many of them have trivial
rational torsion, too.

This is a rank **lower bound**. I haven't proved that the generic rank or
any particular fiber has exact rank 19.

## The two covers

$$
\begin{aligned}
r_1^2 &= 30015061720809t^2-20692173881368t+3538696407184,\\
r_2^2 &= 46784549960425t^2-29557331565600t+4702049024256.
\end{aligned}
$$

Both covers have a rational point above $t=15122/33609$. Their combined
parameter curve has genus one, and that point has infinite order on its
elliptic model.

Each new section has an exact height calculation behind it. The height
matrix for each 18-section cover is positive definite. The two cover
involutions separate the new sections: each section differs from its
conjugate by a point of height 12. That proves all 19 are independent when
the covers are combined.

## Check it

The [proof note](PROOF.md) has the full argument. The [`data/`](data/)
folder holds the equations, section coordinates, and height matrices.
From this directory, run the verifier with SageMath's Python. With a
standard SageMath installation:

```bash
sage -python verify.py
```

If SageMath is installed in a Conda environment, activate that environment
and run `python verify.py` instead.

The verifier checks the equations, the 19-section argument, the infinite
order point, and the finite-field calculations used for trivial torsion.
