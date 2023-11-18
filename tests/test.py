from bengalinlp import normalize  # Assuming your module is named 'bengalinlp'
from bengalinlp import const

def test_text_replacement(data, replacement_type, replacement_string=None):
    for input_text, expected_output in data:
        if replacement_string is None:
            normalized_text = normalize(input_text, replacement_type=replacement_type)
        else:
            normalized_text = normalize(input_text, replacement_type=replacement_type, replacement_string=replacement_string)
        
        assert normalized_text == expected_output, f"Test failed for input: {input_text}"

def test_url_replacements():
    data = [
        [
            "যেভাবে মেম্বার হবেন https://khulnasoft.com এ একটি একাউন্ট খুলুন।",
            "যেভাবে মেম্বার হবেন এ একটি একাউন্ট খুলুন।"
        ]
    ]
    test_text_replacement(data, const.URL_REPLACEMENT)

def test_char_replacements():
    data = [
        [
            "La retirada de Occidente de Afganistán significa que hay mucho en juego para China, Rusia, Pakistán e Irán.",
            "La retirada de Occidente de Afganistan significa que hay mucho en juego para China, Rusia, Pakistan e Iran."
        ]
    ]
    test_text_replacement(data, const.CHAR_REPLACEMENT)

def test_emoji_replacements():
    data = [
        [
            "🗽Удачи, Любви и Счатья!🏝 Срочно👨🏻‍🎨 нужны Тайные📺 Агенты💡! В связи с расширением👩🏻‍🍳",
            "<<emoticon>>Удачи, Любви и Счатья!<<emoticon>> Срочно<<emoticon>> нужны Тайные<<emoticon>> Агенты<<emoticon>>! В связи с расширением<<emoticon>>"
        ]
    ]
    test_text_replacement(data, const.EMOJI_REPLACEMENT, "<<emoticon>>")

def test_punct_replacements():
    data = [
        [
            "যেভাবে মেম্বার হবেন https://khulnasoft.com এ একটি একাউন্ট খুলুন।",
            "যেভাবে মেম্বার হবেন https<<punct>><<punct>><<punct>>khulnasoft<<punct>>com এ একটি একাউন্ট খুলুন<<punct>>"
        ]
    ]
    test_text_replacement(data, const.PUNCT_REPLACEMENT, "<<punct>>")

def test_unicode_replacements():
    data = [
        [
            "\u09F7",
            "\u0964"
        ],
        [
            "\u09af\u09bc",
            "\u09af\u09bc"
        ],
        [
            "\u00a0",
            " "
        ],
        [
            'েশৗ',
            'শৌ'
        ]
    ]
    test_text_replacement(data, const.UNICODE_REPLACEMENT)

if __name__ == "__main__":
    test_url_replacements()
    test_char_replacements()
    test_emoji_replacements()
    test_punct_replacements()
    test_unicode_replacements()
