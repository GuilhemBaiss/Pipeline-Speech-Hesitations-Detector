from train_models_new_dataset.functions_dataset_models import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_predict
import pickle

def mainDecisionTree(path_dataset, path_to_models, criterion):

    x_train, x_test, y_train, y_test = Dataset.get_data(path_dataset)

    model = DecisionTreeClassifier(criterion=criterion)
    model = model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("accuracy decision_tree_model : {}".format(accuracy))
    with open(os.path.join(path_to_models, "decision_tree_model.pickle"), "wb") as f:
        pickle.dump(model, f)

    Functions.write_accuracy_score_text_file(path_to_models, "decision_tree_model", accuracy)


#confusion matrix

# get_confusion_matrix(path_dataset, model, x_test, y_test,
#                     title = 'Confusion matrix, without normalization')

