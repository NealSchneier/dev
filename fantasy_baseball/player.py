class Player(object):

    def __init__(self, name, zips, fans, steamer, oliver, rotochamp):
        self.name = name
        self.zips = zips
        self.fans = fans
        self.steamer = steamer
        self.oliver = oliver
        self.rotochamp = rotochamp
        
    def average(self):
        avg = self.zips + self.fans + self.steamer + self.oliver + self.rotochamp
        
        avg = avg / self.total()
        return avg
	
    def total(self):
        count = 0
        if self.zips > 0:
            count = count + 1
        if self.fans > 0:
            count = count + 1
        if self.steamer > 0:
            count = count + 1
        if self.oliver > 0:
            count = count + 1
        if self.rotochamp > 0:
            count = count + 1
        if count == 0:
            count = 1
        return count
