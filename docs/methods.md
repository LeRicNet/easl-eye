## ALIGNMENT OF EYE TRACKING AND WEB ANALYTICS BACKEND

We first need to align the EASL analytics module with the eye tracking data here. To do this, we align time stamps of each of the readouts.

## TIMESTAMP ALIGNMENT

We integrate the image and eye tracking information using the system timestamps. Currently, these timestamps are not synchronized across our server hosting the image tracking UI and the eye tracking hardware.

The ratio of start time differences and end time differences is approximately 1.

There is approximately a 2% difference between the total duration of each of the datasets. We have yet to investigate this 2% difference.

This alignment should be revised and reinforced to ensure a clean synchronization.


## EYE-TRACKING PREPROCESSING

[Cateyes](https://github.com/DiGyt/cateyes) python package

This Python Toolbox was developed for Peter König's Neurobiopsychology Lab at the Institute of Cognitive Science, Osnabrück. Its aim is to provide easy access to different automated gaze classification algorithms and to generate a unified, simplistic, and elegant way of handling eye tracking data.

Currently available gaze classification algorithms are:

 - REMoDNaV: Dar *, A. H., Wagner *, A. S. & Hanke, M. (2019). REMoDNaV: Robust Eye Movement Detection for Natural Viewing. bioRxiv. DOI: 10.1101/619254
 - U'n'Eye: Bellet, M. E., Bellet, J., Nienborg, H., Hafed, Z. M., & Berens, P. (2019). Human-level saccade detection performance using deep neural networks. Journal of neurophysiology, 121(2), 646-661.
 - NSLR-HMM: Pekkanen, J., & Lappi, O. (2017). A new and general approach to signal denoising and eye movement classification based on segmented linear regression. Scientific reports, 7(1), 1-13.
 - I-DT dispersion-based algorithm: Salvucci, D. D., & Goldberg, J. H. (2000). Identifying fixations and saccades in eye-tracking protocols. In Proceedings of the 2000 symposium on Eye tracking research & applications.
 - I-VT velocity-based algorithm: Salvucci, D. D., & Goldberg, J. H. (2000). Identifying fixations and saccades in eye-tracking protocols. In Proceedings of the 2000 symposium on Eye tracking research & applications.

We are currenlty using the I-VT algorithm, which is [also utilized in Tobii Pro Lab](https://connect.tobii.com/s/article/Gaze-Filter-functions-and-effects?language=en_US).

We attempted to use NSLR-HMM and REMoDNav, however only Fixation events were returned. It may be worth spending more time on this.

## IMAGE PREPROCESSING

We map the image tracking UIDs to the Orthanc IDs so that we can query the Orthanc server for the instance DICOM information. We then extract the pixel array from that data using the pydicom package.

## GENERATING BOUNDING BOXES FOR MEDSAM INPUT

There are two aspects to this problem. The first is to filter and/or smooth raw eye tracking values into discrete shapes, and the second is to (potentially) convert from a polygon/lasso shape to a more rectangular input. The MedSAM paper addresses this second step, and indicate that we should be using rectangular bounding boxes as opposed to creating organic polygon shapes.

MedSAM requires Python>=3.9

It is important that we aggregate the gaze tracking values

expanding out versus in from eye tracking; 

## EVALUATION OF SEGMENTATIONS

At this stage of the project, we do not want to have expert annotations to compare quantitatively (i.e., a DICE score) due to the cost and preliminary nature of the work. For the first evaluation, we will qualitatively evaluate the results by showing the video results to an expert and interviewing them.