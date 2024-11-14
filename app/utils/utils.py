from urllib.parse import urlparse
from newspaper import Article


def is_valid_url(url_to_test: str):
    try:
        result = urlparse(url_to_test)
        return all([result.scheme, result.netloc])
    except:
        return False


def extract_article_from_url(url_to_extract: str):
    article = Article(url_to_extract)
    article.download()
    article.parse()

    return article.text


def summarize_article(article_to_summarize: str):
    # To be implemented
    pass


def entitle_article(article_to_entitle: str):
    # To be implemented
    pass


def theme_article(article_to_theme: str):
    # To be implemented
    pass
