import math

from PIL import Image, ImageDraw

from identiconify.base import BaseIdenticon


class PilIdenticon(BaseIdenticon):
    def generate(self, data: str) -> Image:
        """Generate an identicon based on the MD5 hash of the data.
        :param data: The input data to generate the identicon from.
        :return: A PIL Image object representing the identicon.
        """
        hash_value = self._get_md5_hash(data)
        image = Image.new(mode="RGB", size=(self._size, self._size), color=self._background_color or "#FFFFFF")
        draw = ImageDraw.Draw(image)
        base_color = self._block_color or f"#{hash_value[:6]}"
        base_padding = int(self._size / self._dimensions / 2) if self._padding else 0
        block_size = (self._size - base_padding * 2) / self._dimensions

        for x in range(math.ceil(self._dimensions / 2)):
            for y in range(self._dimensions):
                # 43 and 47 are arbitrary prime numbers to lower the chance of linear patterns
                i = (y * 43 + x * 47) % len(hash_value)
                if int(hash_value[i], 16) % 2 == 0:
                    x0 = x * block_size + base_padding
                    y0 = y * block_size + base_padding
                    x1 = (x + 1) * block_size + base_padding
                    y1 = (y + 1) * block_size + base_padding

                    draw.rectangle([x0, y0, x1, y1], fill=base_color)
                    if x != self._dimensions // 2:
                        # This is to prevent drawing the same rectangle twice in the middle column of odd dimensions

                        x0_mirror = (self._dimensions - x - 1) * block_size + base_padding
                        x1_mirror = (self._dimensions - x) * block_size + base_padding

                        draw.rectangle([x0_mirror, y0, x1_mirror, y1], fill=base_color)
        return image
