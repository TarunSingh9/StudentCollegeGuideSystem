from os import name
from xml.sax.handler import property_interning_dict


name = str(input('Student_id-'))
password = int(input('password-'))
#section = str(input('Section-'))
if(password==1234560):
    print("******************WELCOME TO MY COLLEGE SUBJECT INFORMATION LIBRARY****************")



print("*********************TO FIND THE BOOK********")
print("choose the year")

choice1 = int(input(""))
if(choice1==1):
    print("choose the semsester :")
    
if(choice1==2):
    print("choose the semsester :")

if(choice1==3):    
    print("choose the semsester :")
if(choice1==4):
    print("choose the semsester :")    

choice2 = int(input(""))
if(choice2==1):
    print('''          SUBJCET CODE  :  SUBJECT NAME                 :  AUTHOR AND BOOK
                KAS-101T/KAS-201T  : Engineering Physics         : 1. Engineering Physics: Theory and Practical- Katiyar and Pandey (Wiley India)
                                                                   2. Applied Physics for Engineers- Neeraj Mehta (PHI Learning, New) 
                KAS-102T/KAS-202T  : Engineering Chemistry       : 1. University Chemistry By B.H. Mahan
                                                                   2. University Chemistry By C.N.R. Rao                                          
                           KAS103T : Engineering mathematics I   : 1. B. V. Ramana, Higher Engineering Mathematics, McGraw-Hill Publishing Company Ltd.,
                                                                     2008.
                                                                   2. B. S. Grewal, Higher Engineering Mathematics, Khanna Publisher, 2005.
                                                                   3. R K. Jain & S R K. Iyenger, Advance Engineering Mathematics, Narosa Publishing House
                                                                    2002. 
                        KMC102/202 : Emerging Technology for       : IOT , Cloud computing , Deep learning ,Digital Manufacturing ,Future Trends 
                                        Enginering                                                             
                 KEC-101T/KEC-201  : Emerging domain in electronics : 1. Robert L. Boylestand / Louis Nashelsky “Electronic Devices and Circuit Theory”, Pearson Education.                                                         2. H S Kalsi, “Electronic Instrumentation”, McGraw Publication 
                                       Engineering             
                           ''')

if(choice2==2):
    print('''       SUBJCET CODE  :  SUBJECT NAME                 :  AUTHOR AND BOOK
                          KNC-101 : Soft skills-I                 :1. Technical Communication, (Second Ed.); O.U.P., Meenakshi Raman & S.Sharma New Delhi, 2011                 
                                                                   2. Business Communication for Managers, Payal Mehra, Pearson, Delhi, 2012. 
                                                                   3. Personality Development, Harold R. Wallace et. al, Cengage Learning India Pvt. Ltd; New Delhi 2006                 
                KEE-101T/KEE-201T : Electrical Engineering       : 1. E. Hughes, “Electrical and Electronics Technology”, Pearson, 2010.
                                                                   2. L. S. Bobrow, “Fundamentals of Electrical Engineering”, Oxford University Press.                
              
                KCS-101T/KCS-201T : Programming for problem solving : C programming for beginners , The complete reference ,Let us C             
                               
                    KMC 101/201   :  Artifical Intelligence for   : 1. Artificial Intelligence: A Modern Approach by Stuart Russell and Peter Norvig, Prentice Hall 
                                         Engineers                  2. Artificial Intelligence by Kevin Knight, Elaine Rich, Shivashankar B. Nair, Publisher : McGraw 
                                                                       Hill 
                                       
                         
                          KAS 203T : Engineering mathematics II  : 1. E. Kreyszig, Advance Engineering Mathematics, John Wiley & Sons, 2005.
                                                                   2. Peter V. O’Neil, Advance Engineering Mathematics, Thomson (Cengage) Learning, 2007.
                                                                   3. Maurice D. Weir, Joel Hass, Frank R.Giordano, Thomas, Calculus, Eleventh Edition,
                                                                    Pearson.              
                          KNC-201 : SOFT SKILLS-II                :1. Technical Communication, (Second Ed.); O.U.P., Meenakshi Raman &S.Sharma New Delhi, 2011 
                                                                   2. Personality Development, Harold R. Wallace et. al, Cengage Learning India Pvt. Ltd; New Delhi 2006
                                            ''')

if(choice2==4):
    print(''''       SUBJCET CODE  :  SUBJECT NAME             :  AUTHOR AND BOOK
                           KCS 401 :  OPERATING SYSTEM          :1. Silberschatz, Galvin and Gagne, “Operating Systems Concepts”, Wiley 
                                                             2. Sibsankar Halder and Alex A Aravind, “Operating Systems”, Pearson Education       
                           KCS 402 : THEORY OF AUTOMATA AND     :1. Introduction to Automata theory, Languages and Computation, J.E.Hopcraft, R.Motwani, and Ullman. 2nd 
                                  FORMAL LANGUAGE                               edition, Pearson Education Asia 
                                                             2. Introduction to languages and the theory of computation, J Martin, 3rd Edition, Tata McGraw Hill
                           KCS 403 : MICROPROCESSOR             :1. Gaonkar, Ramesh S , “Microprocessor Architecture, Programming and Applications with 
                                                             2. 8085”, Penram International Publishing. 
                                                             3. Ray A K , Bhurchandi K M , “Advanced Microprocessors and Peripherals”, TMH ''')







