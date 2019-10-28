# Testing out graph libraries
## Build
```bash
pip3 install -r requirements.txt
python3 setup.py build_ext --inplace
```

## networkX module:
```bash
python -m networkXtest.networkXtest
python3 -m networkXtest.networkXtest
```


## neo4j module: 
This module requires you to run a local neo4j instance.
```bash
python -m neo4jtest.connector
python3 -m neo4jtest.connector
```