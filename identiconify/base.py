import hashlib
from abc import ABC, abstractmethod
from typing import Union


class BaseIdenticon(ABC):
    def __init__(
        self,
        dimensions: int = 5,
        size: int = 256,
        padding: bool = True,
        background_color: Union[float, tuple[float, ...], str] = None,
        block_color: Union[float, tuple[float, ...], str] = None,
    ):
        """
        Initialize the Identicon class with the specified dimensions.
        :param dimensions: The number of blocks in each dimension (e.g., 5 for a 5x5 grid).
        :param size: The size of the generated image (default is 256).
        :param extension: The file extension for the generated image (default is "png").
        :param padding: Whether to add padding around the identicon (default is True).
        :param background_color: The background color for the identicon (default is None).
        :param block_color: The color of the blocks in the identicon (default is None).
        """
        self._dimensions = dimensions
        self._size = size
        self._padding = padding
        self._background_color = background_color
        self._block_color = block_color

    @staticmethod
    def _get_md5_hash(data: str) -> str:
        """Generate an MD5 hash for the given data."""
        return hashlib.md5(data.encode()).hexdigest()

    @abstractmethod
    def generate(self, data: str):
        """Generate an identicon based on the MD5 hash of the data."""
        pass
