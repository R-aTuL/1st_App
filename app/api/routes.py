from . import api_blueprint
from flask import request, jsonify
from app.services import openai_service, pinecone_service, scraping_service
from app.utils.helper_functions import chunk_text, build_prompt

PINECONE_INDEX_NAME = "index237"

@api_blueprint.route('/handle-query',methods=['POST'])
def handle_query():
    question = request.json.get('question')
    context_chunks = pinecone_service.get_similar_context_chunks(question, PINECONE_INDEX_NAME)
    context = ' '.join(context_chunks)
    prompt = build_prompt(question, context)
    print("/n=====PROMPT=====/n", prompt)
    answer = openai_service.get_llm_answer(prompt)
    return jsonify({"question": question, "answer": answer})


@api_blueprint.route('/embed-store',methods=['POST'])
def embed_store():
    print("test_1")
    print(request.json)
    data = request.json
    url = data['url']
    print("test_2")
    url_text = scraping_service.scrape_webpage(url)
    chunks = chunk_text(url_text)
    pinecone_service.embed_chunks_to_pinecone(chunks,PINECONE_INDEX_NAME)
    response_json = {
        "message": "Chunks embedded and stored successfully"
        }
    return jsonify(response_json)


@api_blueprint.route('/delete_index',methods=['POST'])
def delete_index():
    pinecone_service.delete_index(PINECONE_INDEX_NAME)
    
    return jsonify({"message": f"Index {PINECONE_INDEX_NAME} deleted successfully"})
