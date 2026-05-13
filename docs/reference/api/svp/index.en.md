---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/SVP API参考/SVP API参考.md
--- # Preface
**Overview<a name="section102mcpsimp"></a>** This document mainly introduces the SVP (Smart Vision Platform) API, data types, and Proc debug information. The SVP platform includes the MAU (Matrix Arithmetic Unit), DPU_RECT, DPU_MATCH, and DSP modules. >![](public_sys-resources/icon-note.gif) **Note:**
>- This document uses Hi3403V100 as an example. Unless otherwise specified, is consistent with Hi3403V100.
>- Some modules (like DSP) may not be available on all platform variants. **Product Version** The product version corresponding to this document is as follows. | Product Name | Product Version |
|---|---|
| Hi3403V100 | V100 |
| | V100 | **Target Audience** - Technical Support Engineers
- Software Development Engineers **Symbol Conventions (see original document for icon images)** **Revision History** | Document Version | Release Date | Revision Description |
|---|---|---|
| 00B01 | 2025-09-15 | First interim release. | # MAU
## Overview<a name="ZH-CN_TOPIC_0000002441853521"></a> The MAU (Matrix Arithmetic Unit) is a hardware accelerator for matrix and vector operations. It supports operations such as matrix multiplication, distance computation (cosine, Euclidean, Manhattan), transposition, vector operations, type conversion, sorting, and FIR filtering. ## Functional Description<a name="ZH-CN_TOPIC_0000002408294284"></a> ### Important Concepts<a name="ZH-CN_TOPIC_0000002441733669"></a> **Blob**: A multi-dimensional array representing data for MAU operations. Each blob has the following attributes:
- **data\_type**: Element data type (OT\_SVP\_BLOB\_TYPE\_S32, OT\_SVP\_BLOB\_TYPE\_U8, OT\_SVP\_BLOB\_TYPE\_F32, etc.)
- **dimension**: Number of dimensions (1D vector, 2D matrix, etc.)
- **shape**: Size of each dimension
- **stride**: Stride of each dimension in bytes **Memory Management**: MAU operations require pre-allocated memory for input/output blobs. Memory can be MMZ or OS memory. **Synchronous/Asynchronous**: MAU operations can be synchronous (blocking) or asynchronous (non-blocking). For asynchronous operations, use ss\_mpi\_svp\_mau\_query to check completion. ### Usage Flow<a name="ZH-CN_TOPIC_0000002408294128"></a> 1. Create source and destination blobs (ot\_svp\_src\_blob, ot\_svp\_dst\_blob).
2. Allocate memory for blobs.
3. Call the appropriate MAU operation function.
4. For async operations, call ss\_mpi\_svp\_mau\_query to wait for completion.
5. Retrieve results from destination blob. ## API Reference<a name="ZH-CN_TOPIC_0000002408294120"></a> ### ss\_mpi\_svp\_mau\_matrix\_mul<a name="ZH-CN_TOPIC_0000002441853557"></a> [Purpose]
Perform matrix multiplication on two input matrices. [Syntax]
```c
#include "ss_svp_mau.h"
td_s32 ss_mpi_svp_mau_matrix_mul(ot_svp_mau_handle *handle, const ot_svp_src_blob src[2], const ot_svp_dst_blob dst[1], const ot_svp_mau_ctrl *ctrl, td_bool sync);
``` [Parameters]
- handle: Pointer to the operation handle (output).
- src[2]: Array of 2 source blobs (matrix A and matrix B).
- dst[1]: Array of 1 destination blob (result matrix C).
- ctrl: Control parameters including transpose flags.
- sync: Synchronous (TD_TRUE) or asynchronous (TD_FALSE). [Description]
Computes C = A * B. Supports optional transposition of A and/or B before multiplication. [Return Value]
Returns 0 on success, non-zero error code on failure. ### ss\_mpi\_svp\_mau\_cos\_dist<a name="ZH-CN_TOPIC_0000002408294444"></a> [Purpose]
Compute cosine distance between vectors. [Syntax]
```c
td_s32 ss_mpi_svp_mau_cos_dist(ot_svp_mau_handle *handle, const ot_svp_src_blob src[2], const ot_svp_dst_blob dst[1], const ot_svp_mau_ctrl *ctrl, td_bool sync);
``` [Description]
Computes the cosine distance (cosine similarity) between feature vectors. The source blobs contain the vector sets, and the output is a distance matrix. ### ss\_mpi\_svp\_mau\_euclid\_dist<a name="ZH-CN_TOPIC_0000002408294448"></a> [Purpose]
Compute Euclidean distance between vectors. [Description]
Computes the Euclidean (L2) distance between two sets of feature vectors. Output is a distance matrix. ### ss\_mpi\_svp\_mau\_manhattan\_dist<a name="ZH-CN_TOPIC_0000002408294148"></a> [Purpose]
Compute Manhattan distance (L1 norm) between vectors. ### ss\_mpi\_svp\_mau\_transpose<a name="ZH-CN_TOPIC_0000002441853525"></a> [Purpose]
Transpose a matrix. [Description]
Performs matrix transposition. Supports 2D and 3D blob transposition. ### ss\_mpi\_svp\_mau\_vector\_op<a name="ZH-CN_TOPIC_0000002408294432"></a> [Purpose]
Perform element-wise vector operations (add, subtract, multiply, divide, etc.). [Description]
Supports operations such as addition, subtraction, multiplication, division, and various comparison operations between two vectors or between a vector and a scalar. ### ss\_mpi\_svp\_mau\_type\_convert<a name="ZH-CN_TOPIC_0000002408294172"></a> [Purpose]
Convert data type of blob elements. [Description]
Converts between supported data types (e.g., U8 to S32, S32 to F32). ### ss\_mpi\_svp\_mau\_get\_sort\_tmpbuf\_size<a name="ZH-CN_TOPIC_0000002408294160"></a> [Purpose]
Get the required temporary buffer size for the sort operation. ### ss\_mpi\_svp\_mau\_sort<a name="ZH-CN_TOPIC_0000002441853597"></a> [Purpose]
Sort elements within each row or column of a matrix. ### ss\_mpi\_svp\_mau\_get\_fir\_tmpbuf\_size<a name="ZH-CN_TOPIC_0000002441853701"></a> [Purpose]
Get the required temporary buffer size for the FIR filter operation. ### ss\_mpi\_svp\_mau\_fir<a name="ZH-CN_TOPIC_0000002441853513"></a> [Purpose]
Apply a Finite Impulse Response (FIR) filter to the input data. ### ss\_mpi\_svp\_mau\_query<a name="ZH-CN_TOPIC_0000002408294188"></a> [Purpose]
Query the completion status of an asynchronous MAU operation. [Syntax]
```c
td_s32 ss_mpi_svp_mau_query(ot_svp_mau_handle handle, td_u32 timeout_ms);
``` [Parameters]
- handle: The operation handle returned by the MAU function.
- timeout_ms: Timeout in milliseconds (OT_WAIT_FOREVER for infinite wait). [Description]
Blocks until the specified MAU operation completes or the timeout expires. ### ss\_mpi\_svp\_mau\_add\_mem\_info<a name="ZH-CN_TOPIC_0000002441853565"></a> [Purpose]
Register a memory region for MAU internal use. ### ss\_mpi\_svp\_mau\_rm\_mem\_info<a name="ZH-CN_TOPIC_0000002408294464"></a> [Purpose]
Remove a previously registered memory region. ## Data Types and Structures<a name="ZH-CN_TOPIC_0000002408134296"></a> ### ot\_svp\_blob\_type<a name="ZH-CN_TOPIC_0000002408134284"></a> [Definition]
```c
typedef enum { OT_SVP_BLOB_TYPE_S32 = 0x0, OT_SVP_BLOB_TYPE_U32, OT_SVP_BLOB_TYPE_S16, OT_SVP_BLOB_TYPE_U16, OT_SVP_BLOB_TYPE_S8, OT_SVP_BLOB_TYPE_U8, OT_SVP_BLOB_TYPE_F32,
} ot_svp_blob_type;
``` [Description]
Enumeration of supported data types for blob elements. ### ot\_svp\_blob<a name="ZH-CN_TOPIC_0000002441853637"></a> [Definition]
```c
typedef struct { ot_svp_blob_type type; td_s32 dimension; td_s32 shape[OT_SVP_MAX_DIM]; td_s32 stride[OT_SVP_MAX_DIM]; td_u64 phy_addr; td_u64 vir_addr;
} ot_svp_blob;
``` [Description]
Defines a multi-dimensional array (blob) for SVP operations. [Members]
- type: Element data type.
- dimension: Number of dimensions (1-4 typically).
- shape: Size of each dimension.
- stride: Byte stride for each dimension.
- phy_addr: Physical address of the blob data.
- vir_addr: Virtual address of the blob data. ### ot\_svp\_src\_blob / ot\_svp\_dst\_blob<a name="ZH-CN_TOPIC_0000002441853749"></a> Wrapper structures for identifying blobs as source or destination in MAU operations. ### ot\_svp\_mem\_info<a name="ZH-CN_TOPIC_0000002408134312"></a> [Definition]
```c
typedef struct { td_u64 phy_addr; td_u64 vir_addr; td_u32 length;
} ot_svp_mem_info;
``` [Description]
Describes a memory region for MAU registration. ### Additional MAU Data Types - **ot\_svp\_mau\_handle**: MAU operation handle type.
- **ot\_svp\_mau\_ctrl**: Control parameters for MAU operations (includes transpose flags, operation type selection, etc.). ## Proc Debug Information<a name="cat /proc/umap/mau"></a> The MAU proc debug information is available at `/proc/umap/mau`. It displays:
- MAU hardware version and status.
- Current operation type and parameters.
- Job queue depth and completion status.
- Memory usage statistics. # DPU\_RECT
## Overview<a name="ZH-CN_TOPIC_0000002441853553"></a> The DPU_RECT module is a hardware accelerator for rectangle-based operations used in object detection. It performs tasks such as:
- Region proposal generation
- Bounding box regression
- Non-maximum suppression (NMS)
- ROI (Region of Interest) extraction ## API Reference ### Key API Functions - **ss\_mpi\_svp\_rect\_retina\_face**: RetinaFace-based face detection processing.
- **ss\_mpi\_svp\_rect\_retina\_face\_use\_fast\_nms**: RetinaFace with fast NMS.
- **ss\_mpi\_svp\_rect\_refine**: Bounding box refinement.
- **ss\_mpi\_svp\_rect\_nms**: Non-maximum suppression.
- **ss\_mpi\_svp\_rect\_nms\_sorted**: NMS on pre-sorted boxes.
- **ss\_mpi\_svp\_rect\_fast\_nms**: Fast NMS algorithm.
- **ss\_mpi\_svp\_rect\_anchor\_op**: Anchor-based region operations.
- **ss\_mpi\_svp\_rect\_quant\_filter**: Quantization-aware filtering.
- **ss\_mpi\_svp\_rect\_gen\_proposal**: Generate proposal regions.
- **ss\_mpi\_svp\_rect\_conv**: Convolution on rectangle features.
- **ss\_mpi\_svp\_rect\_query**: Query DPU_RECT operation status. ### ss\_mpi\_svp\_rect\_retina\_face [Purpose]
Perform Retina Face face detection processing on the DPU_RECT hardware. [Parameters]
- src: Input blobs (feature maps from the neural network).
- dst: Output blobs (detected face bounding boxes and landmarks).
- ctrl: Control parameters (thresholds, anchor parameters, etc.).
- sync: Synchronous or asynchronous execution. [Return Value]
0 on success, non-zero error code on failure. ### ss\_mpi\_svp\_rect\_nms [Purpose]
Perform non-maximum suppression on detected bounding boxes. [Description]
Removes duplicate detections by suppressing boxes with high IoU overlap with higher-scoring boxes. Supports configurable IoU thresholds. ### ss\_mpi\_svp\_rect\_anchor\_op [Purpose]
Perform anchor-based operations for object detection. [Description]
Generates and refines anchor boxes based on feature map locations and learned offsets. ## Data Types ### Key Structures - **ot\_svp\_rect\_handle**: DPU_RECT operation handle.
- **ot\_svp\_rect\_retina\_face\_ctrl**: Control parameters for Retina Face.
- **ot\_svp\_rect\_nms\_ctrl**: NMS control parameters (IoU threshold, max detections).
- **ot\_svp\_rect\_anchor\_ctrl**: Anchor operation control parameters.
- **ot\_svp\_rect\_bbox**: Bounding box structure (left, top, right, bottom, score). ## Proc Debug Information<a name="cat /proc/umap/rect"></a> Available at `/proc/umap/rect`. Displays:
- DPU_RECT version and status.
- Current operation type configuration.
- Processing statistics and performance counters. # DPU\_MATCH
## Overview<a name="ZH-CN_TOPIC_0000002408134356"></a> The DPU_MATCH module is a hardware accelerator for feature matching operations used in object tracking and re-identification. It supports:
- Feature distance computation
- Feature matching with nearest-neighbor search
- Cosine similarity computation between feature sets
- Linear and nearest-neighbor matching algorithms ## API Reference ### Key API Functions - **ss\_mpi\_svp\_match\_calc\_cos\_dist**: Compute cosine distance matrix between feature sets.
- **ss\_mpi\_svp\_match\_calc\_euclid\_dist**: Compute Euclidean distance matrix between feature sets.
- **ss\_mpi\_svp\_match\_calc\_linear**: Perform linear matching between two feature sets.
- **ss\_mpi\_svp\_match\_calc\_nn**: Nearest-neighbor matching.
- **ss\_mpi\_svp\_match\_calc\_nn2**: Enhanced nearest-neighbor matching with ratio test.
- **ss\_mpi\_svp\_match\_query**: Query DPU_MATCH operation status. ### ss\_mpi\_svp\_match\_calc\_cos\_dist [Purpose]
Compute the cosine distance matrix between two sets of feature vectors. [Parameters]
- src[2]: Source blobs containing feature sets A and B.
- dst: Destination blob for the distance matrix.
- ctrl: Control parameters.
- sync: Synchronous or asynchronous. ### ss\_mpi\_svp\_match\_calc\_nn [Purpose]
Perform nearest-neighbor matching between two feature sets. [Description]
For each feature in the query set, finds the nearest neighbor in the reference set based on the specified distance metric. ### ss\_mpi\_svp\_match\_calc\_nn2 [Purpose]
Perform enhanced nearest-neighbor matching with ratio test. [Description]
Similar to NN but returns both the nearest and second-nearest distances for ratio testing (useful for Lowe's ratio test in SIFT matching). ## Data Types ### Key Structures - **ot\_svp\_match\_handle**: DPU_MATCH operation handle.
- **ot\_svp\_match\_ctrl**: Matching control parameters.
- **ot\_svp\_match\_cos\_dist\_ctrl**: Cosine distance control.
- **ot\_svp\_match\_euclid\_dist\_ctrl**: Euclidean distance control.
- **ot\_svp\_match\_linear\_ctrl**: Linear matching control.
- **ot\_svp\_match\_nn\_ctrl**: Nearest-neighbor control parameters. ## Proc Debug Information<a name="cat /proc/umap/match"></a> Available at `/proc/umap/match`. Displays:
- DPU_MATCH version and hardware status.
- Operation configuration and statistics.
- Performance metrics. # DSP
## Overview<a name="ZH-CN_TOPIC_0000002408294116"></a> The DSP (Digital Signal Processor) module on the SVP platform provides general-purpose signal processing capabilities for vision and AI workloads. It is a programmable processor that can execute custom algorithms for image preprocessing, feature extraction, and post-processing. ## API Reference ### Key API Functions - **ss\_mpi\_svp\_dsp\_init**: Initialize the DSP subsystem.
- **ss\_mpi\_svp\_dsp\_exit**: Exit and release DSP resources.
- **ss\_mpi\_svp\_dsp\_load\_firmware**: Load firmware/program to the DSP.
- **ss\_mpi\_svp\_dsp\_invoke**: Invoke a DSP program for execution.
- **ss\_mpi\_svp\_dsp\_query**: Query DSP execution status.
- **ss\_mpi\_svp\_dsp\_add\_mem\_info**: Register a memory region for DSP access.
- **ss\_mpi\_svp\_dsp\_rm\_mem\_info**: Remove a registered memory region. ## Data Types ### Key Structures - **ot\_svp\_dsp\_handle**: DSP operation handle.
- **ot\_svp\_dsp\_ctrl**: DSP control parameters.
- **ot\_svp\_dsp\_mem\_info**: DSP memory region information.
- **ot\_svp\_dsp\_fw\_info**: DSP firmware information. ## Proc Debug Information Available at `/proc/umap/dsp`. Displays:
- DSP firmware version and load status.
- Current task information.
- Memory usage and performance metrics.
