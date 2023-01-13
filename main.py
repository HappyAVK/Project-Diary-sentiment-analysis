import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import glob
analyzer = SentimentIntensityAnalyzer()

path = glob.glob("diary/*.txt")

def word_analysis(e):
    scores = analyzer(e)
    return scores


def diary_compile(p):
    entries = {}
    emotional_range = []
    for d in p:
        with open(d, 'r') as file:
            content = file.read()
            date = d.translate({ord(i): None for i in '.txt diary\\'})
            entries[date] = content.replace('/n', '')


    for journals in entries.items():
        scores = analyzer.polarity_scores(journals[1])
        emotional_range.append(scores)

    return entries, emotional_range


if __name__ == "__main__":
    e, r = diary_compile(path)
    print(len(r))

