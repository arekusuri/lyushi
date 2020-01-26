import sys
def load_data_file():
	if len(sys.argv) < 2:
		print "Usage: " + sys.argv[0] + " data.txt"
		raise Exception("failed")
	else:
		with open(sys.argv[1]) as file:
			return file.readlines()
				

print load_data_file()
