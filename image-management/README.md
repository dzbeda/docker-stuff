
# Docker Image Transfer Script

This Python script simplifies Docker image management tasks such as pulling, saving, tagging, pushing, deleting, and scanning Docker images. It is particularly useful for transferring images from online environments to **air-gapped** environments where direct internet access is unavailable.

---

## Features

The script supports the following functionalities:

1. **Pull and Save Docker Images as TAR Files**

   - Pull images from a source Docker registry and save them as TAR files.
   - Ideal for moving images to air-gapped environments.

2. **Load, Tag, and Push Docker Images**

   - Load images from TAR files, tag them, and push them to a destination Docker registry.

3. **Pull, Tag, and Push Docker Images Directly**

   - Pull images from the source registry, tag them, and push them to the destination registry.

4. **Delete Images by Original Repository Name**

   - Remove images from the local Docker engine based on their original repository name.

5. **Delete Images by Destination Repository Name**

   - Remove images from the local Docker engine based on their destination repository name.

6. **Scan TAR Images with Trivy**

   - Scan TAR files for vulnerabilities using **Trivy** and save JSON reports.

---

## Prerequisites

1. **Python 3.x**   Ensure Python is installed on your system.

2. **Docker**   Docker must be installed and running on your system.

3. **Trivy** (Optional, for Image Scanning)   Install Trivy for vulnerability scanning.   Installation guide: [https://github.com/aquasecurity/trivy](https://github.com/aquasecurity/trivy)

---

## Configuration

Before running the script, configure the following parameters in `docker_image_transfer.py`:

### `image_list`

Define the list of images to manage.Each image entry should include the repository, image name, and tag. Example:

```python
image_list = [
    {'repository': 'docker.io', 'image-name': 'ubuntu', 'image-tag': 'latest'},
    {'repository': 'docker.io', 'image-name': 'python', 'image-tag': 'alpine'}
]
```

### `destination_docker_registry`

The destination Docker registry URL where images will be pushed. Ensure it ends with a `/`.Example: `zbeda-repo.com:8082/devops/`

### `docker_image_folder`

The folder where TAR files will be saved or loaded. Ensure it ends with a `/`.Example: `/home/zbeda/`

### `scan_report_folder`

The folder where Trivy scan reports will be saved. Ensure it ends with a `/`.Example: `/home/zbeda/`

---

## How to Use the Script

1. Run the script in a Python-supported environment.

2. The script displays a menu with six options:

   [1] Pull images from the original repository and save them as TAR files.   [2] Load TAR files, tag images, and push them to the destination repository.   [3] Pull, tag, and push images directly to the destination repository.   [4] Delete images from the local Docker engine by original repository name.   [5] Delete images from the local Docker engine by destination repository name.   [6] Scan TAR image files using Trivy.

3. Select an option by entering the corresponding number.

4. Follow the prompts displayed by the script.

---

## Reference Blog

For a detailed explanation of how to create an air-gapped repository for RedHat-based systems, refer to the following blog post:

[Install Your Own Air-Gapped Offline Repository Based on RedHat Distribution](https://medium.com/@dudu.zbeda_13698/how-to-set-up-an-air-gapped-yum-repository-for-redhat-based-systems-ff76afe48640)

---

## Repository Link

You can access this repository here:[Install Offline YUM Repository Server Repository](#)

---

## Connect on LinkedIn and on Medium

Stay updated on more guides and insights related to Linux, DevOps, and system integration. For updates, please follow me on:

- **LinkedIn**: [www.linkedin.com/in/davidzbeda](https://www.linkedin.com/in/davidzbeda)
- **Medium**: [https://medium.com/@david-dudu-zbeda](https://medium.com/@david-dudu-zbeda)

