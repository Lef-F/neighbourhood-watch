def main(img_path: str, model_name: str, crop: bool) -> None:
    import torch

    # Model
    model = torch.hub.load(
        repo_or_dir="ultralytics/yolov5",
        model=model_name,
    )

    # Inference
    results = model(img_path)

    for result in results.pandas().xyxyn:
        df = result
        print(df)

    if crop:
        results.crop()


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument(
        "--img-path",
        help="Path to the image to be recognized. Can be URL or full path to file.",
    )
    parser.add_argument(
        "--model-name",
        default="yolov5n",
        required=False,
        help="Model name to be used. Can be any model in the repo. Default is yolov5n.",
    )
    parser.add_argument(
        "--crop",
        action="store_true",
        default=False,
        required=False,
        help="Whether to crop the image to the bounding box of the object.",
    )

    args = parser.parse_args()
    main(
        img_path=args.img_path,
        model_name=args.model_name,
        crop=args.crop,
    )
