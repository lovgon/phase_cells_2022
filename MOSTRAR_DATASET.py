import skimage.io as io
import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
import matplotlib.patches as patches

# % matplotlib
# inline


def showObjects(image_df):
    img_path = image_df.filename

    image = io.imread(img_path)
    draw = image.copy()

    # Create figure and axes
    fig, ax = plt.subplots(1)
    ax.imshow(draw)
    rect = patches.Rectangle((image_df.xmin, image_df.ymin),
                             image_df.xmax - image_df.xmin,
                             image_df.ymax - image_df.ymin,
                             linewidth=1,
                             edgecolor='r',
                             facecolor='none')

    plt.axis('off')
    ax.add_patch(rect)
    plt.show()


showObjects(dataset_df.iloc[2])
