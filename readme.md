Скрипт показывает погоду в терминале используя сервис [wttr.in](https://wttr.in).


### Install

```
git clone https://github.com/RNDpacman/weather_console.git
```

```
python -m venv ./weather_console/venv
```

```
cd ./weather_console
```

```
source ./venv/bin/activate
```

```
pip install --upgrade pip
```

```
pip install -r requirements.txt
```

### Help

```
python ./main.py --help
```
```
usage: main.py [-h] [--options OPTIONS] [--lang LANG] locations [locations ...]

Show weather from https://wttr.in

positional arguments:
  locations          locations one or more

options:
  -h, --help         show this help message and exit
  --options OPTIONS  See https://wttr.in/:help. Default: "nM"
  --lang LANG        Language. See https://wttr.in/:help. Default: "ru"
```

### Run

```
python ./main.py Москва Мордор Владивосток 
```

<img src="screenshot.jpg" width="400">


### Integrate

Add this to your `~/.bashrc`
```
function weather_console() {
source /<your path>/weather_console/venv/bin/activate &&
python /<your path>/weather_console/main.py $@ &&
deactivate;
 }
```

Apply changes:
```
source ~/.bashrc
```

And test it:
```
weather_console kiev kharkov
```
