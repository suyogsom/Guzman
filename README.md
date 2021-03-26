# Full stack assignment

### How To Run
1. Clone the repository to local machine:
```
git clone 
```

2. Install `virtualenv`:
```
$ pip install virtualenv
```

3. Open a terminal in the project root directory and run:
```
$ virtualenv env
```

4. Then run the command:
```
$ .\env\Scripts\activate
```

5. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

6. Finally start the web server:
```
$ (env) python app.py
```

The server will start on port 5000 by default. To change this in `app.py` please change the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```