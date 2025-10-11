import os
import random

folders = ["4-1", "4-2"]
output_file = "group_photos.md"

images = []
for folder in folders:
    for f in os.listdir(folder):
        if f.lower().endswith(".jpg"):
            images.append(f"{folder}/{f}")

random.shuffle(images)

groups = []
i = 0
while i < len(images):
    group_size = random.randint(2, 10)
    group = images[i:i + group_size]
    groups.append(group)
    i += group_size

lines = []
for group in groups:
    number = len(group)
    layout = random.randint(1, 3)
    lines.append(f"{{% gp {number}-{layout} %}}")
    for img in group:
        name = os.path.splitext(os.path.basename(img))[0]
        lines.append(f"![{name}]({img})")
    lines.append("{% endgp %}\n")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Finished: {output_file} ({len(images)} images, {len(groups)} groups)")