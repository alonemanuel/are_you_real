class SampleItem:
    base_dir_abspath = None

    def __init__(self, base_dir_abspath, sample_class, csv_abspath, orig_image_url):
        self.base_dir_abspath = base_dir_abspath
        self.sample_class = sample_class
        self.csv_abspath = csv_abspath
        self.orig_image_url = orig_image_url
        self.orig_image_path = None
        self.face_path = None

    def url_to_orig_image(self):
        pass
        # try:
        #     urllib.request.urlretrieve(image_url, output_absfn)
        #     print(f"Found url for: {sample_id}")
        # except Exception as e:
        #     print(f"Couldn't find url for: {sample_id}, error:\n{e}")

    def orig_image_to_face(self):
        pass

    def align_face(self):
        pass
