from src.pipelines import PreFetcher, DataFetcher, PostProcessor, Pipeline


class MyPreFetcher(PreFetcher):
    def run(self):
        return {}


class MyFetcher(DataFetcher):
    def run(self, data):
        return data


class MyPostProcessor(PostProcessor):
    def run(self, data):
        return data


class MyPipeline(Pipeline):
    pre_fetcher = MyPreFetcher
    fetcher = MyFetcher
    post_processor = MyPostProcessor
