import os
__all__ = [mod.split(".")[0] for mod in os.listdir("views") if "__" not in mod]