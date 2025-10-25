from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import os

def visualize_curves(train_loss_list, psnr_list, save_dir, name_prefix="coarse"):

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Plot training loss
    plt.figure()
    plt.plot(train_loss_list, label='Training Loss (' + name_prefix + ')')
    plt.xlabel('Iterations')
    plt.ylabel('Loss')
    plt.title('Train Loss Curve')
    plt.legend()
    plt.grid()
    plt.savefig(os.path.join(save_dir, f'{name_prefix}_train_loss_curve.png'))
    plt.close()

    # Plot training loss
    plt.figure()
    plt.plot(train_loss_list, label='Training Loss (' + name_prefix + ')')
    plt.xlabel('Iterations')
    plt.ylabel('Loss')
    plt.ylim(0, 0.05)
    plt.title('Train Loss Curve')
    plt.legend()
    plt.grid()
    plt.savefig(os.path.join(save_dir, f'{name_prefix}_train_loss_curve_detailed.png'))
    plt.close()

    # Plot PSNR
    plt.figure()
    plt.plot(psnr_list, label='PSNR', color='orange')
    plt.xlabel('Iterations')
    plt.ylabel('PSNR')
    plt.title('Train PSNR Curve (' + name_prefix + ')')
    plt.legend()
    plt.grid()
    plt.savefig(os.path.join(save_dir, f'{name_prefix}_train_psnr_curve.png'))
    plt.close()

def plot_and_save(x_list, y_list, save_path="", title="Test Average PSNR", xlabel="X", ylabel="Y", type_to="coarse"):

    plt.figure(figsize=(6, 4))
    plt.plot(x_list, y_list, marker='o', linestyle='-', linewidth=2)

    plt.title(title + ' (' + type_to + ')')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(save_path+'/'+str(type_to)+"test_average_psnr.png")
    plt.close()

def plot_image_grid(save_path="figure", folder="logs/blender_lego_coarse", type_to="coarse"):

    iteration_list = ["testset_000500", "testset_002000", "testset_005000", "testset_010000", "testset_020000"]
    image_name_list = ["000_rgb.png", "000_depth.png", "001_rgb.png", "001_depth.png", "002_rgb.png", "002_depth.png"]
    titles = ["iter_500", "iter_2000", "iter_5000", "iter_10000", "iter_20000"]

    fig, axes = plt.subplots(6, 5, figsize=(5 * 2.5, 6 * 2.5))
    axes = axes.reshape(6, 5)

    for i in range(6):
        for j in range(5):
            idx = i * 5 + j
            img = mpimg.imread(folder + '/' + iteration_list[j] + '/' + image_name_list[i])
            axes[i, j].imshow(img)
            axes[i, j].axis("off")
            
            if i == 0 and titles:
                axes[i, j].set_title(titles[j], fontsize=18)

            if j == 0:
                if i % 2 == 0:
                    row_label = f"Test image {i // 2}"
                    fig.text(0.04, 1 - (i + 0.9) / 6, row_label, fontsize=25, va='center', rotation=90)
    plt.tight_layout()
    plt.subplots_adjust(left=0.15, wspace=0.05, hspace=0.05)
    plt.savefig(save_path + '/' + str(type_to) + '_image_grid.png', dpi =300)
    plt.close()

#plot_image_grid(save_path="figure", folder="logs/blender_lego_coarse", type_to="coarse")