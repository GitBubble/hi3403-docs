---
title: "Preface"
source: /sessions/sharp-sweet-allen/mnt/hi3403-build/pegasus/docs/zh-CN/KLAD API 参考/KLAD API 参考.md
---

# Preface
**Overview<a name="section1589mcpsimp"></a>**

KLAD is the key management module, integrating key derivation, plaintext KEY transfer, and ROOTKEY hierarchical transfer.

>![](public_sys-resources/icon-note.gif) **Note:**
>Unless otherwise specified in this document, the content for Hi3519AV200 and Hi3403V100 is completely identical.

**Product Version<a name="section1592mcpsimp"></a>**

The product versions corresponding to this document are as follows.

<a name="table1595mcpsimp"></a>
<table><thead align="left"><tr id="row1600mcpsimp"><th class="cellrowborder" valign="top" width="32%" id="mcps1.1.3.1.1"><p id="p1602mcpsimp"><a name="p1602mcpsimp"></a><a name="p1602mcpsimp"></a>Product Name</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.1.3.1.2"><p id="p1604mcpsimp"><a name="p1604mcpsimp"></a><a name="p1604mcpsimp"></a>Product Version</p>
</th>
</tr>
</thead>
<tbody><tr id="row1606mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1608mcpsimp"><a name="p1608mcpsimp"></a><a name="p1608mcpsimp"></a>Hi3403V100</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1610mcpsimp"><a name="p1610mcpsimp"></a><a name="p1610mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row1611mcpsimp"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p1613mcpsimp"><a name="p1613mcpsimp"></a><a name="p1613mcpsimp"></a>SS626</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p1615mcpsimp"><a name="p1615mcpsimp"></a><a name="p1615mcpsimp"></a>V100</p>
</td>
</tr>
<tr id="row149564818401"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.1.3.1.1 "><p id="p8622349102117"><a name="p8622349102117"></a><a name="p8622349102117"></a>Hi3519AV200</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.1.3.1.2 "><p id="p9185184311112"><a name="p9185184311112"></a><a name="p9185184311112"></a>V100</p>
</td>
</tr>
</tbody>
</table>

**Intended Audience<a name="section1616mcpsimp"></a>**

This document (guide) is primarily intended for the following engineers:

-   Technical Support Engineers
-   Software Development Engineers

**Symbol Conventions<a name="section1622mcpsimp"></a>**

The following symbols may appear in this document, and their meanings are described below.

<a name="table1625mcpsimp"></a>
<table><thead align="left"><tr id="row1630mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.3.1.1"><p id="p1632mcpsimp"><a name="p1632mcpsimp"></a><a name="p1632mcpsimp"></a>Symbol</p>
</th>
<th class="cellrowborder" valign="top" width="82%" id="mcps1.1.3.1.2"><p id="p1634mcpsimp"><a name="p1634mcpsimp"></a><a name="p1634mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1636mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p1638mcpsimp"><a name="p1638mcpsimp"></a><a name="p1638mcpsimp"></a><a name="image158"></a><a name="image158"></a><span><img id="image158" src="figures/zh-cn_image_0000002424349514.png" height="23.94" width="67.83"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p1640mcpsimp"><a name="p1640mcpsimp"></a><a name="p1640mcpsimp"></a>Indicates a high-level hazard which, if not avoided, will result in death or serious injury.</p>
</td>
</tr>
<tr id="row1641mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p1643mcpsimp"><a name="p1643mcpsimp"></a><a name="p1643mcpsimp"></a><a name="image159"></a><a name="image159"></a><span><img id="image159" src="figures/zh-cn_image_0000002457868413.png" height="23.94" width="67.83"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p1645mcpsimp"><a name="p1645mcpsimp"></a><a name="p1645mcpsimp"></a>Indicates a medium-level hazard which, if not avoided, could result in death or serious injury.</p>
</td>
</tr>
<tr id="row1646mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p1648mcpsimp"><a name="p1648mcpsimp"></a><a name="p1648mcpsimp"></a><a name="image160"></a><a name="image160"></a><span><img id="image160" src="figures/zh-cn_image_0000002424189674.png" height="23.94" width="67.83"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p1650mcpsimp"><a name="p1650mcpsimp"></a><a name="p1650mcpsimp"></a>Indicates a low-level hazard which, if not avoided, could result in minor or moderate injury.</p>
</td>
</tr>
<tr id="row1651mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p1653mcpsimp"><a name="p1653mcpsimp"></a><a name="p1653mcpsimp"></a><a name="image161"></a><a name="image161"></a><span><img id="image161" src="figures/zh-cn_image_0000002457828281.png" height="23.94" width="67.83"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p1655mcpsimp"><a name="p1655mcpsimp"></a><a name="p1655mcpsimp"></a>Used to convey device or environmental safety alert information. If not avoided, it may result in equipment damage, data loss, reduced equipment performance, or other unpredictable consequences.</p>
<p id="p1656mcpsimp"><a name="p1656mcpsimp"></a><a name="p1656mcpsimp"></a>"Caution" does not involve personal injury.</p>
</td>
</tr>
<tr id="row1657mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.3.1.1 "><p class="msonormal" id="p1659mcpsimp"><a name="p1659mcpsimp"></a><a name="p1659mcpsimp"></a><a name="image162"></a><a name="image162"></a><span><img id="image162" src="figures/zh-cn_image_0000002424189678.png" height="23.94" width="67.83"></span></p>
</td>
<td class="cellrowborder" valign="top" width="82%" headers="mcps1.1.3.1.2 "><p id="p1661mcpsimp"><a name="p1661mcpsimp"></a><a name="p1661mcpsimp"></a>Supplementary explanation of key information in the main text.</p>
<p id="p1662mcpsimp"><a name="p1662mcpsimp"></a><a name="p1662mcpsimp"></a>"Note" is not safety warning information and does not involve personal, equipment, or environmental injury.</p>
</td>
</tr>
</tbody>
</table>

**Revision History<a name="section182223334015"></a>**

<a name="table1557726816410"></a>
<table><thead align="left"><tr id="row2942532716410"><th class="cellrowborder" valign="top" width="20.72%" id="mcps1.1.4.1.1"><p id="p3778275416410"><a name="p3778275416410"></a><a name="p3778275416410"></a>Document Version</p>
</th>
<th class="cellrowborder" valign="top" width="21.27%" id="mcps1.1.4.1.2"><p id="p5627845516410"><a name="p5627845516410"></a><a name="p5627845516410"></a>Release Date</p>
</th>
<th class="cellrowborder" valign="top" width="58.01%" id="mcps1.1.4.1.3"><p id="p2382284816410"><a name="p2382284816410"></a><a name="p2382284816410"></a>Change Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1665351220483"><td class="cellrowborder" valign="top" width="20.72%" headers="mcps1.1.4.1.1 "><p id="p10443201017431"><a name="p10443201017431"></a><a name="p10443201017431"></a>00B01</p>
</td>
<td class="cellrowborder" valign="top" width="21.27%" headers="mcps1.1.4.1.2 "><p id="p6851917114310"><a name="p6851917114310"></a><a name="p6851917114310"></a>2025-09-15</p>
</td>
<td class="cellrowborder" valign="top" width="58.01%" headers="mcps1.1.4.1.3 "><p id="p1946537916410"><a name="p1946537916410"></a><a name="p1946537916410"></a>First interim version release.</p>
</td>
</tr>
</tbody>
</table>

# Overview
## Overview<a name="ZH-CN_TOPIC_0000002457828269"></a>

KLAD is the key management module. It supports key derivation, plaintext KEY transfer, and ROOTKEY hierarchical transfer. It supports 16 KLAD software channels.

### Key Derivation<a name="ZH-CN_TOPIC_0000002424189626"></a>

Users can generate different keys based on different application scenarios, with the ability to derive up to 2<sup>32</sup> ROOTKEYs.

The work key derived from the key can be calculated using the provided derivation tool. For usage instructions, refer to "[Key Derivation Tool Description](#ZH-CN_TOPIC_0000002457828277)".

### Plaintext KEY Transfer<a name="ZH-CN_TOPIC_0000002424349470"></a>

Plaintext KEY refers to the working key used by the encryption/decryption engine, which is securely stored by the user.

-   Supports AES 128/192/256 bits encryption/decryption.
-   Supports SM4 128 bits encryption/decryption.
-   Hi3403V100 and SS626V100 do not support SM4.

### ROOTKEY Transfer<a name="ZH-CN_TOPIC_0000002424189630"></a>

ROOTKEY is the key generated from the root key of the OTP module through key de-obfuscation and key derivation. The ROOTKEY is stored in hardware and is not readable by the user. The working key for encryption/decryption is a KEY obtained after multiple levels of KLAD hierarchical transfer. This KEY is also stored in hardware and is not readable by the user. This scheme is mostly used in scenarios with high security requirements. The OTP root key is securely stored by the user.

-   Supports AES 128/256 bits encryption/decryption.
-   Supports SM4 128 bits encryption/decryption.
-   Hi3403V100 and SS626V100 do not support SM4.
-   Hi3403V100 and SS626V100 support 2-level KLAD transfer.

### KLAD Usage Notes<a name="ZH-CN_TOPIC_0000002424349494"></a>

When KLAD is deployed in different scenarios, its usage may vary.

-   In the Linux environment
    -   User-mode KLAD can be used by linking the static library libss\_klad.a or the dynamic library libss\_klad.so, depending on libsecurec.a or libsecurec.so.
    -   Kernel-mode KLAD uses module insertion, i.e., insmod ot\_klad.ko, which depends on ot\_osal.ko, ot\_base.ko, sys\_config.ko, and ot\_sys.ko.

-   In the OPTEE environment
    -   The user-mode KLAD external interface naming convention changes from ss\_mpi\_xxx in the Linux environment to ot\_tee\_xxx;
    -   The kernel-mode KLAD external interface naming convention changes from ss\_mpi\_xxx in the Linux environment to ot\_drv\_xxx.

-   In the UBOOT environment, the user-mode KLAD external interface naming convention changes from ss\_mpi\_xxx in the Linux environment to ot\_mpi\_xxx.

## Usage Flow<a name="ZH-CN_TOPIC_0000002457828241"></a>

### Plaintext KEY Transfer<a name="ZH-CN_TOPIC_0000002424189654"></a>

#### Scenario Description<a name="ZH-CN_TOPIC_0000002457828265"></a>

When the working key used for encryption/decryption is provided by the user, the plaintext KEY related interfaces need to be used. KLAD transfers the working key to a KEYSLOT. During encryption/decryption, the encryption/decryption engine retrieves the KEY from the corresponding KEYSLOT for encryption/decryption.

#### Workflow<a name="ZH-CN_TOPIC_0000002424349466"></a>

The plaintext KEY transfer development steps are as follows:

