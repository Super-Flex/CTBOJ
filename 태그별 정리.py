import csv
from 문제id입력시정보 import problemInfo_return_key

# CSV 파일 경로
csv_file = "data/문제데이터크롤링.csv"

problem = []
# CSV 파일 읽기
with open(csv_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        # 각 행의 데이터 처리
        for data in row:
            # 데이터 활용
            problem.append(data)
problem = sorted(list(map(int, problem[1:])))
# print(problem)

from collections import defaultdict

tag_cnt = defaultdict(int)
tag_cnt_with_level = defaultdict(int)
max_level_limit = 15

for i in problem:
    tag_list, level = problemInfo_return_key(i)
    if level > max_level_limit:
        continue
    print(tag_list, level)
    for tag in tag_list:
        tag_cnt[tag] += 1
        tag_cnt_with_level[tag] += level

print(tag_cnt)
print(tag_cnt_with_level)

# CSV 파일 경로
csv_file = f"data/태그별정리_{max_level_limit}.csv"

# CSV 파일에 데이터 저장
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["태그", "수"])
    writer.writerows([(tag, cnt) for tag, cnt in tag_cnt.items()])

print(f"{csv_file}에 데이터를 저장했습니다.")

# CSV 파일 경로
csv_file = f"data/태그별레벨합정리_{max_level_limit}.csv"

# CSV 파일에 데이터 저장
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["태그", "수"])
    writer.writerows([(tag, cnt) for tag, cnt in tag_cnt_with_level.items()])

print(f"{csv_file}에 데이터를 저장했습니다.")
"""
no limit
{'dp': 218, 'graphs': 299, 'topological_sorting': 15, 'bruteforcing': 190, 'math': 227, 'implementation': 338, 'combinatorics': 30, 'graph_traversal': 227, 'bfs': 147, 'dfs': 84, 'regex': 3, 'string': 131, 'bitmask': 35, 
'flow': 4, 'dp_bitfield': 9, 'number_theory': 46, 'primality_test': 19, 'sieve': 16, 'data_structures': 198, 'deque': 12, 'greedy': 158, 'sorting': 145, 'geometry': 32, 'prefix_sum': 36, 'divide_and_conquer': 25, 'recursion': 31, 'euclidean': 12, 'backtracking': 73, 'disjoint_set': 23, 'simulation': 106, 'trees': 51, 'binary_search': 74, 'knapsack': 15, 'parametric_search': 23, 'dp_tree': 13, 'ad_hoc': 19, 'ternary_search': 3, 'queue': 13, 'dijkstra': 46, 'mst': 12, 'eulerian_path': 1, 'constructive': 12, 'priority_queue': 31, 'mitm': 4, 'bellman_ford': 3, 'hash_set': 43, 'two_pointer': 39, '0_1_bfs': 9, 'tree_set': 13, 'segtree': 22, 'sliding_window': 10, 'probability': 4, 'floyd_warshall': 18, 'stack': 43, 'lazyprop': 4, 'linked_list': 3, 'case_work': 16, 'parsing': 10, 'arithmetic': 45, 'exponentiation_by_squaring': 4, 'bipartite_matching': 8, 'bipartite_graph': 2, 'convex_hull': 2, 'kmp': 3, 'sweeping': 16, 'arbitrary_precision': 5, 'hashing': 3, 'pythagoras': 3, 'tsp': 3, 
'line_intersection': 2, 'polygon_area': 1, 'lis': 3, 'linear_algebra': 2, 'cht': 6, 'trie': 6, 'permutation_cycle_decomposition': 2, 'coordinate_compression': 4, 'inclusion_and_exclusion': 3, 'crt': 1, 'merge_sort_tree': 1, 'game_theory': 9, 'pbs': 1, 'scc': 2, 'sparse_table': 2, 'lca': 3, 'multi_segtree': 1, 'geometry_3d': 2, 'euler_phi': 1, 'sprague_grundy': 2, 'euler_characteristic': 1, 'mfmc': 2, 'fft': 2, 'sqrt_decomposition': 1, 'modular_multiplicative_inverse': 2, 'centroid': 1, 'centroid_decomposition': 1, 'suffix_array': 2, 'general_matching': 1, 'pigeonhole_principle': 2, 'hungarian': 1, 'offline_queries': 3, 'euler_tour_technique': 1, 'physics': 1, 'mo': 1, 'cartesian_tree': 1, 'hall': 1})
"""
