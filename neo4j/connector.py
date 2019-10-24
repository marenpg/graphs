from neo4j import GraphDatabase

driver = GraphDatabase.driver("localhost:7687", auth=("neo4j", "123456"))


