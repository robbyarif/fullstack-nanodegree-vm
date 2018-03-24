# Item Catalog Project

An item catalog application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## Prerequisites

Make sure you have Vagrant and VirtualBox installed. Clone this repository, then open terminal, go to `vagrant` directory, and launch the Vagrant VM.

```bash
vagrant up
```

Then run `vagrant ssh`

```bash
vagrant ssh
```

## How to Use

After logging in to vagrant navigate to the shared `/vagrant` directory and then navigate to `/catalog` directory for this project.

```bash
cd /vagrant
cd catalog
```

Run database initialization first.

```bash
python database_setup.py
```

Then fill in sample data by running

```bash
python lotsofitems.py
```

Finally, run the application.

```bash
python application.py
```

Open [http://localhost:8000/](http://localhost:8000/) to access the application.

The application provides a list of items within a variety of categories which can be modified by registered users. The application also provides third party authentication using Google Plus OAuth.

## License

The MIT License (MIT)
[MIT License](https://opensource.org/licenses/MIT)