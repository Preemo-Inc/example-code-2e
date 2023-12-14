from dataclasses import dataclass, field

@dataclass
class ClubMember:
    name: str
    # Don't do this, every instance will reference the same list!
    # guests: list = []
    guests: list = field(default_factory=list)

