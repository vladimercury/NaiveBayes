class MessageReader:
    @staticmethod
    def read(filename):
        file = [x for x in open(filename).read().splitlines() if x != '']
        subject = [x for x in map(int, file[0].split()[1:])]
        content = []
        for i in file[1:]:
            content += [x for x in map(int, i.split())]
        return subject, content


class MessageCollector:
    @staticmethod
    def collect(paths, log_paths=False, log_files=False):
        from classmap import ClassMap
        result = []
        classes = ClassMap()
        for path in paths:
            if log_paths:
                print('Processing: ' + path)
            fold = []
            for txt in paths[path]:
                if log_files:
                    print('  Processing: ' + txt[0])
                subject, content = MessageReader.read(path + '/' + txt[0])
                fold.append((subject, content, classes.get_class(txt[1])))
            result.append(fold)
        return result, classes.get_data()
