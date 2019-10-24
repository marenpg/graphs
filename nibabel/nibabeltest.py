import nibabel as nib
import matplotlib.pyplot as plt

img = nib.load('c_map_vertical_checkerboard.nii.gz')
print(img.header)

data = img.get_fdata()
print(data.shape)

plt.imshow(data[:,:,10])
plt.pause(10)

def show_slices(slices):
    fig, axes = plt.subplots(1, len(slices))
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="gray", origin="lower")
        plt.pause(2)
slices = [data[26, :, :], data[:, 30, :], data[:,:, 16]]

show_slices(slices)
