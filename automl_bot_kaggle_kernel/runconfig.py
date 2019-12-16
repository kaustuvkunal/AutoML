from automl_bot_kaggle_kernal.kaggle_bot import KaggleBot

config = {
			"_COMPETITION" : "predict-the-housing-price",
            "_TARGET_COL" : "SalePrice",
            "_ID_COL" : "Id",
            "_NAME": "InClass-HousePrice",
            "_METRIC" : "neg_mean_squared_error",
		   "_TYPE" : "regression",
            "_TEST_FILE":"Test"
              }

plxy = KaggleBot(config)
plxy._prepare() # prepare the kernel
plxy._push() # push the kernel on kaggle




