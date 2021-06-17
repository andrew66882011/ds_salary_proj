#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 14:57:28 2021

@author: jjhua
"""

import glassdoor_scraper as gs
import pandas as pd

path = "/Users/jjhua/Desktop/Python for Data Science/ds_salary_proj/chromedriver"

df = gs.get_jobs("data scientist", 15, False, path, 15)
df.to_csv('glassdoor_jobs.csv', index = False)



