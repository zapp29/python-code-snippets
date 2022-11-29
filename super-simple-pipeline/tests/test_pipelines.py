from src.super_simple_pipeline import PreFetcher, DataFetcher, PostProcessor, Pipeline


class MyPreFetcher1(PreFetcher):
    def run(self):
        return {"a": "1"}


class MyFetcher1(DataFetcher):
    def run(self, data):
        return {**data, "b": "2"}


class MyPostProcessor1(PostProcessor):
    def run(self, data):
        return {**data, "c": "3"}


class MyPreFetcher2(PreFetcher):
    def run(self):
        return {"a": "1"}


class MyFetcher2(DataFetcher):
    def run(self, data):
        return {**data, "a": "2"}


class MyPostProcessor2(PostProcessor):
    def run(self, data):
        return {**data, "a": "3"}


class MyPostProcessor3(PostProcessor):
    def run(self, data):
        return {"d": str(int(data.get("a")) + int(data.get("b")))}


class MyPipeline1(Pipeline):
    pre_fetcher = MyPreFetcher1
    fetcher = MyFetcher1
    post_processor = MyPostProcessor1


class MyPipeline2(Pipeline):
    pre_fetcher = MyPreFetcher2
    fetcher = MyFetcher2
    post_processor = MyPostProcessor2


class MyPipeline3(Pipeline):
    pre_fetcher = MyPreFetcher1
    fetcher = MyFetcher1
    post_processor = MyPostProcessor3


class TestPipeline:
    def test_1(self):
        result = MyPipeline1().run()
        assert result == {"a": "1", "b": "2", "c": "3"}

    def test_2(self):
        result = MyPipeline2().run()
        assert result == {"a": "3"}

    def test_3(self):
        result = MyPipeline3().run()
        assert result == {"d": "3"}
