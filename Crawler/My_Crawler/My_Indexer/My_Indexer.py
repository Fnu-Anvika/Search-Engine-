import pickle
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from bs4 import BeautifulSoup

class Indexer:
    def __init__(self, filename):
        self.filename = filename
        self.documents = self._retrieve_documents()
        print("Retrieved documents:", self.documents)

        self.vectorizer = CountVectorizer(stop_words='english')
        self.term_matrix = self.vectorizer.fit_transform(self.documents)
        self.transformer = TfidfTransformer()
        self.tfidf_matrix = self.transformer.fit_transform(self.term_matrix)
        print("TF-IDF matrix shape:", self.tfidf_matrix.shape)

        self.inverted_index = self._build_inverted_index()

    def _retrieve_documents(self):
        documents = []
        with open(self.filename, 'r', encoding='latin-1') as f:
            html_content = f.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            book_entries = soup.find_all('body')
            for entry in book_entries:
                title = entry.find('h1').get_text(strip=True) if entry.find('h1') else "N/A"
                price = entry.find_all('p')[0].get_text(strip=True) if entry.find_all('p') else "N/A"
                availability = entry.find_all('p')[1].get_text(strip=True) if len(entry.find_all('p')) > 1 else "N/A"
                text = f"Title: {title}\nPrice: {price}\nAvailability: {availability}"
                documents.append(text)
        return documents

    def _build_inverted_index(self):
        inverted_index = {}
        terms = self.vectorizer.get_feature_names_out()
        for i, doc in enumerate(self.documents):
            for term in terms:
                if term in doc:
                    if term not in inverted_index:
                        inverted_index[term] = []
                    inverted_index[term].append(i)
        return inverted_index

    def save_index_to_pickle(self):
        inverted_index_pickle = pickle.dumps(self.inverted_index)
        with open('inverted_index.pkl', 'wb') as f:
            f.write(inverted_index_pickle)

    def load_index_from_pickle(self, filename):
        with open(filename, 'rb') as f:
            self.inverted_index = pickle.load(f)

    def calculate_cosine_similarity(self, query):
        query_vector = self.vectorizer.transform([query])
        cosine_similarities = cosine_similarity(query_vector, self.tfidf_matrix)
        scores = list(cosine_similarities[0])
        print("Cosine similarity scores:", scores)
        result = []
        for i, score in enumerate(scores):
            if score > 0 and i < len(self.documents):
                result.append((self.documents[i], score, self.tfidf_matrix[i]))
        return result

# Example usage
#filename = "C:\\Users\\91855\\OneDrive\\Desktop\\Final_IR\\Crawler\\My_Crawler\\all_pages.html"
filename = "../all_pages.html"

indexer = Indexer(filename)
indexer.save_index_to_pickle()

# Later, you can load the index and perform searches
indexer.load_index_from_pickle('inverted_index.pkl')
query = input("Enter your query: ")
indexer.calculate_cosine_similarity(query)
