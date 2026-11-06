# C4 S3 family of rank at least 6

I start with the Elkies–Klagsbrun C4 surface and its four known independent
sections. An explicit cubic gives three conjugate points on each fiber. Its
S3 splitting field has a genus-one base with infinitely many rational
points. The differences between the three points supply two new independent
directions, giving infinitely many elliptic curves over **Q** with torsion
exactly C4 and rank **at least 6**.

This is a rank lower bound over the genus-one function field. The four
inherited sections rely on the published Elkies–Klagsbrun independence
theorem. I have not proved exact generic rank six.

## Novelty

I have found no duplicate of this S3 construction among the sources checked
so far. The rank-six infinite-family bound and the parent surface are
earlier work. Publication priority remains open because the formulas behind
a separate Dujella–Peral 2026 table entry have not been located.

## Check it

The [proof note](PROOF.md) gives the argument. The [`data/`](data/) folder
holds the cubic, genus-one base, smooth fiber, and exact witnesses. From this
directory, run:

```bash
python verify.py
```

The verifier uses SymPy and checks the new arithmetic exactly. Install the
dependency with `python -m pip install 'sympy>=1.12,<2.0'` if needed.
`SHA256SUMS` records hashes of the entry files.
