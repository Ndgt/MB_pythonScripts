import sys, os, inspect
CurrentFilePath = inspect.currentframe().f_code.co_filename
CurrentDir = os.path.dirname(CurrentFilePath)
targetPath = os.path.join(CurrentDir,"OriginalScripts")
sys.path.append(targetPath)