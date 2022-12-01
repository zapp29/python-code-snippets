## Simple Pipeline

### Build
`python -m build`

### Install
`python -m pip install simple_pipeline-1.0.0.tar.gz`

### How to use Simple Pipeline
| SP object                 | Python object                   | Role                                                       | How to use                                                                  |
|---------------------------|---------------------------------|------------------------------------------------------------|-----------------------------------------------------------------------------|
| Pipeline                  | class                           | define:  - steps that should executed - execution sequence | define high-level pipeline design that will be constant across executions   |
| Pipeline()                | instantianted class             | precise: - run configuration                               | use for single run configurations, that will be different across executions |
| Pipeline().run_pipeline() | run_pipeline() method execution | execution of the Pipeline's steps                          | execute when te Pipeline needs to start working                             |


