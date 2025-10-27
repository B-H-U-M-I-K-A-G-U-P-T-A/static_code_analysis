1. Which issues were the easiest to fix, and which were the hardest? Why?

Easiest:
- Trailing whitespace & blank lines - Simple find/replace, no logic changes
- String formatting (% → f-strings) - Direct substitution
- Missing final newline - One keystroke fix
- Unused imports - Delete or use them
It involved only pure formatting, no business logic involved.
Hardest:-
- Removing global statement - Required complete OOP refactor (procedural → class-based)
- Input validation - Needed to understand business rules (what's valid? what's not?)
- Bare except - Had to identify specific exceptions that could occur
- File operations - Restructuring exception handling with context managers
It required understanding intent, making design decisions, and architectural changes.

2. Did the static analysis tools report any false positives? If so, describe one example.

W0603: Using the global statement
For a simple 50-line script, a global variable is acceptable and straightforward. It is not inherently dangerous - just a style preference. Converting to OOP adds complexity for minimal benefit in small scripts.
However, Pylint is technically correct - OOP is better for scalability, testing, and maintainability.Therefore it is a context-dependent warning, not a true false positive. For production, fix it. For simple scripts, debatable.

3. How would you integrate static analysis tools into your actual software development
workflow? Consider continuous integration (CI) or local development practices.

Local Developments:
# Pre-commit hook (.git/hooks/pre-commit)
pylint **/*.py --fail-under=8.0 || exit 1
flake8 . || exit 1
bandit -r . || exit 1

IDE Integration:
// VS Code settings.json
{
  "python.linting.pylintEnabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.lintOnSave": true
}

CI Pipeline:
- name: Static Analysis
  run: |
    pylint **/*.py --fail-under=8.0
    flake8 .
    bandit -r .

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

Security:
Removed eval() → Prevents code injection
Fixed bare except → Bugs no longer hidden
Added validation → No crashes from bad input

Maintainability:
Snake_case + docstrings → Self-documenting
OOP structure → Clear ownership

Reliability:
File errors → Graceful fallback instead of crash
Logging → Clear error messages for debugging

Metrics:
Pylint: 4.80 → 10.00/10 (+108%)
Security: 2 → 0 issues
Style: 31 → 0 issues
In the end, the code went from prototype to production-ready.

