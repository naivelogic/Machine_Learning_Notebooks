# Machine_Learning_Notebooks

![alt text](https://cdn-images-1.medium.com/max/1600/1*ZGf62foEavtwM0SVo5lYXg.jpeg)

Welcome to my collection of Data Science and Machine Learning Notebooks in Python. 

> as of Oct. 2018, I am taking a more statistical inferntial focus on applying ML to various datasets. 

__Data Science Laboratories__
- [x] LAB1 - **Multiple Linear Regression**


__Kaggle__
* [x] [Kobe Shooting Prediction](https://github.com/naivelogic/Machine_Learning_Notebooks/tree/master/kaggle/kobe)  | [notebook](https://naivelogic.github.io/Machine_Learning_Notebooks/kaggle/kobe/Kobe%20Capstone%20EDA%20and%20Modeling.html) | score: 0.748 8/19


### Setup Environment

```
wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
sh Anaconda3-2019.10-Linux-x86_64.sh
rm Anaconda3-2019.10-Linux-x86_64.sh
source ~/anaconda3/bin/activate


conda create -n stats python=3.7
source activate stats
conda install pandas matplotlib jupyter notebook scipy scikit-learn nb_conda seaborn
```

New Cusotm Jupyter Kernel

```
pip install --user ipykernel
python -m ipykernel install --user --name=stats
```
