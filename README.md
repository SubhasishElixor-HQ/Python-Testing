# Python Testing — Phase-by-Phase Learning Project

A practical Python testing project covering 14 phases, from testing fundamentals to CI/CD and production testing gates.

## 1. Project Goals

Learn how to:

- Write and execute Python tests using `pytest`.
- Design test cases and assertions.
- Perform unit, API, integration, security, and regression testing.
- Use fixtures, mocking, and test isolation.
- Test FastAPI applications.
- Understand performance, reliability, and recovery testing.
- Explore advanced testing techniques.
- Automate testing through CI/CD pipelines.

## 2. Prerequisites

Install the following tools:

- Python
- `uv` — Python project and dependency manager
- Git (recommended)
- Docker Desktop (for PostgreSQL integration testing)

Verify your installations:

```powershell
python --version
uv --version
git --version
docker --version
```

Docker is optional unless you are running the database integration examples.

## 3. Install Dependencies

Open PowerShell in the root directory of this project.

Install the dependencies:

```powershell
uv sync
```

Check the pytest version:

```powershell
uv run pytest --version
```

## 4. Run the Complete Test Suite

Run all automatically discoverable pytest tests:

```powershell
uv run pytest -v
```

Show additional information about skipped tests, expected failures, and warnings:

```powershell
uv run pytest -v -ra
```

Show a short summary:

```powershell
uv run pytest -q
```

Stop after the first failure:

```powershell
uv run pytest -x -v
```

Run tests while displaying Python warnings:

```powershell
uv run pytest -v -W default
```

Treat warnings as errors:

```powershell
uv run pytest -v -W error
```

**Important:** A passing test suite does not guarantee that every possible behavior or production scenario is covered.

## 5. Run Each Phase Individually

Run these commands from the project root, one at a time.

### Phase 1 — Testing Fundamentals

Learn basic assertions and test execution.

```powershell
uv run pytest phases/phase_01_fundamentals -v
```

### Phase 2 — Pytest Basics

Learn test discovery, execution, and pytest conventions.

```powershell
uv run pytest phases/phase_02_pytest -v
```

### Phase 3 — Test Case Design

Practice designing test cases for expected and unexpected inputs.

```powershell
uv run pytest phases/phase_03_test_case_design -v
```

### Phase 4 — Unit Testing

Test individual functions and components.

```powershell
uv run pytest phases/phase_04_unit_testing -v
```

### Phase 5 — Fixtures, Mocking, and Isolation

Learn reusable fixtures, mocks, and isolated tests.

```powershell
uv run pytest phases/phase_05_fixtures_mocking_isolation -v
```

### Phase 6 — FastAPI API Testing

Test HTTP endpoints, status codes, and response bodies.

```powershell
uv run pytest phases/phase_06_fastapi_api_testing -v
```

### Phase 7 — PostgreSQL Integration Testing

This phase requires a separately configured test database and the environment variables and dependencies documented for this phase.

```powershell
uv run pytest phases/phase_07_postgresql_integration -v
```

Do not run database integration tests against production data.

### Phase 8 — Contract and End-to-End Testing

Run the pytest examples:

```powershell
uv run pytest phases/phase_08_contract_e2e -v
```

Some end-to-end examples require a running application and additional browser-testing setup.

### Phase 9 — Regression, Smoke, and Acceptance Testing

```powershell
uv run pytest phases/phase_09_regression_smoke_acceptance -v
```

### Phase 10 — Security Testing

```powershell
uv run pytest phases/phase_10_security_testing -v
```

Use security tests only against applications and environments you are authorized to test.

### Phase 11 — Performance and Load Testing

The Locust example requires a running demo API.

```powershell
uv run locust -f phases/phase_11_performance_load/locustfile.py
```

Follow the Locust terminal instructions to open its interface and configure a target host. Use only an authorized test environment.

### Phase 12 — Reliability and Recovery Testing

```powershell
uv run pytest phases/phase_12_reliability_recovery -v
```

### Phase 13 — Advanced Testing

```powershell
uv run pytest phases/phase_13_advanced -v
```

This phase includes advanced techniques such as property-based testing. Additional tools or configuration may be required for optional exercises.

