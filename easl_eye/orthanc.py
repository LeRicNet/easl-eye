import pandas as pd
import pyorthanc
import requests
import pydicom
from pydicom.filebase import DicomBytesIO

def build_instance_map():
	# Connect to the Orthanc server
	client = pyorthanc.Orthanc('http://amc-tensor1.ucdenver.pvt:8042', username='orthanc', password='orthanc')
	
	instances = client.get_instances()
	instances_dict = {
		'instance': [],
		'id': []
	}
	for instance in instances:
		instances_dict['instance'].append(instance)
		instances_dict['id'].append(client.get_instances_id(instance)['MainDicomTags']['SOPInstanceUID'])
		
	instance_map = pd.DataFrame(instances_dict)
	return instance_map

def extract_url(url):
    identifier = url.split("dicom-web/")[1]
    study = identifier.split("/")[1]
    series = identifier.split("/")[3]
    instance = identifier.split("/")[5]
    return {
        'url': identifier,
        'study': study,
        'series': series,
        'instance': instance
    }

def get_pixel_array(url, instance_map):
	payload = extract_url(url)
	
	
	orthanc_inst_id = instance_map.loc[instance_map.id == extract_url(url)['instance']].instance.values[0]
	response = requests.get("http://amc-tensor1.ucdenver.pvt:8042/instances/{}/file".format(orthanc_inst_id))
	dicom_file = DicomBytesIO(response.content)
	dicom_dataset = pydicom.dcmread(dicom_file)
	return dicom_dataset.pixel_array