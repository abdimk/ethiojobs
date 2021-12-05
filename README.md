<h1 align="center"> 
    ✨ EthioJobs✨ 
</h1>
<h3 align="center"> 
    Search and Find Jobs in Ethiopia
</h3>
<p align="center">
    <a href="https://python.org">
        <img src="http://forthebadge.com/images/badges/made-with-python.svg" alt="made-with-python">
    </a>
<h3 align="center"> 
   Easy start
</h3>

```console
    when you want to use this module always import those stuffs and use pprint function instend instead of defualt print fucntion.
    
    
    from Ethio_jobs.ethio_jobs import EthioJobs 
    from Ethio_jobs.deeptable import TableData 
    from Proxy import proxies
    from pprint import pprint
```
<b>input code</b>
```yaml
uses

To search how many jobs are available in ethio jobs
create an instance of EthioJobs form EthioJobs class
my_job = EthioJobs('manager')
pprint(my_job.numberofjobs())
```
<b>output</b>

132 manager jobs has been found!

<b>input code</b>
```yaml
To get the title of all available mangment jobs
pprint(my_job.scraped_jobs_title(),indent=3)
```
<b>output</b>
```console
['ACCOUNTANT ','Accountant ( COST ACCOUNTANT ; FACTORY EXP MUST) ','Marketing  Department Manger ',
 'Project Director ','Manager - ERP Management and Support ','Import and Export Coordinator ',
 'Hygiene & Sanitation Officer ','Tender Division Manager ','WASH Project Coordinator ',
 'Immediate Vacancy - Program Officer – Operation ']
 ```


