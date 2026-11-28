"""
Day 20 Weekly Project: Eigenfaces - PCA Face Recognizer
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_olivetti_faces
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


def load_data():
    """Download/load the public Olivetti benchmark face dataset."""
    print("Loading Olivetti Faces dataset...")
    dataset = fetch_olivetti_faces(shuffle=True, random_state=42)
    return dataset.data, dataset.target, dataset.images


def show_sample_faces(images, labels):
    """Save a small sample of dataset images."""
    fig, axes = plt.subplots(2, 5, figsize=(9, 4))
    for ax, image, label in zip(axes.flat, images[:10], labels[:10]):
        ax.imshow(image, cmap="gray")
        ax.set_title(f"Person {label}")
        ax.axis("off")
    fig.suptitle("Sample images from Olivetti Faces")
    fig.tight_layout()
    output = RESULTS_DIR / "sample_faces.png"
    fig.savefig(output, dpi=150)
    plt.close(fig)
    print(f"Saved sample images: {output}")


def run_experiment(X_train, X_test, y_train, y_test):
    """Train a PCA + KNN pipeline for each component count."""
    component_counts = [10, 20, 30, 50, 100]
    accuracies = []

    for n_components in component_counts:
        model = make_pipeline(
            StandardScaler(),
            PCA(n_components=n_components, random_state=42),
            KNeighborsClassifier(n_neighbors=3),
        )
        model.fit(X_train, y_train)
        accuracy = model.score(X_test, y_test)
        accuracies.append(accuracy)
        print(
            f"PCA components: {n_components:3d} | "
            f"Test accuracy: {accuracy * 100:.2f}%"
        )

    return component_counts, accuracies


def save_accuracy_plot(component_counts, accuracies):
    """Plot measured test accuracy against PCA component count."""
    plt.figure(figsize=(8, 5))
    plt.plot(
        component_counts,
        np.array(accuracies) * 100,
        marker="o",
        linewidth=2,
    )
    plt.title("Eigenfaces: Accuracy vs PCA Components")
    plt.xlabel("Number of PCA components")
    plt.ylabel("Test accuracy (%)")
    plt.xticks(component_counts)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    output = RESULTS_DIR / "accuracy_vs_components.png"
    plt.savefig(output, dpi=160)
    plt.close()
    print(f"\nSaved accuracy graph: {output}")


def main():
    X, y, images = load_data()
    print(f"Images: {X.shape[0]}")
    print(f"Pixels per image: {X.shape[1]}")
    print(f"People/classes: {len(np.unique(y))}")

    show_sample_faces(images, y)

    # Keep the same stratified split for every PCA experiment.
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y,
    )

    component_counts, accuracies = run_experiment(
        X_train, X_test, y_train, y_test
    )
    save_accuracy_plot(component_counts, accuracies)

    best_index = int(np.argmax(accuracies))
    print(
        "\nBest result in this experiment: "
        f"{component_counts[best_index]} components, "
        f"{accuracies[best_index] * 100:.2f}% accuracy"
    )
    print("\nDone. Check the results/ folder.")


if __name__ == "__main__":
    main()
