from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

CLASSIFIER_FILE_PATH = BASE_DIR / 'models' / 'logistic_regression_classifier.pkl'
VECTORIZER_FILE_PATH = BASE_DIR / 'models' / 'count_vectorizer.pkl'
