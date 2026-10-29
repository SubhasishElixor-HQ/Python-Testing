# Mutation testing exercise

1. Run `uv run pytest phases/phase_13_advanced_testing -v`.
2. In `practice/math_rules.py`, temporarily change the upper bound from `100` to `101`.
3. Rerun the phase 13 tests.
4. Confirm a property test fails.
5. Restore the original implementation and rerun tests.

Do not leave the intentional bug in your code.
