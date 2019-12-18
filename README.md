### README

#### Dev environment setup (Ubuntu 18 LTS)

For purpose of this exercise we will use

1. Install requirements described in localstack README:
https://github.com/localstack/localstack
At point of writing they are:
* python (both Python 2.x and 3.x supported)
* pip (python package manager)
If you are developing in Python you can use Anaconda distribution which includes multiple common packages:
https://docs.anaconda.com/anaconda/install/linux/
```bash
bash ~/Downloads/Anaconda3-2019.10-Linux-x86_64.sh
```
If there is no hard dependency on Python 3.7 install pip, alternatively refer to following StackOverflow question:
https://stackoverflow.com/questions/54633657/how-to-install-pip-for-python-3-7-on-ubuntu-18
```bash
sudo apt-get update
sudo apt install python3-pip
```
* Docker:
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
apt-cache policy docker-ce
sudo apt-get install -y docker-ce
sudo systemctl status docker
sudo usermod -aG docker ${USER}
su - ${USER}
```

2. Install localstack:
```bash
pip install localstack
```
If you have older packages you might get errors during installation, re-install/update packages per error message
`awscli 1.15.17 has requirement botocore==1.10.17, but you'll have botocore 1.13.41 which is incompatible.`

3. Start localstack:
```bash
localstack start
```

4. Verify from browser that localstack is running by browsing to:
http://0.0.0.0:8080/#!/infra

#### References

* AWS whitepaper overview:
https://d0.awsstatic.com/whitepapers/whitepaper-streaming-data-solutions-on-aws-with-amazon-kinesis.pdf
