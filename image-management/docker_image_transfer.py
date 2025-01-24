import subprocess
import os

# Define the images that you wish to download. Specifiy the repository ,image name and tag 
image_list = [
{'repository': 'docker.io', 'image-name': 'ubuntu','image-tag': 'latest'},
{'repository': 'docker.io', 'image-name': 'python','image-tag': 'alpine'}]

destination_docker_registry = 'zbeda-repo.com:8082/devops/' #make sure that the value will be ended with /
docker_image_folder = '/home/zbeda/'  #make sure that the value will be ended with /
scan_report_folder = '/home/zbeda/' #make sure that the value will be ended with /
missing_images_in_repo = []
missing_image_in_folder = []

def image_pull_save():
    is_folder_exist = os.path.exists(docker_image_folder)
    if not is_folder_exist:
        os.umask(0)
        os.makedirs(docker_image_folder, mode=0o777)
    for image in image_list:
        repo_name = image['repository']
        image_name = image['image-name']
        image_tag = image['image-tag']
        source_docker_location = f'{repo_name}/{image_name}:{image_tag}'
        destination_docker_location = f'{destination_docker_registry}{image_name}:{image_tag}'
        respone_docker_pull = subprocess.run(["docker", "pull",source_docker_location])
        if respone_docker_pull.returncode == 1:
            print(f'{source_docker_location} could not be downloaded from repo')
            missing_images_in_repo.append(f'{repo_name}/{image_name}:{image_tag}')
        else:
             respone_docker_save = subprocess.run(["docker", "save", "--output",docker_image_folder + image_name + "_" + image_tag + ".tar", source_docker_location])
             print(f'image {image_name}:{image_tag} was save in {docker_image_folder}')
    return missing_images_in_repo


def image_load_tag_push():
    for image in image_list:
        repo_name = image['repository']
        image_name = image['image-name']
        image_tag = image['image-tag']
        source_docker_location = f'{repo_name}/{image_name}:{image_tag}'
        destination_docker_location = f'{destination_docker_registry}{image_name}:{image_tag}'
        respone_docker_load = subprocess.run(["docker", "load", "--input", docker_image_folder + image_name + "_" + image_tag + ".tar"])
        if respone_docker_load.returncode == 1:
            print(f'{image_name} could not be found in folder')
            missing_image_in_folder.append(f'{image_name}:{image_tag}')
        else:
             respone_docker_tag = subprocess.run(["docker", "tag", source_docker_location, destination_docker_location])
             respone_docker_push = subprocess.run(["docker", "push", destination_docker_location])
    return missing_image_in_folder


def image_pull_tag_push():
    for image in image_list:
        repo_name = image['repository']
        image_name = image['image-name']
        image_tag = image['image-tag']
        source_docker_location = f'{repo_name}/{image_name}:{image_tag}'
        destination_docker_location = f'{destination_docker_registry}{image_name}:{image_tag}'
        respone_docker_pull = subprocess.run(["docker", "pull",source_docker_location])
        if respone_docker_pull.returncode == 1:
            print(f'{source_docker_location} could not be downloaded from repo')
            missing_images_in_repo.append(f'{repo_name}/{image_name}:{image_tag}')
        else:
             respone_docker_tag = subprocess.run(["docker", "tag", source_docker_location, destination_docker_location])
             respone_docker_push = subprocess.run(["docker", "push", destination_docker_location])
    return missing_images_in_repo

def image_rm_based_on_orignal_repository_name():
    for image in image_list:
        repo_name = image['repository']
        image_name = image['image-name']
        image_tag = image['image-tag']
        source_docker_location = f'{repo_name}/{image_name}:{image_tag}'
        destination_docker_location = f'{destination_docker_registry}{image_name}:{image_tag}'
        respone_docker_rm = subprocess.run(["docker", "image", "rm", source_docker_location])

def image_rm_based_on_destination_repository_name():
    for image in image_list:
        repo_name = image['repository']
        image_name = image['image-name']
        image_tag = image['image-tag']
        source_docker_location = f'{repo_name}/{image_name}:{image_tag}'
        destination_docker_location = f'{destination_docker_registry}{image_name}:{image_tag}'
        respone_docker_rm = subprocess.run(["docker", "image", "rm", source_docker_location])
        respone_docker_rm = subprocess.run(["docker", "image", "rm", destination_docker_location])

