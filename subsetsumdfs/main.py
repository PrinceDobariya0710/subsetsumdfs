import time

def subsetsum(items:list, target:float, max_time:int, accuracy:float,max_combinations:int):
    def dfs(index, remaining_sum, path, result):
        if abs(remaining_sum) <= accuracy and abs(remaining_sum) >= 0:
            result.append(path)
        if index >= len(items) or max_combinations == len(result):
            return
        if time.time() - start_time >= max_time:
            return
        dfs(index + 1, round(remaining_sum - items[index]["value"], 2), path + [items[index]], result)
        dfs(index + 1, remaining_sum, path, result)

    start_time = time.time()
    max_time = max_time
    result = []
    dfs(0, target, [], result)
    return result