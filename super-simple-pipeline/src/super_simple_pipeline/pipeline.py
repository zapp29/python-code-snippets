import abc
import logging
from typing import Any

from src.super_simple_pipeline.steps import PreFetcher, DataFetcher, PostProcessor

LOG = logging.getLogger(__name__)
logging.basicConfig(level="INFO")


class Pipeline(abc.ABC):
    pre_fetcher: PreFetcher
    fetcher: DataFetcher
    post_processor: PostProcessor

    def run(self):
        LOG.info(f"Running Pipeline: {self.__class__.__name__}")
        LOG.info(f"Running PreFetcher: {self.pre_fetcher.__name__}")
        prefetch_result: dict[str, Any] = self.pre_fetcher().run()
        LOG.info(f"Executed PreFetcher: {self.pre_fetcher.__name__} with result: {prefetch_result}")

        LOG.info(f"Running DataFetcher: {self.fetcher.__name__}")
        fetch_result = self.fetcher().run(prefetch_result)
        LOG.info(f"Executed DataFetcher: {self.fetcher.__name__} with result: {prefetch_result}")

        LOG.info(f"Running PostProcessor: {self.post_processor.__name__}")
        post_process_result = self.post_processor().run(fetch_result)
        LOG.info(f"Executed PostProcessor: {self.post_processor.__name__} with result {post_process_result}")

        return post_process_result