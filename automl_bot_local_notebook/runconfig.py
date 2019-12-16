from automl_bot_local_notebook.local_bot import LocalBot

config =  {"_TRAIN_FILE": "train",
		   "_TEST_FILE": "test",
		   "_EXT": "csv",
		   "_DATASET_FOLDER_PATH": "/Users/kaustuv/DataScience/DS_projects/AnalyticVidhya/Reg_BlackFridaySale/datasets/",
		   "_TARGET_COL": "User_ID",
		   "_ID_COL":"ID",
		   "_METRIC" : "neg_mean_squared_error",
		   "_TYPE" : "regression"
		   }

plxy = LocalBot(config)
plxy._prepare()
plxy._execute()