if(choice2==3):
    print(''''     SUBJCET CODE  :  SUBJECT NAME             :  AUTHOR AND BOOK
                       KCS 301   : DATA STRUCTURE            :1.Aaron M. Tenenbaum, Yedidyah Langsam and Moshe J. Augenstein, “Data Structures Using C and C++”,  PHI 
                                                                Learning Private Limited, Delhi India 
                                                              2. Horowitz and Sahani, “Fundamentals of Data Structures”, Galgotia Publications Pvt Ltd Delhi India. 
                                                              3. Lipschutz, “Data Structures” Schaum’s Outline Series, Tata McGraw-hill Education (India) Pvt. Ltd.   
                       KCS 302  : COMPUTER ORGANIZATION AND :1. Computer System Architecture - M. Mano 
                                    ARCHITECTURE              2. Carl Hamacher, Zvonko Vranesic, Safwat Zaky Computer Organization, McGraw-Hill, Fifth Edition, Reprint 2012 
                                                              3. John P. Hayes, Computer Architecture and Organization, Tata McGraw Hill, Third Edition, 1998. Reference books
                       KCS 303  : DISCRETE STRUCTURES &     :1.Koshy, Discrete Structures, Elsevier Pub. 2008 Kenneth H. Rosen, Discrete Mathematics and Its Applications, 6/e, 
                                   THEORY OF LOGIC               McGraw-Hill, 2006. 
                                                              2. B. Kolman, R.C. Busby, and S.C. Ross, Discrete Mathematical Structures, 5/e, Prentice Hall, 2004. 
                       KNC302H   : Computer System            1.
                                   Security/Python
                                   Programming                             
                                                     ''''')









if(choice2==5):
    print(''''                   SUBJCET CODE  :   SUBJECT NAME                 :  AUTHOR AND BOOK
                           KCS501  :  DatabaseManagement System   :  Korth,sibertz,Sudarshan
                           KCS502  :  Compiler design             :  Aho,sethi & Ullman , K. Muneeswaran
                           KCS503  :  Design and Analsis of       :  Thomas H.Coreman ,Charles E.Leiserson
                                      Algorthim
                           KCS052  :  Web designing               :  Steven M.Schafer,"HTML,XHTML, CSS Bible ,5ed",Wiley india             
                           KCS058  :  Human Computer Interface    :  Alan Dix, janet finlay, Gregory Abowed
                         KNC501/502:Constitution of india,law and :
                                          Engineering''''')



if(choice2==6):
    print(''''     SUBJCET CODE    :     SUBJECT NAME(BOOKS)       :  AUTHOR AND BOOK
                           KCS601  : Software Engineering         :  RS Pressman, Software Engineering, A Practitioners Approach,McGraw Hill, 
                                                                     Pankaj Jalote,Software Engineering, Wiley
                           KCS602  : Web Technology               :1. Burdman, Jessica, “Collaborative Web Development” Addison Wesley
                                                                     Xavier, C, “ Web Technology and Design” , New Age International
                                                                   2. Ivan Bayross,” HTML, DHTML, Java Script, Perl & CGI”, BPB Publication
                           KCS-061 : Big Data                     :1. Michael Minelli, Michelle Chambers, and Ambiga Dhiraj, "Big Data, Big Analytics: Emerging Business
                                                                     Intelligence and Analytic Trends for Today's Businesses", Wiley
                                                                   2. Big-Data Black Book, DT Editorial Services, Wiley                           
                           KCS-061 : Big Data                     :1. Behrouz Forouzan, “Data Communication and Networking”, McGraw Hill
                                                                   2. Andrew Tanenbaum “Computer Networks”, Prentice Hall.                   
                           KCS-062 : Image Processing             :1.Rafael C. Gonzalez, Richard E. Woods,Digital Image Processing Pearson, Third Edition, 2010
                                                                   2.Anil K. Jain,Fundamentals of Digital Image Processing Pearson, 2002.
                                                                   3.Kenneth R. Castleman,Digital Image Processing Pearson, 2006.        
                           KCS-064 : Data Compression             :1. Khalid Sayood, Introduction to Data Compression, Morgan Kaufmann Publishers
                                                                   2. Elements of Data Compression,Drozdek, Cengage Learning
                                                                   3. Introduction to Data Compression, Second Edition, Khalid Sayood,The Morgan aufmann Series                          ''''')       
   

 
