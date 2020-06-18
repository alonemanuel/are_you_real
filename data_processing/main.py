from data_processing.dataset_manager import DatasetManager

BASE_DIR_PATH = 'G:\My Drive\projects\\are_you_real\samples\instagram_scrape'
def main():
    dataset_builder = DatasetManager(BASE_DIR_PATH)
    dataset_builder.init_dataset()


if __name__ == '__main__':
    main()
