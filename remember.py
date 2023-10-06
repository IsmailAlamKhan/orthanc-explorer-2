Last login: Fri Oct  6 22:50:30 on ttys000
virtualenvwrapper_run_hook:12: no such file or directory: /usr/local/bin/python3
virtualenvwrapper.sh: There was a problem running the initialization hooks.

If Python could not import the module virtualenvwrapper.hook_loader,
check that virtualenvwrapper has been installed for
VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3 and that PATH is
set properly.
muhammadshoaib@Muhammads-MacBook-Air orthanc-explorer-2 % code .
muhammadshoaib@Muhammads-MacBook-Air orthanc-explorer-2 % ls
CMakeLists.txt		Resources		scripts
LICENSE			TODO			tests
Plugin			WebApplication
README.md		release-notes.md
muhammadshoaib@Muhammads-MacBook-Air orthanc-explorer-2 % clear
















































muhammadshoaib@Muhammads-MacBook-Air orthanc-explorer-2 % sudo nano /usr/share/cups/mime/mime.types

Password:




























































  UW PICO 5.09                                                                           File: /usr/share/cups/mime/mime.types                                                                              

                                (contains(2,80,/csh) contains(2,80,/tcsh))
application/x-perl              pl printable(0,1024) + string(0,#!) +\
                                contains(2,80,/perl)
application/x-shell             sh printable(0,1024) + string(0,#!) +\
                                (contains(2,80,/bash) contains(2,80,/ksh)\
                                 contains(2,80,/sh) contains(2,80,/zsh))
application/x-csource           c cxx cpp cc C h hpp \  
                                printable(0,1024) + ! css + \
                                (string(0,/*) string(0,//) \ 
                                 string(0,#include) contains(0,1024,<0a>#include) \
                                 string(0,#define) contains(0,1024,<0a>#define))
text/html                       html htm printable(0,1024) +\
                                (istring(0,"<HTML>") istring(0,"<!DOCTYPE"))
text/plain                      txt printable(0,1024)
text/css                        css

                                 
########################################################################
#
# RSS feed type...
#

application/rss+xml             rss

    
########################################################################
#
# CUPS-specific types...
#
                                
application/vnd.cups-banner     string(0,'#CUPS-BANNER')
application/vnd.cups-command    string(0,'#CUPS-COMMAND')
application/vnd.cups-pdf
application/vnd.cups-postscript
application/vnd.cups-ppd        ppd string(0,"*PPD-Adobe:")
application/vnd.cups-raster     string(0,"RaSt") string(0,"tSaR") \
                                (string(0,"RaS2") + !string(4,PwgRaster<00>)) string(0,"2SaR") \
                                string(0,"RaS3") string(0,"3SaR")
application/vnd.cups-raw        (string(0,<1B>E) + !string(2,<1B>%0B)) \
                                string(0,<1B>@) \
                                (contains(0,128,<1B>%-12345X) + \
                                 (contains(0,4096,"LANGUAGE=PCL") \
                                  contains(0,4096,"LANGUAGE = PCL")))

########################################################################
#                                
# Raw print file support...
#
# Comment the following type to prevent raw file printing.
#

application/octet-stream

    

 

 

                  
