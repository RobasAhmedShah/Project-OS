                                                OPERATING SYSYTEM FINAL PROJECT
                                                                                        
                                                    Voice-Controller-Shell
                                                    
                                              COURSE INSTRUCTOR : MISS RABIA ANSARI  
   
# Introduction

Voice Controll shell By Using Python Based Code Which Allows Easy Access to work on Directories and Commands On linux by Speech .

# Dependencies

- INSTALLING PYAUDIO


                                  sudo apt install python3-pyaudio

<img width="960" alt="proj1" src="https://user-images.githubusercontent.com/110839535/236692044-d7d62474-c251-4888-9b0e-0b64e19236f7.PNG">

- INSTALLING SPEECH_RECOGNITION


                                   pip3 install SpeechRecognition --break-system-package

<img width="956" alt="proj2" src="https://user-images.githubusercontent.com/110839535/236692106-fc6a8eb8-b130-447c-8176-323b847d059b.PNG">

# How Our Conversation Goes

- system asks "say Something"
- we say The Command
- system Runs The Commands if Valid

# Functions

    print("1. List Files")
    print("2. Shutdown")
    print("3. List Files Permissions")
    print("4. List Hidden Files")
    print("5. Current Working Directory")
    print("6. Show Date")
    print("7. Show Day")
    print("8. Show Time")
    print("9. Show Calender")
    print("10. Go to Home Directory")
    print("11. Go to Root Directory")
    print("12. Go to User's Directory")
    print("13. Take Snapshot")
    print("14. Show Network Status")
    print("15. Create a file")
    print("16. Delete a file")
    print("17. Open Nano Editor")
    print("18. Open Gedit Editor")
    print("19. Show Username")
    print("20. Tell the file type")
    print("21. Manual of any Command")
    print("22. Make new Directory")
    print("23. Login as root")
    print("24. List Users")
    print("25. Delete User")
    print("26. Who created you?")

 
We have created a shell that can interact with the user through voice commands and provide output from the terminal.
The overall shell is based on voice inputs meaning user can call shell commands without inputting physically with the system.
The commands are very user friendly and commonly used over the world through communication.
Working:
1)	When the shell is executed it ask to say a voice command from the above mentioned commands.
2)	Once the user says the command a system call is generated with the help of subprocess module ordering the original terminal to execute the command by converting the user said command to the original shell command.
3)	Once the system call gets it results from the kernal, it returns with a utf-8 encoded output
4)	By decoding the output, the result of the command is viewed in front of the user’s screen as a program output

Following commands are embedded in the program that can stimulate the shell and provide response 

List Files:
as user said list files a system call is generated with ‘ls’ in argument and provide the output from the terminal.

 



