"""
Script for fine-tuning a Bengali LLM (HuggingFace Transformers example).
"""

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
)
from datasets import load_dataset


def train_llm(model_name, dataset_path, output_dir):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)
    dataset = load_dataset("csv", data_files=dataset_path)

    def preprocess(examples):
        return tokenizer(examples["text"], truncation=True, padding=True)

    tokenized = dataset.map(preprocess, batched=True)
    args = TrainingArguments(
        output_dir=output_dir, evaluation_strategy="epoch", num_train_epochs=1
    )
    trainer = Trainer(model=model, args=args, train_dataset=tokenized["train"])
    trainer.train()
    model.save_pretrained(output_dir)


if __name__ == "__main__":
    # Example usage
    train_llm("ai4bharat/indic-bert", "./data/train.csv", "./output_model")
