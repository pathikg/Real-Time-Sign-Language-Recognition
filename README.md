<h1 align="center">Real Time Sign Language Recognition </h1>

<div align="center">
 
  [![](https://img.shields.io/badge/Made_with-Python3-red?style=for-the-badge&logo=python)](https://www.python.org/ "Python3")
  [![](https://img.shields.io/badge/Made_with-Tensorflow-red?style=for-the-badge&logo=tensorflow)](https://www.tensorflow.org/ "Tensorflow")
  [![](https://img.shields.io/badge/Made_with-Tkinter-red?style=for-the-badge&logo=tkinter)](https://docs.python.org/3/library/tkinter.html "Tkinter")
  
</div>

<h2> About </h2>

&emsp; Nearly 5% of the world’s population is said to be hearing impaired, this creates a major problem for the communication with the deaf and the dumb, specially abled persons. To decrease the communication gap between hearing impaired community and the normal persons, we have designed a Sign Language Recognition System.
Our application allows users to show a sign on a webcam and that sign gets converted to its respective alphabet and displayed on the screen. 

---

<h2> Functionalities </h2>

* Detecting a sign and displaying the corresponding alphabets from A to Z ( Excluding J and Z)
* Detecting a sign indicated by user on a live feed and displaying corresponding alphabet
* Forming a word/sentence from the individual signs shown by user on a live webcam and displaying that word on a screen
* Recording and storing a video of user showing signs on a webcam with its respective results in a local machine 


---


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
python main.py
```

---

### Keyboard commands  :

* Press R to start recording 
* Press D to add predicted sign to previous displayed result
* Press S to add space to previous displayed result
* Press A to delete last displayed result
* Press C to clear the all displayed results 
* Press T to stop recording 
* Press Q to exit

---



#### This project still has scope of development, so you can also contribute to this Project as follows:
* [Fork](https://github.com/Patrickbro13/Real-Time-Sign-Language-Recognition) this Repository.
* Clone your Fork on a different branch:
	* `git clone -b <name-of-branch> https://github.com/Patrickbro13/Real-Time-Sign-Language-Recognition.git`
* After adding any feature:
	* Goto your fork and create a pull request.
	* We will test your modifications and merge changes.

---
<h4 align="center"><b>Developed with :heart: by 
<a href="https://github.com/Patrickbro13">Pathik Ghugare</a> and <a href="https://github.com/Mayank7832">Mayank Chopra</a> </b> , 
</h4>

---
