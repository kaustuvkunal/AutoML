# AutoML
Bots to Auto generate Baseline DataScience Model Notebook

## Introduction 
The phases of Data Science modeling process is largely fixed. 

Stage of Data Science Modeling process 
1. Fetch Dataset 
2. Data Explore 
3. Data Cleanup and Feature Engineering 
4. Data Modeling 
5. Advance Modeling  (voting/stacking/blending)
6. Final Prediction  

Our bot auto generates notebook code for these phases for provided problem data configuration 

## Salient features 
- Generates Model for both learning type Regression & Classification 
- Performs basic Hyperparameter tuninng of all generated models  
- Provides Model-Leaderboard for model evaluation 
- Covers wide range of Models ( trains data  on total 13 model that includes  5 base models,  2 bagging models, 3 boosting models,  2 voting and  1 stacking model). 
- Automates all generic steps hence saves Time  
- Gives an idea of which model to choose for model
- 

## Project Modules 

1.  automl_bot_local_notebook : AutoGenerate jupyter notebook on local machine

Usage Instruction : Provide/update following configuration parameter inside automl_bot_local_notebook/runconfig.py and execute

"_TRAIN_FILE" ->  Name of training dataset file
"_TEST_FILE" ->  Name of test dataset file
"_EXT" -> Dataset file type extension, currently supports csv and xlsx 
_DATASET_FOLDER_PATH" -> Absolute path of folder where test and train files are present
_TARGET_COL" ->  Name of target feature to be predicted
"_ID_COL" ->  Nmae of unique id column or column which will exist inside final submission file 
"_METRIC" ->  evaluation metric name (as per sklearn library)
"_TYPE"  -> Learning type either regression  or classification
		  

2.  automl_bot_kaggle_kernel : Autogenerates kaggle kernel 

Usage Instruction : 

Update your  kaggle id under id (in line 17) of kaggle_bot.py and provide/update following configuration parameter inside automl_bot_kaggle_kernel/runconfig.py and execute

"_COMPETITION" >  Kaggle competition name
"_TARGET_COL" ->  Feature to be predicted
"_ID_COL" -> Unique id column or column which will exist inside final submission file
"_NAME" -> Name of kaggle kernel  the bot is generating 
"_METRIC" ->  evaluation metric
"_TYPE" ->  Learning type either regression  or classification
"_TEST_FILE" ->  Test File name ( if other than test)
"_TRAIN_FILE" -> Training file name ( if other than train)


             

3.  automl_bot_google_colab : Autogenerates google colab notebook
 
  Usage instruction 



## Future work 
- Automate Deep learning models e.g. image processing
- NLP i.e support for text features
- Optimization 

## References :
-  
