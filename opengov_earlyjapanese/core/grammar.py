"""Grammar teaching utilities (simplified)."""

from typing import Dict, List

from pydantic import BaseModel


class GrammarExplanation(BaseModel):
    pattern: str
    meaning: str
    structure: str
    examples: List[str]


class GrammarTeacher:
    _db: Dict[str, GrammarExplanation] = {
        "です": GrammarExplanation(
            pattern="です",
            meaning="to be (polite copula)",
            structure="[Noun/Adjective] + です",
            examples=["学生です。", "元気です。"],
        )
    }

    def explain(self, pattern: str) -> GrammarExplanation:
        return self._db.get(
            pattern,
            GrammarExplanation(
                pattern=pattern, meaning="(unknown)", structure="", examples=[]
            ),
        )

