from train_models_new_dataset.functions_dataset_models import *
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
import pickle

def mainRandomForestClassifier(path_dataset, path_to_models, number_of_trees, max_features):
    
    # Create the model
    model = RandomForestClassifier(n_estimators=number_of_trees, 
                                bootstrap = True,
                                max_features = max_features)

    # Fit on training data
    x_train, x_test, y_train, y_test = Dataset.get_data(path_dataset)
    model.fit(x_train, y_train)

    # Probabilities for each class
    rf_probs = model.predict_proba(x_test)[:, 1]

    # Calculate roc auc
    accuracy = roc_auc_score(y_test, rf_probs)

    print("accuracy random_forest_model : {}".format(accuracy))

    with open(os.path.join(path_to_models,"random_forest_model.pickle"), "wb") as f:
        pickle.dump(model, f)

    Functions.write_accuracy_score_text_file(path_to_models, "random_forest_model", accuracy)


    #confusion matrix

    # get_confusion_matrix(path_dataset, model, x_test, y_test,
    #                     title = 'Confusion matrix, without normalization')
