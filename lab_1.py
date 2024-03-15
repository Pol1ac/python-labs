def two_sum(nums, target):
  for first_index in range(len(nums)):
    second_index = first_index + 1
    while second_index < len(nums):
      if nums[first_index] + nums[second_index] == target:
        return [first_index, second_index]
      second_index += 1
  return -1


if __name__ == "__main__":
  nums = [3,2,4]
  target = 6

  result = two_sum(nums, target)

  if result == -1:
    print("Не знайдено")
  else:
      print(f"Індекси: {result}")