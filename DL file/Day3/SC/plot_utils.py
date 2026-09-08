
import numpy as np
import seaborn as sns


import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (6, 6)
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']


import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import confusion_matrix


def compareValLoss(history1, history2, label1, label2):
    hist1 = history1.history
    hist2 = history2.history

    val_loss1 = hist1['val_loss']
    val_loss2 = hist2['val_loss']

    epochs = range(1, len(val_loss1) + 1)

    plt.plot(epochs, val_loss1, 'b')
    plt.plot(epochs, val_loss1,'bo', label= label1)

    plt.plot(epochs, val_loss2, 'r')
    plt.plot(epochs, val_loss2, 'r+', label=label2)

    plt.title('Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()


def compareValAcc(history1, history2, label1, label2):
    hist1 = history1.history
    hist2 = history2.history

    val_acc1 = hist1['val_accuracy']
    val_acc2 = hist2['val_accuracy']

    epochs = range(1, len(val_acc1) + 1)

    plt.plot(epochs, val_acc1, 'b')
    plt.plot(epochs, val_acc1,'bo', label= label1)

    plt.plot(epochs, val_acc2, 'r')
    plt.plot(epochs, val_acc2, 'r+', label=label2)

    plt.title('Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()



def plot_metrics(history):
    metrics =  ['loss', 'auc', 'precision', 'recall']
    for n, metric in enumerate(metrics):
        name = metric.replace("_"," ").capitalize()
        plt.subplot(2,2,n+1)
        plt.plot(history.epoch,  history.history[metric], color=colors[0], label='Train')
        plt.plot(history.epoch, history.history['val_'+metric],
                 color=colors[0], linestyle="--", label='Val')
        plt.xlabel('Epoch')
        plt.ylabel(name)

        plt.legend()



def plot_cm(labels, predictions, p=0.5):
    cm = confusion_matrix(labels, predictions > p)
    plt.figure(figsize=(5,5))
    sns.heatmap(cm, annot=True, fmt="d")
    plt.title('Confusion matrix @{:.2f}'.format(p))
    plt.ylabel('Actual label')
    plt.xlabel('Predicted label')

    print('Correctly Labeled as Retained (True Negatives): ', cm[0][0])
    print('Incorrectly Labeled as Churn (False Positives): ', cm[0][1])
    print('Incorrectly Labeled as Retained (False Negatives): ', cm[1][0])
    print('Correctly Labeled as Churn (True Positives): ', cm[1][1])
    print('Total Churn Transaction: ', np.sum(cm[1]))


def plot_roc(name, labels, predictions, **kwargs):
    fp, tp, _ = sklearn.metrics.roc_curve(labels, predictions)
    plt.plot(100*fp, 100*tp, label=name, linewidth=2, **kwargs)
    plt.xlabel('False positives [%]')
    plt.ylabel('True positives [%]')
    plt.grid(True)
    ax = plt.gca()
    ax.set_aspect('equal')

#############################

def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array, true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array, true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)
    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


def plotLoss(history, title, label1, label2):
    hist = history.history
    loss = hist['loss']
    val_loss = hist['val_loss']
    epochs = range(1, len(val_loss) + 1)

    plt.plot(epochs, loss, 'bo', label=label1)
    plt.plot(epochs, loss, c= 'b')

    plt.plot(epochs, val_loss,'r+', label=label2)
    plt.plot(epochs, val_loss,c= 'r')

    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title(title)
    plt.legend()
    plt.show()
    
    
def plotAccuracy(history, title, label1, label2):
    hist = history.history
    acc = hist['accuracy']
    val_acc = hist['val_accuracy']
    epochs = range(1, len(val_acc) + 1)

    plt.plot(epochs, acc, 'bo', label=label1)
    plt.plot(epochs, acc, c= 'b')

    plt.plot(epochs, val_acc,'r+', label=label2)
    plt.plot(epochs, val_acc,c= 'r')

    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.title(title)
    plt.legend()
    plt.show()
