from enum import Enum
from typing import Protocol, Type, TypedDict


class Step(object):
    @staticmethod
    def execute(**params):
        raise NotImplemented


class PPipeline(Protocol):
    steps = []
    parameters: Type[TypedDict]


class PipelineState(Enum):
    PENDING = 1
    RUNNING = 2
    FINISHED = 3


class PipelineResult(Enum):
    NEW_DATA = 1
    NO_NEW_DATA = 2


class FinishedPipeline:
    def __init__(self, result: PipelineResult, params: dict):
        self.result = result
        self.params = params


class PipelineRunner:
    def __init__(self, pipeline: PPipeline):
        self.pipeline = pipeline
        self.state = PipelineState.PENDING
        self.params = pipeline.parameters

    def run_pipeline(self, **params) -> FinishedPipeline:
        if not set(params.keys()) == set(self.params):
            raise Exception(f"Missing parameters: {set(self.params) - set(params.keys())}")
        for param in self.params:
            if not isinstance(params[param], self.params[param]):
                raise Exception(f"Wrong parameter type. '{param}' should be {self.params[param]}, but is {type(params[param])}.")
        if params is None:
            tmp_params = {}
        else:
            tmp_params = params
        for step in self.pipeline.steps:
            if isinstance(step, tuple):
                print("executing steps:",
                      [
                        s.__class__.__name__ if issubclass(type(s), Step) else s.__name__
                        for s in step
                      ]
                )
                if isinstance(tmp_params, tuple):
                    tmp_params = tuple(
                        e[0].execute(**e[1], **{"context": self.pipeline})
                        for e in zip(step, tmp_params)
                    )
                else:
                    tmp_params = tuple(
                        s.execute(**tmp_params, **{"context": self.pipeline}) for s in step
                    )
            else:
                if issubclass(type(step), Step):
                    print("executing step:", step.__class__.__name__)
                else:
                    print("executing step:", step.__name__)
                if isinstance(tmp_params, tuple):
                    # merge params
                    tmp_params = {
                        k: d[k]
                        for d in tmp_params
                        for k in d
                    }
                    tmp_params = step.execute(**tmp_params, **{"context": self.pipeline})
                else:
                    # pass params
                    tmp_params = step.execute(**tmp_params, **{"context": self.pipeline})
        return FinishedPipeline(
            result=PipelineResult.NO_NEW_DATA,
            params=tmp_params
        )
