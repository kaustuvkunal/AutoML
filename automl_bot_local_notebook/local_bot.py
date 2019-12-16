"""

localbot : A bot to auto generate jupyter notebook for ML model solution of variously Ml problems
with learning type Regression* and Classification

__author__ = "Kaustuv Kunal"
__email__  = "kaustuv.kunal@gmail.com"
"""
#from __future__ import print


import runipy
import os
import sys
import subprocess
import nbformat as nbf
import json
import random
from nbconvert.preprocessors import ExecutePreprocessor

class LocalBot():

	## initialize the notebook parameters
	def __init__(self, config):
		self.nb = nbf.v4.new_notebook()
		self.nb['cells'] = []
		self.config = config
		self.template_meta = 'templates/'+self.config['_TYPE']+'/'



		# do you need it or self.config = config will take care of this ?
		# if "_TRAIN_FILE" not in self.config:
		# 	self.config["_TRAIN_FILE"] = "train"
		# if "_TEST_FILE" not in self.config:
		# 	self.config["_TEST_FILE"] = "test"

	def _cleanup(self, string):
		string = string.replace("<text>", "").replace("</text>", "")
		string = string.replace("<code>", "").replace("</code>", "")
		return string.strip()




	def _prepare(self):

		for filename in sorted(os.listdir(self.template_meta)):
			if filename.startswith("."):
				continue

			content = open(self.template_meta + filename).read()
			for key, value in self.config.items():
				if key.startswith("_"):
					content = content.replace("<" + key + ">", value)

			txt = ""
			code = ""
			flag = 0  # by deafult its text

			for j, line in enumerate(content.split("\n")):
				if line.startswith("<text>"):
					flag = 0
				if line.startswith("<code>"):
					flag = 1
				if (flag == 0):
					txt += "\n"
					txt += line
				if (flag == 1):
					code += "\n"
					code += line

				if line.startswith("</code>"):
					code = self._cleanup(code)
					self.nb['cells'].append(nbf.v4.new_code_cell(code))
					code = ""
				if line.startswith("</text>"):
					txt = self._cleanup(txt)
					self.nb['cells'].append(nbf.v4.new_markdown_cell(txt))
					txt = ""




	def _execute(self ,outname ='out'):
		nbf.write(self.nb, 'notebook/'+outname+'.ipynb')
		# ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
		# ep.preprocess(self.nb, {'metadata': {'path': 'localbot/'}})
