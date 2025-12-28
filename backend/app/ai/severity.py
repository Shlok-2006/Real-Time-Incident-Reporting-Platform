from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def predict_severity(text: str):
    result = classifier(text)[0]
    score = result["score"]

    if score > 0.85:
        return "high", round(score, 2)
    elif score > 0.6:
        return "medium", round(score, 2)
    else:
        return "low", round(score, 2)
