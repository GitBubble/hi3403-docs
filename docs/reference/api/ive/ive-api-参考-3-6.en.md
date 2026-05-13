---
title: "Data Types and Data Structures"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/IVE API 参考/IVE API 参考（3--6）.md
--- # Data Types and Data Structures
SVP-related data types and data structures are defined as follows: - [ot\_svp\_img\_type](#ZH-CN_TOPIC_0000002471091210): Defines the image types supported by 2D generalized images.
- [ot\_svp\_img](#ZH-CN_TOPIC_0000002504091103): Defines 2D generalized image information.
- [ot\_svp\_src\_img](#ZH-CN_TOPIC_0000002471091254): Defines the source image.
- [ot\_svp\_dst\_img](#ZH-CN_TOPIC_0000002471091286): Defines the output image.
- [OT\_SVP\_IMG\_ADDR\_NUM](#ZH-CN_TOPIC_0000002470931272): Defines the number of address channels. Fixed-point data types: - [ot\_svp\_data](#ZH-CN_TOPIC_0000002470931244): Defines 2D image information in bytes.
- [ot\_svp\_src\_data](#ZH-CN_TOPIC_0000002503971213): Defines 2D source data information in bytes.
- [ot\_svp\_dst\_data](#ZH-CN_TOPIC_0000002470931290): Defines 2D output data information in bytes.
- [ot\_svp\_8bit](#ZH-CN_TOPIC_0000002503971231): Defines an 8-bit data union.
- [ot\_svp\_point\_u16](#ZH-CN_TOPIC_0000002503971259): Defines a u16-bit point information structure.
- [ot\_svp\_point\_s16](#ZH-CN_TOPIC_0000002504091193): Defines an s16-bit point information structure.
- [ot\_svp\_point\_s25q7](#ZH-CN_TOPIC_0000002503971257): Defines a point information structure represented by s25q7.
- [ot\_svp\_point\_u14q2](#ZH-CN_TOPIC_0000002504091195): Defines a point information structure represented by u14q2.
- [ot\_svp\_rect\_u32](#ZH-CN_TOPIC_0000002470931266): Defines a rectangle information structure represented by u32.
- [ot\_svp\_rect\_u16](#ZH-CN_TOPIC_0000002470931214): Defines a rectangle information structure represented by u16.
- [ot\_svp\_rect\_s24q8](#ZH-CN_TOPIC_0000002503971197): Defines a rectangle information structure represented by s24q8.
- [ot\_svp\_lut](#ZH-CN_TOPIC_0000002503971221): Defines a lookup table structure. IVE-related data types and data structures are defined as follows: - [ot\_ive\_handle](#ZH-CN_TOPIC_0000002471091250): Defines the IVE handle.
- [OT\_IVE\_HIST\_NUM](#ZH-CN_TOPIC_0000002470931262): Defines the number of histogram bins.
- [OT\_IVE\_MAP\_NUM](#ZH-CN_TOPIC_0000002471091274): Defines the number of mapping lookup table entries.
- [OT\_IVE\_MAX\_RGN\_NUM](#ZH-CN_TOPIC_0000002471091214): Defines the maximum number of connected regions.
- [OT\_IVE\_ST\_MAX\_CORNER\_NUM](#ZH-CN_TOPIC_0000002503971193): Defines the maximum number of Shi-Tomasi-like corners.
- [OT\_IVE\_MASK\_NUM](#ZH-CN_TOPIC_0000002471091310): Mask array length.
- [OT\_IVE\_ARR\_RESERVED\_NUM\_TWO](#ZH-CN_TOPIC_0000002503971159): Reserved field array length 2.
- [OT\_IVE\_ARR\_RESERVED\_NUM\_THREE](#ZH-CN_TOPIC_0000002504091161): Reserved field array length 3.
- [OT\_IVE\_ARR\_RESERVED\_NUM\_EIGHT](#ZH-CN_TOPIC_0000002470931298): Reserved field array length 8.
- [OT\_IVE\_ARR\_RESERVED\_NUM\_TWELVE](#ZH-CN_TOPIC_0000002470931230): Reserved field array length 12.
- [OT\_IVE\_ARR\_RESERVED\_NUM\_FOURTEEN](#ZH-CN_TOPIC_0000002470931216): Reserved field array length 14.
- [OT\_IVE\_ARR\_NUM\_THREE](#ZH-CN_TOPIC_0000002503971175): Array length 3.
- [OT\_IVE\_ARR\_NUM\_EIGHT](#ZH-CN_TOPIC_0000002503971255): Array length 8.
- [OT\_IVE\_DEV\_NAME\_LENGTH](#ZH-CN_TOPIC_0000002503971217): IVE device name length.
- [OT\_IVE\_DEV\_DEFAULT\_NODE\_NUM](#ZH-CN_TOPIC_0000002504091127): Default number of IVE nodes.
- [ot\_ive\_mod\_param](#ZH-CN_TOPIC_0000002504091147): IVE module related parameter definition.
- [ot\_ive\_err\_code](#ZH-CN_TOPIC_0000002504091141): Defines error codes.
- [ot\_ive\_dma\_mode](#ZH-CN_TOPIC_0000002470931310): Defines DMA operation mode.
- [ot\_ive\_dma\_ctrl](#ZH-CN_TOPIC_0000002504091157): Defines DMA control information.
- [ot\_ive\_filter\_ctrl](#ZH-CN_TOPIC_0000002503971267): Defines template filter control information.
- [ot\_ive\_csc\_mode](#ZH-CN_TOPIC_0000002470931222): Defines color space conversion mode.
- [ot\_ive\_csc\_ctrl](#ZH-CN_TOPIC_0000002504091137): Defines color space conversion control information.
- [ot\_ive\_filter\_and\_csc\_ctrl](#ZH-CN_TOPIC_0000002471091222): Defines composite template filter plus color space conversion control information.
- [ot\_ive\_sobel\_out\_ctrl](#ZH-CN_TOPIC_0000002503971149): Defines sobel output control information.
- [ot\_ive\_sobel\_ctrl](#ZH-CN_TOPIC_0000002470931226): Defines sobel edge extraction control information.
- [ot\_ive\_mag\_and\_ang\_out\_ctrl](#ZH-CN_TOPIC_0000002471091234): Defines the output format for canny edge magnitude and angle calculation.
- [ot\_ive\_mag\_and\_ang\_ctrl](#ZH-CN_TOPIC_0000002470931264): Defines control information for canny edge magnitude and angle calculation.
- [ot\_ive\_dilate\_ctrl](#ZH-CN_TOPIC_0000002504091109): Defines dilation control information.
- [ot\_ive\_erode\_ctrl](#ZH-CN_TOPIC_0000002470931312): Defines erosion control information.
- [ot\_ive\_threshold\_mode](#ZH-CN_TOPIC_0000002504091197): Defines image binarization output format.
- [ot\_ive\_threshold\_ctrl](#ZH-CN_TOPIC_0000002504091163): Defines image binarization control information.
- [ot\_ive\_sub\_mode](#ZH-CN_TOPIC_0000002470931336): Defines the output format for image subtraction.
- [ot\_ive\_sub\_ctrl](#ZH-CN_TOPIC_0000002471091290): Defines control parameters for image subtraction.
- [ot\_ive\_integ\_out\_ctrl](#ZH-CN_TOPIC_0000002504091081): Defines integral image output control parameters.
- [ot\_ive\_integ\_ctrl](#ZH-CN_TOPIC_0000002504091115): Defines integral image calculation control parameters.
- [ot\_ive\_threshold\_s16\_mode](#ZH-CN_TOPIC_0000002504091143): Defines thresholding mode for 16-bit signed images.
- [ot\_ive\_threshold\_s16\_ctrl](#ZH-CN_TOPIC_0000002504091125): Defines thresholding control parameters for 16-bit signed images.
- [ot\_ive\_threshold\_u16\_mode](#ZH-CN_TOPIC_0000002503971223): Defines thresholding mode for 16-bit unsigned images.
- [ot\_ive\_threshold\_u16\_ctrl](#ZH-CN_TOPIC_0000002504091089): Defines thresholding control parameters for 16-bit unsigned images.
- [ot\_ive\_16bit\_to\_8bit\_mode](#ZH-CN_TOPIC_0000002471091260): Defines conversion mode from 16-bit to 8-bit images.
- [ot\_ive\_16bit\_to\_8bit\_ctrl](#ZH-CN_TOPIC_0000002470931316): Defines conversion control parameters from 16-bit to 8-bit images.
- [ot\_ive\_order\_stats\_filter\_mode](#ZH-CN_TOPIC_0000002470931238): Defines order statistics filter mode.
- [ot\_ive\_order\_stats\_filter\_ctrl](#ZH-CN_TOPIC_0000002471091240): Defines order statistics filter control parameters.
- [ot\_ive\_map\_u8bit\_lut\_mem](#ZH-CN_TOPIC_0000002471091206): Defines the lookup table memory for Map U8C1->U8C1.
- [ot\_ive\_map\_u16bit\_lut\_mem](#ZH-CN_TOPIC_0000002504091091): Defines the lookup table memory for Map U8C1->U16C1.
- [ot\_ive\_map\_s16bit\_lut\_mem](#ZH-CN_TOPIC_0000002504091173): Defines the lookup table memory for Map U8C1->S16C1.
- [ot\_ive\_map\_mode](#ZH-CN_TOPIC_0000002470931320): Defines Map mode.
- [ot\_ive\_map\_ctrl](#ZH-CN_TOPIC_0000002471091224): Defines Map control parameters.
- [ot\_ive\_equalize\_hist\_ctrl\_mem](#ZH-CN_TOPIC_0000002471091324): Defines histogram equalization auxiliary memory.
- [ot\_ive\_equalize\_hist\_ctrl](#ZH-CN_TOPIC_0000002503971189): Defines histogram equalization control parameters.
- [ot\_ive\_add\_ctrl](#ZH-CN_TOPIC_0000002503971153): Defines weighted addition control parameters for two images.
- [ot\_ive\_ncc\_dst\_mem](#ZH-CN_TOPIC_0000002503971173): Defines NCC output memory information.
- [ot\_ive\_rgn](#ZH-CN_TOPIC_0000002471091252): Defines connected region information.
- [ot\_ive\_ccblob](#ZH-CN_TOPIC_0000002503971207): Defines the output information for connected component labeling.
- [ot\_ive\_ccl\_mode](#ZH-CN_TOPIC_0000002470931332): Defines connected component labeling mode.
- [ot\_ive\_ccl\_ctrl](#ZH-CN_TOPIC_0000002471091318): Defines connected component labeling control parameters.
- [ot\_ive\_gmm\_ctrl](#ZH-CN_TOPIC_0000002471091236): Defines control parameters for GMM background modeling.
- [ot\_ive\_gmm2\_sns\_factor\_mode](#ZH-CN_TOPIC_0000002471091300): Defines sensitivity factor mode.
- [ot\_ive\_gmm2\_life\_update\_factor\_mode](#ZH-CN_TOPIC_0000002503971203): Defines model lifetime parameter update mode.
- [ot\_ive\_gmm2\_ctrl](#ZH-CN_TOPIC_0000002504091119): Defines control parameters for GMM2 background modeling.
- [ot\_ive\_canny\_stack\_size](#ZH-CN_TOPIC_0000002504091083): Defines the strong edge point stack size structure for the first half of Canny edge calculation.
- [ot\_ive\_canny\_hys\_edge\_ctrl](#ZH-CN_TOPIC_0000002503971183): Defines control parameters for the first half of Canny edge calculation task.
- [ot\_ive\_lbp\_compare\_mode](#ZH-CN_TOPIC_0000002470931250): Defines LBP texture calculation control parameters.
- [ot\_ive\_lbp\_ctrl](#ZH-CN_TOPIC_0000002471091226): Defines LBP texture calculation control parameters.
- [ot\_ive\_norm\_grad\_out\_ctrl](#ZH-CN_TOPIC_0000002503971179): Defines the output control enumeration type for normalized gradient information calculation.
- [ot\_ive\_norm\_grad\_ctrl](#ZH-CN_TOPIC_0000002470931288): Defines control parameters for normalized gradient information calculation.
- [ot\_ive\_lk\_optical\_flow\_pyr\_out\_mode](#ZH-CN_TOPIC_0000002504091077): Defines the output mode for pyramidal LK optical flow calculation.
- [ot\_ive\_lk\_optical\_flow\_pyr\_ctrl](#ZH-CN_TOPIC_0000002503971181): Defines control parameters for pyramidal LK optical flow calculation.
- [ot\_ive\_st\_max\_eig\_val](#ZH-CN_TOPIC_0000002504091183): Defines the maximum corner response value structure for Shi-Tomasi-like corner calculation.
- [ot\_ive\_st\_cand\_corner\_ctrl](#ZH-CN_TOPIC_0000002504091117): Defines control parameters for Shi-Tomasi-like candidate corner calculation.
- [ot\_ive\_st\_corner\_info](#ZH-CN_TOPIC_0000002503971265): Defines the corner information structure output from Shi-Tomasi-like corner calculation.
- [ot\_ive\_st\_corner\_ctrl](#ZH-CN_TOPIC_0000002471091220): Defines control parameters for Shi-Tomasi-like corner filtering.
- [ot\_ive\_sad\_mode](#ZH-CN_TOPIC_0000002470931274): Defines SAD calculation mode.
- [ot\_ive\_sad\_out\_ctrl](#ZH-CN_TOPIC_0000002471091278): Defines SAD output control mode.
- [ot\_ive\_sad\_ctrl](#ZH-CN_TOPIC_0000002471091212): Defines SAD control parameters.
- [ot\_ive\_resize\_mode](#ZH-CN_TOPIC_0000002503971219): Defines Resize mode.
- [ot\_ive\_resize\_ctrl](#ZH-CN_TOPIC_0000002471091258): Defines Resize control parameters.
- [ot\_ive\_grad\_fg\_mode](#ZH-CN_TOPIC_0000002503971161): Defines gradient foreground calculation mode.
- [ot\_ive\_grad\_fg\_ctrl](#ZH-CN_TOPIC_0000002504091111): Defines gradient foreground calculation control parameters.
- [ot\_ive\_cand\_bg\_pixel](#ZH-CN_TOPIC_0000002503971261): Defines candidate background model data.
- [ot\_ive\_wrok\_bg\_pixel](#ZH-CN_TOPIC_0000002503971171): Defines working background model data.
- [ot\_ive\_bg\_life](#ZH-CN_TOPIC_0000002471091208): Defines background lifetime data.
- [ot\_ive\_bg\_model\_pixel](#ZH-CN_TOPIC_0000002503971177): Defines background model data.
- [ot\_ive\_fg\_status\_data](#ZH-CN_TOPIC_0000002503971239): Defines foreground status data.
- [ot\_ive\_bg\_status\_data](#ZH-CN_TOPIC_0000002503971253): Defines background status data.
- [ot\_ive\_match\_bg\_model\_ctrl](#ZH-CN_TOPIC_0000002503971249): Defines background matching control parameters.
- [ot\_ive\_update\_bg\_model\_ctrl](#ZH-CN_TOPIC_0000002471091248): Defines background update control parameters.
- [ot\_ive\_ann\_mlp\_accurate](#ZH-CN_TOPIC_0000002504091185): Defines ann\_mlp input feature vector type.
- [ot\_ive\_ann\_mlp\_actv\_func](#ZH-CN_TOPIC_0000002503971151): Defines ann\_mlp activation function enumeration type.
- [ot\_ive\_ann\_mlp\_model](#ZH-CN_TOPIC_0000002503971233): Defines ann\_mlp model data structure.
- [ot\_ive\_svm\_type](#ZH-CN_TOPIC_0000002471091314): Defines SVM type.
- [ot\_ive\_svm\_kernel\_type](#ZH-CN_TOPIC_0000002471091268): Defines SVM kernel function type.
- [ot\_ive\_svm\_model](#ZH-CN_TOPIC_0000002470931338): Defines SVM model data structure.
- [ot\_ive\_cnn\_actv\_func](#ZH-CN_TOPIC_0000002470931254): Defines CNN activation function enumeration type.
- [ot\_ive\_cnn\_pooling](#ZH-CN_TOPIC_0000002471091230): Defines CNN pooling operation enumeration type.
- [ot\_ive\_cnn\_conv\_pooling](#ZH-CN_TOPIC_0000002471091306): Defines CNN single-layer Conv-Re LU-Pooling operation package parameter structure.
- [ot\_ive\_cnn\_fc\_info](#ZH-CN_TOPIC_0000002470931296): Defines CNN fully connected network parameter structure.
- [ot\_ive\_cnn\_model](#ZH-CN_TOPIC_0000002504091131): Defines CNN model parameter structure.
- [ot\_ive\_cnn\_ctrl](#ZH-CN_TOPIC_0000002471091238): Defines control parameters for CNN prediction task.
- [ot\_ive\_cnn\_result](#ZH-CN_TOPIC_0000002503971157): Defines CNN single sample prediction result structure.
- [ot\_ive\_persp\_trans\_point\_pair](#ZH-CN_TOPIC_0000002470931326): Defines perspective transformation point pair structure.
- [ot\_ive\_persp\_trans\_alg\_mode](#ZH-CN_TOPIC_0000002471091242): Defines perspective transformation algorithm mode enumeration.
- [ot\_ive\_persp\_trans\_csc\_mode](#ZH-CN_TOPIC_0000002470931228): Defines perspective transformation color space conversion mode.
- [ot\_ive\_kcf\_core\_id](#ZH-CN_TOPIC_0000002504091191): Defines KCF kernel ID.
- [ot\_ive\_persp\_trans\_ctrl](#ZH-CN_TOPIC_0000002471091262): Defines perspective transformation control parameters.
- [ot\_ive\_roi\_info](#ZH-CN_TOPIC_0000002503971155): Defines region of interest information parameters.
- [ot\_ive\_kcf\_proc\_ctrl](#ZH-CN_TOPIC_0000002471091264): Defines tracking processing control parameters.
- [ot\_ive\_list\_head](#ZH-CN_TOPIC_0000002504091189): Defines linked list head structure parameters.
- [ot\_ive\_kcf\_obj](#ZH-CN_TOPIC_0000002471091292): Defines target information structure parameters.
- [ot\_ive\_kcf\_obj\_node](#ZH-CN_TOPIC_0000002470931324): Defines target linked list node parameters.
- [ot\_ive\_kcf\_list\_state](#ZH-CN_TOPIC_0000002504091113): Defines target linked list state enumeration type.
- [ot\_ive\_kcf\_obj\_list](#ZH-CN_TOPIC_0000002470931236): Defines target linked list structure parameters.
- [ot\_ive\_kcf\_bbox](#ZH-CN_TOPIC_0000002504091101): Defines target region information parameters.
- [ot\_ive\_kcf\_bbox\_ctrl](#ZH-CN_TOPIC_0000002470931278): Defines target region information control parameters.
- [ot\_ive\_hog\_mode](#ZH-CN_TOPIC_0000002504091097): Defines HOG (Histogram of Oriented Gradient) feature storage mode enumeration type.
- [ot\_ive\_hog\_ctrl](#ZH-CN_TOPIC_0000002470931248): Defines HOG (Histogram of Oriented Gradient) feature calculation control parameters. ## SVP-Related Data Types and Data Structures<a name="ZH-CN_TOPIC_0000002471091256"></a> ### ot\_svp\_img\_type<a name="ZH-CN_TOPIC_0000002471091210"></a> 【Description】 Defines the image types supported by 2D generalized images. 【Definition】 ```
/* Img type */
typedef enum { OT_SVP_IMG_TYPE_U8C1 = 0x0, OT_SVP_IMG_TYPE_S8C1 = 0x1, OT_SVP_IMG_TYPE_YUV420SP = 0x2, /* YUV420 Semi Planar */ OT_SVP_IMG_TYPE_YUV422SP = 0x3, /* YUV422 Semi Planar */ OT_SVP_IMG_TYPE_YUV420P = 0x4, /* YUV420 Planar */ OT_SVP_IMG_TYPE_YUV422P = 0x5, /* YUV422 planar */ OT_SVP_IMG_TYPE_S8C2_PACKAGE = 0x6, OT_SVP_IMG_TYPE_S8C2_PLANAR = 0x7, OT_SVP_IMG_TYPE_S16C1 = 0x8, OT_SVP_IMG_TYPE_U16C1 = 0x9, OT_SVP_IMG_TYPE_U8C3_PACKAGE = 0xa, OT_SVP_IMG_TYPE_U8C3_PLANAR = 0xb, OT_SVP_IMG_TYPE_S32C1 = 0xc, OT_SVP_IMG_TYPE_U32C1 = 0xd, OT_SVP_IMG_TYPE_S64C1 = 0xe, OT_SVP_IMG_TYPE_U64C1 = 0xf, OT_SVP_IMG_TYPE_BUTT } ot_svp_img_type;
``` 【Members】 <a name="table15961mcpsimp"></a>
<table><thead align="left"><tr id="row15966mcpsimp"><th class="cellrowborder" valign="top" width="43%" id="mcps1.1.3.1.1"><p id="p15968mcpsimp"><a name="p15968mcpsimp"></a><a name="p15968mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.1.3.1.2"><p id="p15970mcpsimp"><a name="p15970mcpsimp"></a><a name="p15970mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row15972mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p15974mcpsimp"><a name="p15974mcpsimp"></a><a name="p15974mcpsimp"></a>OT_SVP_IMG_TYPE_U8C1</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p15976mcpsimp"><a name="p15976mcpsimp"></a><a name="p15976mcpsimp"></a>A single-channel image where each pixel is represented by 1 8-bit unsigned data. See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_U8C1 \ OT_SVP_IMG_TYPE_S8C1 \ OT_SVP_IMG_TYPE_S16C1 \ OT_SVP_IMG_TYPE_U16C1 \ OT_SVP_IMG_TYPE_S32C1 \ OT_SVP_IMG_TYPE_U32C1 \ OT_SVP_IMG_TYPE_S64C1 \ OT_SVP_IMG_TYPE_U64C1.</p>
</td>
</tr>
<tr id="row15978mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p15980mcpsimp"><a name="p15980mcpsimp"></a><a name="p15980mcpsimp"></a>OT_SVP_IMG_TYPE_S8C1</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p15982mcpsimp"><a name="p15982mcpsimp"></a><a name="p15982mcpsimp"></a>A single-channel image where each pixel is represented by 1 8-bit signed data. See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_U8C1 \ OT_SVP_IMG_TYPE_S8C1 \ OT_SVP_IMG_TYPE_S16C1 \ OT_SVP_IMG_TYPE_U16C1 \ OT_SVP_IMG_TYPE_S32C1 \ OT_SVP_IMG_TYPE_U32C1 \ OT_SVP_IMG_TYPE_S64C1 \ OT_SVP_IMG_TYPE_U64C1.</p>
</td>
</tr>
<tr id="row15984mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p15986mcpsimp"><a name="p15986mcpsimp"></a><a name="p15986mcpsimp"></a>OT_SVP_IMG_TYPE_YUV420SP</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p15988mcpsimp"><a name="p15988mcpsimp"></a><a name="p15988mcpsimp"></a>YUV420 Semiplanar format image.</p>
<p id="p15989mcpsimp"><a name="p15989mcpsimp"></a><a name="p15989mcpsimp"></a>See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_YUV420SP.</p>
</td>
</tr>
<tr id="row15991mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p15993mcpsimp"><a name="p15993mcpsimp"></a><a name="p15993mcpsimp"></a>OT_SVP_IMG_TYPE_YUV422SP</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p15995mcpsimp"><a name="p15995mcpsimp"></a><a name="p15995mcpsimp"></a>YUV422 Semiplanar format image.</p>
<p id="p15996mcpsimp"><a name="p15996mcpsimp"></a><a name="p15996mcpsimp"></a>See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_YUV422SP.</p>
</td>
</tr>
<tr id="row15998mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p16000mcpsimp"><a name="p16000mcpsimp"></a><a name="p16000mcpsimp"></a>OT_SVP_IMG_TYPE_YUV420P</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p16002mcpsimp"><a name="p16002mcpsimp"></a><a name="p16002mcpsimp"></a>YUV420 Planar format image. See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_YUV420P.</p>
</td>
</tr>
<tr id="row16004mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p16006mcpsimp"><a name="p16006mcpsimp"></a><a name="p16006mcpsimp"></a>OT_SVP_IMG_TYPE_YUV422P</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p16008mcpsimp"><a name="p16008mcpsimp"></a><a name="p16008mcpsimp"></a>YUV422 Planar format image. See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_YUV422P.</p>
</td>
</tr>
<tr id="row16010mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p16012mcpsimp"><a name="p16012mcpsimp"></a><a name="p16012mcpsimp"></a>OT_SVP_IMG_TYPE_S8C2_PACKAGE</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p16014mcpsimp"><a name="p16014mcpsimp"></a><a name="p16014mcpsimp"></a>A 2-channel image where each pixel is represented by 2 8-bit signed data stored in package format.</p>
<p id="p16015mcpsimp"><a name="p16015mcpsimp"></a><a name="p16015mcpsimp"></a>See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_S8C2_PACKAGE.</p>
</td>
</tr>
<tr id="row16017mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p16019mcpsimp"><a name="p16019mcpsimp"></a><a name="p16019mcpsimp"></a>OT_SVP_IMG_TYPE_S8C2_PLANAR</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p16021mcpsimp"><a name="p16021mcpsimp"></a><a name="p16021mcpsimp"></a>A 2-channel image where each pixel is represented by 2 8-bit signed data stored in planar format.</p>
<p id="p16022mcpsimp"><a name="p16022mcpsimp"></a><a name="p16022mcpsimp"></a>See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_S8C2_PLANAR.</p>
</td>
</tr>
<tr id="row16024mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p16026mcpsimp"><a name="p16026mcpsimp"></a><a name="p16026mcpsimp"></a>OT_SVP_IMG_TYPE_S16C1</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p16028mcpsimp"><a name="p16028mcpsimp"></a><a name="p16028mcpsimp"></a>A single-channel image where each pixel is represented by 1 16-bit signed data. See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_U8C1 \ OT_SVP_IMG_TYPE_S8C1 \ OT_SVP_IMG_TYPE_S16C1 \ OT_SVP_IMG_TYPE_U16C1 \ OT_SVP_IMG_TYPE_S32C1 \ OT_SVP_IMG_TYPE_U32C1 \ OT_SVP_IMG_TYPE_S64C1 \ OT_SVP_IMG_TYPE_U64C1.</p>
</td>
</tr>
<tr id="row16030mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p16032mcpsimp"><a name="p16032mcpsimp"></a><a name="p16032mcpsimp"></a>OT_SVP_IMG_TYPE_U16C1</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p16034mcpsimp"><a name="p16034mcpsimp"></a><a name="p16034mcpsimp"></a>A single-channel image where each pixel is represented by 1 16-bit unsigned data. See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_U8C1 \ OT_SVP_IMG_TYPE_S8C1 \ OT_SVP_IMG_TYPE_S16C1 \ OT_SVP_IMG_TYPE_U16C1 \ OT_SVP_IMG_TYPE_S32C1 \ OT_SVP_IMG_TYPE_U32C1 \ OT_SVP_IMG_TYPE_S64C1 \ OT_SVP_IMG_TYPE_U64C1.</p>
</td>
</tr>
<tr id="row16036mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p16038mcpsimp"><a name="p16038mcpsimp"></a><a name="p16038mcpsimp"></a>OT_SVP_IMG_TYPE_U8C3_PACKAGE</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p16040mcpsimp"><a name="p16040mcpsimp"></a><a name="p16040mcpsimp"></a>A 3-channel image where each pixel is represented by 3 8-bit unsigned data stored in Package format.</p>
<p id="p16041mcpsimp"><a name="p16041mcpsimp"></a><a name="p16041mcpsimp"></a>See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_U8C3_PACKAGE.</p>
</td>
</tr>
<tr id="row16043mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p16045mcpsimp"><a name="p16045mcpsimp"></a><a name="p16045mcpsimp"></a>OT_SVP_IMG_TYPE_U8C3_PLANAR</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p16047mcpsimp"><a name="p16047mcpsimp"></a><a name="p16047mcpsimp"></a>A 3-channel image where each pixel is represented by 3 8-bit unsigned data stored in planar format.</p>
<p id="p16048mcpsimp"><a name="p16048mcpsimp"></a><a name="p16048mcpsimp"></a>See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_U8C3_PLANAR.</p>
</td>
</tr>
<tr id="row16050mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p16052mcpsimp"><a name="p16052mcpsimp"></a><a name="p16052mcpsimp"></a>OT_SVP_IMG_TYPE_S32C1</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p16054mcpsimp"><a name="p16054mcpsimp"></a><a name="p16054mcpsimp"></a>A single-channel image where each pixel is represented by 1 32-bit signed data. See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_U8C1 \ OT_SVP_IMG_TYPE_S8C1 \ OT_SVP_IMG_TYPE_S16C1 \ OT_SVP_IMG_TYPE_U16C1 \ OT_SVP_IMG_TYPE_S32C1 \ OT_SVP_IMG_TYPE_U32C1 \ OT_SVP_IMG_TYPE_S64C1 \ OT_SVP_IMG_TYPE_U64C1.</p>
</td>
</tr>
<tr id="row16056mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p16058mcpsimp"><a name="p16058mcpsimp"></a><a name="p16058mcpsimp"></a>OT_SVP_IMG_TYPE_U32C1</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p16060mcpsimp"><a name="p16060mcpsimp"></a><a name="p16060mcpsimp"></a>A single-channel image where each pixel is represented by 1 32-bit unsigned data. See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_U8C1 \ OT_SVP_IMG_TYPE_S8C1 \ OT_SVP_IMG_TYPE_S16C1 \ OT_SVP_IMG_TYPE_U16C1 \ OT_SVP_IMG_TYPE_S32C1 \ OT_SVP_IMG_TYPE_U32C1 \ OT_SVP_IMG_TYPE_S64C1 \ OT_SVP_IMG_TYPE_U64C1.</p>
</td>
</tr>
<tr id="row16062mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p16064mcpsimp"><a name="p16064mcpsimp"></a><a name="p16064mcpsimp"></a>OT_SVP_IMG_TYPE_S64C1</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p16066mcpsimp"><a name="p16066mcpsimp"></a><a name="p16066mcpsimp"></a>A single-channel image where each pixel is represented by 1 64-bit signed data. See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_U8C1 \ OT_SVP_IMG_TYPE_S8C1 \ OT_SVP_IMG_TYPE_S16C1 \ OT_SVP_IMG_TYPE_U16C1 \ OT_SVP_IMG_TYPE_S32C1 \ OT_SVP_IMG_TYPE_U32C1 \ OT_SVP_IMG_TYPE_S64C1 \ OT_SVP_IMG_TYPE_U64C1.</p>
</td>
</tr>
<tr id="row16068mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p16070mcpsimp"><a name="p16070mcpsimp"></a><a name="p16070mcpsimp"></a>OT_SVP_IMG_TYPE_U64C1</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p16072mcpsimp"><a name="p16072mcpsimp"></a><a name="p16072mcpsimp"></a>A single-channel image where each pixel is represented by 1 64-bit unsigned data. See the ot_svp_img image diagram for OT_SVP_IMG_TYPE_U8C1 \ OT_SVP_IMG_TYPE_S8C1 \ OT_SVP_IMG_TYPE_S16C1 \ OT_SVP_IMG_TYPE_U16C1 \ OT_SVP_IMG_TYPE_S32C1 \ OT_SVP_IMG_TYPE_U32C1 \ OT_SVP_IMG_TYPE_S64C1 \ OT_SVP_IMG_TYPE_U64C1.</p>
</td>
</tr>
</tbody>
</table> 【Notes】 None. 【Related Data Types and AP Is】 - [ot\_svp\_img](#ot_svp_img)
- [ot\_svp\_src\_img](#ot_svp_src_img)
- [ot\_svp\_dst\_img](#ot_svp_dst_img) ### ot\_svp\_img<a name="ZH-CN_TOPIC_0000002504091103"></a> 【Description】 Defines 2D generalized image information. 【Definition】 ```
typedef struct { td_u64 phys_addr[OT_SVP_IMG_ADDR_NUM]; /* RW;The physical address of the image */ td_u64 virt_addr[OT_SVP_IMG_ADDR_NUM]; /* RW;The virtual address of the image */ td_u32 stride[OT_SVP_IMG_STRIDE_NUM]; /* RW;The stride of the image */ td_u32 width; /* RW;The width of the image */ td_u32 height; /* RW;The height of the image */ ot_svp_img_type type; /* RW;The type of the image */
} ot_svp_img;
``` 【Members】 <a name="table7778mcpsimp"></a>
<table><thead align="left"><tr id="row7783mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p7785mcpsimp"><a name="p7785mcpsimp"></a><a name="p7785mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p7787mcpsimp"><a name="p7787mcpsimp"></a><a name="p7787mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row7789mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p7791mcpsimp"><a name="p7791mcpsimp"></a><a name="p7791mcpsimp"></a><span xml:lang="da-DK" id="ph7792mcpsimp"><a name="ph7792mcpsimp"></a><a name="ph7792mcpsimp"></a>phys_addr</span>[<a href="#ZH-CN_TOPIC_0000002470931272">OT_SVP_IMG_ADDR_NUM</a>]</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p7795mcpsimp"><a name="p7795mcpsimp"></a><a name="p7795mcpsimp"></a>Physical address array of the generalized image.</p>
</td>
</tr>
<tr id="row7796mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p7798mcpsimp"><a name="p7798mcpsimp"></a><a name="p7798mcpsimp"></a><span xml:lang="da-DK" id="ph7799mcpsimp"><a name="ph7799mcpsimp"></a><a name="ph7799mcpsimp"></a>virt_addr</span>[OT_SVP_IMG_ADDR_NUM]</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p7802mcpsimp"><a name="p7802mcpsimp"></a><a name="p7802mcpsimp"></a>Virtual address array of the generalized image.</p>
</td>
</tr>
<tr id="row7803mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p7805mcpsimp"><a name="p7805mcpsimp"></a><a name="p7805mcpsimp"></a><span xml:lang="da-DK" id="ph7806mcpsimp"><a name="ph7806mcpsimp"></a><a name="ph7806mcpsimp"></a>stride</span>[OT_SVP_IMG_STRIDE_NUM]</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p7809mcpsimp"><a name="p7809mcpsimp"></a><a name="p7809mcpsimp"></a>Stride of the generalized image.</p>
</td>
</tr>
<tr id="row7810mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="da-DK" id="p7812mcpsimp"><a name="p7812mcpsimp"></a><a name="p7812mcpsimp"></a>width</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p7814mcpsimp"><a name="p7814mcpsimp"></a><a name="p7814mcpsimp"></a>Width of the generalized image.</p>
</td>
</tr>
<tr id="row7815mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p xml:lang="da-DK" id="p7817mcpsimp"><a name="p7817mcpsimp"></a><a name="p7817mcpsimp"></a>height</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p7819mcpsimp"><a name="p7819mcpsimp"></a><a name="p7819mcpsimp"></a>Height of the generalized image.</p>
</td>
</tr>
<tr id="row7820mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p7822mcpsimp"><a name="p7822mcpsimp"></a><a name="p7822mcpsimp"></a>type</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p7824mcpsimp"><a name="p7824mcpsimp"></a><a name="p7824mcpsimp"></a>Type of the generalized image.</p>
</td>
</tr>
</tbody>
</table> 【Notes】 For image diagrams under each type, refer to the ot_svp_img image diagrams for types OT\_SVP\_IMG\_TYPE\_U8C1 \\ OT\_SVP\_IMG\_TYPE\_S8C1 \\ OT\_SVP\_IMG\_TYPE\_S16C1 \\ OT\_SVP\_IMG\_TYPE\_U16C1 \\ OT\_SVP\_IMG\_TYPE\_S32C1 \\ OT\_SVP\_IMG\_TYPE\_U32C1 \\ OT\_SVP\_IMG\_TYPE\_S64C1 \\ OT\_SVP\_IMG\_TYPE\_U64C1 through OT\_SVP\_IMG\_TYPE\_U8C3\_PLANAR. 【Related Data and AP Is】 - [ot\_svp\_img\_type](#ot_svp_img_type)
- [ot\_svp\_src\_img](#ot_svp_src_img)
- [ot\_svp\_dst\_img](#ot_svp_dst_img) ### ot\_svp\_src\_img<a name="ZH-CN_TOPIC_0000002471091254"></a> 【Description】 Defines the source image. 【Definition】 ```
typedef ot_svp_img ot_svp_src_img;
``` 【Members】 None 【Notes】 None 【Related Data and AP Is】 - [ot\_svp\_img\_type](#ot_svp_img_type)
- [ot\_svp\_dst\_img](#ot_svp_dst_img) ### ot\_svp\_dst\_img<a name="ZH-CN_TOPIC_0000002471091286"></a> 【Description】 Defines the output image. 【Definition】 ```
typedef ot_svp_img ot_svp_dst_img;
``` 【Members】 None 【Notes】 None 【Related Data and AP Is】 - [ot\_svp\_img\_type](#ot_svp_img_type)
- [ot\_svp\_src\_img](#ot_svp_src_img) ### OT\_SVP\_IMG\_ADDR\_NUM<a name="ZH-CN_TOPIC_0000002470931272"></a> 【Description】 Defines the number of address channels. 【Definition】 ```
#define OT_SVP_IMAE_ADDR_NUM 3
``` 【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 None. ### OT\_SVP\_IMG\_STRIDE\_NUM<a name="ZH-CN_TOPIC_0000002470931232"></a> 【Description】 Defines the stride array length. 【Definition】 ```
#define OT_SVP_IMG_STRIDE_NUM 3
``` 【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 None. ## Fixed-Point Data Types<a name="ZH-CN_TOPIC_0000002471091272"></a> 【Description】 Defines fixed-point data types. 【Definition】 ```
typedef unsigned char td_u0q8;
typedef unsigned char td_u1q7;
typedef unsigned char td_u5q3;
typedef unsigned char td_u3q5; typedef unsigned short td_u0q16;
typedef unsigned short td_u4q12;
typedef unsigned short td_u6q10;
typedef unsigned short td_u8q8;
typedef unsigned short td_u9q7;
typedef unsigned short td_u12q4;
typedef unsigned short td_u14q2;
typedef unsigned short td_u5q11;
typedef unsigned short td_u1q15;
typedef unsigned short td_u2q14;
typedef td_u6q10 td_ufp16;
typedef short td_s9q7;
typedef short td_s14q2;
typedef short td_s1q15; typedef unsigned int td_u22q10;
typedef unsigned int td_u25q7;
typedef unsigned int td_u21q11;
typedef unsigned int td_u14q18;
typedef unsigned int td_u8q24;
typedef unsigned int td_u4q28; typedef int td_s25q7;
typedef int td_s16q16;
typedef int td_s14q18;
typedef int td_s20q12;
typedef int td_s24q8; typedef unsigned short td_u8q4f4;
``` 【Members】 <a name="table11614mcpsimp"></a>
<table><thead align="left"><tr id="row11619mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.3.1.1"><p id="p11621mcpsimp"><a name="p11621mcpsimp"></a><a name="p11621mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="82%" id="mcps1.1.3.1.2"><p id="p11623mcpsimp"><a name="p11623mcpsimp"></a><a name="p11623mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row11625mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11627mcpsimp"><a name="p11627mcpsimp"></a><a name="p11627mcpsimp"></a>td_u0q8</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11629mcpsimp"><a name="p11629mcpsimp"></a><a name="p11629mcpsimp"></a>0 bits for integer part, 8 bits for fractional part. Represented as UQ0.8 in the documentation.</p>
</td>
</tr>
<tr id="row11630mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11632mcpsimp"><a name="p11632mcpsimp"></a><a name="p11632mcpsimp"></a>td_u1q7</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11634mcpsimp"><a name="p11634mcpsimp"></a><a name="p11634mcpsimp"></a>Upper 1 unsigned bit for integer part, lower 7 bits for fractional part. Represented as UQ1.7 in the documentation.</p>
</td>
</tr>
<tr id="row11635mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11637mcpsimp"><a name="p11637mcpsimp"></a><a name="p11637mcpsimp"></a>td_u5q3</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11639mcpsimp"><a name="p11639mcpsimp"></a><a name="p11639mcpsimp"></a>Upper 5 unsigned bits for integer part, lower 3 bits for fractional part. Represented as UQ5.3 in the documentation.</p>
</td>
</tr>
<tr id="row11640mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11642mcpsimp"><a name="p11642mcpsimp"></a><a name="p11642mcpsimp"></a>td_u3q5</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11644mcpsimp"><a name="p11644mcpsimp"></a><a name="p11644mcpsimp"></a>Upper 3 unsigned bits for integer part, lower 5 bits for fractional part. Represented as UQ3.5 in the documentation.</p>
</td>
</tr>
<tr id="row11645mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11647mcpsimp"><a name="p11647mcpsimp"></a><a name="p11647mcpsimp"></a>td_u0q16</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11649mcpsimp"><a name="p11649mcpsimp"></a><a name="p11649mcpsimp"></a>0 bits for integer part, 16 bits for fractional part. Represented as UQ0.16 in the documentation.</p>
</td>
</tr>
<tr id="row11650mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11652mcpsimp"><a name="p11652mcpsimp"></a><a name="p11652mcpsimp"></a>td_u4q12</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11654mcpsimp"><a name="p11654mcpsimp"></a><a name="p11654mcpsimp"></a>Upper 4 unsigned bits for integer part, lower 12 bits for fractional part. Represented as UQ4.12 in the documentation.</p>
</td>
</tr>
<tr id="row11655mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11657mcpsimp"><a name="p11657mcpsimp"></a><a name="p11657mcpsimp"></a>td_u6q10</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11659mcpsimp"><a name="p11659mcpsimp"></a><a name="p11659mcpsimp"></a>Upper 6 unsigned bits for integer part, lower 10 bits for fractional part. Represented as UQ6.10 in the documentation.</p>
</td>
</tr>
<tr id="row11660mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11662mcpsimp"><a name="p11662mcpsimp"></a><a name="p11662mcpsimp"></a>td_u8q8</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11664mcpsimp"><a name="p11664mcpsimp"></a><a name="p11664mcpsimp"></a>Upper 8 unsigned bits for integer part, lower 8 bits for fractional part. Represented as UQ8.8 in the documentation.</p>
</td>
</tr>
<tr id="row11665mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11667mcpsimp"><a name="p11667mcpsimp"></a><a name="p11667mcpsimp"></a>td_u9q7</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11669mcpsimp"><a name="p11669mcpsimp"></a><a name="p11669mcpsimp"></a>Upper 9 unsigned bits for integer part, lower 7 bits for fractional part. Represented as UQ9.7 in the documentation.</p>
</td>
</tr>
<tr id="row11670mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11672mcpsimp"><a name="p11672mcpsimp"></a><a name="p11672mcpsimp"></a>td_u12q4</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11674mcpsimp"><a name="p11674mcpsimp"></a><a name="p11674mcpsimp"></a>Upper 12 unsigned bits for integer part, lower 4 bits for fractional part. Represented as UQ12.4 in the documentation.</p>
</td>
</tr>
<tr id="row11675mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11677mcpsimp"><a name="p11677mcpsimp"></a><a name="p11677mcpsimp"></a>td_u14q2</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11679mcpsimp"><a name="p11679mcpsimp"></a><a name="p11679mcpsimp"></a>Upper 14 unsigned bits for integer part, lower 2 bits for fractional part. Represented as UQ14.2 in the documentation.</p>
</td>
</tr>
<tr id="row11680mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11682mcpsimp"><a name="p11682mcpsimp"></a><a name="p11682mcpsimp"></a>td_u5q11</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11684mcpsimp"><a name="p11684mcpsimp"></a><a name="p11684mcpsimp"></a>Upper 5 unsigned bits for integer part, lower 11 bits for fractional part. Represented as UQ5.11 in the documentation.</p>
</td>
</tr>
<tr id="row11685mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11687mcpsimp"><a name="p11687mcpsimp"></a><a name="p11687mcpsimp"></a>td_u1q15</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11689mcpsimp"><a name="p11689mcpsimp"></a><a name="p11689mcpsimp"></a>Upper 1 unsigned bit for integer part, lower 15 bits for fractional part. Represented as UQ1.15 in the documentation.</p>
</td>
</tr>
<tr id="row11690mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11692mcpsimp"><a name="p11692mcpsimp"></a><a name="p11692mcpsimp"></a>td_u2q14</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11694mcpsimp"><a name="p11694mcpsimp"></a><a name="p11694mcpsimp"></a>Upper 2 unsigned bits for integer part, lower 14 bits for fractional part. Represented as UQ2.14 in the documentation.</p>
</td>
</tr>
<tr id="row11695mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11697mcpsimp"><a name="p11697mcpsimp"></a><a name="p11697mcpsimp"></a>td_ufp16</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11699mcpsimp"><a name="p11699mcpsimp"></a><a name="p11699mcpsimp"></a>Upper 6 unsigned bits for integer part, lower 10 bits for fractional part. Represented as UQ6.10 in the documentation.</p>
</td>
</tr>
<tr id="row11700mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11702mcpsimp"><a name="p11702mcpsimp"></a><a name="p11702mcpsimp"></a>td_s9q7</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11704mcpsimp"><a name="p11704mcpsimp"></a><a name="p11704mcpsimp"></a>Upper 9 signed bits for integer part, lower 7 bits for fractional part. Represented as SQ9.7 in the documentation.</p>
</td>
</tr>
<tr id="row11705mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11707mcpsimp"><a name="p11707mcpsimp"></a><a name="p11707mcpsimp"></a>td_s14q2</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11709mcpsimp"><a name="p11709mcpsimp"></a><a name="p11709mcpsimp"></a>Upper 14 signed bits for integer part, lower 2 bits for fractional part. Represented as SQ14.2 in the documentation.</p>
</td>
</tr>
<tr id="row11710mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11712mcpsimp"><a name="p11712mcpsimp"></a><a name="p11712mcpsimp"></a>td_s1q15</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11714mcpsimp"><a name="p11714mcpsimp"></a><a name="p11714mcpsimp"></a>Upper 1 signed bit for integer part, lower 15 bits for fractional part. Represented as SQ1.15 in the documentation.</p>
</td>
</tr>
<tr id="row11715mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11717mcpsimp"><a name="p11717mcpsimp"></a><a name="p11717mcpsimp"></a>td_u22q10</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11719mcpsimp"><a name="p11719mcpsimp"></a><a name="p11719mcpsimp"></a>Upper 22 unsigned bits for integer part, lower 10 bits for fractional part. Represented as UQ22.10 in the documentation.</p>
</td>
</tr>
<tr id="row11720mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11722mcpsimp"><a name="p11722mcpsimp"></a><a name="p11722mcpsimp"></a>td_u25q7</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11724mcpsimp"><a name="p11724mcpsimp"></a><a name="p11724mcpsimp"></a>Upper 25 unsigned bits for integer part, lower 7 bits for fractional part. Represented as UQ25.7 in the documentation.</p>
</td>
</tr>
<tr id="row11725mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11727mcpsimp"><a name="p11727mcpsimp"></a><a name="p11727mcpsimp"></a>td_u21q11</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11729mcpsimp"><a name="p11729mcpsimp"></a><a name="p11729mcpsimp"></a>Upper 21 unsigned bits for integer part, lower 11 bits for fractional part. Represented as UQ21.11 in the documentation.</p>
</td>
</tr>
<tr id="row11730mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11732mcpsimp"><a name="p11732mcpsimp"></a><a name="p11732mcpsimp"></a>td_u14q18</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11734mcpsimp"><a name="p11734mcpsimp"></a><a name="p11734mcpsimp"></a>Upper 14 unsigned bits for integer part, lower 18 bits for fractional part. Represented as UQ14.18 in the documentation.</p>
</td>
</tr>
<tr id="row11735mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11737mcpsimp"><a name="p11737mcpsimp"></a><a name="p11737mcpsimp"></a>td_u8q24</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11739mcpsimp"><a name="p11739mcpsimp"></a><a name="p11739mcpsimp"></a>Upper 8 unsigned bits for integer part, lower 24 bits for fractional part. Represented as UQ8.24 in the documentation.</p>
</td>
</tr>
<tr id="row11740mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11742mcpsimp"><a name="p11742mcpsimp"></a><a name="p11742mcpsimp"></a>td_u4q28</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11744mcpsimp"><a name="p11744mcpsimp"></a><a name="p11744mcpsimp"></a>Upper 4 unsigned bits for integer part, lower 28 bits for fractional part. Represented as UQ4.28 in the documentation.</p>
</td>
</tr<tr id="row11745mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11747mcpsimp"><a name="p11747mcpsimp"></a><a name="p11747mcpsimp"></a>td_s25q7</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11749mcpsimp"><a name="p11749mcpsimp"></a><a name="p11749mcpsimp"></a>Upper 25 signed bits for integer part, lower 7 bits for fractional part. Represented as SQ25.7 in the documentation.</p>
</td>
</tr>
<tr id="row11750mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11752mcpsimp"><a name="p11752mcpsimp"></a><a name="p11752mcpsimp"></a>td_s16q16</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11754mcpsimp"><a name="p11754mcpsimp"></a><a name="p11754mcpsimp"></a>Upper 16 signed bits for integer part, lower 16 bits for fractional part. Represented as SQ16.16 in the documentation.</p>
</td>
</tr>
<tr id="row11755mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11757mcpsimp"><a name="p11757mcpsimp"></a><a name="p11757mcpsimp"></a>td_s14q18</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11759mcpsimp"><a name="p11759mcpsimp"></a><a name="p11759mcpsimp"></a>Upper 14 signed bits for integer part, lower 18 bits for fractional part. Represented as SQ14.18 in the documentation.</p>
</td>
</tr>
<tr id="row11760mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11762mcpsimp"><a name="p11762mcpsimp"></a><a name="p11762mcpsimp"></a>td_s20q12</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11764mcpsimp"><a name="p11764mcpsimp"></a><a name="p11764mcpsimp"></a>Upper 20 signed bits for integer part, lower 12 bits for fractional part. Represented as SQ20.12 in the documentation.</p>
</td>
</tr>
<tr id="row11765mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11767mcpsimp"><a name="p11767mcpsimp"></a><a name="p11767mcpsimp"></a>td_s24q8</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11769mcpsimp"><a name="p11769mcpsimp"></a><a name="p11769mcpsimp"></a>Upper 24 signed bits for integer part, lower 8 bits for fractional part. Represented as SQ24.8 in the documentation.</p>
</td>
</tr>
<tr id="row11770mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p id="p11772mcpsimp"><a name="p11772mcpsimp"></a><a name="p11772mcpsimp"></a>td_u8q4f4</p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p11774mcpsimp"><a name="p11774mcpsimp"></a><a name="p11774mcpsimp"></a>Upper 8 unsigned bits for integer part, middle 4 bits for fractional part, lower 4 bits for flags. Represented as UQF8.4.4 in the documentation.</p>
</td>
</tr>
</tbody>
</table> 【Notes】 td\_uxqyfz\\td\_sxqy: - The number x after u indicates x unsigned bits for the integer part.
- The number x after s indicates x signed bits for the integer part.
- The number y after q indicates y bits for the fractional part.
- The number z after f indicates z bits for the flag bits.
- From left to right, high bits to low bits. 【Related Data Types and AP Is】 None. ### ot\_svp\_data<a name="ZH-CN_TOPIC_0000002470931244"></a> 【Description】 Defines 2D data information in bytes. 【Definition】 ```
typedef struct { td_u64 phys_addr; /* RW;The physical address of the data */ td_u64 virt_addr; /* RW;The virtaul address of the data */ td_u32 stride; /* RW;The stride of 2D data by byte */ td_u32 width; /* RW;The width of 2D data by byte */ td_u32 height; /* RW;The height of 2D data by byte */ td_u32 reserved;
} ot_svp_data;
``` 【Members】 <a name="table1382mcpsimp"></a>
<table><thead align="left"><tr id="row1387mcpsimp"><th class="cellrowborder" valign="top" width="31%" id="mcps1.1.3.1.1"><p id="p1389mcpsimp"><a name="p1389mcpsimp"></a><a name="p1389mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="69%" id="mcps1.1.3.1.2"><p id="p1391mcpsimp"><a name="p1391mcpsimp"></a><a name="p1391mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1393mcpsimp"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p xml:lang="da-DK" id="p1395mcpsimp"><a name="p1395mcpsimp"></a><a name="p1395mcpsimp"></a>phys_addr</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p1397mcpsimp"><a name="p1397mcpsimp"></a><a name="p1397mcpsimp"></a>Image physical address.</p>
</td>
</tr>
<tr id="row1398mcpsimp"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p xml:lang="da-DK" id="p1400mcpsimp"><a name="p1400mcpsimp"></a><a name="p1400mcpsimp"></a>virt_addr</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p1402mcpsimp"><a name="p1402mcpsimp"></a><a name="p1402mcpsimp"></a>Image virtual address.</p>
</td>
</tr>
<tr id="row1403mcpsimp"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p xml:lang="da-DK" id="p1405mcpsimp"><a name="p1405mcpsimp"></a><a name="p1405mcpsimp"></a>stride</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p1407mcpsimp"><a name="p1407mcpsimp"></a><a name="p1407mcpsimp"></a>Image stride.</p>
</td>
</tr>
<tr id="row1408mcpsimp"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p xml:lang="da-DK" id="p1410mcpsimp"><a name="p1410mcpsimp"></a><a name="p1410mcpsimp"></a>height</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p1412mcpsimp"><a name="p1412mcpsimp"></a><a name="p1412mcpsimp"></a>Image height.</p>
</td>
</tr>
<tr id="row1413mcpsimp"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p xml:lang="da-DK" id="p1415mcpsimp"><a name="p1415mcpsimp"></a><a name="p1415mcpsimp"></a>width</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p1417mcpsimp"><a name="p1417mcpsimp"></a><a name="p1417mcpsimp"></a>Image width.</p>
</td>
</tr>
<tr id="row1418mcpsimp"><td class="cellrowborder" valign="top" width="31%" headers="mcps1.1.3.1.1 "><p id="p1420mcpsimp"><a name="p1420mcpsimp"></a><a name="p1420mcpsimp"></a>reserved</p>
</td>
<td class="cellrowborder" valign="top" width="69%" headers="mcps1.1.3.1.2 "><p id="p1422mcpsimp"><a name="p1422mcpsimp"></a><a name="p1422mcpsimp"></a>Reserved bit.</p>
</td>
</tr>
</tbody>
</table> 【Notes】 Represents 2D data in bytes; can be converted to/from [ot\_svp\_img](#ZH-CN_TOPIC_0000002504091103). 【Related Data Types and AP Is】 None. ### ot\_svp\_src\_data<a name="ZH-CN_TOPIC_0000002503971213"></a> 【Description】 Defines 2D source data information in bytes. 【Definition】 ```
typedef ot_svp_data ot_svp_src_data;
``` 【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 - [ot\_svp\_img](#ot_svp_img)
- [ot\_svp\_dst\_data](#ot_svp_dst_data) ### ot\_svp\_dst\_data<a name="ZH-CN_TOPIC_0000002470931290"></a> 【Description】 Defines 2D output data information in bytes. 【Definition】 ```
typedef ot_svp_data ot_svp_dst_data;
``` 【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 - [ot\_svp\_img](#ot_svp_img)
- [ot\_svp\_src\_img](#ot_svp_src_img) ### ot\_svp\_8bit<a name="ZH-CN_TOPIC_0000002503971231"></a> 【Description】 Defines an 8-bit data union. 【Definition】 ```
typedef union { td_s8 s8_val; td_u8 u8_val;
} ot_svp_8bit;
``` 【Members】 【Notes】 None 【Related Data Types and AP Is】 None ### ot\_svp\_point\_u16<a name="ZH-CN_TOPIC_0000002503971259"></a> 【Description】 Defines a point information structure represented by u16. 【Definition】 ```
typedef struct { td_u16 x; /* RW;The X coordinate of the point */ td_u16 y; /* RW;The Y coordinate of the point */
} ot_svp_point_u16;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>x</td><td>X coordinate of the point.</td></tr>
<tr><td>y</td><td>Y coordinate of the point.</td></tr>
</tbody></table> 【Notes】 None 【Related Data Types and AP Is】 None ### ot\_svp\_point\_s16<a name="ZH-CN_TOPIC_0000002504091193"></a> 【Description】 Defines a point information structure represented by s16. 【Definition】 ```
typedef struct { td_s16 x; /* RW;The X coordinate of the point */ td_s16 y; /* RW;The Y coordinate of the point */
} ot_svp_point_s16;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>x</td><td>X coordinate of the point.</td></tr>
<tr><td>y</td><td>Y coordinate of the point.</td></tr>
</tbody></table> 【Notes】 None 【Related Data Types and AP Is】 None ### ot\_svp\_point\_s25q7<a name="ZH-CN_TOPIC_0000002503971257"></a> 【Description】 Defines a point information structure represented by s25q7. 【Definition】 ```
typedef struct { td_s25q7 x; /* RW;The X coordinate of the point */ td_s25q7 y; /* RW;The Y coordinate of the point */
} ot_svp_point_s25q7;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>x</td><td>X coordinate of the point, expressed in SQ25.7.</td></tr>
<tr><td>y</td><td>Y coordinate of the point, expressed in SQ25.7.</td></tr>
</tbody></table> 【Notes】 None 【Related Data Types and AP Is】 None ### ot\_svp\_point\_u14q2<a name="ZH-CN_TOPIC_0000002504091195"></a> 【Description】 Defines a point information structure represented by u14q2. 【Definition】 ```
typedef struct { td_u14q2 x; td_u14q2 y;
} ot_svp_point_u14q2;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>x</td><td>X coordinate of the point.</td></tr>
<tr><td>y</td><td>Y coordinate of the point.</td></tr>
</tbody></table> 【Notes】 None 【Related Data Types and AP Is】 None ### ot\_svp\_rect\_u32<a name="ZH-CN_TOPIC_0000002470931266"></a> 【Description】 Defines a rectangle information structure represented by u32. 【Definition】 ```
typedef struct { td_u32 x; /* RW;The location of X axis of the rectangle */ td_u32 y; /* RW;The location of Y axis of the rectangle */ td_u32 width; /* RW;The width of the rectangle */ td_u32 height; /* RW;The height of the rectangle */
} ot_svp_rect_u32;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>x</td><td>X coordinate of the point of the rectangle closest to the origin.</td></tr>
<tr><td>y</td><td>Y coordinate of the point of the rectangle closest to the origin.</td></tr>
<tr><td>width</td><td>Width of the rectangle.</td></tr>
<tr><td>height</td><td>Height of the rectangle.</td></tr>
</tbody></table> 【Notes】 None 【Related Data Types and Structures】 None ### ot\_svp\_rect\_u16<a name="ZH-CN_TOPIC_0000002470931214"></a> 【Description】 Defines a rectangle information structure represented by u16. 【Definition】 ```
typedef struct { td_u16 x; /* RW;The location of X axis of the rectangle */ td_u16 y; /* RW;The location of Y axis of the rectangle */ td_u16 width; /* RW;The width of the rectangle */ td_u16 height; /* RW;The height of the rectangle */
} ot_svp_rect_u16;
``` 【Members】 【Notes】 None 【Related Data Types and Structures】 None ### ot\_svp\_rect\_s24q8<a name="ZH-CN_TOPIC_0000002503971197"></a> 【Description】 Defines a rectangle information structure represented by s24q8. 【Definition】 ```
typedef struct { td_s24q8 x; td_s24q8 y; td_u32 width; td_u32 height;
} ot_svp_rect_s24q8;
``` 【Members】 【Notes】 None 【Related Data Types and Structures】 None ### ot\_svp\_lut<a name="ZH-CN_TOPIC_0000002503971221"></a> 【Description】 Defines a lookup table structure. 【Definition】 ```
typedef struct { ot_svp_mem_info table; td_u16 elem_num; /* RW;LUT's elements number */ td_u8 table_in_precision; td_u8 table_out_norm; td_s32 table_in_lower; /* RW;LUT's original input lower limit */ td_s32 table_in_upper; /* RW;LUT's original input upper limit */
} ot_svp_lut;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>table</td><td>Data memory block information after the lookup table is established.</td></tr>
<tr><td>elem_num</td><td>Number of elements in the lookup table.</td></tr>
<tr><td>table_in_precision</td><td>Lower limit of the value range for establishing the lookup table.</td></tr>
<tr><td>table_out_norm</td><td>Upper limit of the value range for establishing the lookup table.</td></tr>
<tr><td>table_in_lower</td><td>Precision for establishing the lookup table. (table_in_upper - table_in_lower)/(1&lt;&lt; table_in_precision) indicates the interval for establishing the lookup table.</td></tr>
<tr><td>table_in_upper</td><td>Number of bits to shift or divisor to use when normalizing the original data for establishing the lookup table.</td></tr>
</tbody></table> 【Notes】 None 【Related Data Types and Structures】 None ## IVE-Related Data Types and Data Structures<a name="ZH-CN_TOPIC_0000002503971225"></a> ### ot\_ive\_handle<a name="ZH-CN_TOPIC_0000002471091250"></a> 【Description】 Defines the IVE handle. 【Definition】 ```
typedef td_s32 ot_ive_handle;
``` 【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 None. ### OT\_IVE\_HIST\_NUM<a name="ZH-CN_TOPIC_0000002470931262"></a> 【Description】 Defines the number of histogram bins. 【Definition】 ```
#define OT_IVE_HIST_NUM 256
``` 【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 None. ### OT\_IVE\_MAP\_NUM<a name="ZH-CN_TOPIC_0000002471091274"></a> 【Description】 Defines the number of mapping lookup table entries. 【Definition】 ```
#define OT_IVE_MAP_NUM 256
``` 【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 None. ### OT\_IVE\_MAX\_RGN\_NUM<a name="ZH-CN_TOPIC_0000002471091214"></a> 【Description】 Defines the maximum number of connected regions. 【Definition】 ```
#define OT_IVE_MAX_RGN_NUM 254
``` 【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 None. ### OT\_IVE\_ST\_MAX\_CORNER\_NUM<a name="ZH-CN_TOPIC_0000002503971193"></a> 【Description】 Defines the maximum number of Shi-Tomasi-like corners. 【Definition】 ```
#define OT_IVE_ST_MAX_CORNER_NUM 500
``` 【Members】 None. 【Notes】 None. 【Related Data Types and AP Is】 None. ### OT\_IVE\_MASK\_NUM<a name="ZH-CN_TOPIC_0000002471091310"></a> 【Description】 Length of the mask array. 【Definition】 ```
#define OT_IVE_MASK_NUM 25
``` 【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_ARR\_RESERVED\_NUM\_TWO<a name="ZH-CN_TOPIC_0000002503971159"></a> 【Description】 Reserved field array length 2. 【Definition】 ```
#define OT_IVE_ARR_RESERVED_NUM_TWO 2
``` 【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_ARR\_RESERVED\_NUM\_THREE<a name="ZH-CN_TOPIC_0000002504091161"></a> 【Description】 Reserved field array length 3. 【Definition】 ```
#define OT_IVE_ARR_RESERVED_NUM_THREE 3
``` 【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_ARR\_RESERVED\_NUM\_EIGHT<a name="ZH-CN_TOPIC_0000002470931298"></a> 【Description】 Reserved field array length 8. 【Definition】 ```
#define OT_IVE_ARR_RESERVED_NUM_EIGHT 8
``` 【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_ARR\_RESERVED\_NUM\_TWELVE<a name="ZH-CN_TOPIC_0000002470931230"></a> 【Description】 Reserved field array length 12. 【Definition】 ```
#define OT_IVE_ARR_RESERVED_NUM_TWELVE 12
``` 【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_ARR\_RESERVED\_NUM\_FOURTEEN<a name="ZH-CN_TOPIC_0000002470931216"></a> 【Description】 Reserved field array length 14. 【Definition】 ```
#define OT_IVE_ARR_RESERVED_NUM_FOURTEEN 14
``` 【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_ARR\_NUM\_THREE<a name="ZH-CN_TOPIC_0000002503971175"></a> 【Description】 Array length 3. 【Definition】 ```
#define OT_IVE_ARR_NUM_THREE 3
``` 【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_ARR\_NUM\_EIGHT<a name="ZH-CN_TOPIC_0000002503971255"></a> 【Description】 Array length 8. 【Definition】 ```
#define OT_IVE_ARR_NUM_EIGHT 8
``` 【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_DEV\_NAME\_LENGTH<a name="ZH-CN_TOPIC_0000002503971217"></a> 【Description】 IVE device name length. 【Definition】 ```
#define OT_IVE_DEV_NAME_LENGTH 10
``` 【Members】 None 【Related Data Types and AP Is】 None ### OT\_IVE\_DEV\_DEFAULT\_NODE\_NUM<a name="ZH-CN_TOPIC_0000002504091127"></a> 【Description】 Default number of IVE nodes. 【Definition】 ```
#define OT_IVE_DEFAULT_NODE_NUM 512
``` 【Members】 None 【Related Data Types and AP Is】 None ### ot\_ive\_mod\_param<a name="ZH-CN_TOPIC_0000002504091147"></a> 【Description】 IVE module related parameter definition. 【Definition】 ```
typedef struct { td_u16 mod_node_num; td_u8 power_save_en;
} ot_ive_mod_param;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>mod_node_num</td><td>Number of IVE nodes, range [20, 512].</td></tr>
<tr><td>power_save_en</td><td>Low power flag, range [0, 1].</td></tr>
</tbody></table> 【Notes】 None. 【Related Data Types and AP Is】 ive\_std\_mod\_init ### ot\_ive\_err\_code<a name="ZH-CN_TOPIC_0000002504091141"></a> 【Description】 Defines error codes. 【Definition】 ```
typedef enum { OT_IVE_ERR_SYS_TIMEOUT = 0x40, /* IVE process timeout */ OT_IVE_ERR_QUERY_TIMEOUT = 0x41, /* IVE query timeout */ OT_IVE_ERR_BUS_ERR = 0x42, /* IVE BUS error */ OT_IVE_ERR_OPEN_FILE = 0x43, /* IVE open file error */ OT_IVE_ERR_READ_FILE = 0x44, /* IVE read file error */ OT_IVE_ERR_BUTT
} ot_ive_err_code;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>OT_IVE_ERR_SYS_TIMEOUT</td><td>System timeout.</td></tr>
<tr><td>OT_IVE_ERR_QUERY_TIMEOUT</td><td>Query timeout.</td></tr>
<tr><td>OT_IVE_ERR_BUS_ERR</td><td>Bus error.</td></tr>
<tr><td>OT_IVE_ERR_OPEN_FILE</td><td>Failed to open file.</td></tr>
<tr><td>OT_IVE_ERR_READ_FILE</td><td>Failed to read file.</td></tr>
</tbody></table> 【Notes】 None. 【Related Data Types and AP Is】 None. ### ot\_ive\_dma\_mode<a name="ZH-CN_TOPIC_0000002470931310"></a> 【Description】 Defines DMA operation mode. 【Definition】 ```
typedef enum { OT_IVE_DMA_MODE_DIRECT_COPY = 0x0, OT_IVE_DMA_MODE_INTERVAL_COPY = 0x1, OT_IVE_DMA_MODE_SET_3BYTE = 0x2, OT_IVE_DMA_MODE_SET_8BYTE = 0x3, OT_IVE_DMA_MODE_BUTT
} ot_ive_dma_mode;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>OT_IVE_DMA_MODE_DIRECT_COPY</td><td>Direct fast copy mode.</td></tr>
<tr><td>OT_IVE_DMA_MODE_INTERVAL_COPY</td><td>Interval copy mode. See the ss_mpi_ive_dma [Notes].</td></tr>
<tr><td>OT_IVE_DMA_MODE_SET_3BYTE</td><td>3-byte set mode. See the ss_mpi_ive_dma [Notes].</td></tr>
<tr><td>OT_IVE_DMA_MODE_SET_8BYTE</td><td>8-byte set mode. See the ss_mpi_ive_dma [Notes].</td></tr>
</tbody></table> 【Notes】 None. 【Related Data Types and AP Is】 [ot\_ive\_dma\_ctrl](#ot_ive_dma_ctrl) ### ot\_ive\_dma\_ctrl<a name="ZH-CN_TOPIC_0000002504091157"></a> 【Description】 Defines DMA control information. 【Definition】 ```
typedef struct { ot_ive_dma_mode mode; td_u64 val; td_u8 hor_seg_size; td_u8 elem_size; td_u8 ver_seg_rows;
} ot_ive_dma_ctrl
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>mode</td><td>DMA operation mode.</td></tr>
<tr><td>val</td><td>Used only in set mode for memory assignment. 3-byte set mode stores in the lower 3 bytes.</td></tr>
<tr><td>hor_seg_size</td><td>Used only in interval copy mode. The segment size for splitting a row of the source image horizontally. Value range: {2, 3, 4, 8, 16}.</td></tr>
<tr><td>elem_size</td><td>Used only in interval copy mode. The first elem_size bytes of each segment are valid copy fields. Value range: [1, hor_seg_size-1].</td></tr>
<tr><td>ver_seg_rows</td><td>Used only in interval copy mode. Divides the first row of data in every ver_seg_rows into segments of hor_seg_size, copying the first elem_size bytes of each segment. Value range: [1, min{65535/src_stride, src_height}].</td></tr>
</tbody></table> 【Notes】 None. 【Related Data Types and AP Is】 [ot\_ive\_dma\_mode](#ot_ive_dma_mode) ### ot\_ive\_filter\_ctrl<a name="ZH-CN_TOPIC_0000002503971267"></a> 【Description】 Defines template filter control information. 【Definition】 ```
typedef struct { td_s8 mask[OT_IVE_MASK_NUM]; /* Template parameter filter coefficient */ td_u8 norm; /* Normalization parameter, by right shift */
} ot_ive_filter_ctrl
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>mask[OT_IVE_MASK_NUM]</td><td>5x5 template coefficients. Setting peripheral coefficients to 0 implements 3x3 template filtering.</td></tr>
<tr><td>norm</td><td>Normalization parameter. Value range: [0, 13].</td></tr>
</tbody></table> 【Notes】 Different filtering effects can be achieved by configuring different template coefficients. 【Related Data Types and AP Is】 None. ### ot\_ive\_csc\_mode<a name="ZH-CN_TOPIC_0000002470931222"></a> 【Description】 Defines color space conversion mode. 【Definition】 ```
typedef enum { OT_IVE_CSC_MODE_VIDEO_BT601_YUV_TO_RGB = 0x0, /* CSC: YUV_TO_RGB, video transfer mode, RGB value range [16, 235] */ OT_IVE_CSC_MODE_VIDEO_BT709_YUV_TO_RGB = 0x1, /* CSC: YUV_To_RGB, video transfer mode, RGB value range [16, 235] */ OT_IVE_CSC_MODE_PIC_BT601_YUV_TO_RGB = 0x2, /* CSC: YUV_TO_RGB, picture transfer mode, RGB value range [0, 255] */ OT_IVE_CSC_MODE_PIC_BT709_YUV_TO_RGB = 0x3, /* CSC: YUV_TO_RGB, picture transfer mode, RGB value range [0, 255] */ OT_IVE_CSC_MODE_PIC_BT601_YUV_TO_HSV = 0x4, /* CSC: YUV_TO_HSV, picture transfer mode, HSV value range [0, 255] */ OT_IVE_CSC_MODE_PIC_BT709_YUV_TO_HSV = 0x5, /* CSC: YUV_TO_HSV, picture transfer mode, HSV value range [0, 255] */ OT_IVE_CSC_MODE_PIC_BT601_YUV_TO_LAB = 0x6, /* CSC: YUV_TO_LAB, picture transfer mode, Lab value range [0, 255] */ OT_IVE_CSC_MODE_PIC_BT709_YUV_TO_LAB = 0x7, /* CSC: YUV_TO_LAB, picture transfer mode, Lab value range [0, 255] */ OT_IVE_CSC_MODE_VIDEO_BT601_RGB_TO_YUV = 0x8, /* CSC: RGB_TO_YUV, video transfer mode, YUV value range [0, 255] */ OT_IVE_CSC_MODE_VIDEO_BT709_RGB_TO_2YUV = 0x9, /* CSC: RGB_TO_YUV, video transfer mode, YUV value range [0, 255] */ OT_IVE_CSC_MODE_PIC_BT601_RGB_TO_YUV = 0xa, /* CSC: RGB_TO_YUV, picture transfer mode, Y:[16, 235],U\V:[16, 240] */ OT_IVE_CSC_MODE_PIC_BT709_RGB_TO_YUV = 0xb, /* CSC: RGB_TO_YUV, picture transfer mode, Y:[16, 235],U\V:[16, 240] */ OT_IVE_CSC_MODE_BUTT
} ot_ive_csc_mode
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>OT_IVE_CSC_MODE_VIDEO_BT601_YUV_TO_RGB</td><td>BT601 YUV_TO_RGB video conversion.</td></tr>
<tr><td>OT_IVE_CSC_MODE_VIDEO_BT709_YUV_TO_RGB</td><td>BT709 YUV_TO_RGB video conversion.</td></tr>
<tr><td>OT_IVE_CSC_MODE_PIC_BT601_YUV_TO_RGB</td><td>BT601 YUV_TO_RGB picture conversion.</td></tr>
<tr><td>OT_IVE_CSC_MODE_PIC_BT709_YUV_TO_RGB</td><td>BT709 YUV_TO_RGB picture conversion.</td></tr>
<tr><td>OT_IVE_CSC_MODE_PIC_BT601_YUV_TO_HSV</td><td>BT601 YUV_TO_HSV picture conversion.</td></tr>
<tr><td>OT_IVE_CSC_MODE_PIC_BT709_YUV_TO_HSV</td><td>BT709 YUV_TO_HSV picture conversion.</td></tr>
<tr><td>OT_IVE_CSC_MODE_PIC_BT601_YUV_TO_LAB</td><td>BT601 YUV_TO_LAB picture conversion.</td></tr>
<tr><td>OT_IVE_CSC_MODE_PIC_BT709_YUV_TO_LAB</td><td>BT709 YUV_TO_LAB picture conversion.</td></tr>
<tr><td>OT_IVE_CSC_MODE_VIDEO_BT601_RGB_TO_YUV</td><td>BT601 RGB_TO_YUV video conversion.</td></tr>
<tr><td>OT_IVE_CSC_MODE_VIDEO_BT709_RGB_TO_YUV</td><td>BT709 RGB_TO_YUV video conversion.</td></tr>
<tr><td>OT_IVE_CSC_MODE_PIC_BT601_RGB_TO_YUV</td><td>BT601 RGB_TO_YUV picture conversion.</td></tr>
<tr><td>OT_IVE_CSC_MODE_PIC_BT709_RGB_TO_YUV</td><td>BT709 RGB_TO_YUV picture conversion.</td></tr>
</tbody></table> 【Notes】 - OT\_IVE\_CSC\_MODE\_VIDEO\_BT601\_YUV\_TO\_RGB and OT\_IVE\_CSC\_MODE\_VIDEO\_BT709\_YUV\_TO\_RGB modes: output satisfies 16 <= R, G, B <= 235.
- OT\_IVE\_CSC\_MODE\_PIC\_BT601\_YUV\_TO\_RGB and OT\_IVE\_CSC\_MODE\_PIC\_BT709\_YUV\_TO\_RGB modes: output satisfies 0 <= R, G, B <= 255.
- OT\_IVE\_CSC\_MODE\_PIC\_BT601\_YUV\_TO\_HSV and OT\_IVE\_CSC\_MODE\_PIC\_BT709\_YUV\_TO\_HSV modes: output satisfies 0 <= H, S, V <= 255.
- OT\_IVE\_CSC\_MODE\_PIC\_BT601\_YUV\_TO\_LAB and OT\_IVE\_CSC\_MODE\_PIC\_BT709\_YUV\_TO\_LAB modes: output satisfies 0 <= L, A, B <= 255.
- OT\_IVE\_CSC\_MODE\_VIDEO\_BT601\_RGB\_TO\_YUV and OT\_IVE\_CSC\_MODE\_VIDEO\_BT709\_RGB\_TO\_YUV modes: output satisfies 0 <= Y, U, V <= 255.
- OT\_IVE\_CSC\_MODE\_PIC\_BT601\_RGB\_TO\_YUV and OT\_IVE\_CSC\_MODE\_PIC\_BT709\_RGB\_TO\_YUV modes: output satisfies Y [16, 235], U/V [16, 240]. 【Related Data Types and AP Is】 - [ot\_ive\_csc\_ctrl](#ot_ive_csc_ctrl)
- [ot\_ive\_filter\_and\_csc\_ctrl](#ot_ive_filter_and_csc_ctrl) ### ot\_ive\_csc\_ctrl<a name="ZH-CN_TOPIC_0000002504091137"></a> 【Description】 Defines color space conversion control information. 【Definition】 ```
typedef struct { ot_ive_csc_mode mode; /* Working mode */
} ot_ive_csc_ctrl
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>mode</td><td>Working mode.</td></tr>
</tbody></table> 【Notes】 None. 【Related Data Types and AP Is】 [ot\_ive\_csc\_mode](#ot_ive_csc_mode) ### ot\_ive\_filter\_and\_csc\_ctrl<a name="ZH-CN_TOPIC_0000002471091222"></a> 【Description】 Defines composite template filter plus color space conversion control information. 【Definition】 ```
typedef struct { ot_ive_csc_mode mode; /* CSC working mode */ td_s8 mask[OT_IVE_MASK_NUM]; /* Template parameter filter coefficient */ td_u8 norm; /* Normalization parameter, by right shift */
} ot_ive_filter_and_csc_ctrl ;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>mode</td><td>Working mode.</td></tr>
<tr><td>mask[OT_IVE_MASK_NUM]</td><td>5x5 template coefficients.</td></tr>
<tr><td>norm</td><td>Normalization parameter. Value range: [0, 13].</td></tr>
</tbody></table> 【Notes】 Only supports 4 modes of YUV2RGB. 【Related Data Types and AP Is】 [ot\_ive\_csc\_mode](#ot_ive_csc_mode) ### ot\_ive\_sobel\_out\_ctrl<a name="ZH-CN_TOPIC_0000002503971149"></a> 【Description】 Defines sobel output control information. 【Definition】 ```
typedef enum { OT_IVE_SOBEL_OUT_CTRL_BOTH = 0x0, /* Output horizontal and vertical */ OT_IVE_SOBEL_OUT_CTRL_HOR = 0x1, /* Output horizontal */ OT_IVE_SOBEL_OUT_CTRL_VER = 0x2, /* Output vertical */ OT_IVE_SOBEL_OUT_CTRL_BUTT
} ot_ive_sobel_out_ctrl;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>OT_IVE_SOBEL_OUT_CTRL_BOTH</td><td>Output filtering results using both the template and transposed template simultaneously.</td></tr>
<tr><td>OT_IVE_SOBEL_OUT_CTRL_HOR</td><td>Output only the result of direct template filtering.</td></tr>
<tr><td>OT_IVE_SOBEL_OUT_CTRL_VER</td><td>Output only the result of transposed template filtering.</td></tr>
</tbody></table> 【Notes】 None. 【Related Data Types and AP Is】 [ot\_ive\_sobel\_ctrl](#ot_ive_sobel_ctrl) ### ot\_ive\_sobel\_ctrl<a name="ZH-CN_TOPIC_0000002470931226"></a> 【Description】 Defines sobel-like gradient calculation control information. 【Definition】 ```
typedef struct { ot_ive_sobel_out_ctrl out_ctrl; /* Output format */ td_s8 mask[OT_IVE_MASK_NUM]; /* Template parameter */
} ot_ive_sobel_ctrl;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>out_ctrl</td><td>Output control enumeration parameter.</td></tr>
<tr><td>mask[OT_IVE_MASK_NUM]</td><td>5x5 template coefficients.</td></tr>
</tbody></table> 【Notes】 None. 【Related Data Types and AP Is】 [ot\_ive\_sobel\_out\_ctrl](#ot_ive_sobel_out_ctrl) ### ot\_ive\_mag\_and\_ang\_out\_ctrl<a name="ZH-CN_TOPIC_0000002471091234"></a> 【Description】 Defines the output format for gradient magnitude and angle calculation. 【Definition】 ```
typedef enum { OT_IVE_MAG_AND_ANG_OUT_CTRL_MAG = 0x0,/* Only the magnitude is output.*/ OT_IVE_MAG_AND_ANG_OUT_CTRL_MAG_AND_ANG = 0x1, /* The magnitude and angle are output.*/ OT_IVE_MAG_AND_ANG_OUT_CTRL_BUTT
} ot_ive_mag_and_ang_out_ctrl;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>OT_IVE_MAG_AND_ANG_OUT_CTRL_MAG</td><td>Output magnitude only.</td></tr>
<tr><td>OT_IVE_MAG_AND_ANG_OUT_CTRL_MAG_AND_ANG</td><td>Output both magnitude and angle.</td></tr>
</tbody></table> 【Notes】 None. 【Related Data Types and AP Is】 [ot\_ive\_mag\_and\_ang\_ctrl](#ot_ive_mag_and_ang_ctrl) ### ot\_ive\_mag\_and\_ang\_ctrl<a name="ZH-CN_TOPIC_0000002470931264"></a> 【Description】 Defines control information for gradient magnitude and angle calculation. 【Definition】 ```
typedef struct { ot_ive_mag_and_ang_out_ctrl out_ctrl; td_u16 threshld; td_s8 mask[OT_IVE_MASK_NUM]; /* Template parameter. */
} ot_ive_mag_and_ang_ctrl;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>out_ctrl</td><td>Output format.</td></tr>
<tr><td>threshold</td><td>Threshold for thresholding the magnitude.</td></tr>
<tr><td>mask[OT_IVE_MASK_NUM]</td><td>5x5 template coefficients.</td></tr>
</tbody></table> 【Notes】 None. 【Related Data Types and AP Is】 [ot\_ive\_mag\_and\_ang\_out\_ctrl](#ot_ive_mag_and_ang_out_ctrl) ### ot\_ive\_dilate\_ctrl<a name="ZH-CN_TOPIC_0000002504091109"></a> 【Description】 Defines dilation control information. 【Definition】 ```
typedef struct { td_u8 mask[OT_IVE_MASK_NUM]; /* The template parameter value must be 0 or 255. */
} ot_ive_dilate_ctrl;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>mask[OT_IVE_MASK_NUM]</td><td>5x5 template coefficients. Value range: 0 or 255.</td></tr>
</tbody></table> 【Notes】 None. 【Related Data Types and AP Is】 None. ### ot\_ive\_erode\_ctrl<a name="ZH-CN_TOPIC_0000002470931312"></a> 【Description】 Defines erosion control information. 【Definition】 ```
typedef struct { td_u8 mask[OT_IVE_MASK_NUM]; /* The template parameter value must be 0 or 255. */
} ot_ive_erode_ctrl;
``` 【Members】 <table><thead align="left"><tr><th>Member Name</th><th>Description</th></tr></thead>
<tbody><tr><td>mask[OT_IVE_MASK_NUM]</td><td>5x5 template coefficients. Value: 0 or 255.</td></tr>
</tbody></table> 【Notes】 None. 【Related Data Types and AP Is】 None. ### ot\_ive\_threshold\_mode<a name="ZH-CN_TOPIC_0000002504091197"></a> 【Description】 Defines image binarization output format. 【Definition】 ```
typedef enum { OT_IVE_THRESHOLD_MODE_BINARY = 0x0, /* src_val <= low_thr, dst_val = min_val; src_val > low_threshold, dst_val = max_val. */ OT_IVE_THRESHOLD_MODE_TRUNC = 0x1, /* src_val <= low_threshold, dst_val = src_val; src_val > low_threshold, dst_val = max_val. */ OT_IVE_THRESHOLD_MODE_TO_MIN_VAL = 0x2, /* src_val <= low_threshold, dst_val = min_val; src_val > low_threshold, dst_val = src_val. */ OT_IVE_THRESHOLD_MODE_MIN_MID_MAX = 0x3, /* src_val <= low_threshold, dst_val = min_val; low_threshold < src_val <= high_threshold, dst_val = mid_val; src_val > high_threshold, dst_val = max_val. */ OT_IVE_THRESHOLD_MODE_ORIG_MID_MAX = 0x4, /* src_val <= low_threshold, dst_val = src_val; low_threshold < src_val <= high_threshold, dst_val = mid_val; src_val > high_threshold, dst_val = max_val. */ OT_IVE_THRESHOLD_MODE_MIN_MID_ORI = 0x5, /* src_val <= low_threshold, dst_val = min_val; low_threshold < src_val <= high_threshold, dst_val = mid_val; src_val > high_threshold, dst_val = src_val. */ OT_IVE_THRESHOLD_MODE_MIN_ORIG_MAX = 0x6, /* src_val <= low_threshold, dst_val = min_val; low_threshold < src_val <= high_threshold, dst_val = src_val; src_val > high_threshold, dst_val = max_val. */ OT_IVE_THRESHOLD_MODE_ORI_MID_ORIG = 0x7, /* src_val <= low_threshold, dst_val = src_val; low_threshold < src_val <= high_threshold, dst_val = mid_val; src_val > high_threshold, dst_val = src_val. */ OT_IVE_THRESHOLD_MODE_BUTT
} ot_ive_threshold_mode;
``` 【Members】 【Notes】 For calculation formulas, see [Notes] in ss\_mpi\_ive\_threshold. For diagrams, see the 8 thresholding mode diagram. 【Related Data Types and AP Is】 [ot\_ive\_threshold\_ctrl](#ot_ive_threshold_ctrl) ### ot\_ive\_threshold\_ctrl<a name="ZH-CN_TOPIC_0000002504091163"></a> 【Description】 Defines image binarization control information. 【Definition】 ```
typedef struct { ot_ive_threshold_mode mode; td_u8 low_threshold; /* user-defined threshold, 0<=u8Low Thr<=255 */ td_u8 high_threshold; /* user-defined threshold, if mode<OT_IVE_THRESHOLD_MODE_MIN_MID_MAX, high_threshold is not used, else 0<=low_threshold<= high_threshold <=255; */
```
