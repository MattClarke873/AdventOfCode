# This is Day 1
import PythonTools as T

with open('data.txt', 'r') as file:
    data = file.read()



LHS = []
RHS = []
Diff = []
Sim = []



for line in data.strip().split("\n"):
    left, right = map(int, line.split())  # Split each line into two integers
    LHS.append(left)
    RHS.append(right)

# Output the result


LHSsorted = sorted(LHS)
RHSsorted = sorted(RHS)

for i in range(len(LHS)):
    if LHSsorted[i] >= RHSsorted[i]:
        Diff.append(LHSsorted[i] - RHSsorted[i])
    else:
        Diff.append(RHSsorted[i] - LHSsorted[i])
print(sum(Diff))
for i in range(len(LHS)):
    Sim.append(LHSsorted[i] * RHSsorted.count(LHSsorted[i]))
print(sum(Sim))
