# Asset storage class

# images are prepended with I_, sounds with S_, music with M_
# these are all loaded from the LoadingScreen

# If asset variables aren't wrapped in the class, <asset> = None
# will be called every time the module is imported, which is bad.
# If they aren't set to None and just left as <assetName>: Surface,
# they can't be imported properly.

from pygame import Surface


class Assets:
	I_MAINMENU_BACKGROUND: Surface = None

	I_BALL: Surface = None
	I_PADDLE: Surface = None

	I_BRICK_LEVEL1: Surface = None  # 1 HP brick
	I_BRICK_LEVEL2_2: Surface = None  # 2 HP brick at 2 HP
	I_BRICK_LEVEL2_1: Surface = None  # 2 HP brick at 1 HP
	I_BRICK_LEVEL3_3: Surface = None  # 3 HP brick at 3 HP
	I_BRICK_LEVEL3_2: Surface = None  # 3 HP brick at 2 HP
	I_BRICK_LEVEL3_1: Surface = None  # 3 HP brick at 1 HP
	I_BRICK_BOSS: Surface = None  # undestroyable brick
