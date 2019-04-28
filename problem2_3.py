#!/usr/bin/python

import sys
import csv
import statistics as st


class Regression:
    def __init__(self):
        self.inputFile = "./input1.csv"
        self.outputFile = "./output1.csv"
        self.alpha_values = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.5, 5, 10]
        self.number_of_ittirations = 100

        self.my_own_alpha = 1.1
        self.my_own_number_of_ittirations = 30

    def start(self):

        input_data = self.csvReader(self.inputFile)
        input_data = self.normalize_data(input_data)

        for alpha in self.alpha_values:
            result_row = self.getOutputData(alpha, self.number_of_ittirations, input_data)
            print(result_row)
            self.csvWriter(self.outputFile, result_row)

        result_row = self.getOutputData(self.my_own_alpha, self.my_own_number_of_ittirations, input_data)

        print(result_row)
        self.csvWriter(self.outputFile, result_row)

    def getOutputData(self, alpha, number_of_iterations, input_data):

        b_0 = 0
        b_age = 0
        b_weight = 0

        last_Risk, last_b_0, last_b_age, last_b_weight = 10000000000000000000, 0, 0, 0

        for i in range(number_of_iterations):

            Risk, sum = self.getRisk(b_0, b_age, b_weight, input_data)

            if Risk > last_Risk:
                return alpha, number_of_iterations, last_b_0, last_b_age, last_b_weight

            last_Risk, last_b_0, last_b_age, last_b_weight = Risk, b_0, b_age, b_weight

            b_0 = b_0 - alpha * self.getSumForB0(b_0, b_age, b_weight, input_data) / len(input_data)
            b_age = b_age - alpha * self.getSumForBAge(b_0, b_age, b_weight, input_data) / len(input_data)
            b_weight = b_weight - alpha * self.getSumForBWeight(b_0, b_age, b_weight, input_data) / len(input_data)

        return alpha, number_of_iterations, b_0, b_age, b_weight

    def getRisk(self, b_0, b_age, b_weight, input_data):

        sum_ = 0

        for set_ in input_data:
            age = set_[0]
            weight = set_[1]
            height = set_[2]

            sum_ = sum_ + (b_0 + b_age * age + b_weight * weight - height) ** 2

        R = sum_ / (2 * len(input_data)) # R = 1/2n * sum_

        return R, sum_

    def getSumForB0(self, b_0, b_age, b_weight, input_data):

        sum_ = 0
        for set_ in input_data:
            age = set_[0]
            weight = set_[1]
            height = set_[2]

            sum_ = sum_ + (b_0 + b_age * age + b_weight * weight - height)
        return sum_

    def getSumForBAge(self, b_0, b_age, b_weight, input_data):

        sum_ = 0
        for set_ in input_data:
            age = set_[0]
            weight = set_[1]
            height = set_[2]

            sum_ = sum_ + (b_0 + b_age * age + b_weight * weight - height) * age
        return sum_

    def getSumForBWeight(self, b_0, b_age, b_weight, input_data):

        sum_ = 0
        for set_ in input_data:
            age = set_[0]
            weight = set_[1]
            height = set_[2]

            sum_ = sum_ + (b_0 + b_age * age + b_weight * weight - height) * weight
        return sum_

    def normalize_data(self, input_data):

        age_list = []
        weight_list = []
        height_list = []

        for set_ in input_data:
            age_list.append(set_[0])
            weight_list.append(set_[1])
            height_list.append(set_[2])

        age_stdev = st.stdev(age_list)
        weight_stdev = st.stdev(weight_list)
        height_stdev = st.stdev(height_list)
        
        age_mean = st.mean(age_list)
        weight_mean = st.mean(weight_list)
        height_mean = st.mean(height_list)

        for set_ in input_data:
            set_[0] = (set_[0] - age_mean)/age_stdev
            set_[1] = (set_[1] - weight_mean)/weight_stdev

        return input_data

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

        for set in data:
            set[0] = float(set[0])
            set[1] = float(set[1])
            set[2] = float(set[2])

        return data

    def csvWriter(self, output_file, list_obj):

        with open(output_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(list_obj)

        file.close()

def main(input_file, output_file):
    regression = Regression()
    regression.inputFile = input_file
    regression.outputFile = output_file
    regression.start()

if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)