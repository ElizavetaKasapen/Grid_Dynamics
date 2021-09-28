
class BasicStatics:
    
    def __init__(self, sequance_of_numbers):
        self.sequance_of_numbers = sequance_of_numbers 

    def Mean(self):
        return sum(self.sequance_of_numbers)/float(len(self.sequance_of_numbers))

    def Median(self):
        sorted_list = sorted(self.sequance_of_numbers)
        index = (len(self.sequance_of_numbers) -1) // 2
        if(index%2):
            return sorted_list[index]
        return (sorted_list[index]+sorted_list[index+1])/2.0

    def Min(self):
        tmp = self.sequance_of_numbers[0]
        for i in range(len(self.sequance_of_numbers)):
            if self.sequance_of_numbers[i] < tmp:
                tmp = self.sequance_of_numbers[i]
        return tmp

        # or return min(self.sequance_of_numbers)

    def Max(self):
        tmp = self.sequance_of_numbers[0]
        for i in range(len(self.sequance_of_numbers)):
            if self.sequance_of_numbers[i] > tmp:
                tmp = self.sequance_of_numbers[i]
        return tmp
        # or return max(self.sequance_of_numbers)

    def Count(self, value):
        return self.sequance_of_numbers.count(value)


numbers = [12.0, 3.5, 5.0, 27.41,1.1]
basic_statics = BasicStatics(numbers)

print(basic_statics.Max())
print(basic_statics.Min())
print(basic_statics.Median())
print(basic_statics.Mean())
