import os
import shutil
import argparse


#Usage
# VASE
# python separate_image.py --dataset_dir val2017 --xml_dir val_xml --class_image vase

# PERSON
# python separate_image.py --dataset_dir val2017 --xml_dir val_xml --class_image tv



parser = argparse.ArgumentParser(description="Separate image by class from image dataset")
parser.add_argument("--dataset_dir", default=".", help="Directory for storing images classes")
parser.add_argument("--xml_dir", default=".", help="Directory of xml references")
parser.add_argument("--class_image", default=None, help="Directory of image dataset")
args = parser.parse_args()


def main():
    main_dir = os.path.join(os.getcwd(),'dataset')
    des_folder = args.dataset_dir + '_image'
    des_dir = os.path.join(main_dir,des_folder + "/" + args.class_image)
    print(des_dir)
    if not os.path.exists(des_dir):
        os.makedirs(des_dir)
    xml_folder = args.xml_dir + '/' + args.class_image
    list_src = os.listdir(os.path.join(main_dir,xml_folder))
    for file in list_src:
        name_file,type_file = file.split(".")
        name_file = name_file + ".jpg"
        src = os.path.join(main_dir + '/ms_coco/' + args.dataset_dir,name_file)
        des = os.path.join(des_dir,name_file)
        shutil.copyfile(src,des)
        print("copied "+name_file)
	


if __name__ == '__main__':
    main()
