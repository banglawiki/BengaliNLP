import unicodedata
from ftfy import fix_text
from . import const

def fix_quotes(text):
    text = const.SINGLE_QUOTE_REGEX.sub("'", text)
    text = const.DOUBLE_QUOTE_REGEX.sub('"', text)
    return text

def replace_patterns(text, pattern, replacement):
    return pattern.sub(replacement, text)

def apply_char_replacements(text):
    return text.translate(const.CHAR_REPLACEMENTS)

def apply_unicode_replacements(text):
    return const.UNICODE_REPLACEMENTS_REGEX.sub(
        lambda match: const.UNICODE_REPLACEMENTS.get(match.group(0), f"{match.group(1)}\u09cc"),
        text
    )

def normalize(
    text,
    unicode_norm="NFKC",
    punct_replacement=None,
    url_replacement=None,
    emoji_replacement=None,
    apply_unicode_norm_last=True
):
    # Fix encoding-related issues first and group characters for future char replacements to work
    text = fix_text(text, normalization="NFC", explain=False)

    # Normalize variations of quotes
    text = fix_quotes(text)

    # Replace URLs in text with specified replacement (if any)
    if url_replacement is not None:
        text = replace_patterns(text, const.URL_HANDLER_REGEX, url_replacement)

    # Replace punctuations with specified replacement (if any)
    if punct_replacement is not None:
        text = replace_patterns(text, const.PUNCT_HANDLER_REGEX, punct_replacement)

    # Replace emojis in text with specified replacement (if any)
    if emoji_replacement is not None:
        text = replace_patterns(text, const.EMOJI_HANDLER_REGEX, emoji_replacement)

    # Apply char replacements
    text = apply_char_replacements(text)
    
    if not apply_unicode_norm_last:
        text = unicodedata.normalize(text, unicode_norm)

    # Apply unicode replacements    
    text = apply_unicode_replacements(text)

    if apply_unicode_norm_last:
        text = unicodedata.normalize(unicode_norm, text)

    # Finally, clean up extra whitespaces
    text = const.WHITESPACE_HANDLER_REGEX.sub(" ", text)

    return text
