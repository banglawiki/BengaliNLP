import re

def clean_text(text):
    """
    Cleans and normalizes text for natural language processing tasks.

    Args:
        text (str): The text to be cleaned.

    Returns:
        str: The cleaned text.
    """

    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)

    # Replace special characters with their ASCII equivalents
    text = translate(CHAR_REPLACEMENTS, text)

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Convert to lowercase
    text = text.lower()

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)

    return text
