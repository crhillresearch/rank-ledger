# C2 family of rank at least 11

I start with an elliptic K3 family carrying rational 2-torsion and nine
independent sections. Two quadratic covers, numbered 10 and 13 in the source
portfolio, each add a section. Their common base is a genus-one curve with
infinitely many rational points. The two cover involutions show that the new
sections are independent of each other and of the original nine. This gives
infinitely many rational elliptic curves with torsion C2 and rank at least 11.

The rank-11 claim is over the genus-one function field, not the original
parameter line. This is a rank **lower bound**; I have not proved exact rank
11 for the generic curve or every specialization.

## Disclaimer

I've established that the parent K3 differs from Elkies's (2007) and Dujella–Peral (2023) examples.
I have **not** eliminated possible overlap with Elkies (2009).

## Check it

The [proof note](PROOF.md) gives the argument. The [`data/`](data/) folder
holds the exact equations, section coordinates, and height certificates.
From this directory, run the verifier with SageMath's Python:

```bash
sage -python verify.py
```

If SageMath is in a Conda environment, activate it and run `python verify.py`.
The verifier checks the parent and cover height matrices, the genus-one base,
independence of the new sections, and the torsion claim. `SHA256SUMS` records
the hashes of the packet files.
