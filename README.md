# Real-Time-Sign-Language-Recognition

Dataset used : [ASL Dataset](https://drive.google.com/drive/folders/1v3EWedumUJ64xmrPOfQ7e3GJ5K-GC45d?usp=sharing)

Colab notebook : https://colab.research.google.com/drive/1ObDUs0TZ_iXrsWTY5St536yy1ZR-cGMM?usp=sharing

---



  
### To run this project :

Clone the project -
```
  $ git clone https://github.com/Patrickbro13/Real-Time-Sign-Language-Recognition.git
```
  
Install all the reqirements -
```
  $ pip install -r requirements.txt
 ``` 
 
Download the CNN model from this [link](https://drive.google.com/file/d/1-81s-_ke_heseeqBsKTZoJcqbcAON8ct/view?usp=sharing) and store it in your machine.
Then update that model's path in model.py file
```
model = load_model("YOUR_MODEL_PATH")
```

Move to the skinMask200/code/ directory 

Run the following commands -

```
python ui.py
```

---