if(choice2==7):
    print('''         SUBJCET CODE  :   SUBJECT NAME                 :  AUTHOR AND BOOK
                    KCS071 : Artificial Intelligence              :1. S. Russell and P. Norvig, “Artificial Intelligence: A Modern Approach‖, Prentice Hall, Third Edition, 2009.
                                                                   2. I. Bratko, “Prolog: Programming for Artificial Intelligence”, Fourth edition, Addison-Wesley Educational Publishers
                                                                      Inc., 2011.
                                                                   3. M. Tim Jones, ―Artificial Intelligence: A Systems Approach(Computer Science)‖, Jones and Bartlett Publishers,
                                                                      Inc.First Edition, 2008
                    KC072 : Natural Language Processing            :1. Daniel Jurafsky, James H. Martin―Speech and Language Processing: An Introduction to Natural Language
                                                                      Processing, Computational Linguistics and Speech, Pearson Publication, 2014.
                                                                   2. Steven Bird, Ewan Klein and Edward Loper, ―Natural Language Processing with Python, First Edition, OReilly
                                                                       Media, 2009.
                    KCS073 : High Performance Computing            :1. Laurence T.Yang, Minyi Guo – High Performance Computing Paradigm and Infrastructure John Wiley
                                                                    2. Ahmar Abbas, “Grid Computing: Practical Guide to Technology & Applications”, Firewall Media, 2004.                                           
                    KCS074 : Cryptography & Network Security       :1. William Stallings, “Cryptography and Network Security: Principals and Practice”, Pearson Education.
                                                                    2. Behrouz A. Frouzan: Cryptography and Network Security, McGraw Hill .      
                    KCS075 :  Design & Development Of Applications :1. Charlie Collins, Michael Galpin and Matthias Kappler, “Android in Practice”, DreamTech, 2012
                                                                    2. AnubhavPradhan , Anil V Despande Composing Mobile Apps,Learn ,explore,apply                                           
                    KCS076 :  Software Testing                     :1. Yogesh Singh, “Software Testing”, Cambridge University Press, New York, 2012
                                                                    2. K..K. Aggarwal & Yogesh Singh, “Software Engineering”, New Age International Publishers, New Delhi, 2003                 
                                           ''''')
                                                            

if(choice2==8):
    print('''    SUBJCET CODE  :   SUBJECT NAME                   :  AUTHOR AND BOOK
                    KCS077 : Distruibuted system                 : 1. Singhal & Shivaratri, "Advanced Concept in Operating Systems", McGraw Hill 
                                                                   2. Ramakrishna,Gehrke,” Database Management Systems”, McGraw Hill
                    KCS078 : Deep learning                       : 1. Cosma Rohilla Shalizi, Advanced Data Analysis from an Elementary Point of View, 2015. 
                                                                   2. Deng & Yu, Deep Learning: Methods and Applications, Now Publishers, 2013.          
                    KCS079 : Service Oriented Architecture       : 1. Shankar Kambhampaty; Service - Oriented Architecture & Microservices Architecture: For Enterprise, Cloud, Big Data and 
                                                                      Mobile; Wiley; 3rd Edition; 2018; ISBN: 9788126564064. 
                                                                   2. Icon Group International; The 2018-2023 World Outlook for Service-Oriented Architecture (SOA) Software and Services; 
                                                                      ICON Group International; 1st Edition, 2017; ASIN: B06WGPN8YD. 
                    KCS710 : Quantum Computing                   : 1. Micheal A. Nielsen. &Issac L. Chiang, “Quantum Computation and Quantum Information”, Cambridge 
                                                                      University Press, Fint South Asian edition, 2002. 
                                                                   2. Eleanor G. Rieffel, Wolfgang H. Polak , “Quantum Computing - A Gentle Introduction” (Scientific and 
                                                                     Engineering Computation) Paperback  Import, Oct 2014
                    KCS711 : Mobile Computing                    : 1. J. Schiller, Mobile Communications, Addison Wesley. 
                                                                   2. A. Mehrotra, GSM System Engineering.                            
                    KCS712 : Internet of Things                  : 1. Olivier Hersent,David Boswarthick, Omar Elloumi “The Internet of Things key applications and protocols”, wiley 
                                                                   2. Jeeva Jose, Internet of Things, Khanna Publishing House                     
                    KCS713 : Cloud Computing                     : 1. Kai Hwang, Geoffrey C. Fox, Jack G. Dongarra, “Distributed and Cloud Computing, From Parallel Processing to the 
                                                                      Internet of Things”, Morgan Kaufmann Publishers, 2012. 
                                                                   2. Rittinghouse, John W., and James F. Ransome, ―Cloud Computing: Implementation, Management and Security, CRC 
                                                                      Press, 2017.                                     ''')                                                            


         
