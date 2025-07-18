
from . import api_blueprint
from flask import request, jsonify
from app.services import ollama_service, pinecone_service, scraping_service
from app.utils.helper_functions import chunk_text, build_prompt

PINECONE_INDEX_NAME = "index237"

@api_blueprint.route('/handle-query', methods=['POST'])
def handle_query():
    data = request.json
    if not data or 'question' not in data or 'url' not in data:
        return jsonify({"error": "Missing 'question' field"}), 400
    print(data)
    url = data['url']
    question = data['question']


    context_chunks = pinecone_service.get_similar_context_chunks(question, PINECONE_INDEX_NAME,url)

    context = "\n\n".join(context_chunks)
    final_prompt = build_prompt(context_chunks,question)

    answer = ollama_service.get_llm_answer(final_prompt)

    return jsonify({"question": question, "answer": answer})



@api_blueprint.route('/embed-store', methods=['POST'])
def embed_store():
    print("test_1")
    
    data = request.json
    if not data or 'url' not in data:
        return jsonify({"error": "Missing 'url' field"}), 400
    
    url = data['url']
    print("test_2")

    try:
        url_text = scraping_service.scrape_webpage(url)
        print(url_text[:1000])
        chunks = chunk_text(url_text)
        pinecone_service.embed_chunks_to_pinecone(chunks, PINECONE_INDEX_NAME,url)
        
        response_json = {"message": "Chunks embedded and stored successfully"}
        
        return jsonify(response_json)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api_blueprint.route('/delete-index', methods=['POST'])
def delete_index():
    try:
        pinecone_service.delete_index(PINECONE_INDEX_NAME)
        return jsonify({"message": f"Index {PINECONE_INDEX_NAME} deleted successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