![image](https://user-images.githubusercontent.com/123714538/236896120-c1b26987-4f4e-4865-8a85-ad7b7b0eaf20.png)



List File Permissions: Displays the access rights of files in a directory.





![image](https://user-images.githubusercontent.com/123714538/236896259-25254f9f-4fd6-4c3e-be88-4da32a8b4fd6.png)

 
Shutdown: Command to turn off a computer or a server.
Current working directory: Displays the directory path of the current working directory.





 ![image](https://user-images.githubusercontent.com/123714538/236896281-f2e954ba-aa68-41d4-8e55-d229e2caf6c3.png)





List hidden files: Displays a list of all hidden files in a directory.

 



![image](https://user-images.githubusercontent.com/123714538/236896313-a62e77f5-bc23-45bb-ab5e-65879f3d8695.png)





Show date: Displays the current date.

 



![image](https://user-images.githubusercontent.com/123714538/236896335-6980253b-ccac-45f1-9914-a40ebcfd708b.png)





Show day: Displays the current day.





 ![image](https://user-images.githubusercontent.com/123714538/236896388-6381442d-baeb-479f-aea4-6c05ff97f083.png)





Show time: Displays the current time.





 ![image](https://user-images.githubusercontent.com/123714538/236896427-c4f0eb89-b8f7-44a9-86d9-8bbfe8dfd4d5.png)





Show calendar: Displays a calendar for the current month.

 



![image](https://user-images.githubusercontent.com/123714538/236896449-2f4309ad-6302-4c81-8c24-d508770b84e7.png)





Go to home directory: Changes the current working directory to the user's home directory.

 



![image](https://user-images.githubusercontent.com/123714538/236896480-aee49470-1e1d-4d44-8ee9-6ae70a3eb129.png)





Go to root directory: Changes the current working directory to the root directory.
 




 ![image](https://user-images.githubusercontent.com/123714538/236896498-47227b52-a9d1-44bb-ae5c-ee22084d5697.png)





Go to user directory: Changes the current working directory to a specific user's home directory.
 




 ![image](https://user-images.githubusercontent.com/123714538/236896518-bc2d86b1-e379-4275-93e7-1b3d9ca7ac42.png)





Take snapshot: Creates a backup of the current system or a specific file or directory.
 




Show network status: Displays the status of the network connection.
 




![image](https://user-images.githubusercontent.com/123714538/236896537-f2ca082c-d409-4c76-8d2b-81ebc3f68967.png)








Create a file: Creates a new file in the current directory.
 




 ![image](https://user-images.githubusercontent.com/123714538/236896599-278835bb-c354-43b9-9ce3-e297e3c22832.png)

 




A file named ‘new’ was created, u can also provide the extension by saying it like new.txt.
Delete a file: Deletes a specified file.




 
 ![image](https://user-images.githubusercontent.com/123714538/236896639-ccff8bb0-cd21-440d-a5c0-2bd4f2ad21bd.png)

![image](https://user-images.githubusercontent.com/123714538/236896656-5e7496e8-7015-455a-9197-76c7bbff1da1.png)

 




Open nano editor: Opens the nano text editor.

Open editor: Opens a gedit text editor.





![image](https://user-images.githubusercontent.com/123714538/236896679-f26095ac-3511-4e21-942d-cec6519142e0.png)





Asks for file name, in my case I said:





![image](https://user-images.githubusercontent.com/123714538/236896702-57ab8e9f-110f-4069-bca4-f154690a03cc.png)




Show username: Displays the username of the current user.





![image](https://user-images.githubusercontent.com/123714538/236896728-b26b143b-07ca-4a06-91a7-07705423b89e.png)




Tell the file type: Displays the file type of a specified file.




![image](https://user-images.githubusercontent.com/123714538/236896757-121bf1bd-6417-4f61-9939-233c777c2481.png)





Type of the file is mentioned.
 




Manual of any command: Displays the manual page of a specified command.




 ![image](https://user-images.githubusercontent.com/123714538/236896783-88142e40-76c5-493d-8817-4b5f00ee0e06.png)





Asks the command name and displays the manual:




 ![image](https://user-images.githubusercontent.com/123714538/236896798-7d77e10a-9162-4469-9aae-6225ec305145.png)





Make new directory: Creates a new directory in the current working directory.





Login as root: Logs in as the root user.




 ![image](https://user-images.githubusercontent.com/123714538/236896849-7855a016-7485-4aec-954b-2a2884f17bdf.png)





Logged in to root.










List users: Displays a list of all users on the system.




 ![image](https://user-images.githubusercontent.com/123714538/236896892-ef1ad98d-7bce-4ac5-9770-868d6c9b5ba5.png)





who created you :shows you the creator(s) of the program.




 ![image](https://user-images.githubusercontent.com/123714538/236896909-7352d94d-599c-43ab-ad3d-c79e040a9d78.png)


Note: if something is not mentioned means that it gives you output as a voice output so I was unable to demonstrate the audio through pictures, however you can execute the program to be able to witness the best work and results.

Conclusion:
These commands are flexible meaning it is gathered with multiple possibilities of command a user can say if it matches even a little to the embedded command, it provides the results.



