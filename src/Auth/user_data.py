from dataclasses import dataclass

"""
Data for users information. Just example
"""

@dataclass
class Person:
    mail: str
    password: str
    id: int
    