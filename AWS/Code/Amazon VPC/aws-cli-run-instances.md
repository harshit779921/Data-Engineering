# Launch instance in Public 1A
aws ec2 run-instances --image-id ami-02af70169146bbdd3 --instance-type t2.micro --security-group-ids sg-05e39088d5a37edd7 --subnet-id subnet-0c562e9c442f96be9 --key-name cloud-labs-nv --user-data file://user-data-subnet-id


# Launch instance in Private 1B
aws ec2 run-instances --image-id ami-02af70169146bbdd3 --instance-type t2.micro --security-group-ids sg-05e39088d5a37edd7 --subnet-id subnet-0aa805887105c9d26b --key-name cloud-labs-nv --user-data file://user-data-subnet-id


# Launch instance in Public 1B



# Terminate instances

aws ec2 terminate-instances --instance-ids <value> <value>