### Phase 14 — CI/CD and Production Testing Gates

Inspect the GitHub Actions workflow:

```powershell
Get-Content .github/workflows/ci.yml
```

Check the workflow file's Git status:

```powershell
git status --short
```

The workflow must be correctly configured and run in GitHub Actions before you can claim that CI has passed.

## 6. Check One Phase at a Time

Recommended workflow:

1. Run the command for Phase 1.
2. Read the complete output.
3. Check whether tests passed, failed, errored, or were skipped.
4. Investigate warnings.
5. Fix problems and rerun the phase.
6. Record the result.
7. Continue to the next phase.

Do not move to the next phase until you understand the current failures and setup requirements.

## 7. Understand Test Results

| Result | Meaning |
|---|---|
| `PASSED` | The test completed successfully. |
| `FAILED` | An assertion or expected behavior failed. |
| `ERROR` | The test or its setup could not run correctly. |
| `SKIPPED` | The test was not executed. |
| `XFAIL` | The test failed as expected. |
| `XPASS` | A test marked as expected to fail unexpectedly passed. |
| `WARNING` | A potential issue was reported. |

Example of a successful test summary:

```text
======================== 5 passed in 0.10s ========================
```

Example of a test failure:

```text
======================== 1 failed, 4 passed in 0.20s ========================
```

A warning does not necessarily mean a test failed. Read the warning message to determine whether action is needed.

## 8. Useful Debugging Commands

Run a specific test file:

```powershell
uv run pytest path/to/test_file.py -v
```

Run a specific test function:

```powershell
uv run pytest path/to/test_file.py::test_function_name -v
```

Show print output:

```powershell
uv run pytest -v -s
```

Show more detailed failure information:

```powershell
uv run pytest -vv --tb=long
```

List discovered tests without running them:

```powershell
uv run pytest --collect-only -q
```

## 9. Common Problems

### Problem: `uv` is not recognized

Install `uv` using its official installation instructions, then reopen PowerShell and check:

```powershell
uv --version
```

### Problem: A dependency is missing

Synchronize the project environment:

```powershell
uv sync
```

If the error persists, check whether the missing package is declared in `pyproject.toml`.

### Problem: No tests were collected

Check the phase directory and its test files:

```powershell
Get-ChildItem phases -Recurse -File
```

Confirm that test files and functions follow pytest's discovery conventions, such as `test_*.py` and `test_*`.

### Problem: A test fails

Run the failing test by itself:

```powershell
uv run pytest path/to/test_file.py::test_function_name -vv
```

Read the traceback and assertion details before changing code.

### Problem: PostgreSQL integration tests cannot connect

Check the test database configuration, connection URL, database availability, and required dependencies. Use a dedicated test database rather than production data.

## 10. Learning Progress Checklist

- [ ] Phase 1 — Testing Fundamentals
- [ ] Phase 2 — Pytest Basics
- [ ] Phase 3 — Test Case Design
- [ ] Phase 4 — Unit Testing
- [ ] Phase 5 — Fixtures, Mocking, and Isolation
- [ ] Phase 6 — FastAPI API Testing
- [ ] Phase 7 — PostgreSQL Integration Testing
- [ ] Phase 8 — Contract and End-to-End Testing
- [ ] Phase 9 — Regression, Smoke, and Acceptance Testing
- [ ] Phase 10 — Security Testing
- [ ] Phase 11 — Performance and Load Testing
- [ ] Phase 12 — Reliability and Recovery Testing
- [ ] Phase 13 — Advanced Testing
- [ ] Phase 14 — CI/CD and Production Testing Gates

## 11. Recommended Learning Order

Follow the phases in order. Start with fundamentals, then progress to unit testing, API testing, integration testing, security, performance, reliability, and CI/CD.

For every phase, aim to understand:

- What the testing technique means.
- Why it is useful.
- How to write the test.
- How to execute it.
- How to interpret failures and warnings.
- What evidence demonstrates that the test ran successfully.

**Project status:** This repository is a learning project. Running its commands is the first step; passing results must be verified in your own environment. Database, browser, load-testing, and CI/CD exercises may require additional setup.
