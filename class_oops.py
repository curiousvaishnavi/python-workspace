class Factory:
    def __init__(self,pocket,zips,material):
        self.pocket = pocket
        self.zips = zips
        self.material = material

obj1 = Factory(3,2,"Polyster")

print(obj1.material)