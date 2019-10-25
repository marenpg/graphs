from neo4j import GraphDatabase

from common.tasks import getTasks
from common.modules import brain_modules

def toCamelCase(st):
        output = ''.join(x for x in st.title() if x.isalnum())
        return output[0].lower() + output[1:]

class HelloWorldExample:

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def print_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    def build_graph(self):
        tasks = getTasks()
        with self._driver.session() as session:
            session.write_transaction(self._build_graph, tasks, brain_modules)
            print("Graph ready")
        

    @staticmethod
    def _build_graph(tx, tasks, modules):
        for module in modules:
            query= "CREATE (%s:Module {name: '%s'})" % (toCamelCase(module.name), module.name)
            tx.run(query)

        for task in tasks:
            query= "CREATE (%s:Task {name: '%s'})" % (toCamelCase(task.name), task.name)
            tx.run(query)
            for mod in task.modules:
                query= """
                    MATCH (a:Task),(b:Module)
                    WHERE a.name = '%s' AND b.name = '%s'
                    CREATE (a)-[:PART_OF { strength: 100}]->(b)
                """ % (task.name, mod.name)
                tx.run(query)        

    def reset_database(self):
        with self._driver.session() as session:
            session.write_transaction(self._clear_database)

    def get_all_nodes(self):
        with self._driver.session() as session:
            nodes = session.write_transaction(self._get_all_nodes)
            print(nodes.values())

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]
    
    @staticmethod
    def _clear_database(tx):
        clear_database_query = '''
            MATCH (n)
            DETACH DELETE n
        '''
        tx.run(clear_database_query)
    
    @staticmethod
    def _get_all_nodes(tx):
        result = tx.run("MATCH (n) RETURN n")
        return result

if(__name__ == "__main__"):
    hw = HelloWorldExample('bolt://localhost:7687', 'neo4j', '123456')
    #hw.print_greeting("hello")
    hw.reset_database()
    hw.build_graph()
    #hw.get_all_nodes()
    hw.close()