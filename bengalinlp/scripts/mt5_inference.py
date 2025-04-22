"""
mT5 Inference Example for Bengali NLP
"""

from transformers import MT5ForConditionalGeneration, MT5Tokenizer

# You can use 'google/mt5-small', 'google/mt5-base', etc.
MODEL_NAME = "google/mt5-small"


def mt5_generate(text, task_prefix="translate Bengali to English: "):
    tokenizer = MT5Tokenizer.from_pretrained(MODEL_NAME)
    model = MT5ForConditionalGeneration.from_pretrained(MODEL_NAME)
    input_text = task_prefix + text
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    output_ids = model.generate(input_ids, max_length=64, num_beams=4)
    output = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return output


if __name__ == "__main__":
    # Example: Bengali to English translation
    sample_bn = "আমি স্কুলে যাচ্ছি।"
    translated = mt5_generate(sample_bn, task_prefix="translate Bengali to English: ")
    print("Bengali:", sample_bn)
    print("English Translation:", translated)

    # Example: Summarization (if you have a Bengali summary task)
    # summary = mt5_generate("<long Bengali text>", task_prefix="summarize: ")
    # print("Summary:", summary)
