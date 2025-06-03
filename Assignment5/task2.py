lst = list(range(1, 11))
print(f'Original list: {lst}')
lst = lst[:5]
print(f"Extracted first five elements: {lst}")
lst.reverse()
print(f"Reversed extracted elements: {lst}")
