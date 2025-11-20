import numpy as np


virat_runs = np.array([72,45,88,101])
print(virat_runs)
team_run = np.array([
    [72, 45, 88],
    [55,60,47],
    [30,75,50]
])
print(team_run)


identity_array = np.identity(3)
identity_array1 = np.eye(3)

full_array = np.full((3,3),7)
zero_array = np.zeros((3,3))
one_array = np.ones((3,3))
empty_array = np.empty((3,3))
print(empty_array)
player_ages = np.array((35, 37, 31))

player_ages[1] = 41
print(player_ages)

arr = np.arange(55,65)
print(arr,arr[0],arr[5])
print(arr[4])
arr[4]= 54
print(arr[4])
run_rates = np.arange(4,11,1)
print(run_rates)

print(np.arange(1,10,3))
print(np.linspace(5,11,3,dtype=int))

print(np.random.uniform(5,11,3))
print(np.random.normal(5,11,3))
print(np.random.standard_t(5,11))
print(np.random.randint(1,10,(2,3)))
print(np.random.seed(101))