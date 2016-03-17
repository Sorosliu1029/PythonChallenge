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
8. [Python Challenge7](#PC7)
9. [Python Challenge8](#PC8)
10. [Python Challenge9](#PC9)
11. [Python Challenge10](#PC10)
12. [Python Challenge11](#PC11)
13. [Python Challenge12](#PC12)
14. [Python Challegne13](#PC13)
15. [Python Challenge14](#PC14)
16. [Python Challenge15](#PC15)
17. [Python Challenge16](#PC16)
18. [Python Challenge17](#PC17)

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

####<a name='PC7'></a>[Python Challenge7](http://www.pythonchallenge.com/pc/def/oxygen.html)
The whole page only contains a picture, so the solution must lies in the picture.  
Inside the picture there is a blur rectange, and use Python *PIL* library to handle picture.  
The key to success is to find the blur rectangle area.  
If you look carefully at the image, you will find that the vertical blur area is all the same.  
So get the horizontal area data and convert pixel data to ASCII character.  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge7.py)

####<a name='PC8'></a>[Python Challenge8](http://www.pythonchallenge.com/pc/def/integrity.html)
This challenge page shows a bee(a hint) and a hyperlink requiring user name and password.  
The source code containing some **magic** string. It confused me a while, but there is also a hint -- `BZh91AY&SY`. 'BZ' reminds me of Linux compression file suffix *.bz*, so I guess the magic string is compressed by Bz compression format.    
The name is 'huge', and the password is 'file'.  
Challenge is becoming more and more challenging and attractive.  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge8.py)

####<a name='PC9'></a>[Python Challenge9](http://www.pythonchallenge.com/pc/return/good.html)
The page tell us obviously to connect the dots, the only problem is where the dots are.  
In the source code, there are two list: first and second. It may be the line dots.  
Get the dot list data and draw two lines, you will get the solution.    
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge9.py)

####<a name='PC10'></a>[Python Challenge10](http://www.pythonchallenge.com/pc/return/bull.html)
A little difficult if in a Pythonic way.   
The key is to find the rule in the patterns.  The pattern represents number counting, one digit for number and one digit for counting.  
If you find the rule behind it, it's easy to know the next one. A loop could handle all.  BUT it is not Pythonic.  
Sadly, I could not come up a Pythonic way, so I refered to the Python Challenge Community.   
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge10.py)

####<a name='PC11'></a>[Python Challenge11](http://www.pythonchallenge.com/pc/return/5808.html)
The challenge page title tells all the secrets.  
At first, I tried odd row-index&even column-index / even row-index&odd column-index, but found out nothing useful. Then tries all odd or all even index, and got an image revealing the key to next challenge.  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge11.py)

####<a name='PC12'></a>[Python Challenge12](http://www.pythonchallenge.com/pc/return/evil.html)  
This one is confusing. I refered to [this bolg](http://blog.csdn.net/kosl90/article/details/7270605), and got the idea.   
The magic number 5 comes from the *evil1.jpg* showing 5 stacks of cards... Orz....  :imp:  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge12.py)

####<a name='PC13'></a>[Python Challenge13](http://www.pythonchallenge.com/pc/return/disproportional.html)  
This one is quite tough for someone doesn't know aobut XML. I refered to online solution. The evil's name is somewhat annoying.  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge13.py)

####<a name='PC14'></a>[Python Challenge14](http://www.pythonchallenge.com/pc/return/italy.html)  
Here comes a simpler one. From the web page is a bread in clock-wise direction and the original image is just 1 row. The hint says 100 * 100 = 100 + 99 + 99 + 98 + ……, so it is quite obvious to refactor the origin.We ended up in getting a not so cute cat... :cat:  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge14.py)

####<a name='PC15'></a>[Python Challenge15](http://www.pythonchallenge.com/pc/return/uzi.html)
The first part of this challenge is easy, just use *datetime* module to match the calendar pattern, notice that the disered year is a leap year.  
After first part, we get 1756. With the hint 'tomorrow', we get a date: 1756-1-27. Google it, it is Mozart's birthday........:birthday:  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge15.py)

####<a name='PC16'></a>[Python Challenge16](http://www.pythonchallenge.com/pc/return/mozart.html)
At first glance, the image format is *.gif*, so it is intuitive to think about getting each frame out. So I tried `Image.tell()` and `Image.seek()`, but there is only one frame.  
Sadly to google the solution, and it says to align each row's pink bar to the left. Then all done....  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge16.py)

####<a name='PC17'></a>[Python Challenge17](http://www.pythonchallenge.com/pc/return/romance.html)
Now challenge goes with stories. :joy: It's time to put a temporary end to this period of practice. In the next coming summer vocation I will try again.  
[Code Here](https://github.com/Sorosliu1029/PythonChallenge/blob/master/PythonChallenge17.py)