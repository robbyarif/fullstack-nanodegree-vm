# Item Catalog Project

An item catalog application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

## How to Use

Make sure you have Vagrant and VirtualBox installed. Then open terminal, go to `/vagrant` directory, and launch the Vagrant VM.

```bash
$ vagrant up
...
...
$ vagrant ssh
...
...
```

Navigate to `/vagrant` directory.

```bash
cd /vagrant
```

Then fill in sample data by running

```bash
python sampleitems.py
```

Finally, run the application.

```bash
python application.py
```

Open [http://localhost:8000/](http://localhost:8000/) to access the application.

The application provides a list of items within a variety of categories which can be modified by registered users. The application also provides third party authentication using OAuth.

## License

The MIT License (MIT)
[MIT License](https://opensource.org/licenses/MIT)