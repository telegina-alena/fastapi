from pydantic import BaseModel, Field, field_validator
import pymorphy3

morph = pymorphy3.MorphAnalyzer()

class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)

    @field_validator("message")
    @classmethod
    def validate_swear_words(cls, value):
        forbidden_words = {"ужас", "кошмар", "сережа", "илья", "боря"}
        words = value.lower().split()

        for word in words:
            parsed = morph.parse(word)[0]
            normal_form = parsed.normal_form
            if normal_form in forbidden_words:
                raise ValueError(f"Вы написали плохое слово: {word}. Стыд и позор!")
        return value