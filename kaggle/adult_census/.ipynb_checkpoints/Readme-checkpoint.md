
![](https://unitedwaynca.org/wp-content/uploads/2019/04/Census-2020-0411.png)

### Best Parameters
The parameters for each model's grid search are as follows:

```python
LogisticRegression {'C': 10, 'solver': 'sag'}
SVM {'C': 1, 'kernel': 'linear'}
RandomForestClassifier {'max_depth': 10, 'n_estimators': 100}
XGBClassifier {'learning_rate': 0.1, 'max_depth': 7, 'objective': 'binary:logistic'}
KNeighborsClassifier {'metric': 'manhattan', 'n_neighbors': 21, 'weights': 'uniform'}
BernoulliNB {'alpha': 1.0, 'fit_prior': True} 
DecisionTreeClassifier TBD
LGBMClassifier TBD
GradientBoostingClassifier TBD
```

![](./03_Classifiers/Predicting_Income_ALL_ROC.png)


Model|TrainAccuracy|TestAccuracy|Recall Rate|F1-score|AUC value|ROC Curve
---|------|-----|-----|-----|-----|------
LogisticRegression|0.7126839523475823|0.6850815832576967|0.44930417495029823|0.6295264623955432|0.5243619489559165|![LogisticRegression](./03_Classifiers/predicting_income_results/LogisticRegression_ROC.png)    
RandomForestClassifier|0.7792571829011913 |0.6195306876154111 |0.6294117647058823 |0.298050139275766 |0.4045368620037807|![RandomForestClassifier](./03_Classifiers/predicting_income_results/RandomForestClassifer_ROC.png)
XGBClassifier| 0.7855641205325858 |0.6339146922892345| 0.644808743169399 |0.3286908077994429 |0.4354243542435425|![XGBClassifier](./03_Classifiers/XGBClassifier_ROC.png)
BernoulliNB|0.7729502452697968 |0.6106942401385455| 0.6035502958579881 |0.2841225626740947 |0.3863636363636364|![BernoulliNB](./03_Classifiers/predicting_income_results/BernoulliNB_ROC.png)
SVM||||||![SVM]()
GradientBoostingClassifierSVM||||||![GradientBoostingClassifier]()
DecisionTreeClassifierSVM||||||![DecisionTreeClassifier]()