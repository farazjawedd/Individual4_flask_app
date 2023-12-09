from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn", min_length=60)

def summarize(text, length=None):
    """
    Summarize input text
    """
    if length:
        # Truncate summary if length provided
        summary = summarizer(text, max_length=length, min_length=60)[0]['summary_text']   
    else:
        # Default summarization
        summary = summarizer(text)[0]['summary_text']

    return summary


def analyze_summary(original, summary):
    """
    Analyze the similarity between original text 
    and generated summary
    """
    import difflib
    diff = difflib.SequenceMatcher(None, original, summary)

    # Calculate % similarity
    match_pct = diff.ratio() * 100

    results = {
        "word_count": len(summary.split()),        
        "similarity": round(match_pct, 1)
    }

    return results
