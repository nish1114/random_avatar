from pathlib import Path
import imageio.v2 as imageio
image_path = Path('media')
images = list(image_path.glob('*.png'))
image_list = []
for file_name in images:
    image_list.append(imageio.imread(file_name))
imageio.mimwrite('avatar_animated.gif', image_list)