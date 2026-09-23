"""
Week 1 exercise checker — vectors, linear combinations, and span.

Fill in your answers in week01_vectors_practice.ipynb, save it, then run:

    python tests.py

This runs every code cell of your notebook in a fresh namespace and checks
the resulting variables against expected values. It contains checks only —
no exercise solutions.

Exercise C (the quiver plot) isn't graded here since it's a visual check —
just eyeball your plot in the notebook.
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # don't pop up plot windows while checking

import numpy as np
import nbformat

NOTEBOOK_PATH = Path(__file__).parent / "week01_vectors_practice.ipynb"


def run_notebook(path):
    nb = nbformat.read(path, as_version=4)
    namespace = {}
    for cell in nb.cells:
        if cell.cell_type != "code":
            continue
        try:
            exec(compile(cell.source, "<notebook cell>", "exec"), namespace)
        except Exception as e:
            print(f"Your notebook raised an error while running: {type(e).__name__}: {e}")
            print("Fix the error in your notebook (run it top to bottom there first), then try again.")
            sys.exit(1)
    return namespace


def check(results, name, condition, message=""):
    results.append((name, bool(condition), message))


def main():
    if not NOTEBOOK_PATH.exists():
        print(f"Could not find {NOTEBOOK_PATH}")
        sys.exit(1)

    ns = run_notebook(NOTEBOOK_PATH)
    results = []

    # --- Exercise A: 2u + 3z ---
    expected_a = 2 * np.array([2, 1]) + 3 * np.array([-1, 4])
    try:
        loop_arr = np.array(ns.get("loop_result"))
        ok = loop_arr.shape == expected_a.shape and np.array_equal(loop_arr, expected_a)
    except Exception:
        ok = False
    check(results, "A: loop_result == 2u + 3z", ok)

    try:
        numpy_arr = np.array(ns.get("numpy_result"))
        ok = numpy_arr.shape == expected_a.shape and np.array_equal(numpy_arr, expected_a)
    except Exception:
        ok = False
    check(results, "A: numpy_result == 2u + 3z", ok)

    # --- Exercise B: is_parallel ---
    is_parallel = ns.get("is_parallel")
    if callable(is_parallel):
        cases = [
            (np.array([1, 2]), np.array([2, 4]), True),
            (np.array([1, 0]), np.array([0, 1]), False),
            (np.array([3, -1]), np.array([-6, 2]), True),
            (np.array([1, 1]), np.array([1, 2]), False),
            (np.array([-2, 5]), np.array([4, -10]), True),
        ]
        all_ok = True
        for v, w, expected in cases:
            try:
                got = bool(is_parallel(v, w))
            except Exception:
                got = None
            if got != expected:
                all_ok = False
        check(results, "B: is_parallel handles all test cases", all_ok)
    else:
        check(results, "B: is_parallel is defined", False, "is_parallel is not a callable function")

    # --- Exercise D: span of parallel vectors is a line ---
    points_d = ns.get("points_D")
    try:
        pts = np.array(points_d, dtype=float)
        v1 = np.array([1, 2])
        cross = pts[:, 0] * v1[1] - pts[:, 1] * v1[0]
        ok = pts.ndim == 2 and pts.shape[0] >= 50 and pts.shape[1] == 2 and np.allclose(cross, 0, atol=1e-6)
    except Exception:
        ok = False
    check(results, "D: points_D all lie on the line through [1, 2]", ok)

    # --- Exercise E: span of non-parallel vectors is the whole plane ---
    points_e = ns.get("points_E")
    try:
        pts = np.array(points_e, dtype=float)
        v = pts[0]
        cross = pts[:, 0] * v[1] - pts[:, 1] * v[0]
        ok = pts.ndim == 2 and pts.shape[0] >= 50 and pts.shape[1] == 2 and not np.allclose(cross, 0, atol=1e-6)
    except Exception:
        ok = False
    check(results, "E: points_E are not all collinear (they fill the plane)", ok)

    # --- Exercise F: dot products ---
    dot_perp = ns.get("dot_perp")
    dot_parallel = ns.get("dot_parallel")
    try:
        ok = dot_perp is not None and np.isclose(float(dot_perp), 0, atol=1e-6)
    except Exception:
        ok = False
    check(results, "F: dot_perp is ~0", ok)

    try:
        ok = dot_parallel is not None and not np.isclose(float(dot_parallel), 0, atol=1e-6)
    except Exception:
        ok = False
    check(results, "F: dot_parallel is nonzero", ok)

    # --- Report ---
    passed = 0
    for name, ok, message in results:
        status = "PASS" if ok else "FAIL"
        line = f"[{status}] {name}"
        if message and not ok:
            line += f" - {message}"
        print(line)
        if ok:
            passed += 1

    print(f"\n{passed}/{len(results)} checks passed.")
    print("(Exercise C is not graded here - check your plot visually.)")

    if passed < len(results):
        sys.exit(1)


if __name__ == "__main__":
    main()
