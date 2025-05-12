

import os


class Config:
    x_range: tuple[float, float] = (0.01, 1)
    num_points: int = 1000
    output_dir = "render"


os.makedirs(Config.output_dir, exist_ok=True)
