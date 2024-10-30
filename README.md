# Graph-RAG for Private Domain Knowledge Graph Generation


## Project Introduction

This project focuses on the use of Graph-RAG (Graph Retrieval-Augmented Generation) to generate knowledge graphs for private domain data, such as specific books or proprietary texts. It addresses several fundamental limitations of large language models (LLMs) in handling private or domain-specific content.

### Background
While large language models have demonstrated significant capabilities in general question-answering and language comprehension, they often face challenges when dealing with domain-specific or private content that falls outside of their training data. These models may lack the precision, accuracy, and contextual understanding needed for tasks involving specialized knowledge.

### Why Graph-RAG?
Graph-RAG presents a promising solution by integrating the structure and relevance of a knowledge graph with retrieval-augmented generation, creating a hybrid approach that leverages domain-specific data more effectively. Through Graph-RAG, this project can:
- Generate structured knowledge graphs from private data, capturing unique entities, relationships, and context.
- Improve the reasoning capability of LLMs by providing contextual data retrieval based on the generated knowledge graph.

### Project Overview
In this project, we apply Graph-RAG to private domain data (e.g., a specific book) to generate a domain-specific knowledge graph. The generated graph is then used to support LLM reasoning, enabling the model to respond to inquiries more accurately within the context of the given domain.

---

## Project Setup

### 1. Environment Setup
To begin, follow these steps to set up your environment:

- **Create a Conda virtual environment**  
- **Activate a Conda virtual environment**  
- **Install dependencies**  

```shell
# create conda virtual environment
conda create -n GraphRAG python=3.10

# activate conda virtual environment
conda activate GraphRAG

# install packets
pip install -r requirements.txt
```

### 2. Preparation for Running
Before running the project, complete the following:
- **Create testing directories**  
- **Transfer or prepare test data**  
- **Initialize the project**  
- **Configure model environment**

```shell
# create dictionary for test
mkdir -p ./RAGtest/input

# prepare test data
cp data/book.txt ./RAGtest/input/

# initialize the project
python -m graphrag.index --init --root ./RAGtest

# modify 'setting.yaml' and '.env' within dictionary
```

### 3. Index Construction

When constructing the knowledge graph index, it's essential to use the --resume parameter to avoid redoing indexing after any interruptions.

```shell
python -m graphrag.index --root ./RAGtest --resume test
```

Midway through, it may be interrupted due to rate limits. After configuring the `--resume` parameter, you can rerun it from where it left off if it fails. You can also reduce the `concurrent_requests` value in the YAML file.


### 4. Querying

For querying the constructed graph, use the `--data` parameter to specify the source of the index. Queries can be divided into:

- **Global Query**: Retrieves information across the entire knowledge graph.
```shell
# Global Query:
python -m graphrag.query \
--root ./RAGtest \
--data ./RAGtest/output/test/artifacts \
--method global \
"What are the top themes in this story?"
```
- **Local Query**: Retrieves information from specific sections or entities within the graph.
```shell
# Local Query:
python -m graphrag.query \
--root ./RAGtest \
--data ./RAGtest/output/test/artifacts \
--method local \
"Who is the protagonist, and what are his/her main relationships?"
```

### 5. Demonstration of Example Cases

As an example, we illustrate use Graph-RAG in a famous Chinese Book 《活着》 written by YuHua

Please do remember to fill in the `.env` and modify `setting.yaml`

```shell
# create dictionary
mkdir -p ./HuoZhe/input

# copy book from data to project
cp data/huozhe.txt ./HuoZhe/input/

# initialize the project
python -m graphrag.index --init --root ./HuoZhe

# ---------------------------------------------
# fill setting.yaml and .env on your own please
# and change the prompts to Chinese version
# ---------------------------------------------

# create index
python -m graphrag.index --root ./HuoZhe --resume huozhe

# query question 1: 
python -m graphrag.query \
--root ./HuoZhe \
--data ./HuoZhe/output/test/artifacts \
--method local \
"福贵是一个怎样的人？"

# query question 2: 
python -m graphrag.query \
--root ./HuoZhe \
--data ./HuoZhe/output/test/artifacts \
--method local \
"福贵与二喜之间是什么关系？"

# query question 3: 
python -m graphrag.query \
--root ./HuoZhe \
--data ./HuoZhe/output/test/artifacts \
--method global \
"《活着》这本书讲述了一个什么故事？"
```

---

## Contributer
- **[SCUT] JunAn Lu**: 
- **[SCUT] Zeno Pang**: 
- **[SCUT] RuiZhi Huang**: 