1.  Initialize the KLAD device. Call the interface [ss\_mpi\_klad\_init](#ZH-CN_TOPIC_0000002457868405).
2.  Create a KLAD handle. Call the interface [ss\_mpi\_klad\_create](#ZH-CN_TOPIC_0000002457828273).
3.  Bind the KLAD and KEYSLOT handles. Call the interface [ss\_mpi\_klad\_attach](#ZH-CN_TOPIC_0000002424349510).
4.  Set KLAD attributes. Call the interface [ss\_mpi\_klad\_set\_attr](#ZH-CN_TOPIC_0000002457868393).
5.  Set the plaintext KEY. Call the interface [ss\_mpi\_klad\_set\_clear\_key](#ZH-CN_TOPIC_0000002457868373).
6.  Unbind the KLAD and KEYSLOT handles. Call the interface [ss\_mpi\_klad\_detach](#ZH-CN_TOPIC_0000002424349486).
7.  Destroy the KLAD handle. Call the interface [ss\_mpi\_klad\_destroy](#ZH-CN_TOPIC_0000002424189642).
8.  Deinitialize the KLAD device. Call the interface [ss\_mpi\_klad\_deinit](#ZH-CN_TOPIC_0000002424349506).

#### Notes<a name="ZH-CN_TOPIC_0000002457828253"></a>

When using plaintext KEY transfer, please pay special attention to the following points.

-   The KEYSLOT handle must be created through the CIPHER module during KLAD configuration.
-   When transferring a plaintext KEY, the KLAD type must be configured as plaintext KLAD (OT\_KLAD\_TYPE\_CLEARCW).

### ROOTKEY Transfer<a name="ZH-CN_TOPIC_0000002457868389"></a>

#### Scenario Description<a name="ZH-CN_TOPIC_0000002457828257"></a>

Used in scenarios with high security requirements. The ROOTKEY is generated after key de-obfuscation and key derivation, and after multiple levels of KLAD transfer, a real working key is obtained. The working key is stored in hardware and is not readable by the user. KLAD transfers the working key to a KEYSLOT. During encryption/decryption, the encryption/decryption engine retrieves the KEY from the corresponding KEYSLOT for encryption/decryption.

#### Workflow<a name="ZH-CN_TOPIC_0000002457868409"></a>

The ROOTKEY transfer development steps are as follows:

1.  Initialize the KLAD device. Call the interface [ss\_mpi\_klad\_init](#ZH-CN_TOPIC_0000002457868405).
2.  Create a KLAD handle. Call the interface [ss\_mpi\_klad\_create](#ZH-CN_TOPIC_0000002457828273).
3.  Bind the KLAD and KEYSLOT handles. Call the interface [ss\_mpi\_klad\_attach](#ZH-CN_TOPIC_0000002424349510).
4.  Set KLAD attributes. Call the interface [ss\_mpi\_klad\_set\_attr](#ZH-CN_TOPIC_0000002457868393).
5.  Set the 1st to (n-1)th level KLAD key information. Call the interface [ss\_mpi\_klad\_set\_session\_key](#ZH-CN_TOPIC_0000002457868369).
6.  Set the nth level KLAD key information. Call the interface [ss\_mpi\_klad\_set\_content\_key](#ZH-CN_TOPIC_0000002457828237).
7.  Unbind the KLAD and KEYSLOT handles. Call the interface [ss\_mpi\_klad\_detach](#ZH-CN_TOPIC_0000002424349486).
8.  Destroy the KLAD handle. Call the interface [ss\_mpi\_klad\_destroy](#ZH-CN_TOPIC_0000002424189642).
9.  Deinitialize the KLAD device. Call the interface [ss\_mpi\_klad\_deinit](#ZH-CN_TOPIC_0000002424349506).

#### Notes<a name="ZH-CN_TOPIC_0000002457868377"></a>

When using ROOTKEY transfer, please pay special attention to the following points.

-   The KEYSLOT handle must be created through the CIPHER module during KLAD configuration.
-   When transferring ROOTKEY, the KLAD type must be configured as common KLAD (OT\_KLAD\_TYPE\_COMMON).

## Key Derivation Tool Description<a name="ZH-CN_TOPIC_0000002457828277"></a>

The key derivation tool is located in the osdrv/tools/pc/kdf\_customer directory. For usage commands, refer to the readme.txt file in that directory. The following mainly describes the configuration of relevant fields in the key.ini file.

**Table 1**  key.ini field description

<a name="table627mcpsimp"></a>
<table><thead align="left"><tr id="row633mcpsimp"><th class="cellrowborder" valign="top" width="41%" id="mcps1.2.3.1.1"><p id="p635mcpsimp"><a name="p635mcpsimp"></a><a name="p635mcpsimp"></a>Field</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.2.3.1.2"><p id="p637mcpsimp"><a name="p637mcpsimp"></a><a name="p637mcpsimp"></a>Meaning</p>
</th>
</tr>
</thead>
<tbody><tr id="row639mcpsimp"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.3.1.1 "><p id="p641mcpsimp"><a name="p641mcpsimp"></a><a name="p641mcpsimp"></a>function</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.3.1.2 "><p id="p643mcpsimp"><a name="p643mcpsimp"></a><a name="p643mcpsimp"></a>Function. Select 3 (work key).</p>
</td>
</tr>
<tr id="row644mcpsimp"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.3.1.1 "><p id="p646mcpsimp"><a name="p646mcpsimp"></a><a name="p646mcpsimp"></a>encryption</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.3.1.2 "><p id="p648mcpsimp"><a name="p648mcpsimp"></a><a name="p648mcpsimp"></a>Algorithm used. Select 0 (AES).</p>
</td>
</tr>
<tr id="row649mcpsimp"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.3.1.1 "><p id="p651mcpsimp"><a name="p651mcpsimp"></a><a name="p651mcpsimp"></a>oem_root_symc_key</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.3.1.2 "><p id="p653mcpsimp"><a name="p653mcpsimp"></a><a name="p653mcpsimp"></a>Root key flashed into OTP.</p>
</td>
</tr>
<tr id="row654mcpsimp"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.3.1.1 "><p id="p656mcpsimp"><a name="p656mcpsimp"></a><a name="p656mcpsimp"></a>protection_key_l1</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.3.1.2 "><p id="p658mcpsimp"><a name="p658mcpsimp"></a><a name="p658mcpsimp"></a>session_key, 128 bits.</p>
</td>
</tr>
<tr id="row659mcpsimp"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.3.1.1 "><p id="p661mcpsimp"><a name="p661mcpsimp"></a><a name="p661mcpsimp"></a>protection_key_l2</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.3.1.2 "><p id="p663mcpsimp"><a name="p663mcpsimp"></a><a name="p663mcpsimp"></a>content_key. If 128 bit is used, the derived work_key is also 128 bit; if 256 bit is used, the derived work_key is also 256 bit.</p>
</td>
</tr>
<tr id="row664mcpsimp"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.3.1.1 "><p id="p666mcpsimp"><a name="p666mcpsimp"></a><a name="p666mcpsimp"></a>oem_rk_deob_en</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.3.1.2 "><p id="p668mcpsimp"><a name="p668mcpsimp"></a><a name="p668mcpsimp"></a>Obfuscation protection. Default is 0. If the relevant OTP has been flashed, it needs to be set to 1.</p>
</td>
</tr>
<tr id="row669mcpsimp"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.3.1.1 "><p id="p671mcpsimp"><a name="p671mcpsimp"></a><a name="p671mcpsimp"></a>boot_flag</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.3.1.2 "><p id="p673mcpsimp"><a name="p673mcpsimp"></a><a name="p673mcpsimp"></a>Whether the work_key is used during the boot phase.</p>
</td>
</tr>
<tr id="row674mcpsimp"><td class="cellrowborder" valign="top" width="41%" headers="mcps1.2.3.1.1 "><p id="p676mcpsimp"><a name="p676mcpsimp"></a><a name="p676mcpsimp"></a>sw_reg</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.2.3.1.2 "><p id="p678mcpsimp"><a name="p678mcpsimp"></a><a name="p678mcpsimp"></a>Derivation material, owner_id.</p>
</td>
</tr>
</tbody>
</table>

Notes:

1.  Except for the fields mentioned above, no other fields need to be modified.
2.  If content\_key is 128 bit, work\_key is the first 16 bytes of the generated out.bin file; if content\_key is 256 bit, work\_key is the entire out.bin file generated.

# API Reference
KLAD provides the following APIs:

-   [ss\_mpi\_klad\_init](#ZH-CN_TOPIC_0000002457868405): Initializes the KLAD module.
-   [ss\_mpi\_klad\_deinit](#ZH-CN_TOPIC_0000002424349506): Deinitializes the KLAD module.
-   [ss\_mpi\_klad\_create](#ZH-CN_TOPIC_0000002457828273): Creates a KLAD handle.
-   [ss\_mpi\_klad\_destroy](#ZH-CN_TOPIC_0000002424189642): Destroys an existing KLAD handle.
-   [ss\_mpi\_klad\_attach](#ZH-CN_TOPIC_0000002424349510): Binds a KLAD handle and a KEYSLOT handle.
-   [ss\_mpi\_klad\_detach](#ZH-CN_TOPIC_0000002424349486): Unbinds a KLAD handle and a KEYSLOT handle.
-   [ss\_mpi\_klad\_set\_attr](#ZH-CN_TOPIC_0000002457868393): Sets KLAD attributes.
-   [ss\_mpi\_klad\_get\_attr](#ZH-CN_TOPIC_0000002424189662): Gets KLAD attributes.
-   [ss\_mpi\_klad\_set\_session\_key](#ZH-CN_TOPIC_0000002457868369): Configures the 1st to (n-1)th level KLAD KEY.
-   [ss\_mpi\_klad\_set\_content\_key](#ZH-CN_TOPIC_0000002457828237): Configures the last level KLAD KEY and simultaneously passes the key to KEYSLOT.
-   [ss\_mpi\_klad\_set\_clear\_key](#ZH-CN_TOPIC_0000002457868373): Configures a plaintext KEY and simultaneously passes the key to KEYSLOT.

## ss\_mpi\_klad\_init<a name="ZH-CN_TOPIC_0000002457868405"></a>

[Description]

Initializes the KLAD module.

[Syntax]

```
td_s32 ss_mpi_klad_init(td_void);
```

[Parameters]

None.

[Return Values]

<a name="table111mcpsimp"></a>
<table><thead align="left"><tr id="row116mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p118mcpsimp"><a name="p118mcpsimp"></a><a name="p118mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p120mcpsimp"><a name="p120mcpsimp"></a><a name="p120mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row122mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p124mcpsimp"><a name="p124mcpsimp"></a><a name="p124mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p126mcpsimp"><a name="p126mcpsimp"></a><a name="p126mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row127mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p129mcpsimp"><a name="p129mcpsimp"></a><a name="p129mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p131mcpsimp"><a name="p131mcpsimp"></a><a name="p131mcpsimp"></a>See <a href="#ZH-CN_TOPIC_0000002424349490">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table>

[Requirements]

-   Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
-   Library files: libss\_klad.a, libss\_klad.so

[Notes]

-   Supports multiple calls.
-   Initialization and deinitialization must be used in pairs.

[Example]

None.

## ss\_mpi\_klad\_deinit<a name="ZH-CN_TOPIC_0000002424349506"></a>

[Description]

Deinitializes the KLAD module.

[Syntax]

```
td_s32 ss_mpi_klad_deinit(td_void);
```

[Parameters]

None.

[Return Values]

<a name="table298mcpsimp"></a>
<table><thead align="left"><tr id="row303mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p305mcpsimp"><a name="p305mcpsimp"></a><a name="p305mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p307mcpsimp"><a name="p307mcpsimp"></a><a name="p307mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row309mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p311mcpsimp"><a name="p311mcpsimp"></a><a name="p311mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p313mcpsimp"><a name="p313mcpsimp"></a><a name="p313mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row314mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p316mcpsimp"><a name="p316mcpsimp"></a><a name="p316mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p318mcpsimp"><a name="p318mcpsimp"></a><a name="p318mcpsimp"></a>See <a href="#ZH-CN_TOPIC_0000002424349490">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table>

[Requirements]

-   Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
-   Library files: libss\_klad.a, libss\_klad.so

[Notes]

-   Supports multiple calls.
-   Initialization and deinitialization must be used in pairs.

[Example]

None.

## ss\_mpi\_klad\_create<a name="ZH-CN_TOPIC_0000002457828273"></a>

[Description]

Creates a KLAD handle.

[Syntax]

```
td_s32 ss_mpi_klad_create (td_handle *klad);
```

[Parameters]

<a name="table397mcpsimp"></a>
<table><thead align="left"><tr id="row403mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.1"><p id="p405mcpsimp"><a name="p405mcpsimp"></a><a name="p405mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="65%" id="mcps1.1.4.1.2"><p id="p407mcpsimp"><a name="p407mcpsimp"></a><a name="p407mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.4.1.3"><p id="p409mcpsimp"><a name="p409mcpsimp"></a><a name="p409mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row411mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p413mcpsimp"><a name="p413mcpsimp"></a><a name="p413mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.4.1.2 "><p id="p415mcpsimp"><a name="p415mcpsimp"></a><a name="p415mcpsimp"></a>KLAD handle pointer.</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p417mcpsimp"><a name="p417mcpsimp"></a><a name="p417mcpsimp"></a>Output</p>
</td>
</tr>
</tbody>
</table>

[Return Values]

<a name="table419mcpsimp"></a>
<table><thead align="left"><tr id="row424mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p426mcpsimp"><a name="p426mcpsimp"></a><a name="p426mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p428mcpsimp"><a name="p428mcpsimp"></a><a name="p428mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row430mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p432mcpsimp"><a name="p432mcpsimp"></a><a name="p432mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p434mcpsimp"><a name="p434mcpsimp"></a><a name="p434mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row435mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p437mcpsimp"><a name="p437mcpsimp"></a><a name="p437mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p439mcpsimp"><a name="p439mcpsimp"></a><a name="p439mcpsimp"></a>See <a href="#ZH-CN_TOPIC_0000002424349490">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table>

[Requirements]

-   Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
-   Library files: libss\_klad.a, libss\_klad.so

[Notes]

-   klad must not be NULL.
-   After using the channel, the corresponding channel should be destroyed.
-   Channel creation and destruction must be used in pairs.

[Example]

None.

## ss\_mpi\_klad\_destroy<a name="ZH-CN_TOPIC_0000002424189642"></a>

[Description]

Destroys a KLAD.

[Syntax]

```
td_s32 ss_mpi_klad_destroy (td_handle klad);
```

[Parameters]

<a name="table1700mcpsimp"></a>
<table><thead align="left"><tr id="row1706mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.1"><p id="p1708mcpsimp"><a name="p1708mcpsimp"></a><a name="p1708mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="65%" id="mcps1.1.4.1.2"><p id="p1710mcpsimp"><a name="p1710mcpsimp"></a><a name="p1710mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.4.1.3"><p id="p1712mcpsimp"><a name="p1712mcpsimp"></a><a name="p1712mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row1714mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p1716mcpsimp"><a name="p1716mcpsimp"></a><a name="p1716mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.4.1.2 "><p id="p1718mcpsimp"><a name="p1718mcpsimp"></a><a name="p1718mcpsimp"></a>KLAD handle.</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p1720mcpsimp"><a name="p1720mcpsimp"></a><a name="p1720mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table>

[Return Values]

<a name="table1722mcpsimp"></a>
<table><thead align="left"><tr id="row1727mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1729mcpsimp"><a name="p1729mcpsimp"></a><a name="p1729mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1731mcpsimp"><a name="p1731mcpsimp"></a><a name="p1731mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1733mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1735mcpsimp"><a name="p1735mcpsimp"></a><a name="p1735mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1737mcpsimp"><a name="p1737mcpsimp"></a><a name="p1737mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row1738mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1740mcpsimp"><a name="p1740mcpsimp"></a><a name="p1740mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1742mcpsimp"><a name="p1742mcpsimp"></a><a name="p1742mcpsimp"></a>See <a href="#ZH-CN_TOPIC_0000002424349490">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table>

[Requirements]

-   Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
-   Library files: libss\_klad.a, libss\_klad.so

[Notes]

-   The KLAD handle must have been created.
-   Channel creation and destruction must be used in pairs.

[Example]

None.

## ss\_mpi\_klad\_attach<a name="ZH-CN_TOPIC_0000002424349510"></a>

[Description]

Binds a KLAD handle and a KEYSLOT handle.

[Syntax]

```
td_s32 ss_mpi_klad_attach(td_handle klad, td_handle target);
```

[Parameters]

<a name="table149mcpsimp"></a>
<table><thead align="left"><tr id="row155mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.1"><p id="p157mcpsimp"><a name="p157mcpsimp"></a><a name="p157mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="65%" id="mcps1.1.4.1.2"><p id="p159mcpsimp"><a name="p159mcpsimp"></a><a name="p159mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.4.1.3"><p id="p161mcpsimp"><a name="p161mcpsimp"></a><a name="p161mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row163mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p165mcpsimp"><a name="p165mcpsimp"></a><a name="p165mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.4.1.2 "><p id="p167mcpsimp"><a name="p167mcpsimp"></a><a name="p167mcpsimp"></a>KLAD handle.</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p169mcpsimp"><a name="p169mcpsimp"></a><a name="p169mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row170mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p172mcpsimp"><a name="p172mcpsimp"></a><a name="p172mcpsimp"></a>target</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.4.1.2 "><p id="p174mcpsimp"><a name="p174mcpsimp"></a><a name="p174mcpsimp"></a>KEYSLOT handle.</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p176mcpsimp"><a name="p176mcpsimp"></a><a name="p176mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table>

[Return Values]

<a name="table178mcpsimp"></a>
<table><thead align="left"><tr id="row183mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p185mcpsimp"><a name="p185mcpsimp"></a><a name="p185mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p187mcpsimp"><a name="p187mcpsimp"></a><a name="p187mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row189mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p191mcpsimp"><a name="p191mcpsimp"></a><a name="p191mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p193mcpsimp"><a name="p193mcpsimp"></a><a name="p193mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row194mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p196mcpsimp"><a name="p196mcpsimp"></a><a name="p196mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p198mcpsimp"><a name="p198mcpsimp"></a><a name="p198mcpsimp"></a>See <a href="#ZH-CN_TOPIC_0000002424349490">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table>

[Requirements]

-   Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
-   Library files: libss\_klad.a, libss\_klad.so

[Notes]

-   The KLAD and KEYSLOT handles must have been created. If handles are not created, binding between handles may succeed, but functionality will fail.
-   Binding and unbinding must be used in pairs.

[Example]

None.

## ss\_mpi\_klad\_detach<a name="ZH-CN_TOPIC_0000002424349486"></a>

[Description]

Unbinds a KLAD handle and a KEYSLOT handle.

[Syntax]

```
td_s32 ss_mpi_klad_detach(td_handle klad, td_handle target);
```

[Parameters]

<a name="table1524mcpsimp"></a>
<table><thead align="left"><tr id="row1530mcpsimp"><th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.1"><p id="p1532mcpsimp"><a name="p1532mcpsimp"></a><a name="p1532mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="65%" id="mcps1.1.4.1.2"><p id="p1534mcpsimp"><a name="p1534mcpsimp"></a><a name="p1534mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="17%" id="mcps1.1.4.1.3"><p id="p1536mcpsimp"><a name="p1536mcpsimp"></a><a name="p1536mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row1538mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p1540mcpsimp"><a name="p1540mcpsimp"></a><a name="p1540mcpsimp"></a>handle</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.4.1.2 "><p id="p1542mcpsimp"><a name="p1542mcpsimp"></a><a name="p1542mcpsimp"></a>KLAD handle.</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p1544mcpsimp"><a name="p1544mcpsimp"></a><a name="p1544mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row1545mcpsimp"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.1 "><p id="p1547mcpsimp"><a name="p1547mcpsimp"></a><a name="p1547mcpsimp"></a>target</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.1.4.1.2 "><p id="p1549mcpsimp"><a name="p1549mcpsimp"></a><a name="p1549mcpsimp"></a>KEYSLOT handle.</p>
</td>
<td class="cellrowborder" valign="top" width="17%" headers="mcps1.1.4.1.3 "><p id="p1551mcpsimp"><a name="p1551mcpsimp"></a><a name="p1551mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table>

[Return Values]

<a name="table1553mcpsimp"></a>
<table><thead align="left"><tr id="row1558mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1560mcpsimp"><a name="p1560mcpsimp"></a><a name="p1560mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1562mcpsimp"><a name="p1562mcpsimp"></a><a name="p1562mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1564mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1566mcpsimp"><a name="p1566mcpsimp"></a><a name="p1566mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1568mcpsimp"><a name="p1568mcpsimp"></a><a name="p1568mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row1569mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1571mcpsimp"><a name="p1571mcpsimp"></a><a name="p1571mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1573mcpsimp"><a name="p1573mcpsimp"></a><a name="p1573mcpsimp"></a>See <a href="#ZH-CN_TOPIC_0000002424349490">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table>

[Requirements]

-   Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
-   Library files: libss\_klad.a, libss\_klad.so

[Notes]

-   The KLAD and KEYSLOT handles must have been created.
-   Binding and unbinding must be used in pairs.

[Example]

None.

## ss\_mpi\_klad\_set\_attr<a name="ZH-CN_TOPIC_0000002457868393"></a><a name="ss_mpi_klad_set_attr"></a>

[Description]

Sets KLAD attributes.

[Syntax]

```
td_s32 ss_mpi_klad_set_attr(td_handle klad, const ot_klad_attr *attr);<a name="ss_mpi_klad_set_attr"></a>
```

[Parameters]

<a name="table1414mcpsimp"></a>
<table><thead align="left"><tr id="row1420mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.1"><p id="p1422mcpsimp"><a name="p1422mcpsimp"></a><a name="p1422mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.1.4.1.2"><p id="p1424mcpsimp"><a name="p1424mcpsimp"></a><a name="p1424mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.3"><p id="p1426mcpsimp"><a name="p1426mcpsimp"></a><a name="p1426mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row1428mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p1430mcpsimp"><a name="p1430mcpsimp"></a><a name="p1430mcpsimp"></a>klad</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1432mcpsimp"><a name="p1432mcpsimp"></a><a name="p1432mcpsimp"></a>KLAD handle.</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1434mcpsimp"><a name="p1434mcpsimp"></a><a name="p1434mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row1435mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p1437mcpsimp"><a name="p1437mcpsimp"></a><a name="p1437mcpsimp"></a>attr</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p1439mcpsimp"><a name="p1439mcpsimp"></a><a name="p1439mcpsimp"></a>KLAD attributes. Must not be NULL.</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1441mcpsimp"><a name="p1441mcpsimp"></a><a name="p1441mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table>

[Return Values]

<a name="table1443mcpsimp"></a>
<table><thead align="left"><tr id="row1448mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1450mcpsimp"><a name="p1450mcpsimp"></a><a name="p1450mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1452mcpsimp"><a name="p1452mcpsimp"></a><a name="p1452mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1454mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1456mcpsimp"><a name="p1456mcpsimp"></a><a name="p1456mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1458mcpsimp"><a name="p1458mcpsimp"></a><a name="p1458mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row1459mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1461mcpsimp"><a name="p1461mcpsimp"></a><a name="p1461mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1463mcpsimp"><a name="p1463mcpsimp"></a><a name="p1463mcpsimp"></a>See <a href="#ZH-CN_TOPIC_0000002424349490">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table>

[Requirements]

-   Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
-   Library files: libss\_klad.a, libss\_klad.so

[Notes]

-   The KLAD handle must have been created.
-   Can be called multiple times; the last set attributes take effect.

[Example]

None.

## ss\_mpi\_klad\_get\_attr<a name="ZH-CN_TOPIC_0000002424189662"></a><a name="ss_mpi_klad_get_attr"></a>

[Description]

Gets KLAD attributes.

[Syntax]

```
td_s32 ss_mpi_klad_get_attr(td_handle klad, ot_klad_attr*attr);<a name="ss_mpi_klad_get_attr"></a>
```

[Parameters]

<a name="table1814mcpsimp"></a>
<table><thead align="left"><tr id="row1820mcpsimp"><th class="cellrowborder" valign="top" width="22%" id="mcps1.1.4.1.1"><p id="p1822mcpsimp"><a name="p1822mcpsimp"></a><a name="p1822mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.1.4.1.2"><p id="p1824mcpsimp"><a name="p1824mcpsimp"></a><a name="p1824mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.3"><p id="p1826mcpsimp"><a name="p1826mcpsimp"></a><a name="p1826mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row1828mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1830mcpsimp"><a name="p1830mcpsimp"></a><a name="p1830mcpsimp"></a>klad</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1832mcpsimp"><a name="p1832mcpsimp"></a><a name="p1832mcpsimp"></a>KLAD handle.</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1834mcpsimp"><a name="p1834mcpsimp"></a><a name="p1834mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row1835mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1837mcpsimp"><a name="p1837mcpsimp"></a><a name="p1837mcpsimp"></a>attr</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1839mcpsimp"><a name="p1839mcpsimp"></a><a name="p1839mcpsimp"></a>KLAD attributes. Must not be NULL.</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1841mcpsimp"><a name="p1841mcpsimp"></a><a name="p1841mcpsimp"></a>Output</p>
</td>
</tr>
</tbody>
</table>

[Return Values]

<a name="table1843mcpsimp"></a>
<table><thead align="left"><tr id="row1848mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1850mcpsimp"><a name="p1850mcpsimp"></a><a name="p1850mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1852mcpsimp"><a name="p1852mcpsimp"></a><a name="p1852mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1854mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1856mcpsimp"><a name="p1856mcpsimp"></a><a name="p1856mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1858mcpsimp"><a name="p1858mcpsimp"></a><a name="p1858mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row1859mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1861mcpsimp"><a name="p1861mcpsimp"></a><a name="p1861mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1863mcpsimp"><a name="p1863mcpsimp"></a><a name="p1863mcpsimp"></a>See <a href="#ZH-CN_TOPIC_0000002424349490">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table>

[Requirements]

-   Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
-   Library files: libss\_klad.a, libss\_klad.so

[Notes]

The KLAD handle must have been created.

[Example]

None.

## ss\_mpi\_klad\_set\_session\_key<a name="ZH-CN_TOPIC_0000002457868369"></a><a name="ss_mpi_klad_set_session_key"></a>

[Description]

Configures the 1st to (n-1)th level KLAD KEY.

[Syntax]

```
td_s32 ss_mpi_klad_set_session_key(td_handle klad, const ot_klad_session_key *key);<a name="ss_mpi_klad_set_session_key"></a>
```

[Parameters]

<a name="table470mcpsimp"></a>
<table><thead align="left"><tr id="row476mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.1"><p id="p478mcpsimp"><a name="p478mcpsimp"></a><a name="p478mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.1.4.1.2"><p id="p480mcpsimp"><a name="p480mcpsimp"></a><a name="p480mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.3"><p id="p482mcpsimp"><a name="p482mcpsimp"></a><a name="p482mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row484mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p486mcpsimp"><a name="p486mcpsimp"></a><a name="p486mcpsimp"></a>klad</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p488mcpsimp"><a name="p488mcpsimp"></a><a name="p488mcpsimp"></a>KLAD handle.</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p490mcpsimp"><a name="p490mcpsimp"></a><a name="p490mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row491mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p493mcpsimp"><a name="p493mcpsimp"></a><a name="p493mcpsimp"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p495mcpsimp"><a name="p495mcpsimp"></a><a name="p495mcpsimp"></a>1st to (n-1)th level key configuration. Must not be NULL.</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p497mcpsimp"><a name="p497mcpsimp"></a><a name="p497mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table>

[Return Values]

<a name="table499mcpsimp"></a>
<table><thead align="left"><tr id="row504mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p506mcpsimp"><a name="p506mcpsimp"></a><a name="p506mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p508mcpsimp"><a name="p508mcpsimp"></a><a name="p508mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row510mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p512mcpsimp"><a name="p512mcpsimp"></a><a name="p512mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p514mcpsimp"><a name="p514mcpsimp"></a><a name="p514mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row515mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p517mcpsimp"><a name="p517mcpsimp"></a><a name="p517mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p519mcpsimp"><a name="p519mcpsimp"></a><a name="p519mcpsimp"></a>See <a href="#ZH-CN_TOPIC_0000002424349490">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table>

[Requirements]

-   Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
-   Library files: libss\_klad.a, libss\_klad.so

[Notes]

-   The KLAD handle must have been created.
-   Cannot be called multiple times.

[Example]

None.

## ss\_mpi\_klad\_set\_content\_key<a name="ZH-CN_TOPIC_0000002457828237"></a><a name="ss_mpi_klad_set_content_key"></a>

[Description]

Configures the last level KLAD KEY and simultaneously passes the key to KEYSLOT.

[Syntax]

```
td_s32 ss_mpi_klad_set_content_key(td_handle klad, const ot_klad_content_key *key);<a name="ss_mpi_klad_set_content_key"></a>
```

[Parameters]

<a name="table774mcpsimp"></a>
<table><thead align="left"><tr id="row780mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.4.1.1"><p id="p782mcpsimp"><a name="p782mcpsimp"></a><a name="p782mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="59%" id="mcps1.1.4.1.2"><p id="p784mcpsimp"><a name="p784mcpsimp"></a><a name="p784mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.3"><p id="p786mcpsimp"><a name="p786mcpsimp"></a><a name="p786mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row788mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p790mcpsimp"><a name="p790mcpsimp"></a><a name="p790mcpsimp"></a>klad</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p792mcpsimp"><a name="p792mcpsimp"></a><a name="p792mcpsimp"></a>KLAD handle.</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p794mcpsimp"><a name="p794mcpsimp"></a><a name="p794mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row795mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.4.1.1 "><p id="p797mcpsimp"><a name="p797mcpsimp"></a><a name="p797mcpsimp"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.4.1.2 "><p id="p799mcpsimp"><a name="p799mcpsimp"></a><a name="p799mcpsimp"></a>Nth level key configuration. Must not be NULL.</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p801mcpsimp"><a name="p801mcpsimp"></a><a name="p801mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table>

[Return Values]

<a name="table803mcpsimp"></a>
<table><thead align="left"><tr id="row808mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p810mcpsimp"><a name="p810mcpsimp"></a><a name="p810mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p812mcpsimp"><a name="p812mcpsimp"></a><a name="p812mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row814mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p816mcpsimp"><a name="p816mcpsimp"></a><a name="p816mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p818mcpsimp"><a name="p818mcpsimp"></a><a name="p818mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row819mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p821mcpsimp"><a name="p821mcpsimp"></a><a name="p821mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p823mcpsimp"><a name="p823mcpsimp"></a><a name="p823mcpsimp"></a>See <a href="#ZH-CN_TOPIC_0000002424349490">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table>

[Requirements]

-   Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
-   Library files: libss\_klad.a, libss\_klad.so

[Notes]

-   The KLAD handle must have been created.
-   Cannot be called multiple times.

[Example]

None.

## ss\_mpi\_klad\_set\_clear\_key<a name="ZH-CN_TOPIC_0000002457868373"></a><a name="ss_mpi_klad_set_clear_key"></a>

[Description]

Configures a plaintext KEY and simultaneously passes the key to KEYSLOT.

[Syntax]

```
td_s32 ss_mpi_klad_set_clear_key(td_handle klad, const ot_klad_clear_key *key);<a name="ss_mpi_klad_set_clear_key"></a>
```

[Parameters]

<a name="table1238mcpsimp"></a>
<table><thead align="left"><tr id="row1244mcpsimp"><th class="cellrowborder" valign="top" width="22%" id="mcps1.1.4.1.1"><p id="p1246mcpsimp"><a name="p1246mcpsimp"></a><a name="p1246mcpsimp"></a>Parameter Name</p>
</th>
<th class="cellrowborder" valign="top" width="60%" id="mcps1.1.4.1.2"><p id="p1248mcpsimp"><a name="p1248mcpsimp"></a><a name="p1248mcpsimp"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="18%" id="mcps1.1.4.1.3"><p id="p1250mcpsimp"><a name="p1250mcpsimp"></a><a name="p1250mcpsimp"></a>Input/Output</p>
</th>
</tr>
</thead>
<tbody><tr id="row1252mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1254mcpsimp"><a name="p1254mcpsimp"></a><a name="p1254mcpsimp"></a>klad</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1256mcpsimp"><a name="p1256mcpsimp"></a><a name="p1256mcpsimp"></a>KLAD handle.</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1258mcpsimp"><a name="p1258mcpsimp"></a><a name="p1258mcpsimp"></a>Input</p>
</td>
</tr>
<tr id="row1259mcpsimp"><td class="cellrowborder" valign="top" width="22%" headers="mcps1.1.4.1.1 "><p id="p1261mcpsimp"><a name="p1261mcpsimp"></a><a name="p1261mcpsimp"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="60%" headers="mcps1.1.4.1.2 "><p id="p1263mcpsimp"><a name="p1263mcpsimp"></a><a name="p1263mcpsimp"></a>Plaintext KEY configuration. Must not be NULL.</p>
</td>
<td class="cellrowborder" valign="top" width="18%" headers="mcps1.1.4.1.3 "><p id="p1265mcpsimp"><a name="p1265mcpsimp"></a><a name="p1265mcpsimp"></a>Input</p>
</td>
</tr>
</tbody>
</table>

[Return Values]

<a name="table1267mcpsimp"></a>
<table><thead align="left"><tr id="row1272mcpsimp"><th class="cellrowborder" valign="top" width="36%" id="mcps1.1.3.1.1"><p id="p1274mcpsimp"><a name="p1274mcpsimp"></a><a name="p1274mcpsimp"></a>Return Value</p>
</th>
<th class="cellrowborder" valign="top" width="64%" id="mcps1.1.3.1.2"><p id="p1276mcpsimp"><a name="p1276mcpsimp"></a><a name="p1276mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1278mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1280mcpsimp"><a name="p1280mcpsimp"></a><a name="p1280mcpsimp"></a>0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1282mcpsimp"><a name="p1282mcpsimp"></a><a name="p1282mcpsimp"></a>Success.</p>
</td>
</tr>
<tr id="row1283mcpsimp"><td class="cellrowborder" valign="top" width="36%" headers="mcps1.1.3.1.1 "><p id="p1285mcpsimp"><a name="p1285mcpsimp"></a><a name="p1285mcpsimp"></a>Non-0</p>
</td>
<td class="cellrowborder" valign="top" width="64%" headers="mcps1.1.3.1.2 "><p id="p1287mcpsimp"><a name="p1287mcpsimp"></a><a name="p1287mcpsimp"></a>See <a href="#ZH-CN_TOPIC_0000002424349490">Error Codes</a>.</p>
</td>
</tr>
</tbody>
</table>

[Requirements]

-   Header files: ot\_common\_klad.h, ss\_mpi\_klad.h
-   Library files: libss\_klad.a, libss\_klad.so

[Notes]

-   The KLAD handle must have been created.
-   Can be called multiple times; the last set attributes take effect.

[Example]

None.

# Data Types
The relevant data types and data structures are defined as follows (for other common data type definitions, refer to ot\_type.h):

-   [ot\_klad\_rootkey\_sel](#ZH-CN_TOPIC_0000002424189634): Defines the KLAD ROOTKEY selection enum.
-   [ot\_klad\_rootkey\_secure](#ZH-CN_TOPIC_0000002457868397): Defines the KLAD ROOTKEY static value enum.
-   [ot\_klad\_rootkey\_attr](#ZH-CN_TOPIC_0000002424189658): Defines the KLAD ROOTKEY attribute structure.
-   [ot\_klad\_type](#ZH-CN_TOPIC_0000002457828233): Defines the KLAD type enum.
-   [ot\_klad\_cfg](#ZH-CN_TOPIC_0000002424189638): Defines the KLAD configuration information structure.
-   [ot\_klad\_crypto\_alg](#ZH-CN_TOPIC_0000002457868381): Defines the algorithm for which the KEY is used in the encryption/decryption engine.
-   [ot\_klad\_attr](#ZH-CN_TOPIC_0000002424349482): Defines the KLAD attribute structure.
-   [ot\_klad\_alg\_type](#ZH-CN_TOPIC_0000002457868401): Defines the KLAD algorithm type enum.
-   [ot\_klad\_level](#ZH-CN_TOPIC_0000002457868385): Defines the KLAD level enum.
-   [ot\_klad\_session\_key](#ZH-CN_TOPIC_0000002424349502): Defines the 1st to (n-1)th level KLAD key information structure.
-   [ot\_klad\_content\_key](#ZH-CN_TOPIC_0000002424189666): Defines the nth level KLAD key information structure.
-   [ot\_klad\_clear\_key](#ZH-CN_TOPIC_0000002457828245): Defines the plaintext key information structure.
-   [OT\_KLAD\_MAX\_KEY\_LEN](#ZH-CN_TOPIC_0000002424189646): Defines the KLAD maximum key length.

## ot\_klad\_rootkey\_sel<a name="ZH-CN_TOPIC_0000002424189634"></a>

[Description]

Defines the KLAD ROOTKEY selection enum.

[Definition]

```
/* klad rootkey select */ 
typedef enum { 
    OT_KLAD_ROOTKEY_SEL_OEM0 = 0x00, 
    OT_KLAD_ROOTKEY_SEL_OEM1, 
    OT_KLAD_ROOTKEY_SEL_OEM2, 
    OT_KLAD_ROOTKEY_SEL_OEM3, 
    OT_KLAD_ROOTKEY_SEL_VENDOR, 
    OT_KLAD_ROOTKEY_SEL_BUTT, 
}  ot_klad_rootkey_sel;<a name="ot_klad_rootkey_sel"></a>
```

[Members]

<a name="table940mcpsimp"></a>
<table><thead align="left"><tr id="row945mcpsimp"><th class="cellrowborder" valign="top" width="45%" id="mcps1.1.3.1.1"><p id="p947mcpsimp"><a name="p947mcpsimp"></a><a name="p947mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.1.3.1.2"><p id="p949mcpsimp"><a name="p949mcpsimp"></a><a name="p949mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row951mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p953mcpsimp"><a name="p953mcpsimp"></a><a name="p953mcpsimp"></a>OT_KLAD_ROOTKEY_SEL_OEM0</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p955mcpsimp"><a name="p955mcpsimp"></a><a name="p955mcpsimp"></a>OTP key management OEM key 0.</p>
</td>
</tr>
<tr id="row956mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p958mcpsimp"><a name="p958mcpsimp"></a><a name="p958mcpsimp"></a>OT_KLAD_ROOTKEY_SEL_OEM1</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p960mcpsimp"><a name="p960mcpsimp"></a><a name="p960mcpsimp"></a>OTP key management OEM key 1.</p>
</td>
</tr>
<tr id="row961mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p963mcpsimp"><a name="p963mcpsimp"></a><a name="p963mcpsimp"></a>OT_KLAD_ROOTKEY_SEL_OEM2</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p965mcpsimp"><a name="p965mcpsimp"></a><a name="p965mcpsimp"></a>OTP key management OEM key 2.</p>
</td>
</tr>
<tr id="row966mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p968mcpsimp"><a name="p968mcpsimp"></a><a name="p968mcpsimp"></a>OT_KLAD_ROOTKEY_SEL_OEM3</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p970mcpsimp"><a name="p970mcpsimp"></a><a name="p970mcpsimp"></a>OTP key management OEM key 3.</p>
</td>
</tr>
<tr id="row971mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p973mcpsimp"><a name="p973mcpsimp"></a><a name="p973mcpsimp"></a>OT_KLAD_ROOTKEY_SEL_VENDOR</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p975mcpsimp"><a name="p975mcpsimp"></a><a name="p975mcpsimp"></a>OTP key management vendor key.</p>
</td>
</tr>
<tr id="row976mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p978mcpsimp"><a name="p978mcpsimp"></a><a name="p978mcpsimp"></a>OT_KLAD_ROOTKEY_SEL_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p980mcpsimp"><a name="p980mcpsimp"></a><a name="p980mcpsimp"></a>Boundary value, used for boundary checking.</p>
</td>
</tr>
</tbody>
</table>

[Notes]

None.

[Related Data Types and Interfaces]

-   [ot\_klad\_rootkey\_attr](#ot_klad_rootkey_attr)
-   [ot\_klad\_cfg](#ot_klad_cfg)
-   [ot\_klad\_attr](#ot_klad_attr)
-   [ss\_mpi\_klad\_set\_attr](#ss_mpi_klad_set_attr)
-   [ss\_mpi\_klad\_get\_attr](#ss_mpi_klad_get_attr)

## ot\_klad\_rootkey\_secure<a name="ZH-CN_TOPIC_0000002457868397"></a>

[Description]

Defines the KLAD ROOTKEY static value enum.

[Definition]

```
typedef enum { 
    OT_KLAD_ROOTKEY_SEC_REE = 0x00,     /* REE key, TEE CPU can select ree key */ 
    OT_KLAD_ROOTKEY_SEC_TEE,           /* TEE key, REE CPU can't select tee key */ 
    OT_KLAD_ROOTKEY_SEC_BUTT, 
} ot_klad_rootkey_secure;<a name="ot_klad_rootkey_secure"></a>
```

[Members]

<a name="table537mcpsimp"></a>
<table><thead align="left"><tr id="row542mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p544mcpsimp"><a name="p544mcpsimp"></a><a name="p544mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p546mcpsimp"><a name="p546mcpsimp"></a><a name="p546mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row548mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p550mcpsimp"><a name="p550mcpsimp"></a><a name="p550mcpsimp"></a>OT_KLAD_ROOTKEY_SEC_REE</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p552mcpsimp"><a name="p552mcpsimp"></a><a name="p552mcpsimp"></a>Select REE key static value.</p>
</td>
</tr>
<tr id="row553mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p555mcpsimp"><a name="p555mcpsimp"></a><a name="p555mcpsimp"></a>OT_KLAD_ROOTKEY_SEC_TEE</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p557mcpsimp"><a name="p557mcpsimp"></a><a name="p557mcpsimp"></a>Select TEE key static value.</p>
</td>
</tr>
<tr id="row558mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p560mcpsimp"><a name="p560mcpsimp"></a><a name="p560mcpsimp"></a>OT_KLAD_ROOTKEY_SEC_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p562mcpsimp"><a name="p562mcpsimp"></a><a name="p562mcpsimp"></a>Boundary value, used for boundary checking.</p>
</td>
</tr>
</tbody>
</table>

[Notes]

-   Non-secure CPU cannot select the TEE key static value.
-   Secure CPU can select the REE key static value.

[Related Data Types and Interfaces]

-   [ot\_klad\_rootkey\_attr](#ot_klad_rootkey_attr)
-   [ot\_klad\_cfg](#ot_klad_cfg)
-   [ot\_klad\_attr](#ot_klad_attr)
-   [ss\_mpi\_klad\_set\_attr](#ss_mpi_klad_set_attr)
-   [ss\_mpi\_klad\_get\_attr](#ss_mpi_klad_get_attr)

## ot\_klad\_rootkey\_attr<a name="ZH-CN_TOPIC_0000002424189658"></a><a name="ot_klad_rootkey_attr"></a>

[Description]

Defines the KLAD ROOTKEY attribute structure.

[Definition]

```
/* only OT_KLAD_TYPE_COMMON is valid */
    typedef struct {
    td_u32 owner_id;                 /* Derivative material, used for mcipher */
    ot_klad_rootkey_sel   key_sel;        /* common klad route select rootkey */
    ot_klad_rootkey_secure    key_secure;  /* Static value select: for ree key or for tee key */
} ot_klad_rootkey_attr;<a name="ot_klad_rootkey_attr"></a>
```

[Members]

<a name="table848mcpsimp"></a>
<table><thead align="left"><tr id="row853mcpsimp"><th class="cellrowborder" valign="top" width="43%" id="mcps1.1.3.1.1"><p id="p855mcpsimp"><a name="p855mcpsimp"></a><a name="p855mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.1.3.1.2"><p id="p857mcpsimp"><a name="p857mcpsimp"></a><a name="p857mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row859mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p861mcpsimp"><a name="p861mcpsimp"></a><a name="p861mcpsimp"></a>owner_id</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p863mcpsimp"><a name="p863mcpsimp"></a><a name="p863mcpsimp"></a>Derivation material, used for MCIPHER.</p>
</td>
</tr>
<tr id="row864mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p866mcpsimp"><a name="p866mcpsimp"></a><a name="p866mcpsimp"></a>key_sel</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p868mcpsimp"><a name="p868mcpsimp"></a><a name="p868mcpsimp"></a>COMMON KLAD ROOTKEY selection.</p>
</td>
</tr>
<tr id="row869mcpsimp"><td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.1 "><p id="p871mcpsimp"><a name="p871mcpsimp"></a><a name="p871mcpsimp"></a>key_secure</p>
</td>
<td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.2 "><p id="p873mcpsimp"><a name="p873mcpsimp"></a><a name="p873mcpsimp"></a>COMMON KLAD ROOTKEY static value selection.</p>
</td>
</tr>
</tbody>
</table>

[Notes]

Only valid when the KLAD type is OT\_KLAD\_TYPE\_COMMON.

[Related Data Types and Interfaces]

-   [ot\_klad\_cfg](#ot_klad_cfg)
-   [ot\_klad\_attr](#ot_klad_attr)
-   [ss\_mpi\_klad\_set\_attr](#ss_mpi_klad_set_attr)
-   [ss\_mpi\_klad\_get\_attr](#ss_mpi_klad_get_attr)

## ot\_klad\_type<a name="ZH-CN_TOPIC_0000002457828233"></a>

[Description]

Defines the KLAD type enum.

[Definition]

```
/* klad route select */ 
typedef enum { 
    OT_KLAD_TYPE_CLEARCW,            /* Used for clear key  */ 
    OT_KLAD_TYPE_COMMON,            /* Used for root key */ 
    OT_KLAD_TYPE_BUTT, 
} ot_klad_type;<a name="ot_klad_type"></a>
```

[Members]

<a name="table1193mcpsimp"></a>
<table><thead align="left"><tr id="row1198mcpsimp"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="p1200mcpsimp"><a name="p1200mcpsimp"></a><a name="p1200mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="p1202mcpsimp"><a name="p1202mcpsimp"></a><a name="p1202mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1204mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1206mcpsimp"><a name="p1206mcpsimp"></a><a name="p1206mcpsimp"></a>OT_KLAD_TYPE_CLEARCW</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1208mcpsimp"><a name="p1208mcpsimp"></a><a name="p1208mcpsimp"></a>Plaintext KLAD, used for plaintext KEY.</p>
</td>
</tr>
<tr id="row1209mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1211mcpsimp"><a name="p1211mcpsimp"></a><a name="p1211mcpsimp"></a>OT_KLAD_TYPE_COMMON</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1213mcpsimp"><a name="p1213mcpsimp"></a><a name="p1213mcpsimp"></a>Common KLAD, used for ROOTKEY.</p>
</td>
</tr>
<tr id="row1214mcpsimp"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="p1216mcpsimp"><a name="p1216mcpsimp"></a><a name="p1216mcpsimp"></a>OT_KLAD_TYPE_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="p1218mcpsimp"><a name="p1218mcpsimp"></a><a name="p1218mcpsimp"></a>Boundary value, used for boundary checking.</p>
</td>
</tr>
</tbody>
</table>

[Notes]

None.

[Related Data Types and Interfaces]

-   [ot\_klad\_cfg](#ot_klad_cfg)
-   [ot\_klad\_attr](#ot_klad_attr)
-   [ss\_mpi\_klad\_set\_attr](#ss_mpi_klad_set_attr)
-   [ss\_mpi\_klad\_get\_attr](#ss_mpi_klad_get_attr)

## ot\_klad\_cfg<a name="ZH-CN_TOPIC_0000002424189638"></a><a name="ot_klad_cfg"></a>

[Description]

Defines the KLAD configuration information structure.

[Definition]

```
/* klad config */
    typedef struct {
    ot_klad_type klad_type;             /* klad route select: common/clear */
    ot_klad_rootkey_attr rootkey_attr;    /* rootkey attr, OT_KLAD_TYPE_COMMON is valid */
} ot_klad_cfg;
```

[Members]

<a name="table1487mcpsimp"></a>
<table><thead align="left"><tr id="row1492mcpsimp"><th class="cellrowborder" valign="top" width="44%" id="mcps1.1.3.1.1"><p id="p1494mcpsimp"><a name="p1494mcpsimp"></a><a name="p1494mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="56.00000000000001%" id="mcps1.1.3.1.2"><p id="p1496mcpsimp"><a name="p1496mcpsimp"></a><a name="p1496mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1498mcpsimp"><td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.3.1.1 "><p id="p1500mcpsimp"><a name="p1500mcpsimp"></a><a name="p1500mcpsimp"></a>klad_type</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p1502mcpsimp"><a name="p1502mcpsimp"></a><a name="p1502mcpsimp"></a>KLAD type.</p>
</td>
</tr>
<tr id="row1503mcpsimp"><td class="cellrowborder" valign="top" width="44%" headers="mcps1.1.3.1.1 "><p id="p1505mcpsimp"><a name="p1505mcpsimp"></a><a name="p1505mcpsimp"></a>rootkey_attr</p>
</td>
<td class="cellrowborder" valign="top" width="56.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p1507mcpsimp"><a name="p1507mcpsimp"></a><a name="p1507mcpsimp"></a>ROOTKEY attribute configuration.</p>
</td>
</tr>
</tbody>
</table>

[Notes]

rootkey\_attr is only valid when the KLAD type is OT\_KLAD\_TYPE\_COMMON.

[Related Data Types and Interfaces]

-   [ot\_klad\_attr](#ot_klad_attr)
-   [ss\_mpi\_klad\_set\_attr](#ss_mpi_klad_set_attr)
-   [ss\_mpi\_klad\_get\_attr](#ss_mpi_klad_get_attr)

## ot\_klad\_crypto\_alg<a name="ZH-CN_TOPIC_0000002457868381"></a>

[Description]

Defines the algorithm for which the KEY is used in the encryption/decryption engine.

[Definition]

```
/* The key can be used for which algorithm of the crypto engine. */ 
typedef enum { 
    OT_KLAD_CRYPTO_ALG_AES = 0, 
    OT_KLAD_CRYPTO_ALG_SM4, 
    OT_KLAD_CRYPTO_ALG_BUTT, 
} ot_klad_crypto_alg;<a name="ot_klad_crypto_alg"></a>
```

[Members]

<a name="table1001mcpsimp"></a>
<table><thead align="left"><tr id="row1006mcpsimp"><th class="cellrowborder" valign="top" width="45%" id="mcps1.1.3.1.1"><p id="p1008mcpsimp"><a name="p1008mcpsimp"></a><a name="p1008mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="55.00000000000001%" id="mcps1.1.3.1.2"><p id="p1010mcpsimp"><a name="p1010mcpsimp"></a><a name="p1010mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1012mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p1014mcpsimp"><a name="p1014mcpsimp"></a><a name="p1014mcpsimp"></a>OT_KLAD_CRYPTO_ALG_AES</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p1016mcpsimp"><a name="p1016mcpsimp"></a><a name="p1016mcpsimp"></a>Used for AES algorithm.</p>
</td>
</tr>
<tr id="row1017mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p1019mcpsimp"><a name="p1019mcpsimp"></a><a name="p1019mcpsimp"></a>OT_KLAD_CRYPTO_ALG_SM4</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p1021mcpsimp"><a name="p1021mcpsimp"></a><a name="p1021mcpsimp"></a>Used for SM4 algorithm.</p>
</td>
</tr>
<tr id="row1022mcpsimp"><td class="cellrowborder" valign="top" width="45%" headers="mcps1.1.3.1.1 "><p id="p1024mcpsimp"><a name="p1024mcpsimp"></a><a name="p1024mcpsimp"></a>OT_KLAD_CRYPTO_ALG_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="55.00000000000001%" headers="mcps1.1.3.1.2 "><p id="p1026mcpsimp"><a name="p1026mcpsimp"></a><a name="p1026mcpsimp"></a>Boundary value, used for boundary checking.</p>
</td>
</tr>
</tbody>
</table>

[Notes]

Hi3403V100 and SS626V100 do not support SM4.

[Related Data Types and Interfaces]

-   [ss\_mpi\_klad\_set\_content\_key](#ss_mpi_klad_set_content_key)
-   [ss\_mpi\_klad\_set\_clear\_key](#ss_mpi_klad_set_clear_key)

## ot\_klad\_attr<a name="ZH-CN_TOPIC_0000002424349482"></a><a name="ot_klad_attr"></a>

[Description]

Defines the KLAD attribute structure.

[Definition]

```
/* klad attribute */
    typedef struct {
    ot_klad_cfg klad_cfg;
} ot_klad_attr;<a name="ot_klad_attr"></a>
```

[Members]

<a name="table1163mcpsimp"></a>
<table><thead align="left"><tr id="row1168mcpsimp"><th class="cellrowborder" valign="top" width="59%" id="mcps1.1.3.1.1"><p id="p1170mcpsimp"><a name="p1170mcpsimp"></a><a name="p1170mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="41%" id="mcps1.1.3.1.2"><p id="p1172mcpsimp"><a name="p1172mcpsimp"></a><a name="p1172mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1174mcpsimp"><td class="cellrowborder" valign="top" width="59%" headers="mcps1.1.3.1.1 "><p id="p1176mcpsimp"><a name="p1176mcpsimp"></a><a name="p1176mcpsimp"></a>klad_cfg</p>
</td>
<td class="cellrowborder" valign="top" width="41%" headers="mcps1.1.3.1.2 "><p id="p1178mcpsimp"><a name="p1178mcpsimp"></a><a name="p1178mcpsimp"></a>KLAD configuration information.</p>
</td>
</tr>
</tbody>
</table>

[Notes]

None.

[Related Data Types and Interfaces]

-   [ss\_mpi\_klad\_set\_attr](#ss_mpi_klad_set_attr)
-   [ss\_mpi\_klad\_get\_attr](#ss_mpi_klad_get_attr)

## ot\_klad\_alg\_type<a name="ZH-CN_TOPIC_0000002457868401"></a>

[Description]

Defines the KLAD algorithm type enum.

[Definition]

```
/* klad algorithm */ 
typedef enum { 
   OT_KLAD_ALG_TYPE_AES = 0, 
   OT_KLAD_ALG_TYPE_SM4, 
   OT_KLAD_ALG_TYPE_BUTT, 
} ot_klad_alg_type;<a name="ot_klad_alg_type"></a>
```

[Members]

<a name="table1760mcpsimp"></a>
<table><thead align="left"><tr id="row1765mcpsimp"><th class="cellrowborder" valign="top" width="63%" id="mcps1.1.3.1.1"><p id="p1767mcpsimp"><a name="p1767mcpsimp"></a><a name="p1767mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="37%" id="mcps1.1.3.1.2"><p id="p1769mcpsimp"><a name="p1769mcpsimp"></a><a name="p1769mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1771mcpsimp"><td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.1 "><p id="p1773mcpsimp"><a name="p1773mcpsimp"></a><a name="p1773mcpsimp"></a>OT_KLAD_ALG_TYPE_AES</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.2 "><p id="p1775mcpsimp"><a name="p1775mcpsimp"></a><a name="p1775mcpsimp"></a>KLAD uses AES algorithm.</p>
</td>
</tr>
<tr id="row1776mcpsimp"><td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.1 "><p id="p1778mcpsimp"><a name="p1778mcpsimp"></a><a name="p1778mcpsimp"></a>OT_KLAD_ALG_TYPE_SM4</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.2 "><p id="p1780mcpsimp"><a name="p1780mcpsimp"></a><a name="p1780mcpsimp"></a>KLAD uses SM4 algorithm.</p>
</td>
</tr>
<tr id="row1781mcpsimp"><td class="cellrowborder" valign="top" width="63%" headers="mcps1.1.3.1.1 "><p id="p1783mcpsimp"><a name="p1783mcpsimp"></a><a name="p1783mcpsimp"></a>OT_KLAD_ALG_TYPE_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="37%" headers="mcps1.1.3.1.2 "><p id="p1785mcpsimp"><a name="p1785mcpsimp"></a><a name="p1785mcpsimp"></a>Boundary value, used for boundary checking.</p>
</td>
</tr>
</tbody>
</table>

[Notes]

Hi3403V100 and SS626V100 do not support SM4.

[Related Data Types and Interfaces]

-   [ot\_klad\_session\_key](#ot_klad_session_key)
-   [ot\_klad\_content\_key](#ot_klad_content_key)
-   [ss\_mpi\_klad\_set\_session\_key](#ss_mpi_klad_set_session_key)
-   [ss\_mpi\_klad\_set\_content\_key](#ss_mpi_klad_set_content_key)

## ot\_klad\_level<a name="ZH-CN_TOPIC_0000002457868385"></a>

[Description]

Defines the KLAD level enum.

[Definition]

```
/* klad level */ 
typedef enum { 
    OT_KLAD_LEVEL1 = 0, 
    OT_KLAD_LEVEL2, 
    OT_KLAD_LEVEL3, 
    OT_KLAD_LEVEL_BUTT, 
} ot_klad_level;<a name="ot_klad_level"></a>
```

[Members]

<a name="table895mcpsimp"></a>
<table><thead align="left"><tr id="row900mcpsimp"><th class="cellrowborder" valign="top" width="56.99999999999999%" id="mcps1.1.3.1.1"><p id="p902mcpsimp"><a name="p902mcpsimp"></a><a name="p902mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="43%" id="mcps1.1.3.1.2"><p id="p904mcpsimp"><a name="p904mcpsimp"></a><a name="p904mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row906mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.1 "><p id="p908mcpsimp"><a name="p908mcpsimp"></a><a name="p908mcpsimp"></a>OT_KLAD_LEVEL1</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.2 "><p id="p910mcpsimp"><a name="p910mcpsimp"></a><a name="p910mcpsimp"></a>KLAD level 1.</p>
</td>
</tr>
<tr id="row911mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.1 "><p id="p913mcpsimp"><a name="p913mcpsimp"></a><a name="p913mcpsimp"></a>OT_KLAD_LEVEL2</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.2 "><p id="p915mcpsimp"><a name="p915mcpsimp"></a><a name="p915mcpsimp"></a>KLAD level 2.</p>
</td>
</tr>
<tr id="row916mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.1 "><p id="p918mcpsimp"><a name="p918mcpsimp"></a><a name="p918mcpsimp"></a>OT_KLAD_LEVEL3</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.2 "><p id="p920mcpsimp"><a name="p920mcpsimp"></a><a name="p920mcpsimp"></a>KLAD level 3.</p>
</td>
</tr>
<tr id="row921mcpsimp"><td class="cellrowborder" valign="top" width="56.99999999999999%" headers="mcps1.1.3.1.1 "><p id="p923mcpsimp"><a name="p923mcpsimp"></a><a name="p923mcpsimp"></a>OT_KLAD_LEVEL_BUTT</p>
</td>
<td class="cellrowborder" valign="top" width="43%" headers="mcps1.1.3.1.2 "><p id="p925mcpsimp"><a name="p925mcpsimp"></a><a name="p925mcpsimp"></a>Boundary value, used for boundary checking.</p>
</td>
</tr>
</tbody>
</table>

[Notes]

Hi3403V100 and SS626V100 support 2-level KLAD.

[Related Data Types and Interfaces]

-   [ot\_klad\_session\_key](#ot_klad_session_key)
-   [ss\_mpi\_klad\_set\_session\_key](#ss_mpi_klad_set_session_key)

## ot\_klad\_session\_key<a name="ZH-CN_TOPIC_0000002424349502"></a><a name="ot_klad_session_key"></a>

[Description]

Defines the 1st to (n-1)th level KLAD key information structure.

[Definition]

```
/* session key: set 1~n-1 stage common route klad */
    typedef struct {
    ot_klad_session_key level;                  /* klad level */
    ot_klad_alg_type alg;                /* klad algorithm */
    td_u32 key_size;                    /* klad key size */
    td_u8 key[OT_KLAD_MAX_KEY_LEN];  /* klad key */
} ot_klad_session_key;<a name="ot_klad_session_key"></a>
```

[Members]

<a name="table702mcpsimp"></a>
<table><thead align="left"><tr id="row707mcpsimp"><th class="cellrowborder" valign="top" width="52%" id="mcps1.1.3.1.1"><p id="p709mcpsimp"><a name="p709mcpsimp"></a><a name="p709mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="48%" id="mcps1.1.3.1.2"><p id="p711mcpsimp"><a name="p711mcpsimp"></a><a name="p711mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row713mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p id="p715mcpsimp"><a name="p715mcpsimp"></a><a name="p715mcpsimp"></a>level</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p717mcpsimp"><a name="p717mcpsimp"></a><a name="p717mcpsimp"></a>Currently configured KLAD level.</p>
</td>
</tr>
<tr id="row718mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p id="p720mcpsimp"><a name="p720mcpsimp"></a><a name="p720mcpsimp"></a>alg</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p722mcpsimp"><a name="p722mcpsimp"></a><a name="p722mcpsimp"></a>Algorithm used by KLAD.</p>
</td>
</tr>
<tr id="row723mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p id="p725mcpsimp"><a name="p725mcpsimp"></a><a name="p725mcpsimp"></a>key_size</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p727mcpsimp"><a name="p727mcpsimp"></a><a name="p727mcpsimp"></a>KLAD decryption key length (unit: byte).</p>
</td>
</tr>
<tr id="row728mcpsimp"><td class="cellrowborder" valign="top" width="52%" headers="mcps1.1.3.1.1 "><p id="p730mcpsimp"><a name="p730mcpsimp"></a><a name="p730mcpsimp"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="48%" headers="mcps1.1.3.1.2 "><p id="p732mcpsimp"><a name="p732mcpsimp"></a><a name="p732mcpsimp"></a>KLAD decryption key.</p>
</td>
</tr>
</tbody>
</table>

[Notes]

-   key\_size only supports 128 bits, i.e., 16 bytes.
-   For Hi3403V100 and SS626V100, level can only be configured as OT\_KLAD\_LEVEL1.

[Related Data Types and Interfaces]

[ss\_mpi\_klad\_set\_session\_key](#ss_mpi_klad_set_session_key)

## ot\_klad\_content\_key<a name="ZH-CN_TOPIC_0000002424189666"></a><a name="ot_klad_content_key"></a>

[Description]

Defines the last level KLAD key information structure.

[Definition]

```
/* content key: set n stage common route klad */
typedef struct {
    ot_klad_alg_type alg;                /* klad algorithm */
    ot_klad_crypto_alg crypto_alg;        /* allowed target engine algorithm. */
    td_u32 key_size;                     /* klad key size */
    td_u8 key[OT_KLAD_MAX_KEY_LEN];  /* klad key */
} ot_klad_content_key;<a name="ot_klad_content_key"></a>
```

[Members]

<a name="table225mcpsimp"></a>
<table><thead align="left"><tr id="row230mcpsimp"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.1.3.1.1"><p id="p232mcpsimp"><a name="p232mcpsimp"></a><a name="p232mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="72%" id="mcps1.1.3.1.2"><p id="p234mcpsimp"><a name="p234mcpsimp"></a><a name="p234mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row236mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.3.1.1 "><p id="p238mcpsimp"><a name="p238mcpsimp"></a><a name="p238mcpsimp"></a>alg</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.1.3.1.2 "><p id="p240mcpsimp"><a name="p240mcpsimp"></a><a name="p240mcpsimp"></a>Algorithm used by the current KLAD.</p>
</td>
</tr>
<tr id="row241mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.3.1.1 "><p id="p243mcpsimp"><a name="p243mcpsimp"></a><a name="p243mcpsimp"></a>crypto_alg</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.1.3.1.2 "><p id="p245mcpsimp"><a name="p245mcpsimp"></a><a name="p245mcpsimp"></a>Algorithm allowed by the encryption/decryption engine.</p>
</td>
</tr>
<tr id="row246mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.3.1.1 "><p id="p248mcpsimp"><a name="p248mcpsimp"></a><a name="p248mcpsimp"></a>key_size</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.1.3.1.2 "><p id="p250mcpsimp"><a name="p250mcpsimp"></a><a name="p250mcpsimp"></a>KLAD decryption key length (unit: byte), supports 128/256 bits.</p>
</td>
</tr>
<tr id="row251mcpsimp"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.1.3.1.1 "><p id="p253mcpsimp"><a name="p253mcpsimp"></a><a name="p253mcpsimp"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="72%" headers="mcps1.1.3.1.2 "><p id="p255mcpsimp"><a name="p255mcpsimp"></a><a name="p255mcpsimp"></a>KLAD decryption key.</p>
</td>
</tr>
</tbody>
</table>

[Notes]

None.

[Related Data Types and Interfaces]

[ss\_mpi\_klad\_set\_content\_key](#ss_mpi_klad_set_content_key)

## ot\_klad\_clear\_key<a name="ZH-CN_TOPIC_0000002457828245"></a><a name="ot_klad_clear_key"></a>

[Description]

Defines the plaintext key information structure.

[Definition]

```
/* clear key: set clear route klad */
typedef struct {
    ot_klad_crypto_alg crypto_alg;        /* allowed target engine algorithm. */
    td_u32 key_size;                    /* klad key size */
    td_u8 key[OT_KLAD_MAX_KEY_LEN];  /* klad key */
} ot_klad_clear_key;<a name="ot_klad_clear_key"></a>
```

[Members]

<a name="table1122mcpsimp"></a>
<table><thead align="left"><tr id="row1127mcpsimp"><th class="cellrowborder" valign="top" width="23%" id="mcps1.1.3.1.1"><p id="p1129mcpsimp"><a name="p1129mcpsimp"></a><a name="p1129mcpsimp"></a>Member Name</p>
</th>
<th class="cellrowborder" valign="top" width="77%" id="mcps1.1.3.1.2"><p id="p1131mcpsimp"><a name="p1131mcpsimp"></a><a name="p1131mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1133mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p id="p1135mcpsimp"><a name="p1135mcpsimp"></a><a name="p1135mcpsimp"></a>crypto_alg</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p1137mcpsimp"><a name="p1137mcpsimp"></a><a name="p1137mcpsimp"></a>Algorithm allowed by the encryption/decryption engine.</p>
</td>
</tr>
<tr id="row1138mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p id="p1140mcpsimp"><a name="p1140mcpsimp"></a><a name="p1140mcpsimp"></a>key_size</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p1142mcpsimp"><a name="p1142mcpsimp"></a><a name="p1142mcpsimp"></a>KLAD decryption key length (unit: byte), supports 128/192/256 bits.</p>
</td>
</tr>
<tr id="row1143mcpsimp"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.1.3.1.1 "><p id="p1145mcpsimp"><a name="p1145mcpsimp"></a><a name="p1145mcpsimp"></a>key</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.1.3.1.2 "><p id="p1147mcpsimp"><a name="p1147mcpsimp"></a><a name="p1147mcpsimp"></a>KLAD decryption key.</p>
</td>
</tr>
</tbody>
</table>

[Notes]

None.

[Related Data Types and Interfaces]

[ss\_mpi\_klad\_set\_clear\_key](#ss_mpi_klad_set_clear_key)

## OT\_KLAD\_MAX\_KEY\_LEN<a name="ZH-CN_TOPIC_0000002424189646"></a>

[Description]

Defines the KLAD maximum key length.

[Definition]

```
#define OT_KLAD_MAX_KEY_LEN     32
```

[Notes]

None.

[Related Data Types and Interfaces]

-   [ot\_klad\_session\_key](#ot_klad_session_key)
-   [ot\_klad\_content\_key](#ot_klad_content_key)
-   [ot\_klad\_clear\_key](#ot_klad_clear_key)
-   [ss\_mpi\_klad\_set\_session\_key](#ss_mpi_klad_set_session_key)
-   [ss\_mpi\_klad\_set\_content\_key](#ss_mpi_klad_set_content_key)
-   [ss\_mpi\_klad\_set\_clear\_key](#ss_mpi_klad_set_clear_key)

# Error Codes
The error codes provided by KLAD are as follows.

**Table 1**  KLAD module error codes

<a name="_Ref448994233"></a>
<table><thead align="left"><tr id="row1315mcpsimp"><th class="cellrowborder" valign="top" width="18.81%" id="mcps1.2.4.1.1"><p id="p1317mcpsimp"><a name="p1317mcpsimp"></a><a name="p1317mcpsimp"></a>Error Code</p>
</th>
<th class="cellrowborder" valign="top" width="52.480000000000004%" id="mcps1.2.4.1.2"><p id="p1319mcpsimp"><a name="p1319mcpsimp"></a><a name="p1319mcpsimp"></a>Macro Definition</p>
</th>
<th class="cellrowborder" valign="top" width="28.71%" id="mcps1.2.4.1.3"><p id="p1321mcpsimp"><a name="p1321mcpsimp"></a><a name="p1321mcpsimp"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1323mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p1325mcpsimp"><a name="p1325mcpsimp"></a><a name="p1325mcpsimp"></a>0x805d0000</p>
</td>
<td class="cellrowborder" valign="top" width="52.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p1327mcpsimp"><a name="p1327mcpsimp"></a><a name="p1327mcpsimp"></a>OT_ERR_KLAD_NOT_INIT</p>
</td>
<td class="cellrowborder" valign="top" width="28.71%" headers="mcps1.2.4.1.3 "><p id="p1329mcpsimp"><a name="p1329mcpsimp"></a><a name="p1329mcpsimp"></a>Device not initialized</p>
</td>
</tr>
<tr id="row1330mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p1332mcpsimp"><a name="p1332mcpsimp"></a><a name="p1332mcpsimp"></a>0x805d0001</p>
</td>
<td class="cellrowborder" valign="top" width="52.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p1334mcpsimp"><a name="p1334mcpsimp"></a><a name="p1334mcpsimp"></a>OT_ERR_KLAD_FAILED_INIT</p>
</td>
<td class="cellrowborder" valign="top" width="28.71%" headers="mcps1.2.4.1.3 "><p id="p1336mcpsimp"><a name="p1336mcpsimp"></a><a name="p1336mcpsimp"></a>Device initialization failed</p>
</td>
</tr>
<tr id="row1337mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p1339mcpsimp"><a name="p1339mcpsimp"></a><a name="p1339mcpsimp"></a>0x805d0002</p>
</td>
<td class="cellrowborder" valign="top" width="52.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p1341mcpsimp"><a name="p1341mcpsimp"></a><a name="p1341mcpsimp"></a>OT_ERR_KLAD_NULL_PTR</p>
</td>
<td class="cellrowborder" valign="top" width="28.71%" headers="mcps1.2.4.1.3 "><p id="p1343mcpsimp"><a name="p1343mcpsimp"></a><a name="p1343mcpsimp"></a>NULL pointer in parameters</p>
</td>
</tr>
<tr id="row1344mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p1346mcpsimp"><a name="p1346mcpsimp"></a><a name="p1346mcpsimp"></a>0x805d0003</p>
</td>
<td class="cellrowborder" valign="top" width="52.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p1348mcpsimp"><a name="p1348mcpsimp"></a><a name="p1348mcpsimp"></a>OT_ERR_KLAD_INVALID_PARAM</p>
</td>
<td class="cellrowborder" valign="top" width="28.71%" headers="mcps1.2.4.1.3 "><p id="p1350mcpsimp"><a name="p1350mcpsimp"></a><a name="p1350mcpsimp"></a>Invalid parameter</p>
</td>
</tr>
<tr id="row1351mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p1353mcpsimp"><a name="p1353mcpsimp"></a><a name="p1353mcpsimp"></a>0x805d0004</p>
</td>
<td class="cellrowborder" valign="top" width="52.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p1355mcpsimp"><a name="p1355mcpsimp"></a><a name="p1355mcpsimp"></a>OT_ERR_KLAD_FAILED_CREATE_DEV</p>
</td>
<td class="cellrowborder" valign="top" width="28.71%" headers="mcps1.2.4.1.3 "><p id="p1357mcpsimp"><a name="p1357mcpsimp"></a><a name="p1357mcpsimp"></a>Failed to create device</p>
</td>
</tr>
<tr id="row1358mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p1360mcpsimp"><a name="p1360mcpsimp"></a><a name="p1360mcpsimp"></a>0x805d0005</p>
</td>
<td class="cellrowborder" valign="top" width="52.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p1362mcpsimp"><a name="p1362mcpsimp"></a><a name="p1362mcpsimp"></a>OT_ERR_KLAD_DEVICE_BUSY</p>
</td>
<td class="cellrowborder" valign="top" width="28.71%" headers="mcps1.2.4.1.3 "><p id="p1364mcpsimp"><a name="p1364mcpsimp"></a><a name="p1364mcpsimp"></a>Device busy</p>
</td>
</tr>
<tr id="row1365mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p1367mcpsimp"><a name="p1367mcpsimp"></a><a name="p1367mcpsimp"></a>0x805d0006</p>
</td>
<td class="cellrowborder" valign="top" width="52.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p1369mcpsimp"><a name="p1369mcpsimp"></a><a name="p1369mcpsimp"></a>OT_ERR_KLAD_FAILED_SEC_FUNC</p>
</td>
<td class="cellrowborder" valign="top" width="28.71%" headers="mcps1.2.4.1.3 "><p id="p1371mcpsimp"><a name="p1371mcpsimp"></a><a name="p1371mcpsimp"></a>Security function call failed</p>
</td>
</tr>
<tr id="row1372mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p1374mcpsimp"><a name="p1374mcpsimp"></a><a name="p1374mcpsimp"></a>0x805d0007</p>
</td>
<td class="cellrowborder" valign="top" width="52.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p1376mcpsimp"><a name="p1376mcpsimp"></a><a name="p1376mcpsimp"></a>OT_ERR_KLAD_TIMEOUT</p>
</td>
<td class="cellrowborder" valign="top" width="28.71%" headers="mcps1.2.4.1.3 "><p id="p1378mcpsimp"><a name="p1378mcpsimp"></a><a name="p1378mcpsimp"></a>Operation timeout</p>
</td>
</tr>
<tr id="row1379mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p1381mcpsimp"><a name="p1381mcpsimp"></a><a name="p1381mcpsimp"></a>0x805d0008</p>
</td>
<td class="cellrowborder" valign="top" width="52.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p1383mcpsimp"><a name="p1383mcpsimp"></a><a name="p1383mcpsimp"></a>OT_ERR_KLAD_FAILED_MEM</p>
</td>
<td class="cellrowborder" valign="top" width="28.71%" headers="mcps1.2.4.1.3 "><p id="p1385mcpsimp"><a name="p1385mcpsimp"></a><a name="p1385mcpsimp"></a>Memory allocation failed</p>
</td>
</tr>
<tr id="row1386mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p1388mcpsimp"><a name="p1388mcpsimp"></a><a name="p1388mcpsimp"></a>0x805d0009</p>
</td>
<td class="cellrowborder" valign="top" width="52.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p1390mcpsimp"><a name="p1390mcpsimp"></a><a name="p1390mcpsimp"></a>OT_ERR_KLAD_FAILED_OPERATE</p>
</td>
<td class="cellrowborder" valign="top" width="28.71%" headers="mcps1.2.4.1.3 "><p id="p1392mcpsimp"><a name="p1392mcpsimp"></a><a name="p1392mcpsimp"></a>KLAD operation failed</p>
</td>
</tr>
<tr id="row1393mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p1395mcpsimp"><a name="p1395mcpsimp"></a><a name="p1395mcpsimp"></a>0x805d000a</p>
</td>
<td class="cellrowborder" valign="top" width="52.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p1397mcpsimp"><a name="p1397mcpsimp"></a><a name="p1397mcpsimp"></a>OT_ERR_KLAD_INVALID_OWNER</p>
</td>
<td class="cellrowborder" valign="top" width="28.71%" headers="mcps1.2.4.1.3 "><p id="p1399mcpsimp"><a name="p1399mcpsimp"></a><a name="p1399mcpsimp"></a>Invalid KLAD owner</p>
</td>
</tr>
<tr id="row1400mcpsimp"><td class="cellrowborder" valign="top" width="18.81%" headers="mcps1.2.4.1.1 "><p id="p1402mcpsimp"><a name="p1402mcpsimp"></a><a name="p1402mcpsimp"></a>0x805d000b</p>
</td>
<td class="cellrowborder" valign="top" width="52.480000000000004%" headers="mcps1.2.4.1.2 "><p id="p1404mcpsimp"><a name="p1404mcpsimp"></a><a name="p1404mcpsimp"></a>OT_ERR_KLAD_INVALID_HANDLE</p>
</td>
<td class="cellrowborder" valign="top" width="28.71%" headers="mcps1.2.4.1.3 "><p id="p1406mcpsimp"><a name="p1406mcpsimp"></a><a name="p1406mcpsimp"></a>Invalid KLAD Handle</p>
</td>
</tr>
</tbody>
</table>

# Acronyms and Abbreviations
<a name="table1046mcpsimp"></a>
<table><tbody><tr id="row1052mcpsimp"><td class="cellrowborder" colspan="3" valign="top"><p id="p1054mcpsimp"><a name="p1054mcpsimp"></a><a name="p1054mcpsimp"></a><strong id="b1055mcpsimp"><a name="b1055mcpsimp"></a><a name="b1055mcpsimp"></a>K</strong></p>
</td>
</tr>
<tr id="row1056mcpsimp"><td class="cellrowborder" valign="top" width="12%"><p id="p1058mcpsimp"><a name="p1058mcpsimp"></a><a name="p1058mcpsimp"></a>KDF</p>
</td>
<td class="cellrowborder" valign="top" width="37%"><p id="p1060mcpsimp"><a name="p1060mcpsimp"></a><a name="p1060mcpsimp"></a>Key Derivation Function</p>
</td>
<td class="cellrowborder" valign="top" width="51%"><p id="p1062mcpsimp"><a name="p1062mcpsimp"></a><a name="p1062mcpsimp"></a>Key Derivation Function</p>
</td>
</tr>
<tr id="row1063mcpsimp"><td class="cellrowborder" valign="top" width="12%"><p id="p1065mcpsimp"><a name="p1065mcpsimp"></a><a name="p1065mcpsimp"></a>KLAD</p>
</td>
<td class="cellrowborder" valign="top" width="37%"><p id="p1067mcpsimp"><a name="p1067mcpsimp"></a><a name="p1067mcpsimp"></a>Key Ladder</p>
</td>
<td class="cellrowborder" valign="top" width="51%"><p id="p1069mcpsimp"><a name="p1069mcpsimp"></a><a name="p1069mcpsimp"></a>Key Ladder</p>
</td>
</tr>
<tr id="row1072mcpsimp"><td class="cellrowborder" colspan="3" valign="top"><p id="p1074mcpsimp"><a name="p1074mcpsimp"></a><a name="p1074mcpsimp"></a><strong id="b1075mcpsimp"><a name="b1075mcpsimp"></a><a name="b1075mcpsimp"></a>R</strong></p>
</td>
</tr>
<tr id="row1076mcpsimp"><td class="cellrowborder" valign="top" width="12%"><p id="p1078mcpsimp"><a name="p1078mcpsimp"></a><a name="p1078mcpsimp"></a>REE</p>
</td>
<td class="cellrowborder" valign="top" width="37%"><p id="p1080mcpsimp"><a name="p1080mcpsimp"></a><a name="p1080mcpsimp"></a>Rich Execution Environment</p>
</td>
<td class="cellrowborder" valign="top" width="51%"><p id="p1082mcpsimp"><a name="p1082mcpsimp"></a><a name="p1082mcpsimp"></a>Rich Execution Environment</p>
</td>
</tr>
<tr id="row1083mcpsimp"><td class="cellrowborder" valign="top" width="12%"><p id="p1085mcpsimp"><a name="p1085mcpsimp"></a><a name="p1085mcpsimp"></a>RKP</p>
</td>
<td class="cellrowborder" valign="top" width="37%"><p id="p1087mcpsimp"><a name="p1087mcpsimp"></a><a name="p1087mcpsimp"></a>Root Key Process</p>
</td>
<td class="cellrowborder" valign="top" width="51%"><p id="p1089mcpsimp"><a name="p1089mcpsimp"></a><a name="p1089mcpsimp"></a>Root Key Process</p>
</td>
</tr>
<tr id="row1092mcpsimp"><td class="cellrowborder" colspan="3" valign="top"><p id="p1094mcpsimp"><a name="p1094mcpsimp"></a><a name="p1094mcpsimp"></a><strong id="b1639665055310"><a name="b1639665055310"></a><a name="b1639665055310"></a>T</strong></p>
</td>
</tr>
<tr id="row1095mcpsimp"><td class="cellrowborder" valign="top" width="12%"><p id="p1097mcpsimp"><a name="p1097mcpsimp"></a><a name="p1097mcpsimp"></a>TEE</p>
</td>
<td class="cellrowborder" valign="top" width="37%"><p id="p1099mcpsimp"><a name="p1099mcpsimp"></a><a name="p1099mcpsimp"></a>Trusted Execution Environment</p>
</td>
<td class="cellrowborder" valign="top" width="51%"><p id="p1101mcpsimp"><a name="p1101mcpsimp"></a><a name="p1101mcpsimp"></a>Trusted Execution Environment</p>
</td>
</tr>
</tbody>
</table>
