MAIN_WIDGET_COLOR = "grey"
BOARD_WIDGET_COLOR = "white"
GRID_LEN = 20
NUM_GRID_PER_BOARD_ROW = 10
BOARD_LEN = GRID_LEN * NUM_GRID_PER_BOARD_ROW
MY_PIXEL_COLOR = "blue"
OTHER_PIXEL_COLOR = "pink"
OWN_N = 2
SERVER_HOST = "localhost" #"128.237.202.200" #"192.168.1.7"
SERVER_PORT = 9999

def checkRange(x):
	if (x >= 0 and x < NUM_GRID_PER_BOARD_ROW):
		return True
	else:
		return False
