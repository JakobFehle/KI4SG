import codecs

class config:
	def __init__(self):

		self.configItems = {}
	
		# config.ini einlesen
		configFile = codecs.open('config.ini', "r", "utf-8")
		configText = configFile.read()
		configFile.close()
		
		for zeile in configText.split(u'\n'):
			
			# Kommentare (mit '#' abgetrennt) abschneiden
			kommentarBeginn = zeile.find(u'#')
			if kommentarBeginn>=0:
				zeile=zeile[:kommentarBeginn]
				
			zuweisungsZeichen = zeile.find(u'=')
			if zuweisungsZeichen>0:
				self.configItems[zeile[:zuweisungsZeichen].strip().lower()]=zeile[zuweisungsZeichen+1:].strip()
				
	def getAttribute(self,attributeName):
		attributeName=attributeName.lower()
		if self.configItems.has_key(attributeName):
			return self.configItems[attributeName]
		else:
			return ''

configuration = config()