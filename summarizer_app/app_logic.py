import requests

API_TOKEN = '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'

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload, max_length=130, min_length=30):
    payload["parameters"] = {
        "max_length": max_length,
        "min_length": min_length
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
	
input = "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct."

max_length = 20
min_length = 10

output = query({
    "inputs": input
}, max_length=max_length, min_length=min_length)

print (output)








# summarizer = pipeline("summarization", model="facebook/bart-large-cnn", min_length=60)

# def summarize(text, length=None):
#     """
#     Summarize input text
#     """
#     if length:
#         # Truncate summary if length provided
#         summary = summarizer(text, max_length=length, min_length=60)[0]['summary_text']   
#     else:
#         # Default summarization
#         summary = summarizer(text)[0]['summary_text']

#     return summary


# def analyze_summary(original, summary):
#     """
#     Analyze the similarity between original text 
#     and generated summary
#     """
#     import difflib
#     diff = difflib.SequenceMatcher(None, original, summary)

#     # Calculate % similarity
#     match_pct = diff.ratio() * 100

#     results = {
#         "word_count": len(summary.split()),        
#         "similarity": round(match_pct, 1)
#     }

#     return results
