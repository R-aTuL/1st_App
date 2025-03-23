
PROMPT_LIMIT = 3750  # Ollama has no strict limit, but keeping it to avoid excessive context length

def chunk_text(text, chunk_size=200):
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
    """
    Constructs a prompt formatted for Ollama LLM.
    """
    prompt_start = (
        "Use the following context to answer the question. "
        "If the answer is not present in the context, reply with 'I don't know'. "
        "Return only the answer, without adding unnecessary explanations.\n\n"
        "### Context:\n"
    )
    
    prompt_end = f"\n\n### Question: {query}\n### Answer:"

    # Limit the number of context chunks if necessary
    selected_chunks = []
    total_length = 0

    for chunk in context_chunks:
        chunk_length = len(chunk)
        if total_length + chunk_length >= PROMPT_LIMIT:
            break
        selected_chunks.append(chunk)
        total_length += chunk_length

    context_text = "\n\n---\n\n".join(selected_chunks)

    return prompt_start + context_text + prompt_end

# PROMPT_LIMIT = 3750

