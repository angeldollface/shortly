# SHORTLY :chains: :earth_americas:

***A small Django-powered app to shorten long-ass URLs. :ribbon: :scroll:***

## ABOUT :books:

Since sending links around the WWW has become something of a ubiquitous activity, I thought I'd write a small Django-powered app in Python that makes this easy and fun.

## USAGE

### Requirements

make sure you have the following tools installed and available from the command line:

- [Python](https://python.org)
- [Git](https://git-scm.org)

### Steps

To run this app on your own machine, execute these steps:

- 1.) Get the source code:

```bash
git clone https://github.com/angeldollface/shortly
````

- 2.) Install `virtualenv`:

```bash
python3 -m pip install virtualenv
```

- 3.) Change directory into *Blogly*'s root:

```bash
cd shortly
````

- 4.) Create a new virtual environment here:

```bash
python3 -m venv .
```

- 5.) Activate the virtual environment (The command below is for `*nix` systems. Do the equivalent for this on Windows.):

```bash
source bin/activate
```

- 6.) Install the project's dependencies:

```bash
python -m pip install -r requirements.txt
```

- 7.) Setup the database migrations:

```bash
python manage.py --run-syncdb
```

- 8.) Setup a superuser account:

```bash
python manage.py createsuperuser
```

- 9.) Run the local development server:

```bash
python manage.py runserver
```

- 10.) Type in a URL in the top field.

- 11.) Name your URL in the bottom field.

- 12.) You will be redirected to a URL overview page. This page will display some information. The first thing will be the name, when you submitted your URL, then the URL you submitted, and finally, your shortened URL.

- 13.) Enjoy. :heart:


## CHANGELOG :black_nib:

### Version 1.0.0

- Initial release.
- Upload to GitHub.

## NOTE :scroll:

- *Shortly :chains: :earth_americas:* by Alexander Abraham :black_heart: a.k.a. *"Angel Dollface" :dolls: :ribbon:*
- Licensed under the MIT license.