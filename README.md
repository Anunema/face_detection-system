face_detection system
Introduction
1.1.	Overview
	Artificial intelligence and Machine Learning have gained increasing popularity in recent years due to their ability to handle tasks that would otherwise take too much computational power, and due to their versatility, the wide range of problems they have been shown to solve. One of the most well known ask that machine learning has made possible is face recognition. Face recognition technology has been used for a variety of applications including automatic tagging in Facebook photos, Snapchat lenses that overlay dog ears on someone’s head, and security and surveillance, with the more recent capacity to track individuals moving throughout a closed space as they cross in front of security cameras.

	Facial recognition systems rely on unique facial features as and additional layer of security to identify and distinguish people whether they’re new faces or old ones in database.We set out to apply this technique to the field of internet security, along with Captchas, I m not a robot check boxes, security questions, two factor authentication, and many others. Facial recognition has the potential to be a much simpler approach to security than remembering additional security in formation or connecting other accounts and devices.  

Implementation
4.1	 Requirements

4.1.1	Functional Requirements
The functional requirements of our project describe features our system must have to be successful. Users need to be able to create accounts and store their facial data for the site to identify them later. The site needs to be able to identify users with facial recognition, which requires some form of video camera. The site must be able to stop impersonation, distinguishing between real people and fake copies. And finally, the site needs to be able to recognize faces and gestures to log users into the correct accounts.

4.1.2    Non-functional Requirements
	The non-functional requirements describe features that improve the sites performance, or would otherwise benefit the system. A secure API for storing and using face data to identify users andlearn new faces would be ideal to avoid the risk of losing identifiable information in the event of a site hack. Since we imagine nobody wants to sit in front of a camera for minutes on end trying to access an account, the site should be able to identify users quickly, and provide a quick login experience. Since Software programs often require continuous debugging efforts as new features are added and new issues are discovered, the source code should be clear and easy to follow, relying on software tools to simplify the implementation.
4.2 Use Cases 
The use case represents the list of actions and event steps which define the interactions among users, websites, and the API.


Figure 4.1: Use case diagram of the user

4.3 Activity Diagram


                        Figure 4.2: High level view of user operations

As a user, after he/she enters the index page of the website, he/she may attempt to log into by enabling the camera or create an account. The user needs to wait for the system response after the system finishes recording. After that, the user should perform given gestures from the server.


4.4 Architecture Diagram

                                     Figure 4.3: Architecture diagram of the system
              Since all data will be stored in our database, Wedecide to build an advanced data-centric architecture for our design to make the data more accessible and manageable for users. In addition, considering security and management of APIs, we choose to have a three-tier architecture because if the protect data security and improve manageability of different APIs. In our design, users post requests to the web server and the server will call different APIs depending on the requests from users. Multiple users can login to the system at same time from different places.

















