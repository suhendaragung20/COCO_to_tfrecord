import os
import shutil
import argparse


#Usage
# VASE
# separate_image.py --dataset_dir val2017 --class_image vase

# PERSON
# separate_image.py --dataset_dir val2017 --class_image tv



parser = argparse.ArgumentParser(description="Separate image by class from image dataset")
parser.add_argument("--dataset_dir", default=".", help="Directory for storing images classes")
parser.add_argument("--class_image", default=None, help="Directory of image dataset")
args = parser.parse_args()


def main():
	main_dir = 'E:/DDS_Telkom/Task_3/Dataset_to_VOC_converter-master/dataset/'
	list_src = os.listdir(main_dir + 'val_xml/' + args.class_image)
	for file in list_src:
		name_file,type_file = file.split(".")
		name_file = name_file + ".jpg"
		src = os.path.join(main_dir + 'ms_coco/' + args.dataset_dir,name_file)
		des = os.path.join(main_dir + 'val_image/' + args.class_image,name_file)
		shutil.copyfile(src,des)
		print("copied "+name_file)


if __name__ == '__main__':
    main()