def image_pull_save_tag_push():
    is_folder_exist = os.path.exists(docker_image_folder)
    if not is_folder_exist:
        os.umask(0)
        os.makedirs(docker_image_folder, mode=0o777)
    for image in image_list:
        repo_name = image['repository']
        image_name = image['image-name']
        image_tag = image['image-tag']
        source_docker_location = f'{repo_name}/{image_name}:{image_tag}'
        destination_docker_location = f'{destination_docker_registry}{image_name}:{image_tag}'
        respone_docker_pull = subprocess.run(["docker", "pull",source_docker_location])
        if respone_docker_pull.returncode == 1:
            print(f'{source_docker_location} could not be downloaded from repo')
            missing_images_in_repo.append(f'{repo_name}/{image_name}:{image_tag}')
        else:
             respone_docker_save = subprocess.run(["docker", "save", "--output", docker_image_folder + image_name + "_" + image_tag + ".tar",source_docker_location])
             respone_docker_tag = subprocess.run(["docker", "tag", source_docker_location, destination_docker_location])
             respone_docker_push = subprocess.run(["docker", "push", destination_docker_location])
    return missing_images_in_repo

def scan_tar_images():
    is_folder_exist = os.path.exists(scan_report_folder)
    if not is_folder_exist:
        os.umask(0)
        os.makedirs(scan_report_folder, mode=0o777)
    for image in image_list:
        repo_name = image['repository']
        image_name = image['image-name']
        image_tag = image['image-tag']
        print(f'scanning image {image_name}:{image_tag}')
        print('')
        print('')
        trivy_scan = subprocess.run(["trivy", "image", "--debug", "--scanners", "vuln", "-f", "json", "-o",
                                     scan_report_folder + image_name + "_" + image_tag + ".json", "--input",
                                     docker_image_folder + image_name + "_" + image_tag + ".tar"])


def menu():
    print(f'[1] Pull images from the original repository and save it as a tar file - This option is required when images need to be delivered to the site \n'
          f'Please note that upon extraction the tag will be based on the original repository\n'
          f'Please note that the "docker_image_folder" parameters defined the folder path where the image tar should be saved')
    print('')
    print(f'[2] Load images based on tar , tag and push to the required repository - This option is required when images need to upload to the site repository. \n'
          f' Please note that the "destination_docker_location" should be configured with the site repository details\n'
          f'Please note that the "docker_image_folder" parameters defined the folder path of the image tar locations')
    print('')
    print(f'[3] Pull tag and push images to the site repository - This mainly required for lab use, this will pull the images from the origanl repository \n'
          f'Please note that the "destination_docker_location" should be configured with the site repository details')
    print('')
    print(f'[4] Delete images from docker engine on local machine based on original repository name - This option should be run after saving image to disk (option-1')
    print('')
    print(f'[5] Delete images from docker engine on local machine based on destination repository name - This option should be run after loading image from disk (option-2')
    print('')
    print(f'[6] Scan tar images file using trivy - Output will be in json format. Please make sure that trivy is installed on your machine')
    print('')
    print(f'[0] exit program')


menu()
user_option = int(input("Enter your option: "))
if user_option == 1:
    print(f'The images will be pulled based on the defined image_list and the will be saved in under the following path {docker_image_folder}')
    image_pull_save_status = image_pull_save()
    print(f' These are the missing images that could not be download from repo : {image_pull_save_status}')
if user_option == 2:
    print(f'The images will uploaded from {docker_image_folder} folder , tag and push to the {destination_docker_registry} repository')
    image_load_tag_push_status = image_load_tag_push()
    print(f' These are the missing images in folder: {image_load_tag_push_status}')
if user_option == 3:
    print(f'The images will be pulled based on the defined image_list , tag and push to the {destination_docker_registry} repository')
    image_pull_status = image_pull_tag_push()
    print(f' These are the missing images that could not be download from repo : {image_pull_status}')
if user_option == 4:
    image_rm_based_on_orignal_repository_name()
if user_option == 5:
    image_rm_based_on_destination_repository_name()
if user_option == 6:
    scan_tar_images()
