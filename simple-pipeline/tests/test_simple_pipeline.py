from src.simple_pipeline import PPipeline, PipelineRunner


class PipelineOne(PPipeline):
    """
    Linear Pipeline: Step1 -> Step2 -> Step3
    """
    steps = []
    parameters: Type[TypedDict]


class PipelineTwo(PPipeline):
    """
    Forked Pipeline: Step1 -> Step2
                           -> Step3
    """
    steps = []
    parameters: Type[TypedDict]


class PipelineThree(PPipeline):
    """
    Merge Pipeline: Step1 -> Step3
                    Step2 ->
    """
    steps = []
    parameters: Type[TypedDict]


class PipelineFour(PPipeline):
    """
    Fork and Merge Pipeline: Step1 -> Step2 -> Step4
                                   -> Step3 ->
    """
    steps = []
    parameters: Type[TypedDict]


class PipelineFive(PPipeline):
    """
    Merge and Fork Pipeline: Step1 -> Step3 -> Step4
                             Step2 ->       -> Step5
    """
    steps = []
    parameters: Type[TypedDict]


class TestPipelineRunner:
    def test_pipeline_one(self):
        result = PipelineRunner(PipelineOne).run_pipeline()
        assert result == ""

    def test_pipeline_two(self):
        result = PipelineRunner(PipelineTwo).run_pipeline()
        assert result == ""

    def test_pipeline_three(self):
        result = PipelineRunner(PipelineThree).run_pipeline()
        assert result == ""

    def test_pipeline_four(self):
        result = PipelineRunner(PipelineFour).run_pipeline()
        assert result == ""

    def test_pipeline_five(self):
        result = PipelineRunner(PipelineFive).run_pipeline()
        assert result == ""
