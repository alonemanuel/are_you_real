import csv
import os
import pickle

from data_processing.sample_item import SampleItem

PICKLE_NAME = 'ig_dataset.pickle'
SCRAPE_EXT = 'scrape'
ORIG_IM_DIR_EXT = 'origim'
IMAGE_URL_CSV_INDEX = 5


class DatasetManager:

    def __init__(self, base_dir_abspath):
        self.base_dir_abspath = base_dir_abspath
        self.init_pickle()
        self.all_samples_dict = dict()
        self.init_dict()

    def init_dict(self):
        with open(self.pickle_abspath, 'rb') as pickle_infile:
            self.all_samples_dict = pickle.load(pickle_infile)
        print(
            f"Unpickled dataset_dict of length: {len(self.all_samples_dict)}\n"
            f"\tWith first entry being: ")

    def init_pickle(self):
        self.pickle_abspath = os.path.join(self.base_dir_abspath, PICKLE_NAME)
        if not os.path.isfile(self.pickle_abspath):
            with open(self.pickle_abspath, 'w+b') as pickle_outfile:
                pickle.dump(dict(), pickle_outfile)

    def get_csv_file_abspath(self, dir_name):
        csv_folder_base_name = f'{dir_name}_{SCRAPE_EXT}'
        csv_folder_abspath = os.path.join(self.base_dir_abspath, dir_name, csv_folder_base_name)
        assert os.path.isdir(csv_folder_abspath)
        files_in_csv_folder = os.listdir(csv_folder_abspath)
        assert len(files_in_csv_folder) == 1
        csv_file_abspath = os.path.join(csv_folder_abspath, files_in_csv_folder[0])
        assert os.path.isfile(csv_file_abspath)
        return csv_file_abspath

    def get_orig_images_dir_abspath(self, dir_name):
        orig_images_dir_basename = f'{dir_name}_{ORIG_IM_DIR_EXT}'
        orig_images_dir_abspath = os.path.join(self.base_dir_abspath, orig_images_dir_basename)
        os.makedirs(orig_images_dir_abspath, exist_ok=True)
        return orig_images_dir_abspath

    def get_sample_id(self, dir_name, sample_n):
        sample_id = f'{dir_name}_{sample_n}'
        return sample_id

    def init_dataset(self):
        """
        Assuming initial directory hierarchy of:

        |- base_dir_path (scrape folder)
        |--- tag_name_0
        |--- tag_name_1
        ...
        |--- tag_name_2
        |------- tag_name_2_scrape
        """
        for dir_name in os.listdir(self.base_dir_abspath):
            if not os.path.isdir(os.path.join(self.base_dir_abspath, dir_name)):
                continue  # skip pickle

            print(f'\nProcessing dir: {dir_name}...')
            csv_file_abspath = self.get_csv_file_abspath(dir_name)

            with open(csv_file_abspath, 'r', encoding='utf8') as csv_file:
                reader = csv.reader(csv_file)
                next(reader)  # skip headers
                for item_n, line in enumerate(reader):
                    sample_id = self.get_sample_id(dir_name, item_n)
                    if sample_id in self.all_samples_dict.keys():
                        print(f'Passing on sample: {sample_id}')
                    else:
                        print(f'Processing sample: {sample_id}')
                        orig_image_url = line[IMAGE_URL_CSV_INDEX]
                        sample_item = SampleItem(self.base_dir_abspath, dir_name, csv_file_abspath, orig_image_url)
                        self.all_samples_dict[sample_id] = sample_item

            self.pickle_dict()

    def pickle_dict(self):
        print('Pickling dir...')
        with open(self.pickle_abspath, 'w+b') as pickle_outfile:
            pickle.dump(self.all_samples_dict, pickle_outfile)
