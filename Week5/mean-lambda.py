numbers = [[1,2,3],[4,5,6],[7,8,9]]

# def mean(num_list):
#     return sum(num_list)/len(num_list)
mean = lambda num_list:sum(num_list)/len(num_list) 
avg1 = [mean(num) for num in numbers]
avg2 = []
for num in numbers:
    out = mean(num)
    avg2.append(out)
avg3 = list(map(mean, numbers))
nums = [1,2,6]
power = lambda x:x**2
power2 = map(power, nums)
print(power2)
# print(averages)