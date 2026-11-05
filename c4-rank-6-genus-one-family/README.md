# C4 family of rank at least 6

I start with Elkies's discriminant-163 K3 surface and its four known independent
sections. Two explicit quadratic covers each add a section. Their common base
is a genus-one curve with infinitely many rational points, so this gives
infinitely many elliptic curves over **Q** with rational torsion exactly C4 and
rank **at least 6**.

## Check it

The [`data/`](data/) folder holds the parent equation and sections, both
quadratic covers, the common fiber, the genus-one base, and the
`rank6-family-certificate.json` receipt. The [proof note](PROOF.md) gives the
full argument. From this directory, run the SageMath verifier:

```bash
sage -python verify.py
```

If SageMath is in a Conda environment, activate it and run `python verify.py`.
The verifier uses SageMath and its bundled SymPy for exact arithmetic.
`SHA256SUMS` records hashes of the entry files.
