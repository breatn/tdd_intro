def is_balanced(expression: str) -> bool:
    """
    Should return True if all brackets in expression are correctly matched
    - (3+2) passes
    - [A B](C D) passes
    - [A B)[C D) fails
    - (((()) fails
    etc
    """

