# -*- encoding: utf-8 -*-
"""
@author: acedar  
@time: 2024/7/27 18:35
@file: entity_anal.py 
"""

import pandas as pd

data_path = "../doupocangqiong/output/doupo/artifacts/create_final_documents.parquet"
df = pd.read_parquet(data_path)
df_json = df[:1].to_json(orient="records", force_ascii=False)
print("create_final_documents:", df_json)
print(len(df))


data_path = "../doupocangqiong/output/doupo/artifacts/create_final_text_units.parquet"
df = pd.read_parquet(data_path)
df_json = df[:1].to_json(orient="records", force_ascii=False)
print("create_base_text_units:", df_json)
print(len(df))


data_path = "../doupocangqiong/output/doupo/artifacts/create_final_entities.parquet"
df = pd.read_parquet(data_path)
df_json = df[:1].to_json(orient="records", force_ascii=False)
print("create_final_entities:", df_json)
print(len(df))


data_path = "../doupocangqiong/output/doupo/artifacts/create_final_relationships.parquet"
df = pd.read_parquet(data_path)
df_json = df[:1].to_json(orient="records", force_ascii=False)
print("create_final_relationships:", df_json)
print(len(df))


data_path = "../doupocangqiong/output/doupo/artifacts/create_final_nodes.parquet"
df = pd.read_parquet(data_path)
df_json = df[:1].to_json(orient="records", force_ascii=False)
print("create_final_nodes:", df_json)
print(len(df))


data_path = "../doupocangqiong/output/doupo/artifacts/create_final_communities.parquet"
df = pd.read_parquet(data_path)
df_json = df[:1].to_json(orient="records", force_ascii=False)
print("create_final_communities:", df_json)
print(len(df))

data_path = "../doupocangqiong/output/doupo/artifacts/create_final_community_reports.parquet"
df = pd.read_parquet(data_path)
df_json = df[:1].to_json(orient="records", force_ascii=False)
print("create_final_community_reports:", df_json)
print(len(df))
