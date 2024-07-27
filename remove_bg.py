import sys
from PIL import Image # type: ignore
from rembg import remove # type: ignore


def remove_background(input_path,output_path):
    try:
        input_image = Image.open(input_path)

        output_image = remove(input_image)

        output_image.save(output_path)

        print(f"Background removed succceefully.saved to {output_path}")
    except Exception as e:
        print(f"an error ocured:{e}")




if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage:python remove_bg.py")
        sys.exit(1)



    input_path = sys.argv[1]
    output_path = sys.argv[2]


    remove_background(input_path,output_path)
