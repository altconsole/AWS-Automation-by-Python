import boto3
#import pprint
#creating AWS sessions

session = boto3.Session(profile_name = "shubh", region_name = 'ap-southeast-1')
client = session.client(service_name = 'ec2')
all_regions = client.describe_regions()

#creating list of all AWS regions

list_of_aws_regions = []
for each_reg in all_regions['Regions']:
    #print(each_reg['RegionName'])
    list_of_aws_regions.append(each_reg['RegionName'])
    
#print (list_of_aws_regions)

for each_region in list_of_aws_regions:
    session = boto3.Session(profile_name = "shubh", region_name = each_region)
    resource = session.resource(service_name = "ec2")
    print ("List of EC2 Instances from the region:" ,each_region)
    for each_instance in resource.instances.all():
        print (each_instance.id, each_instance.state['Name'])


