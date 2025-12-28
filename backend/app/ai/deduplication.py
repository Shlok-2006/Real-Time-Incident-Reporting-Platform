from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")
SIMILARITY_THRESHOLD = 0.82

def check_duplicate(new_text: str, existing_texts: list[str]):
    if not existing_texts:
        return False, 0.0

    new_embedding = model.encode(new_text, convert_to_tensor=True)
    existing_embeddings = model.encode(existing_texts, convert_to_tensor=True)

    similarities = util.cos_sim(new_embedding, existing_embeddings)[0]
    max_similarity = similarities.max().item()

    return max_similarity >= SIMILARITY_THRESHOLD, round(max_similarity, 2)
