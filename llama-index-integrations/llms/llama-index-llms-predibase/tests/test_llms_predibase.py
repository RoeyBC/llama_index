from llama_index.core.llms.base import BaseLLM
from llama_index.llms.predibase import PredibaseLLM


def test_embedding_class():
    names_of_base_classes = [b.__name__ for b in PredibaseLLM.__mro__]
    assert BaseLLM.__name__ in names_of_base_classes
