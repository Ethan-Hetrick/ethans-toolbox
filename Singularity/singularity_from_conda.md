# How to create a Singularity image from a Conda environment

Sometimes it's helpful to containerize a working Conda environment for portability and reproducibility, especially when there are no pre-existing public containers available. Since these are sometimes tricky to set-up, I have created the following document.

## Step 1: Create a conda environment

```bash
# Create environment
conda create -n <name> <packages>

# Install any additional dependencies
conda install <packages>

# Export environment as yaml
conda env export > <environment>.yml
```

> Note: You will want to remove the `Prefix:` line in the yaml file

## Step 2: Create the Singularity definition (def) file

### Description of each def file element

The Singularity def file is a set of instructions for Singularity to build an image. This is similar to a Dockerfile in Docker. The following is a breakdown of each section of the Singularity def file needed to containerize a conda environment.

1. `Bootstrap` and `From`

```plaintext
Bootstrap: docker
From: continuumio/miniconda3:24.5.0-0
```

- Bootstrap: Specifies the bootstrap method to use for building the container. In this case, we're using Docker as the base for our Singularity container.
- From: Indicates the base Docker image to use. Here, we use the continuumio/miniconda3 image, which is a lightweight image with Miniconda installed. The tag 24.5.0-0 specifies the exact version of the Miniconda image.

2. `%help`

```plaintext
%help
    <insert container description>.
```

- %help: This section provides a description of the container. This text is displayed when the user runs singularity help on the container.

3. `%labels`

```plaintext
%labels
    Maintainer "<name> <email>"
    Version "<version>"
    Description   "<container description"
    Software      "<software name>"
    BaseImage     "continuumio/miniconda3:24.5.0-0"
    Date          "<insert date>"
    URL           "<insert URL>"
```

- Maintainer: Specifies the person responsible for the container.
- Version: Version of the container.
- Description: A brief description of the container's purpose.
- Software: The main software included in the container.
- BaseImage: The base image used for the container.
- Date: The date the container was created.
- URL: A link to the project's source or documentation.

4. `%$%environment`

```plaintext
%environment
    export CONDA_ENV=/opt/conda/envs/<environment>
```
- %environment: Sets environment variables that are available when the container is run.
    - CONDA_ENV: Defines the path to the Conda environment inside the container. This environment will be used by default when the container is executed.

5. `%files`

```plaintext
%files
    <optional add directories, files or binaries>
    <environment>.yml /opt/<enviornment>.yml
```

- %files: Copies files or directories from the host system into the container.
    - The first line copies the entire neissflow directory from a specified path on the host to /opt/neissflow in the container.
    - The second line copies a YAML file, <environment>.yml, which is used to create the Conda environmesnt, to /opt/<environment>.yml inside the container.

6. `%post`

```plaintext
%post
    # Create the Conda environment from the YML file
    conda env create -f /opt/<environment>.yml --prefix /opt/conda/envs/<environment>

    # Configure PATH
    echo "export PATH=/opt/<environment>/bin:$PATH" >> /environment

    # Clean up
    conda clean --all -y
    pip cache purge
```

- %post: Contains commands that are run during the container build process. This section is used to set up the environment and install software.
    - Create Conda environment: Uses the<environment>.yml file to create a new Conda environment at /opt/conda/envs/<environment>.
    - Configure PATH: Adds the paths to the binaries to the system PATH by appending the configuration to the /environment file.
    - Clean up: Cleans up Conda caches to reduce the size of the container.

7. `%runscript`

```plaintext
%runscript
    eval "$(conda shell.bash hook)"
    conda activate $CONDA_ENV
    exec "$@"
```

- %runscript: Defines the default command to run when the container is executed. This script is useful for setting up the environment before running any user commands.
    - Activate Conda environment: Initializes Conda for the bash shell and activates the specified Conda environment.
    - Execute the command: Uses exec "$@" to run any command passed to the container
 
### Final Singularity def file template

```plaintext
Bootstrap: docker
From: continuumio/miniconda3:24.5.0-0

%help
    <container description>

%labels
    Maintainer "<name> <email>"
    Version "<version>"
    Description   "<container description>"
    Software      "<container name>"
    BaseImage     "continuumio/miniconda3:24.5.0-0"
    Date          "<date>"
    URL           "<URL to documentation>"

%environment
    export CONDA_ENV=/opt/conda/envs/<environment>

%files
    <files to copy> /opt/

    <environment>.yml /opt/<environment>.yml

%post
    # Create the Conda environment from the YML file
    conda env create -f /opt/<environment>.yml --prefix /opt/conda/envs/<environment>

    # Configure PATH
    echo "export PATH=/opt/<environment>/bin:$PATH" >> /environment

    # Clean up
    conda clean --all -y
    pip cache purge

%runscript
    eval "$(conda shell.bash hook)"
    conda activate $CONDA_ENV
    exec "$@"
```

## Building the Singularity image

```bash
# Build Singularity image
sudo singularity build <environment>.sif <environment>.def
singularity inspect <environment>.sif

# Test it out!
singularity run <environment>.sif \
    <program> \
    <options>
```
