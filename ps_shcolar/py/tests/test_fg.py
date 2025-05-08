import ps_shcolar

def test_green_fg():
	assert shcolar.fg.green=="\033[32m";
def test_reset_fg():
	assert shcolar.fg.reset=="\033[39m";