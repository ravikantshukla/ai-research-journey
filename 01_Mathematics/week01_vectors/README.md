# Week 1 — Vectors, Linear Combinations, and Span

## Goals

- Understand a vector as both a list of numbers and an arrow in space.
- Be comfortable computing vector addition, scalar multiplication, dot product, and norm — both by hand-coded loops and with NumPy.
- Understand what a *linear combination* is: scaling vectors and adding them.
- Understand *span*: the set of every point reachable via linear combinations of a set of vectors, and why two parallel vectors only span a line while two independent vectors span a whole plane.
- Build intuition for the dot product's geometric meaning (angle/direction between vectors), not just the formula.

## Resources

- [3Blue1Brown — Essence of Linear Algebra](https://www.3blue1brown.com/topics/linear-algebra), episodes 1–4:
  1. Vectors, what even are they?
  2. Linear combinations, span, and basis vectors
  3. Linear transformations and matrices
  4. Matrix multiplication as composition

  (Episode 3–4 preview next week's material on transformations — fine to watch now for context, but the focus this week is episodes 1–2.)

## Setup

From the repo root:

```
.venv\Scripts\activate
jupyter notebook 01_Mathematics/week01_vectors/week01_vectors_practice.ipynb
```

## Checklist

- [ ] Watch 3Blue1Brown episodes 1–2 (vectors, linear combinations & span)
- [ ] Read the recap cell and run the 5 demo cells in `week01_vectors_practice.ipynb`
- [ ] Exercise A — compute `2u + 3z` by loop and by NumPy
- [ ] Exercise B — write `is_parallel(v, w)`
- [ ] Exercise C — plot vectors as arrows with `quiver`
- [ ] Exercise D — show `[1,2]` and `[2,4]` only span a line
- [ ] Exercise E — show `[1,0]` and `[0,1]` span the whole plane
- [ ] Exercise F — compute perpendicular vs. parallel dot products and explain the pattern
- [ ] Run `python tests.py` and get all checks passing (Exercise C is graded visually, not by the script)
- [ ] Commit when done
