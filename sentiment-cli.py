from load.model import TRSClassifier
from load.constants import VECTORIZER_FILE_PATH, CLASSIFIER_FILE_PATH

classifier = TRSClassifier(VECTORIZER_FILE_PATH, CLASSIFIER_FILE_PATH)
classifier.load_pickles()
print(f"\nLoaded models:\n{classifier.get_types()}")

try:
    while True:
        review = input(">>> ")
        state = classifier.prediction(review)
        print(state)
except KeyboardInterrupt:
    print("\n\nExiting...\n")