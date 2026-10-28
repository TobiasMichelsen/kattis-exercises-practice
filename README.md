# Kattis Exercises – Algorithm Design

My solutions and study notes for Kattis problems from the **Algorithm Design** course (MSc Data Science, Autumn 2026). All solutions are written in Python, mostly as Jupyter notebooks that walk through the problem, the input parsing, and the algorithm step by step.

The course follows Kleinberg & Tardos, *Algorithm Design*.

## Contents

| Notebook | Topic / technique | Status |
|---|---|---|
| `Prerequisites/basic_programming2_1.ipynb` | Basic Programming 2 – warm-up techniques (sets, sorting, counting) with `assert` tests | Done |
| `EchoEchoEcho.ipynb` | Reading input / printing output on Kattis | Done |
| `Alternate_B.ipynb` | Simple string processing | Done |
| `NFL_draft.ipynb` | Stable matching (Gale–Shapley variant with team capacities) | In progress |
| `Stable_Perfect_Matching.ipynb` | Stable perfect matching | Not started |
| `YetSatisfiabilityAgain.ipynb` | Brute-force SAT using bitmasks over all variable assignments | Done |
| `Minimum Scalar Product.ipynb` | Greedy – sort one vector ascending, the other descending | Done |
| `Closest_Pair_of_Points.ipynb` | Divide and conquer – closest pair of points in the plane | Done |
| `Closest_Pair_of_Points_TA.ipynb` | Same problem, version worked through with the TA | Done |
| `closestpairnicer.py` | Closest pair as a plain script, ready to submit to Kattis | Done |
| `DynamicProgramming1.ipynb` | Dynamic programming – weighted interval scheduling | Done |
| `max_flow.ipynb` | Network flow – Ford–Fulkerson, residual graphs, max-flow = min-cut | Done |

## How the notebooks are structured

Most notebooks follow the same pattern:

1. **Problem statement** – copied from Kattis (text or screenshot).
2. **Sample input** – pasted into a string such as `sample_input = """..."""`.
3. **Read-in** – parse the input into Python data structures.
4. **Algorithm** – built up in small cells, with print statements to check intermediate state.
5. **Notes** – explanation of why the algorithm works and its running time.

### Local testing vs. Kattis submission

Kattis gives input on *standard input* (`sys.stdin`), but in a notebook it's easier to test with a pasted string. Most notebooks have a toggle like this:

```python
# lines = sys.stdin.read().splitlines()   # real Kattis submission
lines = sample_input.strip().splitlines()  # local testing
```

- **Testing in the notebook:** keep the second line active.
- **Submitting to Kattis:** comment out the second line, uncomment the first, and copy the code cells into a single `.py` file.

- Kleinberg & Tardos, *Algorithm Design* – course textbook
