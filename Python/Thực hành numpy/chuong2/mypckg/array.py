class Array:
    def __init__(self,data):
        self.data = data
        
    @property
    def dtype(self):
        return type(self.data[0])
    
    @property
    def size(self):
        return len(self.data)
    
    @property
    def shape(self):
        if isinstance(self.data, (list,tuple)):
            return (self.size,)
        else:
            return self.data.shape
        
    @property
    def ndim(self):
        if isinstance(self.data, (list,tuple)):
            return 1
        else:
            return self.data.ndim
    
    def __str__(self) -> str:
        return str(self.data)

class OneDArray(Array):
    def __init__(self,data):
        super().__init__(data)
    
    @property
    def shape(self):
        return (self.size,)
    
    @property
    def ndim(self):
        return 1
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, value):
        self.data[index] = value
    
    def __str__(self):
        return "[" + ", ".join(str(x) for x in self.data) + "]"