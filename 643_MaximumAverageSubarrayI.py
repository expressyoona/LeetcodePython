nums = [1, 5, 3, 5, 2, -6, 4, 2]
k = 4
SUM = []
SUM.append(nums[0])
for i in range(1, len(nums)):
	SUM.append(SUM[i-1] + nums[i])
print(SUM)
res = SUM[k-1] * 1 / k
for i in range(k, len(nums)):
	print(SUM[i], SUM[i-k])
	res = max(res, (SUM[i] - SUM[i-k]) * 1 / k)