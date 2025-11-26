# # Backend/utils/semantic_matcher.py
# from sentence_transformers import SentenceTransformer
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity
#
# # Load lightweight model (change to a stronger one if you want)
# MODEL_NAME = "all-MiniLM-L6-v2"
# model = SentenceTransformer(MODEL_NAME)
#
# def embed_texts(texts):
#     """
#     texts: list of strings
#     returns: numpy array (n x dim)
#     """
#     return np.array(model.encode(texts, convert_to_numpy=True, show_progress_bar=False))
#
# def compute_scores(job_text, resumes_texts):
#     """
#     job_text: single string (job description)
#     resumes_texts: list of strings (each resume text)
#     returns: list of dicts with score (0-100) and cosine similarity
#     """
#     # create embeddings
#     all_texts = [job_text] + resumes_texts
#     embeddings = embed_texts(all_texts)
#     job_vec = embeddings[0].reshape(1, -1)
#     resume_vecs = embeddings[1:]
#
#     # cosine similarities
#     sims = cosine_similarity(job_vec, resume_vecs)[0]  # shape (n,)
#     # normalize to 0-100 (optional)
#     scores = (sims - sims.min()) / (sims.max() - sims.min() + 1e-9) * 100 if len(sims) > 1 else sims * 100
#     # If single resume, just convert
#     if len(sims) == 1:
#         scores = [float(sims[0] * 100)]
#
#     results = []
#     for i, s in enumerate(sims):
#         results.append({
#             "index": i,
#             "cosine": float(s),
#             "score": round(float(scores[i]), 2)
#         })
#     return results
