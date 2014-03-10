VERSION = (
	0 , # Major 
	1 , # Minor
	1 ) # Patches or Sprint version

def get_version():
	version = ".".join(map(str, VERSION))
	return version
