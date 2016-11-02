class ClassMap:
    def __init__(self):
        self.data = {"spmsg": 0, "legit": 1}
        self.counter = 0

    def get_class(self, class_name):
        if class_name in self.data:
            return self.data[class_name]
        else:
            self.data[class_name] = self.counter
            self.counter += 1
            return self.data[class_name]

    def get_data(self):
        return self.data
