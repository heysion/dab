# dab
deepin auto build tools platform

# dmd
deepin build  maker discs tools  platform

## init db
```
git clone https://github.com/heysion/deepin-auto-build.git
cd deepin-auto-build/dab
python manager.py --initdir
python manager.py --initdb
```

## run

```
git clone https://github.com/heysion/deepin-auto-build.git
cd deepin-auto-build
git checkout heysion@v2
virtualenv -p python3 env
source  env/bin/activate
python setup.py install
cd -
pip install -r requirements.txt
python app.py
```

## test

chrome http://127.0.0.1:8000/newtask

