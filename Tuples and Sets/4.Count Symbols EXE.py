text = input()

histogram = dict()

for i in text:
    if i not in histogram:
        histogram[i] = 0
    histogram[i] += 1


for k, v in sorted(histogram.items()):
   print(f"{k}: {v} time/s")