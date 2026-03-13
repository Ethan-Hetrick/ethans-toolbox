# Using Singularity to run Rstudio from HPC

Below are general instructions for running RStudio Server inside a Singularity container on an HPC system and accessing it from your local browser through SSH port forwarding.

This example uses the `rocker/tidyverse` image and starts RStudio so it listens only on `127.0.0.1` on the remote system.

## Pull the image

```bash
singularity pull --name rstudio.simg docker://rocker/tidyverse:latest
```

## Minimal launch script

Save the following as `launch-rstudio.sh`:

```bash
mkdir -p "$HOME/rstudio/etc"
mkdir -p "$HOME/rstudio/varlib"
mkdir -p "$HOME/rstudio/run"
touch "$HOME/rstudio/etc/database.conf"

PASSWORD=test singularity exec \
  --home "$HOME" \
  --bind "$HOME/rstudio/etc:/etc/rstudio" \
  --bind "$HOME/rstudio/varlib:/var/lib/rstudio-server" \
  --bind "$HOME/rstudio/run:/var/run/rstudio-server" \
  rstudio.simg rserver \
  --server-user "$USER" \
  --www-address=127.0.0.1 \
  --www-port=8787
```

Then run it on the HPC system:

```bash
bash launch-rstudio.sh
```

If the command starts successfully, it will remain in the foreground and keep the RStudio Server process running.

## Tunnel from your local machine

From your **local computer**, open an SSH tunnel to the HPC system:

```bash
ssh -L 8787:127.0.0.1:8787 your_username@your_hpc_host
```

Then open in your browser:

```text
http://localhost:8787
```

Login with your HPC username and the password you set in `PASSWORD=`.

## Notes

* Replace `your_username@your_hpc_host` with your actual HPC login.
* Keep the terminal running `launch-rstudio.sh` open while you use RStudio.
* Keep the SSH tunnel session open while connected in your browser.
* Change `PASSWORD=test` to a stronger password before regular use.
* If port `8787` is already in use, change it in both the launch script and the SSH tunnel command.
* Some HPC systems require launching long-running applications from an interactive job rather than a login node.
