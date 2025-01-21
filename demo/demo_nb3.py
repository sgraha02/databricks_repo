# Databricks notebook source
from datetime import datetime, date, time

# COMMAND ----------

date.weekday(date.today())

# COMMAND ----------

if date.weekday(date.today()) == 1:
    print("It's Monday")
else:
    print("It's not Monday")

# COMMAND ----------


