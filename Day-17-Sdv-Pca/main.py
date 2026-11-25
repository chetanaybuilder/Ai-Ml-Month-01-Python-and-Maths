import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

# 1. Load images
digits = load_digits()
image = digits.images[0]

# 2. Apply SVD
U, S, VT = np.linalg.svd(image)

# 3. Reconstruct using top 3 components
compressed = U[:, :3] @ np.diag(S[:3]) @ VT[:3, :]

# 4. Apply PCA
X = digits.data

pca = PCA(n_components=10)
X_reduced = pca.fit_transform(X)

# 5. Reconstruct PCA image
X_reconstructed = pca.inverse_transform(X_reduced)
pca_image = X_reconstructed[0].reshape(8, 8)

# 6. Display results
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(compressed, cmap="gray")
plt.title("SVD")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(pca_image, cmap="gray")
plt.title("PCA")
plt.axis("off")

# Save figure instead of blocking on plt.show() so the script
# runs headlessly / in CI environments
output_file = "svd_pca_comparison.png"
plt.tight_layout()
plt.savefig(output_file, dpi=150, bbox_inches="tight")
plt.close()
print(f"Figure saved to: {output_file}")

print("Original features:", X.shape[1])
print("PCA features:", X_reduced.shape[1])
print("PCA variance retained:",
      round(sum(pca.explained_variance_ratio_) * 100, 2), "%")