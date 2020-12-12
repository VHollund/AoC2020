class bag():
    def __init__(self,color,bags):
        self.color = color
        self.contains=bags

    def get_content(self):
        return self.contains