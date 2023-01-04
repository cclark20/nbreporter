import os
from tqdm import tqdm
from .my_parser import parse_args, validate_args
from ..reporter import generate_report

def main() -> None:
    args = parse_args()
    validate_args(args)
    if args.input_dir:
        input_yamls = sorted([file for file in os.listdir(args.input_dir) if file.endswith('.yaml')])
        if len(input_yamls) == 0:
            raise Exception(f"Could not find input yamls in --input_dir {args.input_dir} or they don't exist.")
        print(input_yamls)
        for file in tqdm(input_yamls):
            args.input_file = f'{args.input_dir}/{file}'
            generate_report(args)
    else:
        generate_report(args)

    return None

if __name__ == '__main__':
    main()