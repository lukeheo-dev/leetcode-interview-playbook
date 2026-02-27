# Project

## Setup
- `make init`

## Commands
- `make lint`
- `make format`

# LeetCode Study Notes

A collection of algorithm solutions and problem insights.

Start here if you're unsure where to begin — follow the study path I used to build skills step by step.

This repo is organized by **study phase** and **problem patterns**, so you can progress from fundamentals to advanced topics in a structured way.

## Repo structure

- `curriculum/` — roadmap + pattern notes (what to study, in what order)
- `problems/` — solved problems by phase/pattern
- `playbook/templates/` — templates for new problems

## Local workflow (recommended)

Run solutions locally with tests, then paste the final solution into LeetCode.

```bash
# create / refresh venv
uv venv --clear
source .venv/bin/activate

# install test runner
uv pip install -U pytest

# run all tests
pytest -q

# or run a single problem folder
pytest -q problems/phase_00_reset/p01_arrays_hashing/lc_0001_two_sum
```

## Blog (GitHub Pages)

Posts will live under `docs/` and can be published via GitHub Pages.

- `docs/index.md` — landing page
- `docs/posts/` — posts (one per problem)

## Notes

- Keep each problem folder self-contained: `solution.py`, `test_solution.py`, `notes.md`.
- Prefer an **optimized solution** as the main `solution.py`.
  - If you want to keep brute force for learning, put it in the same file as a second function (e.g., `two_sum_bruteforce`) or document it in `notes.md`.