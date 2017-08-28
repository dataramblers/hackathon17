# Use Case Description

## Infrastructure

- 1st Elasticsearch index (runs on 1st ES instance): Crossref data
- 2nd Elasticsearch index (rund on 2nd ES instance): Edoc data
- Flink instance: Retrieval, matching and writing
- Zeppelin instance: Workflow definition, analytics

## Workflow overview

1. Get edoc documents with no DOI from 2nd ES instance
2. For each retrieved document: Check if a matching record in 1st ES instance
exists
3. If true: Get DOI and add it to document. Write document to 2nd ES instance
