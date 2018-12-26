import Augmentor
import sys
p = Augmentor.Pipeline("./"+sys.argv[1])
p.rotate(probability=0.5, max_left_rotation=5, max_right_rotation=5)
p.flip_left_right(probability=0.5)
p.sample(150)

