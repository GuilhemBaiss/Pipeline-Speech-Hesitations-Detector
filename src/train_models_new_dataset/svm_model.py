from train_models_new_dataset.functions_dataset_models import *
from sklearn.svm import SVC
import pickle
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

def mainSVMModel(path_dataset, path_to_models, kernel):

    model = SVC(kernel= kernel)

    x_train, x_test, y_train, y_test = Dataset.get_data(path_dataset)

    print("fiting SVM Model ...")
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test, y_pred)

    with open(os.path.join(path_to_models, "svm_model.pickle"), "wb") as f:
        pickle.dump(model, f)

    print("accuracy svm_model : {}".format(accuracy))

    Functions.write_accuracy_score_text_file(path_to_models, "svm_model", accuracy)

    # get_confusion_matrix(path_dataset, model, x_test, y_test,
    #                     title = 'Confusion matrix, without normalization')
