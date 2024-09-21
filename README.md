# Remote Printer V1.0

This service automatically prints attachments from a specific email inbox using an IMAP SSL connection and CUPS (Common Unix Printing System).

## Before installation

First, you need to have a CUPS server installed on the host machine, with a default printer set that allows printing by simply using the `lp` command. There's plenty of documentation available on how to do this.

Next, download this repository and create an `.env` file in the root folder of the project with the following environment variables:

```dotenv
EMAIL_SERVER=youremail.serverurl.com
EMAIL_ADDRESS=youremail@address.com
EMAIL_PASSWORD=yourgreatpassword
```

That's it!

## Installation
### Docker

The Docker Compose file uses a network called `local` to spin up the container, which you likely don't have. You can create it by typing `sudo docker network create local` or change the name of the network in `docker-compose.yml` to match a network of your choice.

Once the network is ready, go the root folder of the project and simply run:

```shell
sudo docker compose up -d
```

### Linux

Make sure that Python and Pip are installed in the machine by running `python --version` and `pip --version`. Then, go the root folder of the project and run:

```shell
# Create the environment  
python -m venv env
# Activate the environment  
source env/bin/activate
# Install dependencies  
pip install -r requirements.txt
# Launch the service  
python main.py
```

## Limitations

Because this app uses basic authentication, you may encounter issues when using Gmail or Outlook email addresses. To work around this, you'll need to modify the code in `inbox/connect.py` and use more advanced authentication.