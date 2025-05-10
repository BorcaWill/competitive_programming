def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    n = int(data[0])  # 图像数量
    images = []  # 存储所有图像
    i = 1  # 从第二行开始处理输入
    
    # 读取所有图像
    while i < len(data):
        image = []
        for j in range(5):  # 每幅图像有 5 行
            image.append([1 if c == '#' else 0 for c in data[i + j]])
        images.append(image)
        i += 6  # 跳过图像的 5 行和空行

    # 计算每幅图像的等价值（黑色像素数量）
    image_values = [(sum(sum(row) for row in image), image) for image in images]
    
    # 按等价值从小到大排序
    image_values.sort(key=lambda x: (x[0], x[1]))
    count = 0

    # 外层：从小到大取出“当前小图”，内层：在剩余列表中找大图
    while image_values:
        small_val, small_img = image_values.pop(0)
        # 尝试找到一个更大的图像包含 small_img
        found_large = False
        for idx, (large_val, large_img) in enumerate(image_values):
            if is_contained_in(small_img, large_img):
                found_large = True
                # small_img 已被 large_img 覆盖，删除 small_img 后标记 large_img
                # 检查 large_img 是否被更大的图像包含
                has_bigger = False
                for _, (bigger_val, bigger_img) in enumerate(image_values[idx+1:], start=idx+1):
                    if is_contained_in(large_img, bigger_img):
                        has_bigger = True
                        break
                if not has_bigger:
                    # large_img 不会被更大的图覆盖，需要一次打印，删除它并计数
                    image_values.pop(idx)
                    count += 1
                break
        if not found_large:
            # small_img 没有被任何大图包含，需要单独打印
            count += 1
        # 继续处理下一个 small_img
    print(count)


def is_contained_in(small, large):
    """检查 small 图像是否被 large 图像包含"""
    for i in range(len(small)):
        for j in range(len(small[0])):
            if small[i][j] == 1 and large[i][j] != 1:
                return False
    return True

if __name__ == "__main__":
    main()