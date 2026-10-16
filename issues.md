\# Lab 5: Static Code Analysis — Parking Lot System



| Issue | Severity / Type | Description | Fix Applied |

|---|---|---|---|

| Unsafe `eval()` | Medium — Security | Evaluating arbitrary expressions can execute unsafe code. | Replaced with validated numeric fee calculation. |

| Weak MD5 hashing | High — Security | MD5 is unsuitable for security-sensitive hashing. | Replaced with SHA-256. |

| Shell command execution | High — Security | `os.system()` can introduce command-injection risks. | Removed shell execution and printed the export message directly. |

| Bare exception handling | Low — Robustness | Silently ignoring exceptions hides errors. | Reworked slot release to check whether the slot exists. |

| Insecure random PIN | Low — Security | `random.randint()` is not designed for security-sensitive PIN generation. | Used Python's `secrets` module. |

| Mutable default argument | Code quality | A shared default list can retain data across function calls. | Used `None` and initialized the list inside the function. |

| Unused imports and variables | Code quality | Unused names reduce readability. | Removed unnecessary imports and variables. |

| Inconsistent naming and missing documentation | Code quality | Non-standard names and missing docstrings make code harder to maintain. | Used snake\_case names and added docstrings. |

| Long lines and missing newline | Style | Formatting issues violate Python style conventions. | Reformatted long lines and maintained proper file formatting. |

| Unsafe file handling | Robustness | File operations lacked explicit encoding and reliable resource management. | Used a context manager and UTF-8 encoding. |



\*\*Note:\*\* Line numbers and original findings refer to the initial version of the program. Final analysis results should be recorded separately from the original findings.

