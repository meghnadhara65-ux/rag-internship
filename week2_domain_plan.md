# Project Title: BanglarSafar - West Bengal Tourism AI Assistant

## 1. Target User
The target users are independent travelers, backpackers, family vacationers, and students looking to explore the diverse geographic circuits of West Bengal (including the North Bengal hills, the Sundarbans mangrove forests, historical plains, and coastal beaches). These users look for quick, accurate lookup information regarding destination highlights, local transport logistics, and official government tourism protocols.

## 2. Problem Statement
Planning travel across West Bengal often requires navigating multiple fragmented sources, heavy long-form travel brochures, and complex government notices. Traditional search engines return overwhelming blog results that require tedious filtering. This chatbot solves the problem by serving as a single, unified Retrieval-Augmented Generation (RAG) assistant that extracts exact, verified context from structured tourism files to answer localized logistics, cultural rules, and itinerary timelines instantly.

## 3. Knowledge Sources (Documents to be Used)
The RAG pipeline will ingest the following 3 public-domain text documents placed inside `data/raw_documents/`:
1. `wbtdcl_handbook.txt`: Official guide detailing West Bengal Tourism Development Corporation Limited rules, booking policies, guidelines, and helpline contacts.
2. `kolkata_sundarbans_guide.md`: Structured destination guide covering historical landmarks in Kolkata (e.g., Victoria Memorial), transit pathways, and safaris in the Sundarbans Tiger Reserve.
3. `north_bengal_hills_itineraries.pdf`: Document containing specific multi-day sightseeing circuits for Darjeeling, Kalimpong, and the Dooars wildlife zones.

## 4. Expected Evaluation Dataset (10 Baseline Questions)
The system's retrieval and parsing accuracy will be stress-tested using these 10 targeted easy questions:

### Category A: Direct Geography & Attractions
1. What are the major tourist attractions to visit in Darjeeling?
2. In which district of West Bengal is the Jaldapara National Park located?
3. What is the best time of the year to visit the Sundarbans Mangrove Forest?
4. Name three popular beaches located in the coastal tourism circuit of West Bengal.

### Category B: Culture & Festivals
5. Which major annual festival celebrated in West Bengal is recognized as an UNESCO Intangible Cultural Heritage?
6. In which town is the famous Visva-Bharati University, founded by Rabindranath Tagore, located?
7. What traditional art and terracotta temples is the town of Bishnupur famous for?

### Category C: Simple Logistics & WBTDCL Rules
8. What is the official helpline number for the West Bengal Tourism Development Corporation Limited (WBTDCL)?
9. What standard photo ID cards are mandatory for tourists to carry when boarding a WBTDCL package tour?
10. What are the operational timings and weekly closing day for the Victoria Memorial Hall in Kolkata?

## 5. Out-of-Scope Queries (What the System Should NOT Answer)
To ensure safety and guardrails, the chatbot will use prompt-engineering to decline queries falling under these categories:
*   Real-time booking transactions, train/flight PNR status checks, or live seat availability modifications.
*   Personal financial transactions or gathering sensitive user identity records.
*   General political history or generic Indian topics outside the geographical and operational bounds of West Bengal Tourism.

## 6. Success Criteria
The RAG pipeline initialization for Week 2 will be deemed successful if:
*   **Data Layout Completeness:** The repository matches the requested layout (`data/raw_documents/`, `src/`, `notebooks/`) exactly.
*   **Retrieval Target Accuracy:** For all 10 baseline questions, the retrieval engine successfully surfaces the exact text chunk containing the ground truth fact inside the top-3 results.
*   **Hallucination Prevention:** The LLM cleanly relies on the extracted context and answers "I cannot find this information in the provided documents" for out-of-scope or missing queries, rather than guessing data.