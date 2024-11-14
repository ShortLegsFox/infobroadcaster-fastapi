from fastapi import APIRouter


router = APIRouter(
    prefix="/rainbow",
    tags=["rainbow"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def read_rainbow():
    return {"message": "This is the rainbow route"}
