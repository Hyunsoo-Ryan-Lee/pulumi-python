import pulumi
import pulumi_aws as aws

user_script = """
#!/bin/bash
sudo apt-get update
sudo apt-get install apache2 -y
sudo chown -R $USER:$USER /var/www
echo "<h1>HELLO WORLD from $(hostname -f)</h1>" > /var/www/html/index.html
"""

def ec2_infra():

    ec2_instance = aws.ec2.Instance(
        resource_name="pulumi-ec2",
        ami="ami-09a7535106fbd42d5",
        instance_type="t2.micro",
        key_name="K8S",
        tags={
            "Name":"pulumi"
        },
        user_data=user_script,
        subnet_id="subnet-0e45b3ae2898b0821",
        vpc_security_group_ids=["sg-083c7967737299150"]
    )

    # Export the name of the bucket
    pulumi.export('ec2_public_ip', ec2_instance.public_ip)