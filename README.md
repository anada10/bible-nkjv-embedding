# bible-nkjv-embedding
This is a repo which contains the NKJV bible which has been embedded and is prepared for LLM RAG

**What's in this repo?**
- The bible.py file takes the [orginal JSON from here]([url](https://github.com/jplehmann/textbites/blob/master/textbites/data/NKJV.bible.json)) and then converts it to .avro format

- The avro file contains an embedding field (which can be used when building an LLM RAG application.)

**How to build a RAG Chat app with this?**
I used [Agent Cloud]([url](https://github.com/rnadigital/agentcloud)) to build a RAG Chat app for the NKJV bible.
To do this you need to
- Run [Agent Cloud locally]([url](https://github.com/rnadigital/agentcloud)) or sign up https://agentcloud.dev
- Upload the avro file to bigquery or another DB supported by agentcloud
- Go into the Data Sources > Add New > Enter form for Bigquery or otherwise > Select fields > Select Embedding model/field to embed > Save
- Create an Agent
- Create a Chat App

**Qdrant Snapshot**
I have provided a [Qdrant snapshot here](https://drive.google.com/file/d/1dACXx1mDaGuw4z7TOLa4Hhx0xtJvkr-o/view?usp=sharing) if you want to save money, this was embedded with open ai text-embedding-3-small
