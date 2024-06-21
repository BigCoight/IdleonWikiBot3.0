from pywikibot.login import ClientLoginManager

from AllRepos import AllRepos
from helpers.CodeReader import IdleonReader

newV = IdleonReader("2.11", True)
oldV = IdleonReader("2.10", True)

upload = False
if upload:
	loginManager = ClientLoginManager()
	loginManager.login()

for repo in AllRepos:
	repo.compareVersions(oldV, newV, upload = upload)
