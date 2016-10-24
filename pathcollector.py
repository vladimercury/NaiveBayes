class PathCollector:
    @staticmethod
    def collect(base_path, pattern):
        from re import compile
        from os import walk
        match = compile(pattern)
        result = dict()
        for root, dirs, files in walk(base_path):
            if not files:
                continue
            result[root] = [(file, match.findall(file)[0]) for file in files]
        return result
