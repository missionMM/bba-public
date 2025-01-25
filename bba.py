import json


class FileDict:

    def __init__(self,filename):
        if not filename.endswith(".bba"):
            filename += ".bba"
        filename = "./" + filename
        self.filename = filename

    def createFile(self):
        try:
            with open(self.filename,"w") as f:
                json.dump({},f)

        except Exception as e:
            print(f'[+] Error while creating file : {e}')

    def _load(self):
        try:
            with open(self.filename,"r") as f:
                return json.load(f)
        except FileNotFoundError:
            print("not found")
            return {}
    
    def _save(self,data):
        try:
            with open(self.filename,"w") as f:
                json.dump(data,f)

        except Exception as e:
            print(f'[+] Error while adding the data')
        
    def __getitem__(self,key):
        data = self._load()
        return data[key]
    
    def __setitem__(self,key,value):
        data = self._load()
        data[key] = value
        self._save(data)
    
    def returnWholeDict(self):
        data = self._load()
        return data