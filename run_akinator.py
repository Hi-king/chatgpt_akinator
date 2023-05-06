import llmakinator
import fire
import pickle

def main(classifier: str):
    print(classifier)
    classifier_model = pickle.load(open(classifier, "rb"))
    print(classifier_model)
    llmakinator.akinator.run(classifier=classifier_model)

if __name__ == '__main__':
    fire.Fire(main)