## ALIGNMENT OF EYE TRACKING AND WEB ANALYTICS BACKEND

We first need to align the EASL analytics module with the eye tracking data here. To do this, we align time stamps of each of the readouts.


## EYE-TRACKING PREPROCESSING

[Cateyes](https://github.com/DiGyt/cateyes) python package

This Python Toolbox was developed for Peter König's Neurobiopsychology Lab at the Institute of Cognitive Science, Osnabrück. Its aim is to provide easy access to different automated gaze classification algorithms and to generate a unified, simplistic, and elegant way of handling eye tracking data.

Currently available gaze classification algorithms are:

 - REMoDNaV: Dar *, A. H., Wagner *, A. S. & Hanke, M. (2019). REMoDNaV: Robust Eye Movement Detection for Natural Viewing. bioRxiv. DOI: 10.1101/619254
 - U'n'Eye: Bellet, M. E., Bellet, J., Nienborg, H., Hafed, Z. M., & Berens, P. (2019). Human-level saccade detection performance using deep neural networks. Journal of neurophysiology, 121(2), 646-661.
 - NSLR-HMM: Pekkanen, J., & Lappi, O. (2017). A new and general approach to signal denoising and eye movement classification based on segmented linear regression. Scientific reports, 7(1), 1-13.
 - I-DT dispersion-based algorithm: Salvucci, D. D., & Goldberg, J. H. (2000). Identifying fixations and saccades in eye-tracking protocols. In Proceedings of the 2000 symposium on Eye tracking research & applications.
 - I-VT velocity-based algorithm: Salvucci, D. D., & Goldberg, J. H. (2000). Identifying fixations and saccades in eye-tracking protocols. In Proceedings of the 2000 symposium on Eye tracking research & applications.
 

## GENERATING BOUNDING BOXES FOR MEDSAM INPUT

There are two aspects to this problem. The first is to filter and/or smooth raw eye tracking values into discrete shapes, and the second is to (potentially) convert from a polygon/lasso shape to a more rectangular input. The MedSAM paper addresses this second step, and indicate that we should be using rectangular bounding boxes as opposed to creating organic polygon shapes.