In order to use this script, you need in line 39, in which the _analyze()_ function is called, and inside _parse_txt_report()_. 
The _parse_txt_report()_ function takes 2 arguments: the path to the report in the "txt" format, and the path to the class matching template.
The template is compiled by you based on how you think the neural network should classify sounds.
For convenience, you can put the report itself in the "templates" folder, and the report in the "reports" folder.
The analysis results will be located in the "stat" folder.