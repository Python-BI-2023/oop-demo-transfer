from dataclasses import dataclass


@dataclass
class Data:
    source: str
    name: str
    email: str
    text: str

    def to_dict(self):
        return {
            "source": self.source,
            "name": self.name,
            "email": self.email,
            "text": self.text,
        }
