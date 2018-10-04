import sys
from PIL import Image
import numpy as np

# castle-top.png 0.15 0.08
def get_ascii(file_path, scale, factor):
    characters = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "
    chars = np.asarray(list(characters))
    f, SC, GCF, WCF = file_path, scale, factor, 7/4
    img = Image.open(f)
    S = ( round(img.size[0]*SC*WCF), round(img.size[1]*SC) )
    img = np.sum( np.asarray( img.resize(S) ), axis=2)
    img -= img.min()
    img = (1.0 - img/img.max())**GCF*(chars.size-1)
    return "\n".join(("".join(r) for r in chars[img.astype(int)]))