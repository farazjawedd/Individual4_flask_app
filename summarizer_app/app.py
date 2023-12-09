from claude import Claude

claude = Claude()

text = "Your text to summarize"

summary = claude.summarize(text)
print(summary)