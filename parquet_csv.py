import pyarrow.parquet as pq
import pandas as pd
import os
import time

parquet_filename = "fhvhv_tripdata_2020-03.parquet"
csv_filename = "fhvhv_tripdata_2020-03.csv"

start_time = time.time()
parquet_df = pq.ParquetFile(parquet_filename).read().to_pandas()
print(time.time() - start_time)
# 6.662230730056763

start_time = time.time()
csv_df = pd.read_csv(csv_filename)
print(time.time() - start_time)
# 53.7181191444397

# check file size
print("parquet", format(os.stat(parquet_filename).st_size, ","))
print("csv", format(os.stat(csv_filename).st_size, ","))
# parquet 346,478,514
# csv   2,203,226,784

print(parquet_df.info())
print(csv_df.info())
# memory usage: 2.4+ GB
# memory usage: 2.5+ GB