import random
import time

def run(classifier):
    print(classifier)
    node = 0
    while True:
        threshold = classifier.tree_.threshold[node]
        right = ["はい"]
        left = ["いいえ"]
        if threshold >= 0:
            left.append("場合による")
        else:
            right.append("場合による")    
        
        print(
            classifier.feature_names_in_[classifier.tree_.feature[node]], 
        )
        choice = f'type 0 or 1 ... 0: {left}, 1: {right}'
        # print(choice)
        time.sleep(1)
        decision = int(input(choice))
        print(f'あなたの回答: {decision} {left if decision <= 0 else right}')
        node = classifier.tree_.children_left[node] if decision <= 0 else classifier.tree_.children_right[node]
        candidates = classifier.classes_[(classifier.tree_.value[node] == 1)[0]]
        if len(candidates) == 1:
            print(f'あなたが思い浮かべているのは {candidates[0]} です')
            break
        if len(candidates) > 5:
            print(f'候補: {random.choices(candidates, k=5)} など {len(candidates)}候補')
        else:
            print(f'候補: {candidates}')
        time.sleep(1)
        