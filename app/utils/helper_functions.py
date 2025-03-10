

PROMPT_LIMIT = 3750

def chunk_text(text, chunk_size = 200):
    sentences = text.split('. ')
    chunks = []
    curr_chunk = ""
    for sentence in sentences:
        if len(curr_chunk) + len(sentence) <= chunk_size:
            curr_chunk += sentence + '. '
        else:
            chunks.append(curr_chunk)
            curr_chunk = sentence + '. '
    if curr_chunk:
        chunks.append(curr_chunk)
    return chunks

def build_prompt(query,context_chunks):
    prompt_start = (
        "Answer the question based on the context below. If you don't know the answer based on the context provided below, just respond with 'I don't know' instead of making up an answer. Return just the answer to the question, don't add anything else. Don't start your response with the word 'Answer:'. Make sure your response is in markdown format\n\n"+
        "Context:\n")
    prompt_end = (
        f"\n\nQuestion: {query}\nAnswer:")

    prompt = ""
    for i in range(1, len(context_chunks)):
        if len("\n\n---\n\n".join(context_chunks[:i])) >= PROMPT_LIMIT:
            prompt = (
                prompt_start +
                "\n\n---\n\n".join(context_chunks[:i-1]) +
                prompt_end
            )
            break
        elif i == len(context_chunks)-1:
            prompt = (
                prompt_start +
                "\n\n---\n\n".join(context_chunks) +
                prompt_end
            )
    return prompt
