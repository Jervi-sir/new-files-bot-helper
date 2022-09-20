a script that

``` 
->[Reads name of all .mp4 files existing in folder]
	-> [open old saved file that contains saved file name, and put it into array]
		-> [if file name already exists in array, it will just delete it]
			-> [otherwise it will push it into the array]
				-> [save array in the opened file]
```
### To run
just drop the `filter_bot.py` file in the targeted folder
it will create `filesVisited.pkl` file that contains already saved file's names
```
	python filter_bot.py
```

### packages used

``` python
import os
import pickle
from pathlib import Path
```

