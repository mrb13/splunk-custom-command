# splunk-custom-command
This repo demonstrates how to create a custom command within Splunk Enterprise &amp; invoke that command with Splunk's SPL language. 

## Assumptions
Instead of creating a new custom app, this demo will leverage the existing Search & Reporting app.  This demo will update the default "Search" app by adding a new python file & updating the commands.conf file. 

This demo assumes Splunk Enterprise on a Linux server is being used. 

## Deploy Python File

* Deploy demo.py to directory /opt/splunk/etc/apps/search/bin
* Ensure file is owned by splunk user & permissions are 555

## Update commands.conf 

* Update commands.conf file located at /opt/splunk/etc/apps/search/local/commands.conf 

```
[py_demo2]
filename = demo.py
type = python
```

* NOTE the value in the brackets will be the name of the function invoked by the Splunk SPL

* Once the above deployment steps have been completed, restart Splunk. 

```
cd /opt/splunk/bin 
./splunk restart 
```

# Splunk SPL 


## References  / Sources 
* https://community.splunk.com/t5/Developing-for-Splunk-Enterprise/Can-you-help-me-with-a-script-command-to-generate-or-show-output/m-p/387279
 
