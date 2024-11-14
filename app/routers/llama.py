from fastapi import APIRouter, HTTPException
from app.schema.schema import LlamaResponse
from app.utils.utils import is_valid_url, extract_article_from_url, summarize_article, entitle_article, theme_article

router = APIRouter(
    prefix="/llama",
    tags=["llama"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def read_llama():
    return {
        "message": "This is the llama route"
    }


@router.post("/summarize")
def summarize_llama(article_url: str):
    if not is_valid_url(article_url):
        raise HTTPException(status_code=404, detail="Invalid Url provided")

    extracted_article = extract_article_from_url(article_url)

    return LlamaResponse(
        summarized=summarize_article(extracted_article),
        title=entitle_article(extracted_article),
        themes=theme_article(extracted_article)
    )
