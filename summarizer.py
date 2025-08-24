# summarizer.py
from transformers import pipeline

# Load summarization pipeline (BART model)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text, min_length=30, max_length=100):
    """
    Summarizes input text using BART model
    :param text: input string
    :param min_length: minimum words in summary
    :param max_length: maximum words in summary
    :return: summarized text
    """
    summary = summarizer(text, min_length=min_length, max_length=max_length, do_sample=False)
    return summary[0]['summary_text']
