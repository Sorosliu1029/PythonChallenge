# PythonChallenge
Code for practicing python, based on the [PythonChallenge](http://www.pythonchallenge.com/)  
*PythonChallenge*  is an interesting website for **any-level** coder to pratice Python.  
Here I recorded my way to solve the challenge.   
I try to solve on my own, if there is any reference, I will recored it in the *.py file.    

**If you find a better or another way, please feel free to leave a comment. Thanks a lot**

###Directory:  

1. [Warm Up](#warm_up)
2. [Python Challenge1](#PC1)
3. [Python Challenge2](#PC2)
4. [Python Challenge3](#PC3)
5. [Python Challenge4](#PC4)
6. [Python Challenge5](#PC5)
7. [Python Challenge6](#PC6)


###Detail:
####<a name='warm_up'></a>[Warm Up](http://www.pythonchallenge.com/pc/def/0.html)
Warm Up game. Just to show the power of Python to calculate big number.  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge0.py)

####<a name='PC1'></a>[Python Challenge1](http://www.pythonchallenge.com/pc/def/map.html)
Try to make full use of all the information from the page.  
It's an easy replacement trick. Use string.*maketrans* and string.*translate* function.  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge1.py)

####<a name='PC2'></a>[Python Challenge2](http://www.pythonchallenge.com/pc/def/ocr.html)
Dig deeper into the page, the **whole** page.  
And you will find some secrets in the html file of the page.  
The main task for this challenge is doing some statistics. Here reveals the power of Python in data analysis.  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge2.py)

####<a name='PC3'></a>[Python Challenge3](http://www.pythonchallenge.com/pc/def/equality.html)
The hint has clearly stated the secret of this challenge.  
Dig into the html source code and there is the key to success.  
First idea came to me is using regular expression and everything is nice. And the page title is 're', so it is obvious. :)  
Regular expression is a powerful tool to deal with string.  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge3.py)

####<a name='PC4'></a>[Python Challenge4](http://www.pythonchallenge.com/pc/def/linkedlist.php)
The first page is just a new URL and so on.  And the URL 'linkedlist' reveals that there will be many item like this page.  
So it is time to show the magic of Python urllib.  
Dig into the source code and you will find how to solve the challenge.  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge4.py)

####<a name='PC5'></a>[Python Challenge5](http://www.pythonchallenge.com/pc/def/peak.html)
Peak Hell? At first I didn't understand the meaning and went for Google for help.  
This challenge uses python *pickle* library, which is used to save object to file.  
The source code has a **banner.p** file and the file contains some strange characters. Guess **banner.p** file is the pickled file, so I try to restore from it.  
Then I get a list object, try some times and you will find the list indicates the character and the continuous number in sequence. Everything is done.  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge5.py)

####<a name='PC6'></a>[Python Challenge6](http://www.pythonchallenge.com/pc/def/channel.html)
At beginning of the source code, there is a comment **zip** reminding me of the Python function *zipfile* .  
The very first step to solve this challenge is to modify the URL. Change the *.jpg* suffix to *.zip* and you will get a zip file. The solution lies in the zip file.  ;)
The following steps are very easy.  
However there is still a riddle lying in the final solution.  
Have fun!  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge6.py)

