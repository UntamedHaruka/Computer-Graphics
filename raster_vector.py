from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
# Create a blank raster image
image = Image.new("RGB", (500, 500), "white")

# Create a drawing object
draw = ImageDraw.Draw(image)

# Draw the house body
draw.rectangle((150, 220, 350, 400), fill="lightblue", outline="black", width=3)

# Draw the roof
draw.polygon(
    [(120, 220), (250, 100), (380, 220)],
    fill="red",
    outline="black"
)

# Draw the door
draw.rectangle((220, 300, 280, 400), fill="brown", outline="black", width=3)

# Draw a window
draw.rectangle((170, 260, 210, 300), fill="yellow", outline="black", width=2)

# Save the raster image
image.save("raster_house.png")

# Display the image
image.show()

print("Raster image created successfully!")




# -------------------------------
# Create the vector version
# -------------------------------

fig, ax = plt.subplots(figsize=(5, 5))

# House body
body = Rectangle(
    (1.5, 1),
    2,
    1.8,
    facecolor="lightblue",
    edgecolor="black",
    linewidth=2
)
ax.add_patch(body)

# Roof
roof = Polygon(
    [(1.2, 2.8), (2.5, 4), (3.8, 2.8)],
    closed=True,
    facecolor="red",
    edgecolor="black",
    linewidth=2
)
ax.add_patch(roof)

# Door
door = Rectangle(
    (2.2, 1),
    0.6,
    1,
    facecolor="brown",
    edgecolor="black",
    linewidth=2
)
ax.add_patch(door)

# Window
window = Rectangle(
    (1.7, 2.0),
    0.4,
    0.4,
    facecolor="yellow",
    edgecolor="black",
    linewidth=2
)
ax.add_patch(window)

# Set graph limits
ax.set_xlim(0.5, 4.5)
ax.set_ylim(0.5, 4.5)

# Remove axes
ax.set_aspect("equal")
ax.axis("off")
# --------------------------------
# Raster vs Vector Comparison
# --------------------------------

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Original Raster
axes[0, 0].imshow(image)
axes[0, 0].set_title("Raster - Original")
axes[0, 0].axis("off")

# Original Vector
axes[0, 1].add_patch(
    Rectangle((1.5, 1), 2, 1.8, facecolor="lightblue", edgecolor="black")
)

axes[0, 1].add_patch(
    Polygon(
        [(1.2, 2.8), (2.5, 4), (3.8, 2.8)],
        facecolor="red",
        edgecolor="black"
    )
)

axes[0, 1].add_patch(
    Rectangle((2.2, 1), 0.6, 1, facecolor="brown", edgecolor="black")
)

axes[0, 1].add_patch(
    Rectangle((1.7, 2), 0.4, 0.4, facecolor="yellow", edgecolor="black")
)

axes[0, 1].set_xlim(0.5, 4.5)
axes[0, 1].set_ylim(0.5, 4.5)
axes[0, 1].set_aspect("equal")
axes[0, 1].set_title("Vector - Original")
axes[0, 1].axis("off")


# Raster Zoom
axes[1, 0].imshow(image.resize((1000, 1000)))
axes[1, 0].set_title("Raster - Zoomed")
axes[1, 0].axis("off")


# Vector Zoom
axes[1, 1].add_patch(
    Rectangle((1.5, 1), 2, 1.8, facecolor="lightblue", edgecolor="black")
)

axes[1, 1].add_patch(
    Polygon(
        [(1.2, 2.8), (2.5, 4), (3.8, 2.8)],
        facecolor="red",
        edgecolor="black"
    )
)

axes[1, 1].add_patch(
    Rectangle((2.2, 1), 0.6, 1, facecolor="brown", edgecolor="black")
)

axes[1, 1].add_patch(
    Rectangle((1.7, 2), 0.4, 0.4, facecolor="yellow", edgecolor="black")
)

axes[1, 1].set_xlim(1.2, 3.8)
axes[1, 1].set_ylim(1.2, 4)
axes[1, 1].set_aspect("equal")
axes[1, 1].set_title("Vector - Zoomed")
axes[1, 1].axis("off")


plt.suptitle("Comparative Visualization of Raster and Vector Graphics")
plt.tight_layout()

plt.show()

print("Raster vs Vector comparison completed!")