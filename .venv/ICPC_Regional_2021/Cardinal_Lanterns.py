def main():
    # 读取输入
    parameters = input().strip().split()
    n, row, collmn = int(parameters[0]), int(parameters[1]), int(parameters[2])
    
    # 使用集合记录被覆盖的行和列
    covered_rows = set()
    covered_columns = set()
    
    # 读取灯笼位置并更新覆盖的行和列
    for _ in range(n):
        r, c = map(int, input().strip().split())
        covered_rows.add(r)
        covered_columns.add(c)
    
    # 计算未被覆盖的格子数
    total_cells = row * collmn
    uncovered_cells = (row-len(covered_rows)) * (collmn - len(covered_columns))
    result = total_cells - uncovered_cells
    
    # 输出结果
    print(result)

if __name__ == "__main__":
    main()