import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for characte in message:
    count.setdefault(characte, 0)
    count[characte] = count[characte] + 1

print(pprint.pformat(count))