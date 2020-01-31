from PIL import Image, ImageSequence
im = Image.open("./pictures/4.png")
# target_pixels = [im.getpixel((x, y)) for x in range(0, im.size[0]) for y in range(0, im.size[1])]
target_pixels = [im.getpixel((2, x)) for x in range(0, im.size[1])]
print(len(target_pixels))
print(target_pixels)
# 求每一行像素点的rgb值的平均
# avg_count = []
# for x in range(0, im.size[0]):
#     r_mean = []
#     g_mean = []
#     b_mean = []
#     for y in range(0, im.size[1]):
#         r_mean.append(im.getpixel((x, y))[0])
#         g_mean.append(im.getpixel((x, y))[1])
#         b_mean.append(im.getpixel((x, y))[2])
#     avg_count.append(((int)(sum(r_mean)/im.size[0]), (int)(sum(g_mean)/im.size[0]), (int)(sum(b_mean)/im.size[0])))

# print(len(avg_count))
# print((avg_count))



count = 1
for i in range(0, len(target_pixels)):
    if target_pixels[i][0] == target_pixels[i+1][0] and target_pixels[i][1] == target_pixels[i+1][1] and target_pixels[i][2] == target_pixels[i+1][2]:
        count += 1
    else:
        print(count)
        count = 1
    if i+1 == 251:
        break

