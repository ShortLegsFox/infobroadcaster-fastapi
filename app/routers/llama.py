from fastapi import APIRouter

router = APIRouter(
    prefix="/llama",
    tags=["llama"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def read_llama():
    return {"message": "This is the llama route"}
