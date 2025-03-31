def findMinArrowShots(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    sorted_points = sorted(points, key=lambda point: point[0])
    merged = []
    for i in sorted_points:
        if not merged:
            merged.append(i)
            continue

        if not (i[0] > merged[len(merged)-1][1] or merged[len(merged)-1][0] > i[1]): 
            merged[-1][0] = min(i[0],merged[-1][0])
            merged[-1][1] = min(i[1],merged[-1][1])
        else:
            merged.append(i)
    return len(merged)


print(findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))  # Should print 2
