import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the lightweight local embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# ==========================================
# ASSIGNMENT 1: Embeddings Creation
# ==========================================
print("--- TASK 1: EMBEDDING CREATION ---")

# 5 representative chunks from the West Bengal Tourism domain
chunks = [
    "WBTDCL Helpline & Support: The official West Bengal Tourism Development Corporation Limited hotline operates 24/7 at 1800-212-1655 for tourist assistance and emergency inquiries.",
    "Jaldapara Wildlife: Jaldapara National Park is situated in the Alipurduar district of northern West Bengal and is famous for its thriving population of the Great Indian One-Horned Rhinoceros.",
    "Victoria Memorial Rules: The Victoria Memorial Hall museum grounds in Kolkata are open from 10:00 AM to 6:00 PM, closed on Mondays. The entry ticket fee for Indian citizens is ₹50.",
    "WBTDCL Booking Documents: All travelers booking WBTDCL package tours must present valid government photo identification, such as Aadhaar Card, Passport, or Voter ID card, prior to departure.",
    "Sundarbans 2-Night Itinerary: Day 1 includes transfer from Kolkata to Godkhali boat jetty and evening watchtower visits. Day 2 covers deep mangrove boat safaris across Sudhanyakhali and Dobanki watchtowers."
]

# Generate chunk embeddings
chunk_embeddings = model.encode(chunks)

print(f"Total Chunks Processed: {len(chunks)}")
print(f"Embedding Dimension Size: {len(chunk_embeddings[0])}\n")


# ==========================================
# ASSIGNMENT 2: Top Chunk Retrieval
# ==========================================
print("--- TASK 2: QUERY RETRIEVAL (TOP CHUNK) ---")

user_questions = [
    "How can I contact the West Bengal tourism department helpline for emergencies?",
    "Where is Jaldapara National Park located and what animal is it known for?",
    "What are the ticket prices and visiting hours for Victoria Memorial?",
    "Which photo ID proof is required to join a government WBTDCL tour?",
    "Can you give me a schedule for a 2-day mangrove safari in Sundarbans?"
]

# Generate query embeddings and compute cosine similarity
query_embeddings = model.encode(user_questions)

for i, (q, q_emb) in enumerate(zip(user_questions, query_embeddings), 1):
    # Reshape query embedding to 2D array for sklearn comparison
    scores = cosine_similarity([q_emb], chunk_embeddings)[0]
    best_index = int(np.argmax(scores))
    best_score = float(scores[best_index])
    
    print(f"Q{i}: {q}")
    print(f"   -> Top Retrieved Chunk [{best_index + 1}]: \"{chunks[best_index]}\"")
    print(f"   -> Cosine Similarity Score: {best_score:.4f}\n")


# ==========================================
# ASSIGNMENT 3: Semantic vs. Keyword Search
# ==========================================
print("--- TASK 3: SEMANTIC VS KEYWORD COMPARISON ---")

comparison_examples = [
    {
        "query": "Who do I call if I get lost or need urgent help during my Bengal trip?",
        "keyword_fail_reason": "The query uses terms like 'call', 'get lost', 'urgent help', whereas the source document uses 'Hotline', '24/7', 'Helpline', and 'Emergency inquiries'. Keyword search fails because zero words match, but semantic search maps the intent of 'calling for urgent help' to '24/7 hotline assistance'."
    },
    {
        "query": "What identity cards must I carry to board the official sight-seeing bus?",
        "keyword_fail_reason": "The query asks for 'identity cards' and 'sight-seeing bus', while the text contains 'photo identification' and 'package tours'. Keyword matching misses the match completely, whereas semantic search understands that 'identity cards' and 'photo identification' share the exact same context."
    }
]

for i, example in enumerate(comparison_examples, 1):
    print(f"Example {i}:")
    print(f"Query: \"{example['query']}\"")
    print(f"Explanation: {example['keyword_fail_reason']}\n")