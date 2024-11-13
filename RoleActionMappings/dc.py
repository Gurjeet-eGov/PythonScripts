from dataclasses import dataclass

@dataclass
class ActionID:
    id: int = None
    url: str = None
    nav_url: str = None