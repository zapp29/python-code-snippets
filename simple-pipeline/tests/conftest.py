import pytest

from src.simple_pipeline import Step


class Step1(Step):
    def __init__(self, input_param, destination_param):
        self.input_param = input_param
        self.destination_param = destination_param

    def execute(self, **params):
        ...
        return {
            **params
        }


class Step2(Step):
    def __init__(self, input_param, destination_param):
        self.input_param = input_param
        self.destination_param = destination_param

    def execute(self, **params):
        ...
        return {
            **params
        }


class Step3(Step):
    def __init__(self, input_param, destination_param):
        self.input_param = input_param
        self.destination_param = destination_param

    def execute(self, **params):
        ...
        return {
            **params
        }


class Step4(Step):
    def __init__(self, input_param, destination_param):
        self.input_param = input_param
        self.destination_param = destination_param

    def execute(self, **params):
        ...
        return {
            **params
        }


class Step5(Step):
    def __init__(self, input_param, destination_param):
        self.input_param = input_param
        self.destination_param = destination_param

    def execute(self, **params):
        ...
        return {
            **params
        }


@pytest.fixture
def step_1():
    return Step1


@pytest.fixture
def step_2():
    return Step2


@pytest.fixture
def step_3():
    return Step3


@pytest.fixture
def step_4():
    return Step4


@pytest.fixture
def step_5():
    return Step5
