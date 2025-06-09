# make_dataset.py
import glob, os
with open('dataset.txt', 'w', encoding='ascii') as f:
    imgs = glob.glob('calib_imgs/**/*.jpg', recursive=True)
    imgs.sort()
    for p in imgs:
        f.write(p.replace('\\', '/') + '\n')   # 换成正斜杠更通用
print(f'写入 {len(imgs)} 行 -> dataset.txt')
