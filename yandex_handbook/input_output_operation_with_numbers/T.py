
result_weight = int(input())
result_price = int(input())
first_price = int(input())
second_price = int(input())
weight_ratio = (result_price - first_price) / (second_price - first_price)
second_weight = result_weight * weight_ratio
first_weight = result_weight - second_weight
print(int(first_weight), int(second_weight))