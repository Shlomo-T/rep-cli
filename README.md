# Rep-cli
A cli tool that use Censys services for researching websites by ipv4 addresses and domains.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Installing

Clone the source code from github:

```
git clone git@github.com:Shlomo-T/rep-cli.git
```

Go and pip install it into virtual environment:

```
cd rep-cli
virtualenv venv
pip install .
```

### How to use
After installation check that rep cli is really working, you should see short explanation about rep and rep commands
```
rep
```

First step when working with rep is to configure Censys credentials, rep expecting to receive them in the format of
 <api-id>|<api-secret>
```
rep configure 'api-id|api-secret'
```

After credentials have been set 'scan' command is available and you can scan domains and ipv4 addresses.
The result should retrieve the website title and top 10 keywords that by default would be saved to cache for 10 min.
In order to prevent caching use --nocache flag and set it to true
```
rep scan google.com --nocache=true
```

You can clear all the results from the cache by using clear_cache command
```
rep clear_cache
```

## Authors

* **Shlomo Tadela** - *projects* - [Shlomo-T](https://github.com/Shlomo-T/)

