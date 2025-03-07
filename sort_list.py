from __future__ import annotations

import argparse
import logging


def main(args):
    item_list = []
    with open(args.input, "r") as fp:
        while True:
            aline = fp.readline()
            if not aline:
                break
            if aline.startswith("- http"):
                item = {}
                item["lines"] = [aline]
                while True:
                    aline = fp.readline()
                    if not aline:
                        break
                    elif aline == "\n":
                        item["name"] = item["lines"][-1].replace("[", "")
                        item["lines"].append("\n")
                        item_list.append(item)
                        break
                    else:
                        item["lines"].append(aline)

    sorted_item_list = sorted(item_list, key=lambda item: item["name"].lower())
    for k in sorted_item_list:
        logging.info("".join(k["lines"]))


def cli():
    parse = argparse.ArgumentParser()
    parse.add_argument("--input", type=str, help="input file", default="tmp.md")
    parse.add_argument("--output", "-o", type=str, help="output file")

    _args = parse.parse_args()

    if not _args.output:
        _args.output = f"{_args.input}.sort_list.md"

    print(_args)

    file_handler = logging.FileHandler(_args.output, mode="w")
    file_handler.setLevel(logging.INFO)
    # manually deal terminator
    file_handler.terminator = ""
    logging.basicConfig(
        handlers=[file_handler], level=logging.INFO, format="%(message)s"
    )

    main(_args)


if __name__ == "__main__":
    cli()
