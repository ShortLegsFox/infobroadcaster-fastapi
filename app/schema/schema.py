from pydantic import BaseModel
from typing import List


class LlamaResponse(BaseModel):
    summarized: str
    title: str
    themes: List[str]
