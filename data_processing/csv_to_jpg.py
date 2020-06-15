## Assuming a csv file has:
## Image Name (ImageID) in column 1 (line[0])
## Full Resolution URL (OriginalURL) in column 3 (line[2])

import sys
import urllib.request
from csv import reader
import os.path

# folder containing directories per instagram hashtag
# e.g. 
SCRAPE_FOLDERS_PATH = "G:\My Drive\projects\\are_you_real\samples\instagram_scrape"


csv_filename = os.path.join('..', 'samples', 'instagram_scrape', 'blogger_girl',
                            'dataset_my-task_2020-06-15_14-05-27-033') if len(sys.argv) < 2 else sys.argv[1]
DISPLAY_URL_INDEX = 5

with open(csv_filename + ".csv".format(csv_filename), 'r', encoding="utf8") as csv_file:
    reader = reader(csv_file)
    next(reader)
    for item_n, line in enumerate(reader):
        print(f'processing item {item_n}')

        image_url = line[DISPLAY_URL_INDEX]
        if os.path.isfile("fullres/" + line[DISPLAY_URL_INDEX] + ".jpg"):
            print("Image skipped for {0}".format(line[0]))
        else:
            try:
                fn_save_path = (os.path.join('..', 'samples', 'instagram_scrape', 'blogger_girl', "fullres"))
                urllib.request.urlretrieve(image_url, os.path.join(os.path.join(fn_save_path, f'{item_n}.jpg')))
                print("Image saved for {0}".format(image_url))
            except Exception as e:
                print(f"No result for {image_url}, error:\n{e}")
