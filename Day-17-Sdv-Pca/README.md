# Day-17: SVD vs PCA — Image Compression & Dimensionality Reduction

A hands-on exploration of **Singular Value Decomposition (SVD)** and **Principal Component Analysis (PCA)** applied to the scikit-learn digits dataset. This project compresses an 8×8 handwritten-digit image with SVD and reduces the full 64-dimensional digit dataset to 10 principal components with PCA, visualizing the reconstruction quality and variance retention.

## 📂 Project Structure

```
Day-17-Sdv-Pca/
├── main.py              # SVD image compression + PCA dimensionality reduction script
├── requirements.txt     # Python dependencies
├── .gitignore           # Git ignore rules
├── README.md            # This file
└── svd_pca_comparison.png   # Generated comparison figure (Original | SVD | PCA)
```

## 🎯 Objectives

- Apply **SVD** to a single 8×8 grayscale digit image and reconstruct it using the top 3 singular components.
- Apply **PCA** to the full digits dataset (64 features → 10 components) and reconstruct the first digit.
- Compare **Original**, **SVD-compressed**, and **PCA-reconstructed** images side by side.
- Report dimensionality reduction and the percentage of variance retained by PCA.

## 📦 Requirements

| Package | Version |
|---------|---------|
| Python  | 3.14+   |
| numpy   | 2.5.0   |
| matplotlib | 3.11.0 |
| scikit-learn | 1.9.1 |

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the script:

```bash
python main.py
```

Expected output:

```
Figure saved to: svd_pca_comparison.png
Original features: 64
PCA features: 10
PCA variance retained: 73.82 %
```

The script generates `svd_pca_comparison.png`, a side-by-side visualization of:

| Panel | Description |
|-------|-------------|
| Original | The raw 8×8 digit image from `sklearn.datasets.load_digits` |
| SVD | Reconstruction using the top 3 singular components (`U[:, :3] @ diag(S[:3]) @ VT[:3, :]`) |
| PCA | Reconstruction after projecting onto 10 principal components and inverting the transform |

## 🔬 How It Works

### SVD (Single Image)
1. Load the first digit image (`8×8` pixels).
2. Compute the full SVD: `U, S, VT = np.linalg.svd(image)`.
3. Truncate to the top 3 components and reconstruct:
   $$ \text{compressed} = U_{[:,:3]} \, \Sigma_{[:3]} \, VT_{[:3,:]} $$

### PCA (Full Dataset)
1. Flatten all digit images into a feature matrix `X` of shape `(n_samples, 64)`.
2. Fit `sklearn.decomposition.PCA(n_components=10)`.
3. Project to 10 principal components and reconstruct via `inverse_transform`.
4. Reshape the first reconstructed sample back to `8×8` for visualization.

## 📊 Results

- **Original dimensionality:** 64 features per image
- **PCA reduced dimensionality:** 10 features (~84% reduction)
- **Variance retained by 10 components:** ~73.82%

## 🛠 Customization

Edit `main.py` to experiment:

```python
# SVD: change number of components
compressed = U[:, :k] @ np.diag(S[:k]) @ VT[:k, :]

# PCA: change number of components
pca = PCA(n_components=k)
```

## 🧪 Testing

Verify the environment and run:

```bash
python -c "import numpy, matplotlib, sklearn; print('deps OK')"
python main.py
```

A successful run prints the feature/variance stats and writes `svd_pca_comparison.png` to the project folder.

## 📜 License

This project is for educational purposes (Day-17 AI/ML practice).

---
*Built with Python, NumPy, Matplotlib, and scikit-learn.*