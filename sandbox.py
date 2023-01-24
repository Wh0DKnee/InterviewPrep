def minimumPerimeter(radius):
    apples = 0

    upper_n, lower_n = 2 * radius - 1, radius
    # everything except corners and axis points
    apples += 8 * ((((upper_n ** 2) + upper_n) / 2) - (((lower_n ** 2) + lower_n) / 2))
    # corners and axis points:
    apples += 12 * radius

    return int(apples)


prev = 0
l = []
for i in range(1, 11):
    app = minimumPerimeter(i) + prev
    prev = app
    l.append(app)

print(l)
