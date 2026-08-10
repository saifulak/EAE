EAE — Machine Learning Course Materials
This repository contains course notebooks, exercises, and datasets for a
machine learning training course (EAE). It includes the instructor's
solution-copy (SC) notebooks alongside student exercise submissions.
Structure
```
.
├── SC/                     # Instructor "solution copy" course notebooks
├── Excercise/ML Exercise/  # Student exercise submissions
├── Data/                   # Datasets used across the course
└── images/                 # Diagrams and figures used in the notebooks
```
`SC/` — Course Notebooks
File	Topic
`ML00_Intro_to_ML.pdf`	Course introduction
`ML01_Linear_Regression_SC.ipynb`	Simple and multidimensional linear regression, feature scaling, categorical predictors, polynomial basis functions
`ML02_Classification_SC.ipynb`	k-Nearest Neighbours, decision trees, logistic regression
`ML03a_Validation_metrics_SC.ipynb`	Confusion matrix, precision/recall/F1, SVM, model comparison
`ML03b_CrossValidation_HyperParameterTuning_SC.ipynb`	Cross-validation and grid search
`Data/`
Datasets used in the course notebooks and exercises:
`Advertising.csv` — used in the linear regression module
`breast_cancer_wisconsin.csv` — used in the classification module
`iris.csv` — classic classification dataset
`insurance.csv`
`indian_liver_patient.csv`
`mobile_price_train.csv`
`fruit_data_with_colors.txt`
`Excercise/ML Exercise/`
Student submissions completing the course exercises (primarily the
cross-validation / hyperparameter tuning exercise from `ML03b`, plus a few
linear regression, logistic regression, and SVM exercises). Includes its own
`data/` subfolder with additional datasets used by some submissions
(customer churn, housing prices, manufacturing quality).
`images/`
Diagrams and figures referenced by the course notebooks (bias-variance
tradeoff, decision trees, KNN, PCA, neural networks, confusion matrices,
etc.).
Usage
The notebooks are standard Jupyter notebooks (`.ipynb`) built around
`scikit-learn`. Open them with Jupyter Notebook/Lab, or any compatible
editor, and run cells in order — each notebook loads its dataset from the
`Data/` directory using a relative path.
