# Big Data Learning Lab

This repository is a hands-on learning workspace for the foundations of Big Data processing with Python, Hadoop-style MapReduce, and Apache Spark. It is organized as a progression from small local examples to distributed data processing concepts, Spark SQL, streaming, and basic machine learning workflows.

The material is intentionally practical: most topics are represented as runnable Python scripts, mapper/reducer programs, Jupyter notebooks, or small datasets that can be used while learning.

## What This Repository Covers

- MapReduce fundamentals using pure Python.
- Generalized and parallel MapReduce patterns
- Hadoop Streaming-style mapper and reducer scripts
- Order/category counting examples with CSV input
- A small Olist payment-type MapReduce pipeline example
- Spark session basics and DataFrame operations
- RDD transformations, actions, and file processing
- Spark SQL filtering, sorting, aggregation, and grouping
- Spark MLlib regression and pipeline basics
- Spark Streaming concepts
- A delivery delay prediction mini-project using Spark ML

## Suggested Learning Path

1. Start with `Hadoop/001_word_count_mapReduce_func.py` to understand the map, shuffle, and reduce phases.
2. Move to `Hadoop/002_generalised_mapReduce_framework.py` to see how MapReduce can be expressed as reusable mapper and reducer functions.
3. Run `Hadoop/003_parallel_mapReduce.py` to connect the same idea with parallel execution.
4. Explore `Hadoop/mapreduce-jobs/`, `Hadoop/orders/`, and `Hadoop/olist_project/` to learn the mapper/reducer pattern used by Hadoop Streaming.
5. Open `Spark/1.Spark Basics.ipynb` and continue through the Spark notebooks in order.
6. Use `Spark/delivery_delay_pred/` as a small end-to-end Spark ML project that combines data generation, feature preparation, model training, and saved model output.

## Prerequisites

Recommended tools:

- Python 3.10+
- Jupyter Notebook or JupyterLab
- Apache Spark / PySpark
- Java, required by Spark
- Optional: Hadoop, if you want to run the mapper/reducer examples through Hadoop Streaming

Install the core Python dependency with:

```bash
python3 -m pip install pyspark jupyter pandas
```

Depending on your environment, Spark may also require `JAVA_HOME` to be configured.

## Running Examples

Run the pure Python MapReduce examples:

```bash
python3 Hadoop/001_word_count_mapReduce_func.py
python3 Hadoop/002_generalised_mapReduce_framework.py
python3 Hadoop/003_parallel_mapReduce.py
```

Run the basic streaming-style word count locally:

```bash
cat Hadoop/mapreduce-jobs/input.txt \
  | python3 Hadoop/mapreduce-jobs/mapper.py \
  | sort \
  | python3 Hadoop/mapreduce-jobs/reducer.py
```

Run the orders category count locally:

```bash
cat Hadoop/orders/orders.csv \
  | python3 Hadoop/orders/mapper.py \
  | sort \
  | python3 Hadoop/orders/reducer.py
```

Start Jupyter for the Spark notebooks:

```bash
jupyter notebook
```

Then open the notebooks under `Spark/` in numeric order.

## Notes For Learners

- The Hadoop examples focus on the logic behind MapReduce before introducing cluster tooling.
- The Spark notebooks are best studied in order because later notebooks assume familiarity with Spark sessions, DataFrames, RDDs, and SQL operations.
- The delivery delay project is useful for seeing how Spark ML pipelines organize feature engineering and model training.
- Saved Spark model directories can contain generated metadata and Parquet files. Regenerate them locally when needed instead of treating them as source code.

