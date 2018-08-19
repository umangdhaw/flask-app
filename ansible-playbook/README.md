Simple ansible playbook to run the flask app.

Steps to use -

* Launch a new instance on AWS (tested on Amazon Linux 2 AMI with ID ami-04681a1dbd79675a5)
* Flask by default runs on port 5000, so add inbound rule for port 5000 on the instance
* To deploy, run from your local machine (ansible needed) - 
```
ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i "<PUBLIC-IP-OF-EC2-INSTANCE>," -u ec2-user flask.yml
```


We need a High Availability solution to ensure that service is always available. Here's the proposed solution -

* Run 2 instances behind an ELB, both running the flask application
* Use Elasticache as the central storage solution
* For deployment, launch 2 new nodes and deploy latest code to them with ansible
* Once deploy is successful, register them with ELB
* Once they are InService in ELB, remove old nodes from ELB



All of this can be automated to work at a larger scale and allow deployments whenever needed.