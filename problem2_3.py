import matplotlib.pyplot as plt
import csv


class Perceptron:
    def __init__(self):
        self.inputFile = "./input1.csv"
        self.outputFile = "./output1.csv"
        self.b = 0

    def start(self):

        input_data = self.csvReader(self.inputFile)
        self.display(input_data)

    def display(self, input_data, xlist=None, ylist=None):

        fig = plt.figure()

        for dot in input_data:
            if int(dot[2]) == 1:
                c = "red"
            else:
                c = "blue"
            plt.scatter(int(dot[0]), int(dot[1]), c=c)

        if xlist and ylist:
            plt.plot(xlist, ylist)

        plt.grid(True)  # линии вспомогательной сетки
        plt.show()

    def csvReader(self, input_file):

        data = []
        with open(input_file, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                row_data = []
                for value in row:
                    row_data.append(value)
                data.append(row_data)

        file.close()

        return data

    def csvWriter(self, output_file, list_obj):

        with open(output_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(list_obj)

        file.close()


def main():
    perceptron = Perceptron()
    perceptron.start()


if __name__ == '__main__':
    main()
