from setuptools import setup, find_packages

setup(name="graphs",
      version="0.1",
      author="Maren Parnas Gulnes",
      license="MIT",
      packages=find_packages(),
      setup_requires=["neo4j"],
      scripts=["common/modules.py", "common/tasks.py", 
        "networkX/networkXtest.py", "neo4/connector.py"],
      zip_safe=False)
