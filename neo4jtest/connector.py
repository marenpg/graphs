# from neo4j import GraphDatabase

# driver = GraphDatabase.driver("localhost:7687", auth=("neo4j", "123456"))


from neo4j import GraphDatabase

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def print_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]

hw = HelloWorldExample('bolt://localhost:7687', 'neo4j', '123456')
hw.print_greeting("hello")
hw.close()

# if(__name__ == "__main__"):
#     print("Main called")
#     tasks = getTasks()
#     graph = buildGraph(modules, tasks)
#     printGraph(graph)