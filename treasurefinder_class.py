import csv

PATH_TO_CSV = 'test.csv'


class TreasureFinder:
    def __init__(self, csv_file):
        self._path_to_csv = csv_file
        self._counter = 1
        self._row = 0
        self._column = 0
        self.data = None

    @property
    def element(self):
        return self.data[self._row][self._column]

    def _csv_to_array(self):
        with open(self._path_to_csv) as f:
            reader = csv.reader(f)
            return list(reader)

    def finder(self):
        self.data = self._csv_to_array()
        while self._counter < 26:
            if self.element[0] == str(self._row+1) and self.element[1] == str(self._column+1):
                return f"You've found treasure in the cell {self.element}"
            self._counter += 1
            self._row, self._column = (int(i)-1 for i in self.element)
        return "Unfortunately there is no treasure here"


my_treasure_finder = TreasureFinder(PATH_TO_CSV)
print(my_treasure_finder.finder())
