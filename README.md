# Wuxiaworld crawler
This api accepts your e-mail, the start chapter and the end chapter (decided by you) of a wuxiaworld novel, crawls
wuxiaworld and writes the content of the chapters to a pdf file which is sent to your mail when it is done.

The parameters `start_chapter`, `end_chapter` and `email` are sent to the specified url in a GET request.
Note: All the parameters are compulsory.

### How do I get set up? ###

* Ensure you are running python 3 or use a virteul env running python 3
* RUN "pip install -r requirements.txt"
* set up environment variables as stated in sample.env
* run `chmod +x run.sh`
* run `./run.sh`

