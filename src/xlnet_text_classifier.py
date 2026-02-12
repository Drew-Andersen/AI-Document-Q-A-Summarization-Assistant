from transformers import pipeline


def load_classifier():
    # Load a text classification pipline using XLNet
    classifier = pipeline(
        task="text-classification",
        model="xlnet-base-cased",
        tokenizer="xlnet-base-cased"
    )
    return classifier


def classify_text(classifier, text):
    # Classify input text and return prediction
    result = classifier(text)
    return result


def main():
    classifier = load_classifier()

    print("XLNet Text Classifier")
    print("-" * 50)

    sample_texts = [
        "I absolutely love this product. It works perfectly!",
        "This is the worst experience I have ever had.",
        "The movie was okay, not great but not terrible either."
    ]

    for text in sample_texts:
        prediction = classify_text(classifier, text)[0]

        label = prediction["label"]
        confidence = prediction["score"]

        print(f"\nText: {text}")
        print(f"Predicted Label: {label}")
        print(f"Confidence Score: {confidence:.4f}")


if __name__ == "__main__":
    main()
