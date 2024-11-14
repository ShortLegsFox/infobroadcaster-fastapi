from pydantic import BaseModel


class Test(BaseModel):
    test_name: str
    test_value: str
