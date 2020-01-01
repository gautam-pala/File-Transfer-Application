# File-Transfer-Application
The repository contain  
1) FTPclient.py  
2) FTPserver.py

Implementation of File Transfer Application: 
Client should send a file name with path to the server.Server can respond in one of the following ways: If the file is not found, this information is communicated and the communication terminates If the file is found, The first message contains its size, and message size (this helps the client in determining how many data messages are expected) Sequence of data packets containing file content Client will receive the data messages and do the following: For the message stating ""file not found", it just displays that message to the user If the file found, Ask the user about the name of the file to be created and the path Receive and process the first message sent by the server: based on the file size and message size, the message count is determined Receive the sequence of messages containing file data and write the contents to the created file On receiving all the messages, close the file
