from flask import Flask, request, jsonify, render_template
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
import json

app = Flask(__name__)

class Indexer:
    def __init__(self, documents):
        self.documents = documents
        self.vectorizer = CountVectorizer(stop_words='english')
        self.term_matrix = self.vectorizer.fit_transform(self.documents)
        self.transformer = TfidfTransformer()
        self.tfidf_matrix = self.transformer.fit_transform(self.term_matrix)

    def search(self, query, top_k=5):
        query_term_matrix = self.vectorizer.transform([query])
        query_tfidf_matrix = self.transformer.transform(query_term_matrix)
        cosine_similarities = cosine_similarity(query_tfidf_matrix, self.tfidf_matrix)
        scores = list(cosine_similarities[0])

        result = []
        for i, score in enumerate(scores):
            if score > 0:
                result.append({'title': self.documents[i].split('\n')[0], 'plot': self.documents[i].split('\n')[1], 'cosine_similarity_score': score})

        # Sort by cosine similarity score
        result.sort(key=lambda x: x['cosine_similarity_score'], reverse=True)

        # Return top-K results
        return result[:top_k]

def load_documents_from_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = f.read()
    # Parse JSON data
    json_data = json.loads(data)
    # Extract text content from each entry, handling None values
    documents = []
    for entry in json_data:
        title = entry.get('title', 'N/A')
        plot = entry.get('plot', 'N/A')
        transcript = entry.get('transcript', 'N/A')
        text = f"{title}\n{plot}\n{transcript}"
        documents.append(text)
    return documents

# Path to your output.json file
json_file = '../output.json'

# Load documents from JSON file
documents = load_documents_from_json(json_file)

# Initialize the indexer
indexer = Indexer(documents)

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    req_data = request.get_json()

    # Check if 'query' is present in the request
    if 'query' not in req_data:
        return jsonify({'error': 'Query parameter missing in JSON'}), 400

    query = req_data['query']

    # Perform search
    results = indexer.search(query)

    # Check if any results found
    if not results:
        return jsonify({'message': 'No matching products found'}), 404

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
