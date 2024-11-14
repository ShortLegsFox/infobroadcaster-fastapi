


model =  "llama3.2:3b"


def summarize_article(article_content, lang):
    language = "English"

    if lang is "fr":
        language = "French"

    post_data = {
        "model": model,
        "prompt": f'Answer this prompt with a summary of no more than 50 words in {language}, using a concise sentence '
                  f'and without providing any explanation or additional comments. Only the translated text should be'
                  f' returned. Here\'s the text : {article_content}\n',
        "stream": False
    }

    # Send post_data to llama
    summarized_article = ""

    return summarized_article


def extract_theme(text_to_extract: str):
    post_data = {
        "model": model,
        "prompt": f"Analyze the following text: {text_to_extract}. Identify and list 3 keywords, that summarize the main"
                  f" themes. Present the results as a comma-separated list. Just answer me with your analysis, without "
                  f"further comment or presentation of the data.",
        "stream": False
    }
