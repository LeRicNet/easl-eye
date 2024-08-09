
def annotate_synthseg_segmentations(post_data):
	for idx in range(post_data.shape[-2]):
    print("Image Index: {}".format(idx))
    for i, k in enumerate(label_key.keys()):
        _sum_value = post_data[:,:,idx,i].sum()
        if _sum_value > 0:
            print('\t - found: {}'.format(label_key[k]))

label_key = {
    '0': 'Background',
    '2': 'left cerebral white matter',
    '3': 'left cerebral cortex',
    '4': 'left lateral ventricle',
    '5': 'left inferior lateral ventricle',
    '7': 'left cerebellum white matter',
    '8': 'left cerebellum cortex',
    '10': 'left thalamus',
    '11': 'left caudate',
    '12': 'left putamen',
    '13': 'left pallidum',
    '14': '3rd ventricle',
    '15': '4th ventricle',
    '16': 'brain-stem',
    '17': 'left hippocampus',
    '18': 'left amygdala',
    '26': 'left accumbens area',
    '24': 'CSF',
    '28': 'left ventral DC',
    '41': 'right cerebral white matter',
    '42': 'right cerebral cortex',
    '43': 'right lateral ventricle',
    '44': 'right inferior lateral ventricle',
    '46': 'right cerebellum white matter',
    '47': 'right cerebellum cortex',
    '49': 'right thalamus',
    '50': 'right caudate',
    '51': 'right putamen',
    '52': 'right pallidum',
    '53': 'right hippocamus',
    '54': 'right amygdala',
    '58': 'right accumbens area',
    '60': 'right ventral DC'
}