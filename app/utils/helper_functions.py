
PROMPT_LIMIT = 3750  # Ollama has no strict limit, but keeping it to avoid excessive context length

def chunk_text(text, chunk_size=150):
    sentences = text.split('. ')
    chunks = []
    curr_chunk = ""
    
    for sentence in sentences:
        if len(curr_chunk) + len(sentence) <= chunk_size:
            curr_chunk += sentence + '. '
        else:
            chunks.append(curr_chunk.strip())
            curr_chunk = sentence + '. '

    if curr_chunk:
        chunks.append(curr_chunk.strip())

    return chunks

def build_prompt(query, context_chunks):
    final_prompt = f"""Use the following webpage content to answer the questions.
    Webpage content:{context_chunks}
    Question: {query}
    Answer:"""
    return final_prompt


