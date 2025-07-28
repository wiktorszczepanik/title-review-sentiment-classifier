import pickle

class TRSClassifier:

    def __init__(self, vectorizer_path, model_path):
        self.vectorizer_path = vectorizer_path
        self.model_path = model_path
        self.vectorizer = None
        self.model = None


    def load_pickles(self) -> None:

        with open(self.vectorizer_path, 'rb') as file:
            self.vectorizer = pickle.load(file)

        with open(self.model_path, 'rb') as file:
            self.model = pickle.load(file)


    def get_types(self) -> str:
        return f"\nVectorizer type: {type(self.vectorizer)}\nClassifier type: {type(self.model)}\n"


    def prediction(self, review: str) -> str:
        transformed_review = self.vectorizer.transform([review])
        state = self.model.predict(transformed_review)
        return 'Positive' if state else 'Negative'