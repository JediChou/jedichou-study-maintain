import cStringIO, zipfile

class ZipString(ZipFile)
	def __init__(self, datastring):
			ZipFile.__init__(self, cStringIO.StringIO(datastring))

if __name__ == "__main__":
	pass	
